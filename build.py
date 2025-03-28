import os
from pathlib import Path
import markdown
import logging
import staticjinja
from staticjinja import Site
from externals.markdown_extensions import *

markdowner = markdown.Markdown(
    output_format = "html",
    extensions = (
        "meta", "toc", "md_in_html",
        extended_tables_extension.ExtendedTableExtension(),
        highlight_extensions.UnsureHighlightExtension(),
        highlight_extensions.WarningHighlightExtension(),
        header_extensions.SectionsViaHeadersExtension(),
        header_extensions.AddBlanksAroundHeadersExtension(),
        small_image_extension.SmallImageExtension(),
        ps2_buttons_extension.PS2ButtonsExtension(imgs_path="./", imgs_extension="png")
    )
)


def md_context(template):
    markdown_content = Path(template.filename).read_text()
    return {
        "text": markdowner.convert(markdown_content),
        "title": markdowner.Meta["title"][0],
        "toc": markdowner.toc
    }


def render_md(site, template, **kwargs):
    # i.e. posts/post1.md -> build/posts/post1.html
    out = site.outpath / Path(template.name).with_suffix(".html")

    # Compile and stream the result
    os.makedirs(out.parent, exist_ok=True)
    site.get_template("partials/_wikipage.html").stream(**kwargs).dump(str(out), encoding="utf-8")


site = Site.make_site(
    searchpath="templates",
    staticpaths=["style.css"], # Yes, this is deprecated... too bad!
    outpath="_out",
    contexts=[(r".*\.md", md_context)],
    rules=[(r".*\.md", render_md)],
)

staticjinja.logger.setLevel(logging.DEBUG)
site.render()
