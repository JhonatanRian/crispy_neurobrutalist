from typing import Any, Literal

from crispy_forms.layout import BaseInput


class Submit(BaseInput):
    input_type = "submit"

    def __init__(self, *args: Any, css_class: str | None = None, **kwargs: Any) -> None:
        if css_class is None:
            self.field_classes = (
                "w-full font-bold text-lg text-white bg-black border-2 border-black "
                "rounded-lg py-3 neo-shadow-sm neo-button hover:bg-gray-800"
            )
        else:
            self.field_classes = css_class
        super().__init__(*args, **kwargs)


class Button(BaseInput):
    input_type = "button"

    def __init__(
        self,
        *args: Any,
        css_class: str | None = None,
        color: Literal["primary", "success", "warning", "danger", "purple"] = "primary",
        **kwargs: Any,
    ) -> None:
        if css_class is None:
            mapcolor = {
                "primary": "bg-blue-400 hover:bg-blue-500",
                "success": "bg-green-400 hover:bg-green-500",
                "warning": "bg-yellow-400 hover:bg-yellow-500",
                "danger": "bg-red-400 hover:bg-red-500",
                "purple": "bg-purple-400 hover:bg-purple-500",
            }
            self.field_classes = (
                f"font-bold text-black {mapcolor[color]} border-2 border-black "
                f"rounded-lg px-7 py-3 neo-shadow neo-button transition-all"
            )
        else:
            self.field_classes = css_class
        super().__init__(*args, **kwargs)
