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


class TestSelect2Support:
    """Test suite for django-select2 support in CSSContainer."""

    SELECT2_WIDGET_TYPES = [
        "select2",
        "select2multiple",
        "select2tag",
        "heavyselect2",
        "heavyselect2multiple",
        "heavyselect2tag",
        "modelselect2",
        "modelselect2multiple",
        "modelselect2tag",
    ]

    def test_select2_widget_types_initialized_with_base(self):
        """Test that all Select2 widget types are initialized when using base style."""
        css = CSSContainer({"base": "test-class"})

        for widget_type in self.SELECT2_WIDGET_TYPES:
            assert hasattr(css, widget_type), f"Missing widget type: {widget_type}"
            assert css.__dict__[widget_type] == "test-class"

    def test_select2_widget_types_initialized_empty(self):
        """Test that Select2 widget types exist with empty base."""
        css = CSSContainer({})

        for widget_type in self.SELECT2_WIDGET_TYPES:
            assert hasattr(css, widget_type), f"Missing widget type: {widget_type}"
            assert css.__dict__[widget_type] == ""

    def test_select2_specific_styles_override(self):
        """Test that specific Select2 styles merge with base."""
        css = CSSContainer({
            "base": "border-2",
            "select2": "neo-shadow-sm",
            "select2multiple": "min-h-[52px]",
        })

        assert "border-2" in css.select2
        assert "neo-shadow-sm" in css.select2
        assert "border-2" in css.select2multiple
        assert "min-h-[52px]" in css.select2multiple

    def test_select2_add_operator(self):
        """Test adding classes to Select2 widget types."""
        css = CSSContainer({"select2": "border-2"})

        css += {"select2": "rounded-lg"}

        assert "border-2" in css.select2
        assert "rounded-lg" in css.select2

    def test_select2_subtract_operator(self):
        """Test removing classes from Select2 widget types."""
        css = CSSContainer({"select2": "border-2 rounded-lg neo-shadow-sm"})

        css -= {"select2": "neo-shadow-sm"}

        assert "border-2" in css.select2
        assert "rounded-lg" in css.select2
        assert "neo-shadow-sm" not in css.select2

    def test_get_input_class_for_mocked_select2_widget(self):
        """Test get_input_class resolves Select2 widget names correctly."""

        class FakeSelect2Widget(forms.Select):
            """Mock widget class simulating Select2Widget naming."""
            pass

        # Rename to match django-select2's class name pattern
        FakeSelect2Widget.__name__ = "Select2Widget"

        class TestForm(forms.Form):
            choice = forms.ChoiceField(
                choices=[("a", "A"), ("b", "B")],
                widget=FakeSelect2Widget(),
            )

        form = TestForm()
        field = form["choice"]

        css = CSSContainer({"select2": "neo-shadow-sm border-2"})
        result = css.get_input_class(field)

        assert set(result.split()) == {"neo-shadow-sm", "border-2"}

    def test_get_input_class_for_mocked_select2_multiple_widget(self):
        """Test get_input_class resolves Select2MultipleWidget correctly."""

        class FakeSelect2MultipleWidget(forms.SelectMultiple):
            pass

        FakeSelect2MultipleWidget.__name__ = "Select2MultipleWidget"

        class TestForm(forms.Form):
            choices = forms.MultipleChoiceField(
                choices=[("a", "A"), ("b", "B")],
                widget=FakeSelect2MultipleWidget(),
            )

        form = TestForm()
        field = form["choices"]

        css = CSSContainer({"select2multiple": "border-2 min-h-[52px]"})
        result = css.get_input_class(field)

        assert set(result.split()) == {"border-2", "min-h-[52px]"}

    def test_get_input_class_for_mocked_heavy_select2_widget(self):
        """Test get_input_class resolves HeavySelect2Widget correctly."""

        class FakeHeavySelect2Widget(forms.Select):
            pass

        FakeHeavySelect2Widget.__name__ = "HeavySelect2Widget"

        class TestForm(forms.Form):
            choice = forms.ChoiceField(
                choices=[("a", "A")],
                widget=FakeHeavySelect2Widget(),
            )

        form = TestForm()
        field = form["choice"]

        css = CSSContainer({"heavyselect2": "neo-shadow-sm"})
        result = css.get_input_class(field)

        assert "neo-shadow-sm" in result

    def test_get_input_class_for_mocked_model_select2_widget(self):
        """Test get_input_class resolves ModelSelect2Widget correctly."""

        class FakeModelSelect2Widget(forms.Select):
            pass

        FakeModelSelect2Widget.__name__ = "ModelSelect2Widget"

        class TestForm(forms.Form):
            choice = forms.ChoiceField(
                choices=[("a", "A")],
                widget=FakeModelSelect2Widget(),
            )

        form = TestForm()
        field = form["choice"]

        css = CSSContainer({"modelselect2": "border-2 rounded-lg"})
        result = css.get_input_class(field)

        assert set(result.split()) == {"border-2", "rounded-lg"}

    def test_all_widget_types_include_select2(self):
        """Test that the full default_items list includes all Select2 types."""
        css = CSSContainer({"base": "x"})

        all_types = [
            "text", "number", "email", "url", "password", "hidden",
            "multiplehidden", "file", "clearablefile", "textarea",
            "date", "datetime", "time", "checkbox", "select",
            "nullbooleanselect", "selectmultiple", "radioselect",
            "checkboxselectmultiple", "multi", "splitdatetime",
            "splithiddendatetime", "selectdate", "error_border",
        ] + self.SELECT2_WIDGET_TYPES

        for widget_type in all_types:
            assert hasattr(css, widget_type), f"Missing: {widget_type}"


