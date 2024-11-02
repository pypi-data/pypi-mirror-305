import datetime

import pytest

from sgelt import mdparse, pages, utils


def test_tables():
    """Test that markdown conversion add class attributes to table elements"""
    s = """
a | table
--- | ---
spam | egg
"""

    expected = """\
<table class="responsive-table">
<thead>
<tr>
<th>a</th>
<th>table</th>
</tr>
</thead>
<tbody>
<tr>
<td>spam</td>
<td>egg</td>
</tr>
</tbody>
</table>\
"""
    assert mdparse.slicer.md.convert(s) == expected


class FakeMdPage:
    """A Mockup class for MdPage"""

    parser = pages.MdPage.parser
    _parse_shortcodes = pages.MdPage._parse_shortcodes

    def __init__(self, website, team=None):
        self.conf = website.conf
        self.data = website.data
        self.category = "team" if team else None
        self.metadata = {"team": team}
        self.team_seminars = pages.MdPage._get_team_seminars(self)


def test_shortcode_team_members(miniwebsite):
    md_content = """\
# Membres

## Membres permanents

{{% team_members permanent=True %}}

## Membres non permanents

{{% team_members permanent=False %}}

"""
    expected = """\
# Membres

## Membres permanents


- Marguerite Le Roux, Chargée de recherche
- [Océane Klein](https://fake.fr/~klein/), Directrice de recherche émérite
- [Amélie Samson](https://fake.fr/~samson/), Ingénieure
- Cécile Millet, Maîtresse de conférences émérite
- [Cécile Verdier](https://fake.fr/~verdier/), Maîtresse de conférences émérite
- [Audrey Duval](https://fake.fr/~duval/), Professeure

## Membres non permanents


- Jacques Ribeiro, ATER
- Adrien Germain, ATER
- [Lucy Foucher](https://fake.fr/~foucher/), Invitée

"""

    md_page = FakeMdPage(miniwebsite, "TU")
    assert md_page._parse_shortcodes(md_content) == expected


def test_shortcode_team_seminars(miniwebsite):
    miniwebsite.build()
    md_content = """\

{{% team_seminars %}}

"""
    md_page = FakeMdPage(miniwebsite, "TU")
    expected = """
L'équipe anime :

- le groupe de travail [Inspirer sauter fatigue croix appuyer](../groupes-de-travail/groupe-de-travail-inspirer-sauter-fatigue-croix-appuyer.html)
- le séminaire [Donc repas éternel sein travers pénétrer](../seminaires/seminaire-donc-repas-eternel-sein-travers-penetrer.html)

"""
    assert md_page._parse_shortcodes(md_content) == expected

    md_page = FakeMdPage(miniwebsite, "RA")
    expected = """
L'équipe anime le séminaire [Beau souffrance réveiller beauté horizon manquer](../seminaires/seminaire-beau-souffrance-reveiller-beaute-horizon-manquer.html).

"""
    md_page = FakeMdPage(miniwebsite, "RA")
    assert md_page._parse_shortcodes(md_content) == expected

    md_page = FakeMdPage(miniwebsite, "WG")
    expected = """
L'équipe anime le séminaire [Donc repas éternel sein travers pénétrer](../seminaires/seminaire-donc-repas-eternel-sein-travers-penetrer.html).

"""
    assert md_page._parse_shortcodes(md_content) == expected


def test_shortcode_button(miniwebsite):
    md_page = FakeMdPage(miniwebsite)

    # Test with icon
    md_content = """\
{{% button href="attachments/file.pdf" icon="cloud_download" text="Download PDF" %}}
"""
    expected = """\
<div class="center">
  <a class="waves-effect waves-light btn" href="attachments/file.pdf" >
    <i class="material-icons right" aria-hidden="true">cloud_download</i>Download PDF
  </a>
</div>
"""
    assert md_page._parse_shortcodes(md_content) == expected

    # Test without icon
    md_content = """\
{{% button href="attachments/file.pdf" text="Download PDF" %}}
"""
    expected = """\
<div class="center">
  <a class="waves-effect waves-light btn" href="attachments/file.pdf" >
    Download PDF
  </a>
</div>
"""
    assert md_page._parse_shortcodes(md_content) == expected

    # Test with btn-class
    md_content = """\
{{% button href="attachments/file.pdf" text="Download PDF" btn_class="btn-small" %}}
"""
    expected = """\
<div class="center">
  <a class="waves-effect waves-light btn-small" href="attachments/file.pdf" >
    Download PDF
  </a>
</div>
"""
    assert md_page._parse_shortcodes(md_content) == expected

    # Test with external url
    md_content = """\
{{% button href="https://fake.fr" text="Go to URL" %}}
"""
    expected = """\
<div class="center">
  <a class="waves-effect waves-light btn" href="https://fake.fr" referrerpolicy="no-referrer" rel="noopener noreferrer" target="_blank">
    Go to URL
  </a>
</div>
"""
    assert md_page._parse_shortcodes(md_content) == expected


def test_parse_md_file(tmp_path):
    template = """\
---
title: Présentation
menu_item: "L'institut"
category: "static"
date: {}
---

Some content on
two lines.

"""

    def get_expected_template(date_obj) -> dict:
        return {
            "title": "Présentation",
            "menu_item": "L'institut",
            "category": "static",
            "date": date_obj,
        }

    s = template.format("2015-02-03 15:28:09")
    # Write string content in test.md
    md_filepath = tmp_path / "test.md"
    md_filepath.write_text(s)
    metadata, md_content = mdparse.split_mdfile(md_filepath)
    assert metadata == get_expected_template(datetime.datetime(2015, 2, 3, 15, 28, 9))
    assert md_content == "Some content on\ntwo lines."

    s = template.format("2015-02-03")

    # Write string content in test.md
    md_filepath = tmp_path / "test.md"
    md_filepath.write_text(s)
    metadata, md_content = mdparse.split_mdfile(md_filepath)
    assert metadata == get_expected_template(datetime.date(2015, 2, 3))
    assert md_content == "Some content on\ntwo lines."

    s = template.format("2015-02-03 15:28")
    # Write string content in test.md
    md_filepath = tmp_path / "test.md"
    md_filepath.write_text(s)
    with pytest.raises(SystemExit) as e:
        metadata, md_content = mdparse.split_mdfile(md_filepath)
    assert e.type is SystemExit
    assert e.value.code == 1


def test_MetaDataParsingError(tmp_path):
    mdfile_path = tmp_path / "test.md"
    metadata = {
        "title": "Présentation",
        "menu_item": "L'institut",
        "category": "static",
        "date": "2015-02-03 15:28",
    }
    with pytest.raises(mdparse.MetaDataParsingError) as e:
        raise mdparse.MetaDataParsingError(mdfile_path, metadata)
    assert "2015-02-03 15:28" in str(e.value)
