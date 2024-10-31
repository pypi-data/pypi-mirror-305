from pathlib import Path
from textwrap import dedent

import pytest

from opla import markdown


@pytest.fixture
def theme():
    return "theme:\n    name: materialize"


class TestParseMarkdownFile:
    @pytest.fixture
    def setup_dir(self, tmp_path, theme) -> Path:
        """Create a markdown file with a header and sections for testing"""
        data = f"""\
---
title: Ma page perso
name: Erica
occupation: Chargée de recherche
{theme}
---

## Section 1

Section 1 content

## Section 2

### Section 2.1

Section 2.1 content

### Section 2.2

Section 2.2 content
Section 2.2 content

## Section 3

Section 3 content
"""
        with open(tmp_path / "test.md", "w") as f:
            f.write(data)
        mdfilepath = tmp_path / Path("test.md")

        return mdfilepath

    @pytest.mark.parametrize(
        "theme", ["theme:\n    name: materialize", "", "theme:\n    name: rawhtml"]
    )
    def test_parse_file_header(self, setup_dir, theme):
        header, _, _ = markdown.parse_file(setup_dir)

        expected = {
            "title": "Ma page perso",
            "name": "Erica",
            "occupation": "Chargée de recherche",
            "theme": {"name": "water"},
        }

        if theme == "theme:\n    name: rawhtml":
            expected["theme"] = {"name": "rawhtml"}
            assert header == expected
        elif theme == "theme:\n    name: materialize":
            expected["theme"] = {"name": "materialize", "color": "teal"}
            assert header == expected
        else:
            assert header == expected

    def test_parse_file_sections(self, setup_dir):
        expected = [
            {
                "content": dedent("""
                <p>Section 1 content</p>
                """),
                "id": "section-1",
                "title": "Section 1",
            },
            {
                "content": dedent("""
                <h3>Section 2.1</h3>
                <p>Section 2.1 content</p>
                <h3>Section 2.2</h3>
                <p>Section 2.2 content
                Section 2.2 content</p>
                """),
                "id": "section-2",
                "title": "Section 2",
            },
            {
                "content": "\n<p>Section 3 content</p>",
                "id": "section-3",
                "title": "Section 3",
            },
        ]
        _, sections, _ = markdown.parse_file(setup_dir)

        assert sections == expected

    def test_parse_file_menu(self, setup_dir):
        expected = [
            {"href": "#section-2", "text": "Section 2"},
            {"href": "#section-3", "text": "Section 3"},
        ]
        _, _, menu = markdown.parse_file(setup_dir)
        assert menu == expected


def test_convert_md_list_to_html():
    contact_markdown = [
        "<jlrda@dix-huitieme-siecle.fr>",
        "Six feet under the carrefour de Chateaudun-Place Kossuth, 75009 Paris, France",
        "+33 1 01 02 03 04",
    ]
    contact_html = markdown.convert_md_list_to_html(contact_markdown)
    expected = [
        '<a href="&#109;&#97;&#105;&#108;&#116;&#111;&#58;&#106;&#108;&#114;&#100;&#97;&#64;&#100;&#105;&#120;&#45;&#104;&#117;&#105;&#116;&#105;&#101;&#109;&#101;&#45;&#115;&#105;&#101;&#99;&#108;&#101;&#46;&#102;&#114;">&#106;&#108;&#114;&#100;&#97;&#64;&#100;&#105;&#120;&#45;&#104;&#117;&#105;&#116;&#105;&#101;&#109;&#101;&#45;&#115;&#105;&#101;&#99;&#108;&#101;&#46;&#102;&#114;</a>',
        "Six feet under the carrefour de Chateaudun-Place Kossuth, 75009 Paris, France",
        "+33 1 01 02 03 04",
    ]
    assert contact_html == expected