class TestSelect2Filter:
    """Test suite for the is_select2 template filter."""

    def test_is_select2_returns_false_for_regular_select(self):
        """Test that is_select2 returns False for standard Django Select widgets."""
        from crispy_neurobrutalist.templatetags.neo_field import is_select2

        class TestForm(forms.Form):
            choice = forms.ChoiceField(choices=[("a", "A"), ("b", "B")])

        form = TestForm()
        field = form["choice"]

        assert is_select2(field) is False

    def test_is_select2_returns_false_for_regular_multiselect(self):
        """Test that is_select2 returns False for standard SelectMultiple."""
        from crispy_neurobrutalist.templatetags.neo_field import is_select2

        class TestForm(forms.Form):
            choices = forms.MultipleChoiceField(choices=[("a", "A")])

        form = TestForm()
        field = form["choices"]

        assert is_select2(field) is False

    def test_is_select2_returns_false_for_text_input(self):
        """Test that is_select2 returns False for TextInput."""
        from crispy_neurobrutalist.templatetags.neo_field import is_select2

        class TestForm(forms.Form):
            name = forms.CharField()

        form = TestForm()
        field = form["name"]

        assert is_select2(field) is False

    def test_is_select2_graceful_without_django_select2(self):
        """Test that is_select2 doesn't crash when django-select2 is not installed."""
        from unittest.mock import patch

        from crispy_neurobrutalist.templatetags.neo_field import is_select2

        class TestForm(forms.Form):
            choice = forms.ChoiceField(choices=[("a", "A")])

        form = TestForm()
        field = form["choice"]

        # Simulate django_select2 not being installed
        with patch.dict("sys.modules", {"django_select2": None, "django_select2.forms": None}):
            result = is_select2(field)
            assert result is False


class TestSelect2DefaultStyles:
    """Test suite for Select2 widget types in CrispyNeuroBrutaListFieldNode default_styles."""

    def test_select2_in_default_styles(self):
        """Test that Select2 widget types are in the default_styles dict."""
        from crispy_neurobrutalist.templatetags.neo_field import CrispyNeuroBrutaListFieldNode

        select2_types = [
            "select2", "select2multiple", "select2tag",
            "heavyselect2", "heavyselect2multiple", "heavyselect2tag",
            "modelselect2", "modelselect2multiple", "modelselect2tag",
        ]

        for widget_type in select2_types:
            assert widget_type in CrispyNeuroBrutaListFieldNode.default_styles, (
                f"Missing {widget_type} in default_styles"
            )
            assert CrispyNeuroBrutaListFieldNode.default_styles[widget_type] == ""

    def test_default_container_has_select2_attrs(self):
        """Test that the default_container CSSContainer has Select2 attributes."""
        from crispy_neurobrutalist.templatetags.neo_field import CrispyNeuroBrutaListFieldNode

        container = CrispyNeuroBrutaListFieldNode.default_container

        select2_types = [
            "select2", "select2multiple", "select2tag",
            "heavyselect2", "heavyselect2multiple", "heavyselect2tag",
            "modelselect2", "modelselect2multiple", "modelselect2tag",
        ]

        for widget_type in select2_types:
            assert hasattr(container, widget_type), f"Container missing: {widget_type}"

