import re
from typing import Any


class CSSContainer:
    def __init__(self, css_styles: dict[str, str]) -> None:
        default_items = [
            "text",
            "number",
            "email",
            "url",
            "password",
            "hidden",
            "multiplehidden",
            "file",
            "clearablefile",
            "textarea",
            "date",
            "datetime",
            "time",
            "checkbox",
            "select",
            "nullbooleanselect",
            "selectmultiple",
            "radioselect",
            "checkboxselectmultiple",
            "multi",
            "splitdatetime",
            "splithiddendatetime",
            "selectdate",
            "error_border",
        ]

        base = css_styles.get("base", "")
        for item in default_items:
            setattr(self, item, base)

        for key, value in css_styles.items():
            if key != "base":
                current_class = set(getattr(self, key).split())
                current_class.update(set(value.split()))
                new_classes = " ".join(current_class)
                setattr(self, key, new_classes)

    def __repr__(self) -> str:
        return str(self.__dict__)

    def __add__(self, other: dict[str, str]) -> "CSSContainer":
        for field, css_class in other.items():
            current_class = set(getattr(self, field).split())
            current_class.update(set(css_class.split()))
            new_classes = " ".join(current_class)
            setattr(self, field, new_classes)
        return self

    def __sub__(self, other: dict[str, str]) -> "CSSContainer":
        for field, css_class in other.items():
            current_class = set(getattr(self, field).split())
            removed_classes = set(css_class.split())
            new_classes = " ".join(current_class - removed_classes)
            setattr(self, field, new_classes)
        return self

    def get_input_class(self, field: Any) -> str:
        widget_name = re.sub(r"widget$|input$", "", field.field.widget.__class__.__name__.lower())
        css_classes = getattr(self, widget_name, None)

        if css_classes is None:
            import warnings

            warnings.warn(
                f"Widget type '{widget_name}' (from {field.field.widget.__class__.__name__}) "
                f"is not configured in CSSContainer. Field: {field.name}",
                UserWarning,
                stacklevel=2,
            )
            return ""

        return css_classes
