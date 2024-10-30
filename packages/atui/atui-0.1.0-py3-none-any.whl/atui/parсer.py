from .components import Window, Button, InputPanel
from .styles import CSSStyle  # Импортируем CSSStyle

def parse_element(element):
    if element.tag == "window":
        window = Window(
            title=element.attrib.get("title"),
            width=int(element.attrib.get("width", 800)),
            height=int(element.attrib.get("height", 600)),
        )
        for child in element:
            window.add_child(parse_element(child))
        return window

    elif element.tag == "button":
        style = CSSStyle()
        if 'style' in element.attrib:
            # Парсим стили из атрибутов
            style_string = element.attrib['style']
            for style_property in style_string.split(";"):
                if ":" in style_property:
                    property_name, value = style_property.split(":")
                    style.set_property(property_name.strip(), value.strip())
        
        return Button(
            text=element.attrib.get("text"),
            style=style,
            id=element.attrib.get("id")
        )

    elif element.tag == "inputpanel":
        style = CSSStyle()
        if 'style' in element.attrib:
            style_string = element.attrib['style']
            for style_property in style_string.split(";"):
                if ":" in style_property:
                    property_name, value = style_property.split(":")
                    style.set_property(property_name.strip(), value.strip())

        return InputPanel(
            value=element.attrib.get("value", ""),
            style=style,
            id=element.attrib.get("id")
        )

    else:
        raise ValueError(f"Неизвестный элемент: {element.tag}")
