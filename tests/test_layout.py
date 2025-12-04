"""Tests for layout components."""

import pytest
from crispy_forms.layout import HTML, Field

from crispy_neurobrutalist.layout import (
    Alert,
    Button,
    Card,
    FormActions,
    InlineCheckboxes,
    InlineRadios,
    Reset,
    Submit,
)


class TestSubmit:
    """Test suite for Submit button component."""

    def test_submit_default_styling(self):
        """Test Submit button uses default neurobrutalist styling."""
        submit = Submit("submit", "Save")
        
        assert submit.input_type == "submit"
        assert "w-full" in submit.field_classes
        assert "font-bold" in submit.field_classes
        assert "bg-black" in submit.field_classes
        assert "neo-shadow-sm" in submit.field_classes
        assert "neo-button" in submit.field_classes

    def test_submit_custom_css_class(self):
        """Test Submit button with custom CSS classes."""
        submit = Submit("submit", "Save", css_class="custom-class")
        
        assert submit.field_classes == "custom-class"

    def test_submit_button_type(self):
        """Test that Submit has correct input type."""
        submit = Submit("submit", "Save")
        
        assert submit.input_type == "submit"


class TestButton:
    """Test suite for Button component."""

    def test_button_default_color(self):
        """Test Button uses primary color by default."""
        button = Button("cancel", "Cancel")
        
        assert "bg-blue-400" in button.field_classes
        assert "hover:bg-blue-500" in button.field_classes

    def test_button_primary_color(self):
        """Test Button with primary color."""
        button = Button("action", "Action", color="primary")
        
        assert "bg-blue-400" in button.field_classes

    def test_button_success_color(self):
        """Test Button with success color."""
        button = Button("action", "Action", color="success")
        
        assert "bg-green-400" in button.field_classes
        assert "hover:bg-green-500" in button.field_classes

    def test_button_warning_color(self):
        """Test Button with warning color."""
        button = Button("action", "Action", color="warning")
        
        assert "bg-yellow-400" in button.field_classes

    def test_button_danger_color(self):
        """Test Button with danger color."""
        button = Button("action", "Action", color="danger")
        
        assert "bg-red-400" in button.field_classes

    def test_button_purple_color(self):
        """Test Button with purple color."""
        button = Button("action", "Action", color="purple")
        
        assert "bg-purple-400" in button.field_classes

    def test_button_custom_css(self):
        """Test Button with custom CSS classes."""
        button = Button("action", "Action", css_class="custom-button")
        
        assert button.field_classes == "custom-button"

    def test_button_has_neurobrutalist_classes(self):
        """Test Button has neurobrutalist styling classes."""
        button = Button("action", "Action")
        
        assert "border-2" in button.field_classes
        assert "border-black" in button.field_classes
        assert "neo-shadow" in button.field_classes
        assert "neo-button" in button.field_classes
        assert "transition-all" in button.field_classes

    def test_button_type(self):
        """Test that Button has correct input type."""
        button = Button("action", "Action")
        
        assert button.input_type == "button"


class TestReset:
    """Test suite for Reset button component."""

    def test_reset_default_color(self):
        """Test Reset button uses warning color by default."""
        reset = Reset("reset", "Clear")
        
        assert "bg-yellow-400" in reset.field_classes
        assert "hover:bg-yellow-500" in reset.field_classes

    def test_reset_primary_color(self):
        """Test Reset with primary color."""
        reset = Reset("reset", "Clear", color="primary")
        
        assert "bg-blue-400" in reset.field_classes

    def test_reset_warning_color(self):
        """Test Reset with warning color explicitly set."""
        reset = Reset("reset", "Clear", color="warning")
        
        assert "bg-yellow-400" in reset.field_classes

    def test_reset_danger_color(self):
        """Test Reset with danger color."""
        reset = Reset("reset", "Clear", color="danger")
        
        assert "bg-red-400" in reset.field_classes

    def test_reset_custom_css(self):
        """Test Reset with custom CSS classes."""
        reset = Reset("reset", "Clear", css_class="custom-reset")
        
        assert reset.field_classes == "custom-reset"

    def test_reset_type(self):
        """Test that Reset has correct input type."""
        reset = Reset("reset", "Clear")
        
        assert reset.input_type == "reset"

    def test_reset_has_neurobrutalist_classes(self):
        """Test Reset has neurobrutalist styling."""
        reset = Reset("reset", "Clear")
        
        assert "border-2" in reset.field_classes
        assert "border-black" in reset.field_classes
        assert "neo-shadow" in reset.field_classes


