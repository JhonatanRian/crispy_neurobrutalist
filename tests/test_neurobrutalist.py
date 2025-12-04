"""Tests for CSSContainer class."""

import pytest
from django import forms

from crispy_neurobrutalist.neurobrutalist import CSSContainer


class TestCSSContainer:
    """Test suite for CSSContainer class."""

    def test_initialization_with_base_style(self):
        """Test that CSSContainer initializes with base style applied to all widget types."""
        css = CSSContainer({"base": "border-2 rounded"})
        
        assert css.text == "border-2 rounded"
        assert css.checkbox == "border-2 rounded"
        assert css.select == "border-2 rounded"
        assert css.email == "border-2 rounded"

    def test_initialization_with_specific_styles(self):
        """Test that specific widget styles override base styles."""
        css = CSSContainer({
            "base": "border-2",
            "text": "rounded-lg p-3",
            "checkbox": "w-5 h-5"
        })
        
        # Base + specific styles merged
        assert "border-2" in css.text
        assert "rounded-lg" in css.text
        assert "p-3" in css.text
        
        assert "border-2" in css.checkbox
        assert "w-5" in css.checkbox
        assert "h-5" in css.checkbox

    def test_initialization_without_base(self):
        """Test initialization with only specific widget styles."""
        css = CSSContainer({
            "text": "w-full p-3",
            "checkbox": "w-5 h-5"
        })
        
        assert set(css.text.split()) == {"w-full", "p-3"}
        assert set(css.checkbox.split()) == {"w-5", "h-5"}
        assert css.select == ""  # No base, no specific style

    def test_add_operator_adds_classes(self):
        """Test that the + operator adds CSS classes."""
        css = CSSContainer({"text": "border-2"})
        
        css += {"text": "rounded-lg p-3"}
        
        assert "border-2" in css.text
        assert "rounded-lg" in css.text
        assert "p-3" in css.text

    def test_add_operator_to_new_widget_type(self):
        """Test adding classes to a widget type that wasn't initialized."""
        css = CSSContainer({"base": "border-2"})
        
        css += {"text": "focus:ring-2"}
        
        assert "border-2" in css.text
        assert "focus:ring-2" in css.text

    def test_add_operator_returns_self(self):
        """Test that + operator returns self for chaining."""
        css = CSSContainer({"text": "border-2"})
        
        result = css + {"text": "rounded"}
        
        assert result is css

    def test_subtract_operator_removes_classes(self):
        """Test that the - operator removes CSS classes."""
        css = CSSContainer({"text": "border-2 rounded-lg p-3 bg-white"})
        
        css -= {"text": "rounded-lg bg-white"}
        
        assert "border-2" in css.text
        assert "p-3" in css.text
        assert "rounded-lg" not in css.text
        assert "bg-white" not in css.text

    def test_subtract_operator_returns_self(self):
        """Test that - operator returns self for chaining."""
        css = CSSContainer({"text": "border-2 rounded"})
        
        result = css - {"text": "rounded"}
        
        assert result is css

    def test_subtract_nonexistent_class(self):
        """Test that subtracting non-existent class doesn't cause error."""
        css = CSSContainer({"text": "border-2"})
        
        css -= {"text": "nonexistent-class"}
        
        assert css.text == "border-2"

    def test_chaining_operators(self):
        """Test chaining add and subtract operators."""
        css = CSSContainer({"text": "border-2"})
        
        css += {"text": "rounded-lg p-3"}
        css -= {"text": "border-2"}
        css += {"text": "border-4"}
        
        assert "border-4" in css.text
        assert "rounded-lg" in css.text
        assert "p-3" in css.text
        assert "border-2" not in css.text

    def test_repr_method(self):
        """Test __repr__ returns string representation of dict."""
        css = CSSContainer({"text": "border-2", "checkbox": "w-5"})
        
        repr_str = repr(css)
        
        assert isinstance(repr_str, str)
        assert "text" in repr_str
        assert "checkbox" in repr_str

    def test_get_input_class_for_text_input(self):
        """Test get_input_class returns correct classes for TextInput."""
        from django.forms import BoundField, Form
        
        class TestForm(Form):
            name = forms.CharField()
        
        form = TestForm()
        field = form['name']
        
        css = CSSContainer({"text": "w-full p-3 border-2"})
        result = css.get_input_class(field)
        
        assert set(result.split()) == {"w-full", "p-3", "border-2"}

    def test_get_input_class_for_email_input(self):
        """Test get_input_class returns correct classes for EmailInput."""
        from django.forms import BoundField, Form
        
        class TestForm(Form):
            email = forms.EmailField()
        
        form = TestForm()
        field = form['email']
        
        css = CSSContainer({"email": "w-full border-2 focus:ring-blue-500"})
        result = css.get_input_class(field)
        
        assert set(result.split()) == {"w-full", "border-2", "focus:ring-blue-500"}

    def test_get_input_class_for_checkbox(self):
        """Test get_input_class returns correct classes for CheckboxInput."""
        from django.forms import BoundField, Form
        
        class TestForm(Form):
            agree = forms.BooleanField()
        
        form = TestForm()
        field = form['agree']
        
        css = CSSContainer({"checkbox": "w-5 h-5 custom-checkbox"})
        result = css.get_input_class(field)
        
        assert set(result.split()) == {"w-5", "h-5", "custom-checkbox"}

    def test_get_input_class_for_select(self):
        """Test get_input_class returns correct classes for Select widget."""
        from django.forms import BoundField, Form
        
        class TestForm(Form):
            CHOICES = [('a', 'A'), ('b', 'B')]
            choice = forms.ChoiceField(choices=CHOICES)
        
        form = TestForm()
        field = form['choice']
        
        css = CSSContainer({"select": "w-full p-2 border-2"})
        result = css.get_input_class(field)
        
        assert set(result.split()) == {"w-full", "p-2", "border-2"}

    def test_get_input_class_for_unknown_widget(self):
        """Test get_input_class warns and returns empty string for unknown widget."""
        from django.forms import BoundField, Form
        
        class CustomWidget(forms.Widget):
            pass
        
        class TestForm(Form):
            custom = forms.CharField(widget=CustomWidget())
        
        form = TestForm()
        field = form['custom']
        
        css = CSSContainer({"base": "border-2"})
        
        with pytest.warns(UserWarning, match="Widget type 'custom' .* is not configured"):
            result = css.get_input_class(field)
        
        assert result == ""

    def test_get_input_class_strips_widget_suffix(self):
        """Test that get_input_class properly strips 'widget' and 'input' suffixes."""
        from django.forms import BoundField, Form
        
        class TestForm(Form):
            password = forms.CharField(widget=forms.PasswordInput())
        
        form = TestForm()
        field = form['password']
        
        css = CSSContainer({"password": "w-full border-2"})
        result = css.get_input_class(field)
        
        # PasswordInput -> password (stripped 'input')
        assert set(result.split()) == {"w-full", "border-2"}

    def test_error_border_class(self):
        """Test that error_border class is available."""
        css = CSSContainer({
            "error_border": "bg-red-100 border-red-500"
        })
        
        assert set(css.error_border.split()) == {"bg-red-100", "border-red-500"}

    def test_all_default_widget_types_initialized(self):
        """Test that all default widget types are initialized."""
        css = CSSContainer({"base": "test"})
        
        widget_types = [
            "text", "number", "email", "url", "password", "hidden",
            "multiplehidden", "file", "clearablefile", "textarea",
            "date", "datetime", "time", "checkbox", "select",
            "nullbooleanselect", "selectmultiple", "radioselect",
            "checkboxselectmultiple", "multi", "splitdatetime",
            "splithiddendatetime", "selectdate", "error_border"
        ]
        
        for widget_type in widget_types:
            assert hasattr(css, widget_type)
            assert css.__dict__[widget_type] == "test"

    def test_duplicate_classes_not_added(self):
        """Test that duplicate classes are not added when using + operator."""
        css = CSSContainer({"text": "border-2 rounded"})
        
        css += {"text": "border-2 focus:ring-2"}
        
        # Should only have one 'border-2'
        text_classes = css.text.split()
        assert text_classes.count("border-2") == 1
        assert "rounded" in text_classes
        assert "focus:ring-2" in text_classes
