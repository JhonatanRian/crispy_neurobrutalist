"""
Crispy Neurobrutalist - A Django app providing Neurobrutalist themes for django-crispy-forms.

This package provides a neurobrutalist template pack for django-crispy-forms,
featuring bold, high-contrast styling with Tailwind CSS and custom neo-brutalist utilities.
"""

__version__ = "0.5.0"
__author__ = "Jhonatan Rian"
__email__ = "jhonatanrian@zohomail.com"
__license__ = "CC-BY-NC-4.0"

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
from crispy_neurobrutalist.neurobrutalist import CSSContainer

__all__ = [
    "Alert",
    "Button",
    "Card",
    "CSSContainer",
    "FormActions",
    "InlineCheckboxes",
    "InlineRadios",
    "Reset",
    "Submit",
    "__version__",
]