class TestFormActions:
    """Test suite for FormActions container."""

    def test_form_actions_initialization(self):
        """Test FormActions initializes correctly."""
        submit = Submit("submit", "Save")
        cancel = Button("cancel", "Cancel", color="danger")
        
        actions = FormActions(submit, cancel)
        
        assert len(actions.fields) == 2

    def test_form_actions_default_css_class(self):
        """Test FormActions has default CSS classes."""
        actions = FormActions(Submit("submit", "Save"))
        
        assert "flex" in actions.css_class
        assert "gap-4" in actions.css_class
        assert "mt-6" in actions.css_class
        assert "justify-end" in actions.css_class

    def test_form_actions_custom_css_class(self):
        """Test FormActions with custom CSS classes."""
        actions = FormActions(
            Submit("submit", "Save"),
            css_class="custom-actions"
        )
        
        assert actions.css_class == "custom-actions"

    def test_form_actions_empty(self):
        """Test FormActions can be created empty."""
        actions = FormActions()
        
        assert len(actions.fields) == 0


class TestAlert:
    """Test suite for Alert component."""

    def test_alert_default_type(self):
        """Test Alert uses info type by default."""
        alert = Alert(HTML("Test message"))
        
        assert "bg-blue-200" in alert.css_class
        assert "border-blue-600" in alert.css_class
        assert "text-blue-900" in alert.css_class

    def test_alert_info_type(self):
        """Test Alert with info type."""
        alert = Alert(HTML("Test"), alert_type="info")
        
        assert "bg-blue-200" in alert.css_class

    def test_alert_success_type(self):
        """Test Alert with success type."""
        alert = Alert(HTML("Success!"), alert_type="success")
        
        assert "bg-green-200" in alert.css_class
        assert "border-green-600" in alert.css_class
        assert "text-green-900" in alert.css_class

    def test_alert_warning_type(self):
        """Test Alert with warning type."""
        alert = Alert(HTML("Warning!"), alert_type="warning")
        
        assert "bg-yellow-200" in alert.css_class
        assert "border-yellow-600" in alert.css_class

    def test_alert_error_type(self):
        """Test Alert with error type."""
        alert = Alert(HTML("Error!"), alert_type="error")
        
        assert "bg-red-200" in alert.css_class
        assert "border-red-600" in alert.css_class

    def test_alert_not_dismissible(self):
        """Test Alert is not dismissible by default."""
        alert = Alert(HTML("Test"))
        
        assert "relative" not in alert.css_class
        assert "pr-12" not in alert.css_class

    def test_alert_dismissible(self):
        """Test Alert with dismissible option."""
        alert = Alert(HTML("Test"), dismissible=True)
        
        assert "relative" in alert.css_class
        assert "pr-12" in alert.css_class

    def test_alert_has_neurobrutalist_classes(self):
        """Test Alert has neurobrutalist styling."""
        alert = Alert(HTML("Test"))
        
        assert "p-4" in alert.css_class
        assert "border-2" in alert.css_class
        assert "rounded-lg" in alert.css_class
        assert "neo-shadow-sm" in alert.css_class


