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

### 4. Add Custom Neo-Brutalist Styles

Include the custom CSS classes for the neo-brutalist effects:

```css
/* static/css/neurobrutalist.css */

/* Custom checkbox styling */
.custom-checkbox {
    position: relative;
    cursor: pointer;
}

.custom-checkbox:checked {
    background-color: black;
}

.custom-checkbox:checked::after {
    content: "✓";
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    color: white;
    font-weight: bold;
}

/* Custom radio styling */
.custom-radio {
    position: relative;
    cursor: pointer;
}

.custom-radio:checked {
    background-color: black;
}

.custom-radio:checked::after {
    content: "";
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 8px;
    height: 8px;
    background-color: white;
    border-radius: 50%;
}

/* Neo-brutalist shadows */
.neo-shadow {
    box-shadow: 4px 4px 0px 0px rgba(0, 0, 0, 1);
}

.neo-shadow-sm {
    box-shadow: 2px 2px 0px 0px rgba(0, 0, 0, 1);
}

/* Button hover effect */
.neo-button {
    transition: all 0.1s ease;
}

.neo-button:hover {
    transform: translate(2px, 2px);
    box-shadow: 2px 2px 0px 0px rgba(0, 0, 0, 1);
}

.neo-button:active {
    transform: translate(4px, 4px);
    box-shadow: none;
}
```

Then include it in your template:

```html
<!-- base.html -->
<link rel="stylesheet" href="{% static 'css/neurobrutalist.css' %}">
```

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

## 🤝 Contributing

Contributions are welcome! However, please note this project is under a non-commercial license.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

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
