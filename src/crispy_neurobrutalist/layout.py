"""Neurobrutalist layout components for django-crispy-forms."""

from typing import Any, Literal

from crispy_forms.layout import BaseInput, Div, Field


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


class Reset(BaseInput):
    """
    Reset button with neurobrutalist styling.

    Creates a reset button that clears form inputs.

    Example:
        >>> from crispy_neurobrutalist.layout import Reset
        >>> Reset('reset', 'Clear Form', color='warning')
    """

    input_type = "reset"

    def __init__(
        self,
        *args: Any,
        css_class: str | None = None,
        color: Literal["primary", "warning", "danger"] = "warning",
        **kwargs: Any,
    ) -> None:
        """
        Initialize Reset button.

        Args:
            *args: Positional arguments passed to BaseInput (name, value).
            css_class: Optional custom CSS classes.
            color: Color variant. Options: primary, warning (default), danger.
            **kwargs: Additional keyword arguments passed to BaseInput.
        """
        if css_class is None:
            mapcolor = {
                "primary": "bg-blue-400 hover:bg-blue-500",
                "warning": "bg-yellow-400 hover:bg-yellow-500",
                "danger": "bg-red-400 hover:bg-red-500",
            }
            self.field_classes = (
                f"font-bold text-black {mapcolor[color]} border-2 border-black "
                f"rounded-lg px-7 py-3 neo-shadow neo-button transition-all"
            )
        else:
            self.field_classes = css_class
        super().__init__(*args, **kwargs)


class FormActions(Div):
    """
    Container for form action buttons (Submit, Reset, Cancel, etc.).

    Wraps buttons in a div with neurobrutalist styling and proper spacing.

    Example:
        >>> from crispy_neurobrutalist.layout import FormActions, Submit, Button
        >>> FormActions(
        ...     Submit('submit', 'Save'),
        ...     Button('cancel', 'Cancel', color='danger')
        ... )
    """

    def __init__(self, *fields: Any, **kwargs: Any) -> None:
        """
        Initialize FormActions container.

        Args:
            *fields: Layout objects (buttons) to include.
            **kwargs: Additional keyword arguments (css_class, css_id, etc.).
        """
        kwargs.setdefault("css_class", "flex gap-4 mt-6 justify-end")
        super().__init__(*fields, **kwargs)


class Alert(Div):
    """
    Alert/notification box with neurobrutalist styling.

    Creates an alert box with different color variants for different message types.

    Example:
        >>> from crispy_neurobrutalist.layout import Alert
        >>> from crispy_forms.layout import HTML
        >>> Alert(
        ...     HTML('<strong>Success!</strong> Your changes have been saved.'),
        ...     alert_type='success'
        ... )
    """

    def __init__(
        self,
        *fields: Any,
        alert_type: Literal["info", "success", "warning", "error"] = "info",
        dismissible: bool = False,
        **kwargs: Any,
    ) -> None:
        """
        Initialize Alert box.

        Args:
            *fields: Content to display in the alert.
            alert_type: Type of alert (info, success, warning, error).
            dismissible: Whether the alert can be dismissed.
            **kwargs: Additional keyword arguments.
        """
        alert_colors = {
            "info": "bg-blue-200 border-blue-600 text-blue-900",
            "success": "bg-green-200 border-green-600 text-green-900",
            "warning": "bg-yellow-200 border-yellow-600 text-yellow-900",
            "error": "bg-red-200 border-red-600 text-red-900",
        }

        base_classes = f"p-4 border-2 rounded-lg neo-shadow-sm {alert_colors[alert_type]}"
        if dismissible:
            base_classes += " relative pr-12"

        kwargs.setdefault("css_class", base_classes)
        super().__init__(*fields, **kwargs)


class Card(Div):
    """
    Card container with neurobrutalist styling.

    Creates a card-style container with border, shadow, and padding.

    Example:
        >>> from crispy_neurobrutalist.layout import Card
        >>> from crispy_forms.layout import Field, HTML
        >>> Card(
        ...     HTML('<h3 class="text-xl font-bold mb-4">Personal Info</h3>'),
        ...     Field('first_name'),
        ...     Field('last_name'),
        ... )
    """

    def __init__(self, *fields: Any, **kwargs: Any) -> None:
        """
        Initialize Card container.

        Args:
            *fields: Layout objects to include in the card.
            **kwargs: Additional keyword arguments (css_class, css_id, etc.).
        """
        kwargs.setdefault(
            "css_class", "bg-white border-2 border-black rounded-lg p-6 neo-shadow mb-4"
        )
        super().__init__(*fields, **kwargs)


class InlineCheckboxes(Field):
    """
    Render checkboxes inline (horizontally) instead of stacked.

    Example:
        >>> from crispy_neurobrutalist.layout import InlineCheckboxes
        >>> InlineCheckboxes('preferences')
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """
        Initialize InlineCheckboxes field.

        Args:
            *args: Field name and other positional arguments.
            **kwargs: Additional keyword arguments.
        """
        kwargs.setdefault("wrapper_class", "flex gap-4 flex-wrap")
        super().__init__(*args, **kwargs)


class InlineRadios(Field):
    """
    Render radio buttons inline (horizontally) instead of stacked.

    Example:
        >>> from crispy_neurobrutalist.layout import InlineRadios
        >>> InlineRadios('gender')
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """
        Initialize InlineRadios field.

        Args:
            *args: Field name and other positional arguments.
            **kwargs: Additional keyword arguments.
        """
        kwargs.setdefault("wrapper_class", "flex gap-4 flex-wrap")
        super().__init__(*args, **kwargs)
