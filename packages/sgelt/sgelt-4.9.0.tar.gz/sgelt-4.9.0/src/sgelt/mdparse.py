"""Parse markdown content"""

from __future__ import annotations
from datetime import datetime, date
import logging
from pathlib import Path
import sys

from markdown.treeprocessors import Treeprocessor
from markdown.extensions import Extension
from markdown_link_attr_modifier import LinkAttrModifierExtension
from mdslicer import MDSlicer, split_header_and_content
import shortcodes
import yaml


log = logging.getLogger(__name__)


class MetaDataParsingError(Exception):
    """A class to handle Markdown files parsing errors"""

    def __init__(
        self, mdfile_path: Path, metadata: dict, message="Error parsing file metadata"
    ):
        self.mdfile_path = mdfile_path
        self.metadata = metadata
        self.message = message
        super().__init__(self.message)

    def __str__(self) -> str:
        return f"""\
{self.message} for {self.mdfile_path}: date field \
{self.metadata['date']} is not formed as datetime or date. \
"See https://jekyllrb.com/docs/front-matter/#predefined-variables-for-posts"
"""


def check_metadata_date(metadata: dict, mdfile_path: Path) -> None:
    """
    Check if metadata date is a datetime or date object

    Args:
        metadata: Metadata of the markdown file
        mdfile_path: Path to the markdown file

    Raises:
        MetaDataParsingError: If metadata date is not a datetime or date object
    """
    try:
        if type(metadata["date"]) not in (datetime, date):
            raise MetaDataParsingError(mdfile_path=mdfile_path, metadata=metadata)
    except MetaDataParsingError as e:
        log.error(e)
        sys.exit(1)
    except KeyError:
        pass


def split_mdfile(mdfile_path: Path | str) -> tuple[dict, str]:
    """
    Split markdown file into metadata and content

    Args:
        mdfile_path: Path to markdown file

    Returns:
        tuple: metadata and content
    """

    mdfile_path = Path(mdfile_path)
    mdfile_content = mdfile_path.read_text()
    try:
        metadata, md_content = split_header_and_content(mdfile_content)
    except (yaml.scanner.ScannerError, yaml.parser.ParserError) as e:
        sys.exit(f"Cannot parse {mdfile_path}:\n{mdfile_content}\nReason: {e}")

    check_metadata_date(metadata, mdfile_path)
    return metadata, md_content


class TableProcessor(Treeprocessor):
    def run(self, root):
        for element in root.iter("table"):
            element.set("class", "responsive-table")


class TableExtension(Extension):
    """Add class="responsive-table" to all table elements"""

    def extendMarkdown(self, md):
        md.treeprocessors.register(TableProcessor(md), "tableextension", 15)


slicer = MDSlicer(
    extensions=[
        "toc",
        "attr_list",
        "tables",
        LinkAttrModifierExtension(new_tab="external_only", no_referrer="external_only"),
        TableExtension(),
    ]
)


def parse_md_file(mdfile_path: Path) -> tuple[dict, list[dict[str, str]]]:
    """
    Parse markdown file to return a tuple of metadata and markdown content
    """
    try:
        metadata, sections = slicer.slice_file(mdfile_path)
    except (yaml.scanner.ScannerError, yaml.parser.ParserError) as e:
        sys.exit(f"Cannot parse {mdfile_path}:\nReason: {e}")

    check_metadata_date(metadata, mdfile_path)
    return metadata, sections


@shortcodes.register("team_members")
def team_members_handler(_, kwargs: dict, context) -> str:
    """
    A short code to inject team members markdown.
    Usage:
    {{% team_members permanent=True %}}
    """
    env = context["page"].conf.env

    team_name = context["page"].metadata["team"]
    # json lib does not convert json boolean so:
    permanent = bool(kwargs["permanent"] == "True")
    all_members = context["data"].teams[team_name]["members"]

    members = [member for member in all_members if member["permanent"] == permanent]

    template_string = """\
{%- for member in members %}
{%- if member.url %}
- [{{ member.firstname }} {{ member.name }}]({{ member.url }}){{ ', {}'\
.format(member.status) if member.status }}
{%- else %}
- {{ member.firstname }} {{ member.name }}{{ ', {}'.format(member.status)\
if member.status }}
{%- endif -%}
{%- endfor -%}
"""
    template = env.from_string(template_string)
    return template.render(members=members)


@shortcodes.register("team_seminars")
def team_seminars_handler(_, kwargs: dict, context) -> str:
    """
    A shortcode to inject links to the seminars organized by the team.
    Usage:
    {{% team_seminars %}}
    """
    env = context["page"].conf.env

    team_seminars = context["page"].team_seminars
    sem_template = (
        r"le {{ seminar.type |lower }} [{{ seminar.title }}]"
        r"(../{{ seminar.html_path }})"
    )
    if len(team_seminars) == 1:
        template_string = f"L'équipe anime {sem_template}."
        template = env.from_string(template_string)
        return template.render(seminar=team_seminars[0])
    else:
        template_string = """L'équipe anime :
{{% for seminar in seminars %}}
- {}
{{%- endfor -%}}
""".format(sem_template)
        template = env.from_string(template_string)
        return template.render(seminars=team_seminars)


@shortcodes.register("button")
def button_handler(_, kwargs: dict, context) -> str:
    """
    A shortcode to inject an html button.
    Usage:
    {{% button href="attachments/file.pdf" text="Document PDF" \
icon="cloud_download" %}}
    """
    href = kwargs["href"]
    text = kwargs["text"]
    icon = kwargs.get("icon")
    btn_class = kwargs.get("btn_class", "btn")

    env = context["page"].conf.env

    template_string = """\
<div class="center">
  <a class="waves-effect waves-light {{ btn_class }}" href="{{ href }}" \
{{ href | external_url }}>
    {{ '<i class="material-icons right" aria-hidden="true">{}</i>'\
.format(icon) if icon }}{{ text }}
  </a>
</div>"""
    template = env.from_string(template_string)
    return template.render(href=href, text=text, icon=icon, btn_class=btn_class)