class TestCard:
    """Test suite for Card container."""

    def test_card_initialization(self):
        """Test Card initializes with fields."""
        card = Card(
            HTML("<h3>Title</h3>"),
            Field("field1"),
            Field("field2")
        )
        
        assert len(card.fields) == 3

    def test_card_default_css_class(self):
        """Test Card has default neurobrutalist styling."""
        card = Card(HTML("Content"))
        
        assert "bg-white" in card.css_class
        assert "border-2" in card.css_class
        assert "border-black" in card.css_class
        assert "rounded-lg" in card.css_class
        assert "p-6" in card.css_class
        assert "neo-shadow" in card.css_class
        assert "mb-4" in card.css_class

    def test_card_custom_css_class(self):
        """Test Card with custom CSS classes."""
        card = Card(HTML("Content"), css_class="custom-card")
        
        assert card.css_class == "custom-card"

    def test_card_empty(self):
        """Test Card can be created empty."""
        card = Card()
        
        assert len(card.fields) == 0


class TestInlineCheckboxes:
    """Test suite for InlineCheckboxes component."""

    def test_inline_checkboxes_initialization(self):
        """Test InlineCheckboxes initializes correctly."""
        inline = InlineCheckboxes("preferences")
        
        assert len(inline.fields) == 1

    def test_inline_checkboxes_wrapper_class(self):
        """Test InlineCheckboxes has flex wrapper class."""
        inline = InlineCheckboxes("preferences")
        
        assert "flex" in inline.wrapper_class
        assert "gap-4" in inline.wrapper_class
        assert "flex-wrap" in inline.wrapper_class

    def test_inline_checkboxes_custom_wrapper_class(self):
        """Test InlineCheckboxes with custom wrapper class."""
        inline = InlineCheckboxes("preferences", wrapper_class="custom-wrapper")
        
        assert inline.wrapper_class == "custom-wrapper"


class TestInlineRadios:
    """Test suite for InlineRadios component."""

    def test_inline_radios_initialization(self):
        """Test InlineRadios initializes correctly."""
        inline = InlineRadios("gender")
        
        assert len(inline.fields) == 1

    def test_inline_radios_wrapper_class(self):
        """Test InlineRadios has flex wrapper class."""
        inline = InlineRadios("gender")
        
        assert "flex" in inline.wrapper_class
        assert "gap-4" in inline.wrapper_class
        assert "flex-wrap" in inline.wrapper_class

    def test_inline_radios_custom_wrapper_class(self):
        """Test InlineRadios with custom wrapper class."""
        inline = InlineRadios("gender", wrapper_class="custom-wrapper")
        
        assert inline.wrapper_class == "custom-wrapper"


class TestLayoutIntegration:
    """Integration tests for layout components working together."""

    def test_form_actions_with_all_button_types(self):
        """Test FormActions containing all button types."""
        actions = FormActions(
            Submit("submit", "Save"),
            Button("draft", "Draft", color="warning"),
            Reset("reset", "Clear", color="danger")
        )
        
        assert len(actions.fields) == 3

    def test_card_with_alert(self):
        """Test Card containing Alert."""
        card = Card(
            Alert(HTML("Important info"), alert_type="warning"),
            Field("field1")
        )
        
        assert len(card.fields) == 2

    def test_nested_cards(self):
        """Test Cards can be nested."""
        outer_card = Card(
            HTML("<h2>Outer</h2>"),
            Card(
                HTML("<h3>Inner</h3>"),
                Field("field1")
            )
        )
        
        assert len(outer_card.fields) == 2

    def test_complex_layout_structure(self):
        """Test complex layout with multiple components."""
        from crispy_forms.layout import Layout
        
        layout = Layout(
            Alert(HTML("Welcome"), alert_type="info"),
            Card(
                HTML("<h3>Section 1</h3>"),
                Field("field1"),
                InlineCheckboxes("options")
            ),
            Card(
                HTML("<h3>Section 2</h3>"),
                InlineRadios("choice")
            ),
            FormActions(
                Submit("submit", "Submit"),
                Reset("reset", "Reset")
            )
        )
        
        assert len(layout.fields) == 4
