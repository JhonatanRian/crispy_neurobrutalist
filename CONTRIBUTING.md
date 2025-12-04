# Contributing to Crispy Neurobrutalist

Thank you for your interest in contributing to Crispy Neurobrutalist! 🎉

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [How to Contribute](#how-to-contribute)
- [Style Guidelines](#style-guidelines)
- [Testing](#testing)
- [Pull Request Process](#pull-request-process)

## Code of Conduct

This project follows a simple code of conduct:

- Be respectful and inclusive
- Provide constructive feedback
- Focus on what is best for the community
- Show empathy towards other community members

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/crispy_neurobrutalist.git`
3. Add upstream remote: `git remote add upstream https://github.com/JhonatanRian/crispy_neurobrutalist.git`

## Development Setup

### Prerequisites

- Python 3.12 or higher
- uv (recommended) or pip
- Git

### Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/crispy_neurobrutalist.git
cd crispy_neurobrutalist

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
uv pip install -e ".[dev]"

# Install pre-commit hooks (optional but recommended)
pre-commit install
```

### Running Tests

```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=crispy_neurobrutalist --cov-report=html

# Run specific test file
pytest tests/test_neurobrutalist.py

# Run with verbose output
pytest -v
```

### Code Quality Checks

```bash
# Format code with black
black src/

# Lint with ruff
ruff check src/

# Type checking with mypy
mypy src/
```

## How to Contribute

### Reporting Bugs

Before creating a bug report, please check existing issues to avoid duplicates.

When filing an issue, include:

- **Description**: Clear description of the bug
- **Steps to Reproduce**: Minimal steps to reproduce the behavior
- **Expected Behavior**: What you expected to happen
- **Actual Behavior**: What actually happened
- **Environment**:
  - Python version
  - Django version
  - django-crispy-forms version
  - OS and version

### Suggesting Enhancements

Enhancement suggestions are welcome! Please provide:

- **Clear description** of the proposed feature
- **Use case**: Why this would be useful
- **Examples**: How it would work in practice
- **Alternative solutions**: Other approaches you've considered

### Contributing Code

1. **Pick an issue** or create one describing what you want to work on
2. **Create a branch**: `git checkout -b feature/your-feature-name`
3. **Make your changes**: Write code, add tests, update documentation
4. **Run tests**: Ensure all tests pass
5. **Commit**: Use clear, descriptive commit messages
6. **Push**: `git push origin feature/your-feature-name`
7. **Create Pull Request**: Open a PR with a clear description

## Style Guidelines

### Python Code

- Follow [PEP 8](https://pep8.org/)
- Use [Black](https://black.readthedocs.io/) for code formatting (line length: 100)
- Use type hints where appropriate
- Write docstrings for public functions and classes
- Keep functions focused and concise

### Django Templates

- Use 4 spaces for indentation
- Keep template logic simple
- Add comments for complex template sections
- Follow Django template naming conventions

### Git Commits

Use conventional commits format:

```
type(scope): subject

body (optional)

footer (optional)
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

Examples:
```
feat(layout): add Alert component
fix(templates): correct checkbox styling issue
docs(readme): add installation instructions
```

## Testing

### Writing Tests

- Write tests for all new features
- Ensure tests are isolated and repeatable
- Use descriptive test names
- Aim for high code coverage (>80%)

### Test Structure

```python
# tests/test_feature.py
import pytest
from django.test import TestCase


class TestFeature(TestCase):
    def setUp(self):
        """Set up test fixtures"""
        pass
    
    def test_expected_behavior(self):
        """Test should do X when Y happens"""
        # Arrange
        # Act
        # Assert
        pass
```

## Pull Request Process

1. **Update Documentation**: Update README.md, CHANGELOG.md if needed
2. **Add Tests**: Ensure your changes are covered by tests
3. **Pass CI Checks**: All automated checks must pass
4. **Get Review**: Wait for maintainer review
5. **Address Feedback**: Make requested changes
6. **Merge**: Maintainer will merge after approval

### PR Checklist

- [ ] Code follows the style guidelines
- [ ] All tests pass locally
- [ ] Added tests for new functionality
- [ ] Updated documentation
- [ ] Updated CHANGELOG.md
- [ ] Commit messages are clear and descriptive
- [ ] No merge conflicts

## Questions?

Feel free to:

- Open a [discussion](https://github.com/JhonatanRian/crispy_neurobrutalist/discussions)
- Ask in an issue
- Email: jhonatanrian@zohomail.com

## License Note

By contributing, you agree that your contributions will be licensed under the same CC BY-NC 4.0 License that covers the project. This means your contributions cannot be used for commercial purposes.

Thank you for contributing! 🚀
