import textwrap
import panel as pn
from config import (
    ACCENT,
    get_code_editor_theme,
    DEFAULT_XML,
)
from panel_modal import Modal
from splitter import Splitter

from panel_xml import XML

# Panel Configuration
pn.extension(
    "codeeditor", "jsoneditor", "modal", sizing_mode="stretch_width",
)


# Component Definitions
xml_viewer = XML(object=DEFAULT_XML, depth=2)
code = pn.widgets.CodeEditor.from_param(
    xml_viewer.param.object,
    theme=get_code_editor_theme(),
    sizing_mode="stretch_both",
)

docs_modal = Modal()
docs_section = pn.Column(
    pn.widgets.Button.from_param(
        docs_modal.param.open,
        name="Show Documentation",
        button_type="primary",
        button_style="outline",
        description="Click here to show the MermaidDiagram documentation",
    ),
    docs_modal,
)


# Callback Definitions
@pn.depends(docs_modal.param.open)
def docs_content(event=None):
    return pn.Column(
        pn.pane.Markdown(
            textwrap.dedent(xml_viewer.__doc__)
            + "\n### Parameters\n\n"
            + xml_viewer.param._repr_html_(),
        ),
        height=500,
        scroll=True,
    )


# Layout Setup
docs_modal[:] = [docs_content]

sidebar = [
    docs_section,
    xml_viewer.settings(),
]

main_content = Splitter(
    left=code,
    right=xml_viewer,
    sizing_mode="stretch_both",
    margin=(10, 10, 50, 10),
)


# Template Setup
pn.template.FastListTemplate(
    title="Panel XML | Editor",
    sidebar=sidebar,
    main=[main_content],
    main_layout=None,
    accent=ACCENT,
).servable()
