import os
import sys

import erdantic as erd
from pydantic import BaseModel

import {{ cookiecutter.package_name }}
import {{ cookiecutter.package_name }}.rig
import {{ cookiecutter.package_name }}.task_logic

sys.path.insert(0, os.path.abspath("../src/DataSchemas"))

SOURCE_ROOT = "https://github.com/AllenNeuralDynamics/{{ cookiecutter.repository_name }}/tree/main/src/DataSchemas/"

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "{{ cookiecutter.repository_name.replace('.', ' ') }} project"
copyright = "{{ cookiecutter.year }}, Allen Institute for Neural Dynamics"
author = "{{ cookiecutter.author_name }}"
release = {{ cookiecutter.package_name }}.__version__

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx-jsonschema",
    "sphinx_jinja",
    "sphinx.ext.napoleon",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx.ext.githubpages",
    "sphinx.ext.linkcode",
    "sphinx_mdinclude",
    "sphinxcontrib.autodoc_pydantic",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

autosummary_generate = True

autodoc_pydantic_model_show_json = False
autodoc_pydantic_settings_show_json = False

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_static_path = ["_static"]
html_title = "{{ cookiecutter.repository_name.replace('.', ' ') }}"
html_favicon = "_static/favicon.ico"
html_theme_options = {
    "light_logo": "light-logo.svg",
    "dark_logo": "dark-logo.svg",
}

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = False


# -- Options for linkcode extension ---------------------------------------
def linkcode_resolve(domain, info):
    if domain != "py":
        return None
    if not info["module"]:
        return None
    filename = info["module"].replace(".", "/")
    return f"{SOURCE_ROOT}/{filename}.py"


# -- Class diagram generation (Optional) ---------------------------------------
def export_model_diagram(model: BaseModel, root: str = "_static") -> None:
    diagram = erd.create(model)
    diagram.draw(f"{root}/{model.__name__}.svg")


_diagram_root = "_static"
#export_model_diagram(MyPydanticBaseModel, _diagram_root)