import panel as pn

ACCENT = "#db2777"
REACT_XML_VIEWER_URL = "https://github.com/alissonmbr/react-xml-viewer"
PANEL_XML_URL = "https://github.com/awesome-panel/panel-xml"
DEFAULT_XML = """
<examples>
    <example id="person">
        <person>
            <name>John Doe</name>
            <age>30</age>
            <city>New York</city>
        </person>
    </example>
    <example id="colors">
        <tag attribute-key="Attribute value" />
        <![CDATA[some stuff]]>
        <!-- this is a comment -->
        <tag-name />
        <tag>Text</tag>
    </example>
</examples>
"""

def get_code_editor_theme():
    if pn.config.theme == "dark":
        return "chaos"
    return "crimson_editor"
