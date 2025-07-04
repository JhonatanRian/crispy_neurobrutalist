import re

from crispy_forms.utils import TEMPLATE_PACK, get_template_pack
from django import forms, template
from django.conf import settings
from django.template import Context, loader

from crispy_neurobrutalist.neurobrutalist import CSSContainer

register = template.Library()


@register.filter
def is_checkbox(field):
    return isinstance(field.field.widget, forms.CheckboxInput)


@register.filter
def is_password(field):
    return isinstance(field.field.widget, forms.PasswordInput)


@register.filter
def is_radioselect(field):
    return isinstance(field.field.widget, forms.RadioSelect)


@register.filter
def is_select(field):
    return isinstance(field.field.widget, forms.Select)


@register.filter
def is_multiselect(field):
    return isinstance(field.field.widget, forms.SelectMultiple)


@register.filter
def is_checkboxselectmultiple(field):
    return isinstance(field.field.widget, forms.CheckboxSelectMultiple)


@register.filter
def is_file(field):
    return isinstance(field.field.widget, forms.FileInput)


@register.filter
def is_clearable_file(field):
    return isinstance(field.field.widget, forms.ClearableFileInput)


@register.filter
def is_multivalue(field):
    return isinstance(field.field.widget, forms.MultiWidget)


@register.filter
def classes(field):
    """
    Returns CSS classes of a field
    """
    return field.widget.attrs.get("class", None)


@register.filter
def css_class(field):
    """
    Returns widgets class name in lowercase
    """
    return field.field.widget.__class__.__name__.lower()


def pairwise(iterable):
    """s -> (s0,s1), (s2,s3), (s4, s5), ..."""
    a = iter(iterable)
    return zip(a, a)


class CrispyNeuroBrutaListFieldNode(template.Node):
    base_input = (
        "w-full p-3 bg-white border-2 border-black rounded-lg focus:outline-none focus:ring-2 "
        "focus:ring-blue-400 neo-shadow-sm"
    )

    default_styles = {
        "text": base_input,
        "number": base_input,
        "radioselect": "",
        "email": base_input,
        "url": base_input,
        "password": base_input,
        "hidden": "",
        "multiplehidden": "",
        "file": "mt-1 w-full text-sm font-semibold text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-lg "
        "file:border-2 file:border-black file:neo-shadow-sm file:font-bold file:bg-gray-200 file:text-black "
        "hover:file:bg-gray-300",
        "clearablefile": "mt-1 w-full text-sm font-semibold text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-lg "
        "file:border-2 file:border-black file:neo-shadow-sm file:font-bold file:bg-gray-200 file:text-black "
        "hover:file:bg-gray-300",
        "textarea": base_input,
        "date": base_input,
        "datetime": base_input,
        "time": base_input,
        "checkbox": "w-5 h-5 border-2 border-black rounded-md appearance-none custom-checkbox",
        "select": "",
        "nullbooleanselect": "",
        "selectmultiple": "",
        "checkboxselectmultiple": "",
        "multi": "",
        "splitdatetime": "text-gray-700 bg-white focus:outline border border-gray-300 leading-normal px-4 "
        "appearance-none rounded-lg py-2 focus:outline-none mr-2",
        "splithiddendatetime": "",
        "selectdate": "",
        "error_border": "bg-red-100 border-red-500 border-2",
    }

    default_container = CSSContainer(default_styles)

    def __init__(self, field, attrs):
        self.field = field
        self.attrs = attrs
        self.html5_required = "html5_required"

    def render(self, context):
        if self not in context.render_context:
            context.render_context[self] = (
                template.Variable(self.field),
                self.attrs,
                template.Variable(self.html5_required),
            )

        field, attrs, html5_required = context.render_context[self]
        field = field.resolve(context)
        try:
            html5_required = html5_required.resolve(context)
        except template.VariableDoesNotExist:
            html5_required = False

        template_pack = context.get("template_pack", TEMPLATE_PACK)

        widgets = getattr(
            field.field.widget,
            "widgets",
            [getattr(field.field.widget, "widget", field.field.widget)],
        )

        if isinstance(attrs, dict):
            attrs = [attrs] * len(widgets)

        converters = {}
        converters.update(getattr(settings, "CRISPY_CLASS_CONVERTERS", {}))

        for widget, attr in zip(widgets, attrs):
            class_name = widget.__class__.__name__.lower()
            class_name = converters.get(class_name, class_name)
            css_class = widget.attrs.get("class", "")
            if css_class:
                if css_class.find(class_name) == -1:
                    css_class += " %s" % class_name
            else:
                css_class = class_name

            if template_pack == "neobrutalist" and '"class"' not in attr.keys():
                css_container = context.get("css_container", self.default_container)
                if css_container:
                    css = " " + css_container.get_input_class(field)
                    css_class += css
                if field.errors:
                    error_border_class = css_container.error_border
                    css_class = re.sub(r"border-\S+", error_border_class, css_class)

            widget.attrs["class"] = css_class

            if (
                html5_required
                and field.field.required
                and "required" not in widget.attrs
            ):
                if field.field.widget.__class__.__name__ != "RadioSelect":
                    widget.attrs["required"] = "required"

            for attribute_name, attribute in attr.items():
                attribute_name = template.Variable(attribute_name).resolve(context)

                if attribute_name in widget.attrs:
                    widget.attrs[attribute_name] += " " + template.Variable(
                        attribute
                    ).resolve(context)
                else:
                    widget.attrs[attribute_name] = template.Variable(attribute).resolve(
                        context
                    )

        return str(field)


@register.tag(name="neo_field")
def neo_field(parser, token):
    token = token.split_contents()
    field = token.pop(1)
    attrs = {}

    token.pop(0)
    for attribute_name, value in pairwise(token):
        attrs[attribute_name] = value

    return CrispyNeuroBrutaListFieldNode(field, attrs)


@register.simple_tag()
def crispy_addon(field, append="", prepend="", form_show_labels=True):
    """
    Renders a form field using bootstrap's prepended or appended text::

        {% crispy_addon form.my_field prepend="$" append=".00" %}

    You can also just prepend or append like so

        {% crispy_addon form.my_field prepend="$" %}
        {% crispy_addon form.my_field append=".00" %}
    """
    if field:
        context = Context(
            {
                "field": field,
                "form_show_errors": True,
                "form_show_labels": form_show_labels,
            }
        )
        template = loader.get_template(
            "%s/layout/prepended_appended_text.html" % get_template_pack()
        )
        context["crispy_prepended_text"] = prepend
        context["crispy_appended_text"] = append

        if not prepend and not append:
            raise TypeError("Expected a prepend and/or append argument")

        context = context.flatten()

        return template.render(context)
    return None
