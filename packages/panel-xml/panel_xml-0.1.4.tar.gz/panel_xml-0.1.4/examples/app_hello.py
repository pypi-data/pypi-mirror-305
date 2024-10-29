import panel as pn
from panel_xml import XML

pn.extension()

xml = '''
<ul>
<li>Hello</li>
<li>World</li>
</ul>
'''

XML(object=xml, depth=2).servable()