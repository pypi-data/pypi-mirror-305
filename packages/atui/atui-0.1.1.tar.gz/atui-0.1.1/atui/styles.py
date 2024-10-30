class CSSStyle:
    def __init__(self):
        self.styles = {}

    def set_property(self, property_name, value):
        """Устанавливает CSS-свойство."""
        self.styles[property_name] = value

    def border(self, value):
        """Устанавливает границу."""
        self.set_property('border', value)

    def border_radius(self, value):
        """Устанавливает радиус границы."""
        self.set_property('border-radius', value)

    def padding(self, value):
        """Устанавливает внутренние отступы."""
        self.set_property('padding', value)

    def margin(self, top=None, right=None, bottom=None, left=None):
        """Устанавливает внешние отступы."""
        if top is not None:
            self.set_property('margin-top', top)
        if right is not None:
            self.set_property('margin-right', right)
        if bottom is not None:
            self.set_property('margin-bottom', bottom)
        if left is not None:
            self.set_property('margin-left', left)

    def render(self):
        """Возвращает строку CSS-стилей."""
        return "; ".join(f"{key}: {value}" for key, value in self.styles.items())
