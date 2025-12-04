# 🎨 Crispy Neurobrutalist

[![PyPI version](https://badge.fury.io/py/crispy-neurobrutalist.svg)](https://badge.fury.io/py/crispy-neurobrutalist)
[![Python](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![Django](https://img.shields.io/badge/django-4.2+-green.svg)](https://www.djangoproject.com/)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)

A Django app that provides **Neurobrutalist design themes** for `django-crispy-forms`. Transform your Django forms with bold, high-contrast styling using Tailwind CSS with custom neo-brutalist utilities.

![Neurobrutalist Form Example](https://via.placeholder.com/800x400?text=Neurobrutalist+Form+Preview)

## ✨ Features

- 🎯 **Bold Design**: High-contrast forms with thick borders and striking shadows
- 🎨 **Tailwind-based**: Built on Tailwind CSS with custom neo-brutalist utilities
- 🔧 **Easy Integration**: Drop-in template pack for django-crispy-forms
- 📦 **Pre-styled Widgets**: All form widgets styled out of the box
- 🎭 **Custom Components**: Neurobrutalist buttons with color variants
- ♿ **Accessible**: Maintains Django form accessibility features

## 📦 Installation

### 1. Install the package

```bash
pip install crispy-neurobrutalist
```

Or with uv:

```bash
uv pip install crispy-neurobrutalist
```

### 2. Add to INSTALLED_APPS

```python
# settings.py
INSTALLED_APPS = [
    # ...
    'crispy_forms',
    'crispy_neurobrutalist',
    # ...
]

# Configure crispy forms to use the neurobrutalist template pack
CRISPY_ALLOWED_TEMPLATE_PACKS = "neobrutalist"
CRISPY_TEMPLATE_PACK = "neobrutalist"
```

### 3. Include Tailwind CSS

Add Tailwind CSS to your project. You can use the CDN for quick testing:

```html
<!-- base.html -->
<head>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
```

### 4. Include Neurobrutalist Styles

The package includes custom CSS for neurobrutalist effects. Include it in your base template:

```html
<!-- base.html -->
{% load static %}
<head>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="{% static 'crispy_neurobrutalist/css/neurobrutalist.css' %}">
</head>
```

The CSS file provides essential classes for:
- ✓ **Custom checkbox/radio styling** - `.custom-checkbox`, `.custom-radio`
- ✓ **Neo-brutalist shadows** - `.neo-shadow`, `.neo-shadow-sm`, `.neo-shadow-md`
- ✓ **Button animations** - `.neo-button` with press effect
- ✓ **Optional utilities** - `.neo-card`, `.neo-border`, color variants

**Note:** Make sure `django.contrib.staticfiles` is in your `INSTALLED_APPS` and you've run `python manage.py collectstatic` in production.

## 🚀 Usage

### Basic Form Rendering

```python
# forms.py
from django import forms
from crispy_forms.helper import FormHelper

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
```

```html
<!-- template.html -->
{% load crispy_forms_tags %}

<form method="post">
    {% csrf_token %}
    {{ form|crispy }}
    <button type="submit" class="w-full font-bold text-lg text-white bg-black border-2 border-black rounded-lg py-3 neo-shadow-sm neo-button hover:bg-gray-800">
        Submit
    </button>
</form>
```

### Using Layout Components

```python
# forms.py
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Div
from crispy_neurobrutalist.layout import Submit, Button

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    remember_me = forms.BooleanField(required=False)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('username'),
            Field('password'),
            Field('remember_me'),
            Div(
                Submit('submit', 'Login'),
                Button('button', 'Reset', color='danger'),
                css_class='flex gap-4 mt-4'
            )
        )
```

### Custom CSS Container

Override default styles for specific widget types:

```python
# forms.py
from crispy_neurobrutalist.neurobrutalist import CSSContainer

css_container = CSSContainer({
    "text": "w-full p-4 bg-yellow-100 border-4 border-black rounded-xl",
    "checkbox": "w-6 h-6 border-4 border-purple-500",
})

# In your view context
context = {
    'form': form,
    'css_container': css_container,
}
```

### Available Button Colors

The `Button` component supports multiple color variants:

```python
from crispy_neurobrutalist.layout import Button

Button('name', 'Primary', color='primary')   # Blue
Button('name', 'Success', color='success')   # Green
Button('name', 'Warning', color='warning')   # Yellow
Button('name', 'Danger', color='danger')     # Red
Button('name', 'Purple', color='purple')     # Purple
```

## 🎨 Widget Styles

All Django form widgets are pre-styled with neurobrutalist design:

| Widget | Styling |
|--------|---------|
| TextInput, EmailInput, URLInput | Bold border, thick shadow, blue focus ring |
| Textarea | Same as text inputs with auto-resize |
| Select | Custom dropdown with neurobrutalist styling |
| Checkbox | Custom checkbox with checkmark |
| Radio | Custom radio buttons with dot indicator |
| FileInput | Styled file upload with bold button |
| PasswordInput | Masked input with same text styling |

## 📚 Template Tags

### `{% neo_field %}`

Renders a single field with neurobrutalist styling:

```html
{% load neo_field %}

{% neo_field form.email %}
```

### `|crispy` filter

Renders entire form:

```html
{% load crispy_forms_tags %}

{{ form|crispy }}
```

### `|as_crispy_field` filter

Renders individual field:

```html
{{ form.username|as_crispy_field }}
```

## 🔧 Customization

### Override Default Styles

Create a custom CSS container in your view:

```python
from crispy_neurobrutalist.neurobrutalist import CSSContainer

# Start with defaults and modify
css_container = CSSContainer({
    "base": "w-full p-3 bg-white border-2 border-black rounded-lg",
})

# Add specific styles
css_container += {
    "text": "focus:border-purple-500",
    "email": "focus:border-blue-500",
}

# Remove classes
css_container -= {
    "text": "rounded-lg",
}
```

### Custom Templates

Override specific templates by creating them in your project:

```
your_project/
    templates/
        neobrutalist/
            field.html          # Override field template
            layout/
                checkbox.html   # Override checkbox template
```

## � Development & Testing

This project uses **uv** for dependency management and **pytest** for testing.

### Setting Up Development Environment

```bash
# Clone the repository
git clone https://github.com/JhonatanRian/crispy_neurobrutalist.git
cd crispy_neurobrutalist

# Install dependencies with uv
uv pip install -e ".[dev]"
```

### Running Tests

```bash
# Run all tests
uv run pytest

# Run with coverage report
uv run pytest --cov=src/crispy_neurobrutalist --cov-report=term-missing

# Run specific test file
uv run pytest tests/test_layout.py -v

# Run specific test
uv run pytest tests/test_layout.py::TestSubmit::test_submit_default_styling -v
```

### Test Coverage

The project maintains **96% code coverage** with **65 unit tests**:

- `test_neurobrutalist.py` - 20 tests for CSSContainer class
- `test_layout.py` - 45 tests for layout components (Submit, Button, Reset, Alert, Card, etc.)

```
Name                            Stmts   Miss  Cover
----------------------------------------------------
layout.py                          49      0   100%
neurobrutalist.py                  36      0   100%
__init__.py                         7      0   100%
----------------------------------------------------
TOTAL                             106      4    96%
```

### Code Quality Tools

```bash
# Format code with black
uv run black src/ tests/

# Lint with ruff
uv run ruff check src/ tests/

# Type checking with mypy
uv run mypy src/
```

## �🤝 Contributing

Contributions are welcome! However, please note this project is under a non-commercial license.

### Contribution Guidelines

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **Make your changes**
   - Follow existing code style (black formatting, line length 100)
   - Add tests for new features
   - Ensure all tests pass: `uv run pytest`
4. **Commit your changes** (`git commit -m 'Add amazing feature'`)
5. **Push to the branch** (`git push origin feature/amazing-feature`)
6. **Open a Pull Request**

### Development Requirements

- Python 3.12+
- uv (for dependency management)
- Django 4.2+
- django-crispy-forms 2.4+

## 📝 License

This project is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International License**. See the [LICENSE](LICENSE) file for details.

### You are free to:

* **Share** — copy and redistribute the material in any medium or format
* **Adapt** — remix, transform, and build upon the material

### Under the following terms:

* **Attribution** — You must give appropriate credit to Jhonatan Rian, provide a link to the license, and indicate if changes were made.
* **NonCommercial** — You may not use the material for commercial purposes.

This is a human-readable summary of (and not a substitute for) the [license](https://creativecommons.org/licenses/by-nc/4.0/).

## 🙏 Credits

Created by **Jhonatan Rian** ([@JhonatanRian](https://github.com/JhonatanRian))

Built on top of:
- [django-crispy-forms](https://github.com/django-crispy-forms/django-crispy-forms)
- [Tailwind CSS](https://tailwindcss.com/)

## 📧 Support

For issues, questions, or suggestions, please open an issue on [GitHub](https://github.com/JhonatanRian/crispy_neurobrutalist/issues).
