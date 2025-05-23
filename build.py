import os
import shutil
import markdown
import logging
import staticjinja
import re
from pathlib import Path
from staticjinja import Site
from externals.markdown_extensions import *

OUTPATH = "./_site"
SEARCHPATH = "./templates"
STATICPATH = "./static"

dirs = {}

markdowner = markdown.Markdown(
    output_format = "html",
    extensions = (
        "meta", "toc", "md_in_html",
        extended_tables_extension.ExtendedTableExtension(),
        highlight_extensions.UnsureHighlightExtension(superscript="?", tooltip="This is speculative/unconfirmed"),
        highlight_extensions.WarningHighlightExtension(),
        header_extensions.SectionsViaHeadersExtension(),
        header_extensions.AddBlanksAroundHeadersExtension(),
        small_image_extension.SmallImageExtension(),
        ps2_buttons_extension.PS2ButtonsExtension(imgs_path="/btns/", imgs_extension="png"),
        inline_extensions.LinkBlankInlineExtension(extra_text='<span class="material-symbols-outlined">open_in_new</span>')
    )
)

def dit_dict(name: str, dir: str) -> dict:
    return {"name": name, "dir": dir, "children": []}

def md_context(template):
    global dirs
    markdown_content = Path(template.filename).read_text()
    text = markdowner.convert(markdown_content)
    title = markdowner.Meta["title"][0]

    site_dir_names = []
    path = template.name.split("/")
    target = dirs

    # Iteratively walk the known directories
    # Since staticjinja walks the directory in order, and due to how the website is structured, here we can assume every access to the dict/lists is valid
    for i in path[:-2]: # Divide path to get folders
        for j in target["children"]: # Iterate current directory to find the subdirectory
            if j["dir"] == i:
                target = j
                site_dir_names.append(target["name"]) # Append the "fancy" name of the directory
                break

    # Due to how the website is structured, we can always assume the last directory has to be added
    if len(path) > 1:
        target["children"].append(dit_dict(title, path[-2]))
        target = target["children"][-1]
        site_dir_names.append(target["name"])

    # Create the nav header
    SEPARATOR = """<span class="header-nav-separator">&gt;</span>"""
    href = "/"
    nav = f"""<a href="{href}"><span class="material-symbols-outlined">home</span> Home</a>""" # Home
    # Create links for all but the last directory
    for i in range(len(path) - 2):
        href += f"{path[i]}/"
        nav += f"""{SEPARATOR}<a href="{href}">{site_dir_names[i]}</a>"""

    # Create non-link text for the last (current) directory
    if len(path) > 1:
        nav += f"""{SEPARATOR}<span>{site_dir_names[-1]}</span>"""

    return {
        "text": text,
        "title": title,
        "toc": markdowner.toc,
        "target_template": markdowner.Meta["template"][0],
        "header_nav": nav
    }


def render_md(site, template, **kwargs):
    # !index.md is done to make sure the index is the first file rendered by jinja, otherwise it way mess up when generating the nav links
    # I could've done it in a more elegant way, but I can't be bothered
    out = site.outpath / Path(re.sub(r"!index", "index", template.name)).with_suffix(".html")

    # Compile and stream the result
    os.makedirs(out.parent, exist_ok=True)
    site.get_template(f"_partials/{kwargs['target_template']}").stream(**kwargs).dump(str(out), encoding="utf-8")


site = Site.make_site(
    searchpath=SEARCHPATH,
    outpath=OUTPATH,
    contexts=[(r".*\.md", md_context)],
    rules=[(r".*\.md", render_md)],
)

# Initialize the fancy home link
dirs = dit_dict("""<span class="material-symbols-outlined">home</span>Home""", "")

staticjinja.logger.setLevel(logging.DEBUG)
shutil.rmtree(OUTPATH, ignore_errors=True)
os.makedirs(OUTPATH, exist_ok=True)
shutil.copytree(STATICPATH, OUTPATH, dirs_exist_ok=True)
site.render()
