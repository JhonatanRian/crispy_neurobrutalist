# Installation Guide

Complete installation and setup guide for Crispy Neurobrutalist.

## Table of Contents

- [Requirements](#requirements)
- [Installation Methods](#installation-methods)
- [Django Configuration](#django-configuration)
- [Tailwind CSS Setup](#tailwind-css-setup)
- [Custom Styles](#custom-styles)
- [Verification](#verification)
- [Troubleshooting](#troubleshooting)

## Requirements

- **Python**: 3.12 or higher
- **Django**: 4.2 or higher
- **django-crispy-forms**: 2.4 or higher
- **Tailwind CSS**: 3.x (via CDN or build process)

## Installation Methods

### Using pip

```bash
pip install crispy-neurobrutalist
```

### Using uv (recommended)

```bash
uv pip install crispy-neurobrutalist
```

### From Source

```bash
git clone https://github.com/JhonatanRian/crispy_neurobrutalist.git
cd crispy_neurobrutalist
pip install -e .
```

## Django Configuration

### 1. Add to INSTALLED_APPS

Edit your `settings.py`:

```python
INSTALLED_APPS = [
    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third-party apps
    'crispy_forms',
    'crispy_neurobrutalist',  # Add this
    
    # Your apps
    'myapp',
]
```

### 2. Configure Crispy Forms

Add these settings to `settings.py`:

```python
# Crispy Forms Configuration
CRISPY_ALLOWED_TEMPLATE_PACKS = "neobrutalist"
CRISPY_TEMPLATE_PACK = "neobrutalist"
```

### 3. Load Template Tags

In your templates, load the crispy forms tags:

```django
{% load crispy_forms_tags %}
```

## Tailwind CSS Setup

Crispy Neurobrutalist requires Tailwind CSS. Choose one of the following methods:

### Method 1: CDN (Quick Start)

Add to your base template (`base.html` or similar):

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}My Site{% endblock %}</title>
    
    <script src="https://cdn.tailwindcss.com"></script>
    
    <!-- Include crispy-neurobrutalist CSS (automatically included with package) -->
    <link rel="stylesheet" href="{% static 'crispy_neurobrutalist/css/neurobrutalist.css' %}">
</head>
<body>
    {% block content %}{% endblock %}
</body>
</html>
```

**Note**: 
- CDN is great for development but not recommended for production.
- The neurobrutalist CSS is included automatically with the package installation.
- Make sure `django.contrib.staticfiles` is in your `INSTALLED_APPS`.

### Method 2: Django-Tailwind (Recommended for Production)

```bash
# Install django-tailwind
pip install django-tailwind

# Add to INSTALLED_APPS
INSTALLED_APPS = [
    # ...
    'tailwind',
    'theme',  # your theme app
]

# Initialize tailwind
python manage.py tailwind init

# Install dependencies
python manage.py tailwind install

# Start development server (in separate terminal)
python manage.py tailwind start
```

### Method 3: Custom Build Process

1. Install Tailwind via npm:

```bash
npm install -D tailwindcss
npx tailwindcss init
```

2. Configure `tailwind.config.js`:

```javascript
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './myapp/templates/**/*.html',
    './src/crispy_neurobrutalist/templates/**/*.html',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

3. Create input CSS file (`static/src/input.css`):

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

4. Build CSS:

```bash
npx tailwindcss -i ./static/src/input.css -o ./static/css/output.css --watch
```

5. Include in template:

```html
<link rel="stylesheet" href="{% static 'css/output.css' %}">
```

## Custom Styles (Already Included!)

The neurobrutalist CSS styles are **automatically included** with the package installation. You don't need to create any CSS file manually!

### What's Included

The package provides `crispy_neurobrutalist/css/neurobrutalist.css` with:

- **Custom checkbox styling** (`.custom-checkbox`) - Black checkmark on white background
- **Custom radio styling** (`.custom-radio`) - Dot indicator when selected
- **Neo-brutalist shadows** (`.neo-shadow`, `.neo-shadow-sm`, `.neo-shadow-md`, `.neo-shadow-lg`, `.neo-shadow-xl`)
- **Colored shadow variants** (`.neo-shadow-blue`, `.neo-shadow-red`, `.neo-shadow-green`, `.neo-shadow-purple`)
- **Button animations** (`.neo-button`) - Press effect on hover/active
- **Card styles** (`.neo-card`) - Neurobrutalist container
- **Border utilities** (`.neo-border`, `.neo-border-thick`)
- **Background colors** (`.neo-bg-primary`, `.neo-bg-success`, `.neo-bg-warning`, `.neo-bg-danger`)

### How to Include

Simply load it in your base template (already shown in step 2):

```html
{% load static %}
<link rel="stylesheet" href="{% static 'crispy_neurobrutalist/css/neurobrutalist.css' %}">
```

**That's it!** The CSS file is distributed with the package and works with Django's static files system.

### For Production

Make sure to run collectstatic:

```bash
python manage.py collectstatic
```

This will copy the neurobrutalist CSS to your `STATIC_ROOT` directory.

### Static Files Configuration

In `settings.py`:

```python
import os

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
```

## Verification

### Test Your Installation

1. Create a simple form:

```python
# forms.py
from django import forms

class TestForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
```

2. Create a view:

```python
# views.py
from django.shortcuts import render
from .forms import TestForm

def test_view(request):
    form = TestForm()
    return render(request, 'test.html', {'form': form})
```

3. Create a template:

```django
<!-- templates/test.html -->
{% load crispy_forms_tags %}
{% load static %}
<!DOCTYPE html>
<html>
<head>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="{% static 'crispy_neurobrutalist/css/neurobrutalist.css' %}">
</head>
<body class="p-8 bg-gray-100">
    <div class="max-w-md mx-auto bg-white p-6 rounded-lg">
        <h1 class="text-2xl font-bold mb-4">Test Form</h1>
        <form method="post">
            {% csrf_token %}
            {{ form|crispy }}
            <button type="submit" class="w-full font-bold text-lg text-white bg-black border-2 border-black rounded-lg py-3 neo-shadow-sm neo-button hover:bg-gray-800">
                Submit
            </button>
        </form>
    </div>
</body>
</html>
```

4. Add URL pattern:

```python
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test_view, name='test'),
]
```

5. Run the server and visit `http://localhost:8000/test/`

You should see a neurobrutalist-styled form!

## Troubleshooting

### Templates Not Found

**Error**: `TemplateDoesNotExist: neobrutalist/field.html`

**Solution**: Ensure `crispy_neurobrutalist` is in `INSTALLED_APPS` and comes after `crispy_forms`.

### Styles Not Applying

**Problem**: Form appears unstyled

**Solutions**:
1. Verify Tailwind CSS is loaded (check browser developer tools)
2. Ensure `neurobrutalist.css` is included
3. Check that `CRISPY_TEMPLATE_PACK = "neobrutalist"` is set
4. Clear browser cache and Django cache

### Static Files Not Loading

**Problem**: Custom CSS file not found

**Solutions**:
1. Run `python manage.py collectstatic` (production)
2. Ensure `STATIC_URL` and `STATICFILES_DIRS` are configured
3. Check file path in template matches actual file location

### Import Errors

**Error**: `No module named 'crispy_neurobrutalist'`

**Solutions**:
1. Ensure package is installed: `pip list | grep crispy-neurobrutalist`
2. Activate correct virtual environment
3. Reinstall: `pip install --force-reinstall crispy-neurobrutalist`

### CSS Classes Not Working

**Problem**: `neo-shadow`, `neo-button` classes have no effect

**Solution**: These are custom classes defined in `neurobrutalist.css`. Ensure the file is included in your template.

## Next Steps

- Read the [README.md](README.md) for usage examples
- Check out [CONTRIBUTING.md](CONTRIBUTING.md) if you want to contribute
- See the [examples/](examples/) directory for complete working examples
- Review the [CHANGELOG.md](CHANGELOG.md) for version history

## Getting Help

If you encounter issues:

1. Check existing [GitHub Issues](https://github.com/JhonatanRian/crispy_neurobrutalist/issues)
2. Open a new issue with details about your problem
3. Include your environment details (Python, Django versions, etc.)
4. Provide a minimal reproducible example

Happy styling! 🎨
