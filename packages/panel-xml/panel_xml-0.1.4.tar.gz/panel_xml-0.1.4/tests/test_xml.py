from panel_xml import XML


def test_configuration():
    xml = """
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
    viewer = XML(object=xml)
    assert viewer.object
    assert viewer.settings()

    XML(xml, depth=2)
    