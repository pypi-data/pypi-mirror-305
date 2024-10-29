# ✨ panel-xml

[![License](https://img.shields.io/badge/License-MIT%202.0-blue.svg)](https://opensource.org/licenses/MIT)
[![py.cafe](https://py.cafe/badge.svg)](https://py.cafe/awesome.panel.org/panel-xml-basic)

`panel-xml` provides the `XML` *pane* to display and explore XML in notebooks and [Panel](https://panel.holoviz.org/) data apps.

![panel-xml in notebook](https://github.com/awesome-panel/panel-xml/blob/main/static/panel-xml-notebook.png?raw=true)

It is based on [react-xml-viewer](https://github.com/alissonmbr/react-xml-viewer).

## Key Features

- **Configurable Depth**: Set an initial collapsible depth for better navigation.
- **Collapse/Expand Tags**: Intuitively collapse or expand tags to streamline XML exploration.
- **Customizable Theme**: Configure the colors and appearance with a customizable theme.

## Installation

You can install `panel-xml` using `pip`:

```bash
pip install panel-xml
```

## Usage

### Basic XML Pane

[![py.cafe](https://py.cafe/badge.svg)](https://py.cafe/awesome.panel.org/panel-xml-basic)

[![panel-xml](https://github.com/awesome-panel/panel-xml/blob/main/static/panel-xml.png?raw=true)](https://py.cafe/awesome.panel.org/panel-xml-editor)

Here’s how to create a simple XML pane using the `XML` widget:

```python
import panel as pn
from panel_xml import XML

pn.extension()

xml = '''
<ul>
<li>Hello</li>
<li>World</li>
</ul>
'''

XML(xml, depth=2).servable()
```

## Api

### Parameters

- `object` (str): The XML string to display in a prettified format.
- `indent_size` (int): The size of the indentation.
- `collapsible` (bool): Enable collapsing/expanding tags. When collapsed, content and attributes are hidden.
- `depth` (int): When `collapsible` is set to `True`, this defines the initial collapsed depth. Set it to `0` for fully collapsed, or `-1` for fully expanded.
- `theme` (dict): A dictionary to customize the theme. See the [react-xml-viewer theme documentation](https://github.com/alissonmbr/react-xml-viewer#theme-object) for details.

## XML Editor

[![py.cafe](https://py.cafe/badge.svg)](https://py.cafe/awesome.panel.org/panel-xml-editor)

[Open the XML Editor](https://py.cafe/awesome.panel.org/panel-xml-editor) to explore the features and documentation of the `XML` pane interactively.

[![Panel XML | Diagram Editor](https://github.com/awesome-panel/panel-xml/blob/main/static/panel-xml-editor.gif?raw=true)](https://py.cafe/awesome.panel.org/panel-xml-editor)

## ❤️ Contributions

Contributions and co-maintainers are very welcome! Please submit issues or pull requests to the [GitHub repository](https://github.com/awesome-panel/panel-xml). Check out the [DEVELOPER_GUIDE](DEVELOPER_GUIDE.md) for more information.

## Alternatives

- [Panel CodeEditor](https://panel.holoviz.org/reference/widgets/CodeEditor.html): Displays XML nicely if `language="xml"`.

----

Start using `panel-xml` to integrate rich, interactive XML displays directly into your Python applications!
