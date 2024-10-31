"""
Parse markdown file into header and sections and create menu from sections
"""

from pathlib import Path

from mdslicer import MDSlicer
from markdown_link_attr_modifier import LinkAttrModifierExtension

from .shortcodes import parser

slicer = MDSlicer(
    extensions=["attr_list", LinkAttrModifierExtension()],
    additional_parser=parser.parse,
)


def parse_file(mdfile_path: Path) -> tuple[str, list[dict], list[dict]]:
    """
    Parse a markdown file into a header and a content

    Args:
        mdfile_path: Path to the markdown file

    Returns:
        (header of the markdown file, content sections of the markdown file, menu items)
    """
    slicer = MDSlicer(
        extensions=["attr_list", LinkAttrModifierExtension()],
        additional_parser=parser.parse,
    )
    header, sections = slicer.slice_file(mdfile_path)
    process_header(header)
    menu = create_menu(sections)
    return header, sections, menu


def process_header(header: dict) -> None:
    """
    Process the metadata header of the markdown file

    Args:
        header: Header of the markdown file
    """

    # Default theme is water
    try:
        header["theme"]["name"]
    except KeyError:  # Default theme
        header["theme"] = {"name": "water"}

    # Add default color to materialize theme
    if header["theme"]["name"] == "materialize":
        color = header["theme"].get("color", "teal")
        header["theme"]["color"] = color

    # Convert markdown lists to HTML in footer
    if "footer" in header:
        for key in header["footer"]:
            if key != "social":  # leave social list rendering to jinja templating
                # parse contact list or other lists
                header["footer"][key] = convert_md_list_to_html(header["footer"][key])


def convert_md_list_to_html(md_list: list[str]) -> list[str]:
    """
    Convert list of markdown content to list of HTML

    Args:
        md_list: a list of markdown content

    Returns:
        List[str]: a list of HTML content
    """
    # Remove <p> and </p> tags
    return [slicer.md.convert(md_element)[3:-4] for md_element in md_list]


@staticmethod
def create_menu(sections: list[dict]) -> list[dict]:
    """
    Create a menu from a collection of sections

    Args:
        sections: Sections of the markdown with an id and a title

    Returns:
        A list of menu items with a link href and a text
    """
    menu_links = []
    for section in sections[1:]:
        if section["id"]:
            menu_links.append({"href": f"#{section['id']}", "text": section["title"]})

    return menu_links
