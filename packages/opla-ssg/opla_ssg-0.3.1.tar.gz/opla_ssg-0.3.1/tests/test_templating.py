import pytest
from pathlib import Path
from opla import opla, templating, markdown, payload


class TestGetTemplate:
    def test_materialize(self):
        template = opla.get_template("materialize")
        assert (
            Path(template.filename)
            == templating.TEMPLATES_PATH / "materialize/templates/index.html.j2"
        )

    def test_rawhtml(self):
        template = opla.get_template("rawhtml")
        assert Path(template.filename) == templating.TEMPLATES_PATH / Path(
            "rawhtml/templates/index.html.j2"
        )

    def test_unknown_theme(self):
        with pytest.raises(ValueError, match=r"Unknown theme name: 'doesnotexist'"):
            opla.get_template("doesnotexist")


def test_social_media(tmp_path):
    header, _, _ = markdown.parse_file(Path(__file__).parent / "example_media.md")
    template = templating.get_template(header["theme"]["name"])
    output_directory_path = tmp_path / "output"
    payload.copy_files(header, output_directory_path)

    html_out = template.render(
        sections=[],
        header=header,
        menu=[],
        output=output_directory_path,
        color=header["theme"].get("color"),
    )
    footer_extract = """\
            <div id="social" style="margin: 2rem 0 2rem 0;">
                <a href="https://www.github.com/jlrda" style="padding-right: 1rem; text-decoration: none">
                    <i aria-hidden="true" class="fa-brands fa-github fa-2xl"
                        style="color: white;"></i>
                    <span class="fa-sr-only">Link to my github account</span>
                </a>
                <a href="https://www.researchgate.com/jlrda" style="padding-right: 1rem; text-decoration: none">
                    <i aria-hidden="true" class="fa-brands fa-researchgate fa-2xl"
                        style="color: black;"></i>
                    <span class="fa-sr-only">Link to my researchgate account</span>
                </a>
                <a href="https://www.twitter.com/jlrda" style="padding-right: 1rem; text-decoration: none">
                    <i aria-hidden="true" class="fa-brands fa-twitter fa-2xl"
                        style="color: black;"></i>
                    <span class="fa-sr-only">Link to my twitter account</span>
                </a>
                <a href="https://www.gitlab.inria.fr/jlrda" style="padding-right: 1rem; text-decoration: none">
                    <i aria-hidden="true" class="fa-brands fa-gitlab fa-2xl"
                        style="color: black;"></i>
                    <span class="fa-sr-only">Link to my gitlab account</span><span>Inria</span>
                </a>
                
            </div>"""
    assert footer_extract in html_out
