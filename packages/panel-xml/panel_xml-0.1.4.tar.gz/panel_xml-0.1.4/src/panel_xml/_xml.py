import param
import panel as pn
from panel.custom import ReactComponent

XML_VIEWER_VERSION = "2.0.4"
REACT_VERSION = "18.3.1"

_THEME = {
    "attributeKeyColor": "#2a7ab0",
    "attributeValueColor": "#008000",
    "cdataColor": "#1D781D",
    "commentColor": "#aaa",
    "fontFamily": "monospace",
    "separatorColor": "var(--neutral-foreground-rest, var(--panel-on-background-color))",
    "tagColor": "#d43900",
    "textColor": "var(--neutral-foreground-rest, var(--panel-on-background-color))",
}


class XML(ReactComponent):
    """\
    A XML Pane

    Based on https://github.com/alissonmbr/react-xml-viewer

    Example:

    ```python
    import panel as pn
    from panel_xml import XML

    pn.extension()

    xml = '''
    <person>
        <name>John Doe</name>
        <age>30</age>
        <city>New York</city>
    </person>
    <tag attribute-key="Attribute value" />
    <![CDATA[some stuff]]>
    <!-- this is a comment -->
    <tag-name />
    <tag>Text</tag>
    '''

    viewer = XML(object=xml, depth=2)
    ```
    """
    
    object: str = param.String(doc="""A xml string to prettify.""")
    indent_size: int = param.Integer(
        default=2, bounds=(1, 10), doc="""The size of the indentation."""
    )
    collapsible: bool = param.Boolean(
        default=True,
        doc="""Allow collapse/expand tags by click on them. When tag is collapsed its content and attributes are hidden.""",
    )
    depth: int = param.Integer(
        default=-1,
        bounds=(-1, 10),
        doc="""When the collapsible is True, this sets the the level that will be collapsed to
        initially. For example, if you want to everything starts as collapsed, set 0. If you want
        it fully expanded set it to -1.""",
    )
    theme: dict = param.Dict(
        default=_THEME,
        doc="""A dictionary to customize the default theme.
        See https://github.com/alissonmbr/react-xml-viewer#theme-object""",
    )

    _esm = """
import XMLViewer from 'react-xml-viewer';

export function render({ model }) {
    const [object, setObject] = model.useState('object');
    const [indentSize, setIndentSize] = model.useState('indent_size');
    let [depth, setDepth] = model.useState('depth');
    const [collapsible, setCollapsible] = model.useState('collapsible');
    const [theme, setTheme] = model.useState('theme');
    
    if (depth === -1) {
        depth = null;
    }

    if (model.object) {
        return (
            <div style={{padding: "10px"}}>
                <XMLViewer
                    xml={object}
                    indentSize={indentSize}
                    initialCollapsedDepth={depth}
                    collapsible={collapsible}
                    theme={theme}
                />
            </div>
        );
    } else {
        return <div></div>;
    }
}
"""

    _importmap = {
        "imports": {
            "react-xml-viewer": f"https://esm.sh/react-xml-viewer@{XML_VIEWER_VERSION}",
        }
    }

    _react_version = REACT_VERSION

    def __init__(self, object: str, **params):
        """A XML Pane

        Args:
            object (str): The xml string to display.
        """
        super().__init__(object=object, **params)

    def settings(self, **params):
        return pn.Column(
            pn.pane.Markdown("**XML Settings**", margin=(10, 5, -10, 5)),
            self.param.indent_size,
            self.param.collapsible,
            self.param.depth,
            pn.pane.Markdown("Theme", margin=(-5, 5, -10, 5)),
            pn.widgets.JSONEditor.from_param(self.param.theme,),
            **params,
        )

XML.param.margin.default=(5,10,5,10)

