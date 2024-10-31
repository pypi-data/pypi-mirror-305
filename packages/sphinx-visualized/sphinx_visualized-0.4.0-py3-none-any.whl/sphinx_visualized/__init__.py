#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import json
import sphinx
from packaging import version
import os
import shutil
from collections import Counter
from pathlib import Path
from docutils import nodes as docutils_nodes
from multiprocessing import Manager, Queue

__version__ = "0.4.0"


def setup(app):
    app.connect("builder-inited", create_objects)
    app.connect("doctree-resolved", get_links)
    app.connect("build-finished", create_json)

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }


def create_objects(app):
    """
    Create objects when builder is initiated
    """
    builder = getattr(app, "builder", None)
    if builder is None:
        return

    manager = Manager()
    builder.env.app.pages = manager.dict() # an index of page names
    builder.env.app.references = manager.Queue() # a queue of every internal reference made between pages


def get_links(app, doctree, docname):
    """
    Gather internal link connections
    """

    #TODO handle troctree entries?
    #TODO get targets
    # for node in doctree.traverse(sphinx.addnodes.toctree):
    #     print(vars(node))

    for node in doctree.traverse(docutils_nodes.reference):
        # add internal references
        if node.tagname == 'reference' and node.get('internal') and node.get('refuri'):
            # calulate path of the referenced page in relation to docname
            ref = node.attributes['refuri'].split("#")[0]
            refname = os.path.abspath(os.path.join(os.path.dirname(f"/{docname}.html"), ref))[1:-5]

            #TODO some how get ref/doc/term for type?
            # add each link as an individual reference
            app.env.app.references.put((f"/{docname}.html", f"/{refname}.html", "ref"))

            docname_page = f"/{docname}.html"
            app.env.app.pages[docname_page] = True

            refname_page = f"/{refname}.html"
            app.env.app.pages[refname_page] = True


def build_toctree_hierarchy(app):
    """
    Take toctree_includes and build the document hierarchy while gathering page metadata.
    """
    node_map = {}
    data = app.env.toctree_includes

    for key, value in data.items():
        if key not in node_map:
            node_map[key] = {
                "id": key,
                "label": app.env.titles.get(key).astext(),
                "path": f"../../../{key}.html",
                "children": [],
            }

        for child in data[key]:
            if child not in node_map:
                node_map[child] = {
                    "id": child,
                    "label": app.env.titles.get(child).astext(),
                    "path": f"../../../{child}.html",
                    "children": [],
                }
            node_map[key]["children"].append(node_map[child])

    return node_map[app.builder.config.root_doc]


def create_json(app, exception):
    """
    Create and copy static files for visualizations
    """
    page_list = list(app.env.app.pages.keys()) # list of pages with references

    # create directory in _static and over static assets
    os.makedirs(Path(app.outdir) / "_static" / "sphinx-visualized", exist_ok=True)
    if version.parse(sphinx.__version__) >= version.parse("8.0.0"):
        # Use the 'force' argument if it's available
        sphinx.util.fileutil.copy_asset(
            os.path.join(os.path.dirname(__file__), "static"),
            os.path.join(app.builder.outdir, '_static', "sphinx-visualized"),
            force=True,
        )
    else:
        # Fallback for older versions without 'force' argument
        shutil.rmtree(Path(app.outdir) / "_static" / "sphinx-visualized")
        sphinx.util.fileutil.copy_asset(
            os.path.join(os.path.dirname(__file__), "static"),
            os.path.join(app.builder.outdir, '_static', "sphinx-visualized"),
        )

    # convert pages and groups to lists
    nodes = [] # a list of nodes and their metadata
    for page in page_list:
        if app.env.titles.get(page[1:-5]):
            title = app.env.titles.get(page[1:-5]).astext()
        else:
            title = page

        nodes.append({
            "id": page_list.index(page),
            "label": title,
            "path": f"../../..{page}",
        })

    # convert queue to list
    reference_list = []
    while not app.env.app.references.empty():
        reference_list.append(app.env.app.references.get())

    # create object that links references between pages
    links = [] # a list of links between pages
    references_counts = Counter(reference_list)
    for ref, count in references_counts.items():
        links.append({
            "target": page_list.index(ref[1]),
            "source": page_list.index(ref[0]),
            "strength": count,
            "type": ref[2],
        })

    filename = Path(app.outdir) / "_static" / "sphinx-visualized" / "js" / "links.js"
    with open(filename, "w") as json_file:
        json_file.write(f'var links_data = {json.dumps(links, indent=4)};')

    filename = Path(app.outdir) / "_static" / "sphinx-visualized" / "js" / "nodes.js"
    with open(filename, "w") as json_file:
        json_file.write(f'var nodes_data = {json.dumps(nodes, indent=4)};')

    filename = Path(app.outdir) / "_static" / "sphinx-visualized" / "js" / "toctree.js"
    with open(filename, "w") as json_file:
        json_file.write(f'var toctree = {json.dumps(build_toctree_hierarchy(app), indent=4)};')
