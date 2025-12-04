# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.5.0] - 2025-12-04

### Added
- ✅ **Static CSS file now included with package** - `neurobrutalist.css` automatically available
- ✅ Complete test suite with **65 unit tests** (96% code coverage)
- ✅ Tests for `CSSContainer` class (20 tests)
- ✅ Tests for all 9 layout components (45 tests)
- ✅ Pytest configuration in `pyproject.toml`
- ✅ Static files properly configured for Django's static system
- ✅ Development documentation in README (testing, contributing)

### Changed
- ⚠️ **BREAKING**: CSS path changed from `{% static 'css/neurobrutalist.css' %}` to `{% static 'crispy_neurobrutalist/css/neurobrutalist.css' %}`
- ⚠️ **BREAKING**: Must add `{% load static %}` in templates
- ✅ Updated all documentation (README, INSTALLATION, DOCS)
- ✅ Migrated pytest config from `pytest.ini` to `pyproject.toml`
- ✅ Cleaner package structure - removed redundant files

### Removed
- ❌ `MANIFEST.in` - redundant (Hatchling uses pyproject.toml)
- ❌ `pytest.ini` - migrated to pyproject.toml
- ❌ `tests/README.md` - info moved to main README
- ❌ Unnecessary README in static directory

### Fixed
- ✅ Static files now properly included in wheel distribution
- ✅ Package build works correctly with Hatchling
- ✅ All tests passing successfully

## [0.1.0] - 2024-12-04

### Added
- Initial release of crispy-neurobrutalist
- Neurobrutalist template pack for django-crispy-forms
- Custom template tags: `{% neo_field %}`
- Layout components: `Submit` and `Button` with color variants
- CSSContainer class for managing widget styles
- Support for all standard Django form widgets
- Tailwind CSS-based styling with custom neo-brutalist utilities
- Template filters: `crispy`, `as_crispy_field`, `as_crispy_errors`
- Widget-specific templates for enhanced customization

### Changed
- N/A

### Deprecated
- N/A

### Removed
- N/A

### Fixed
- N/A

### Security
- N/A

## [0.1.0] - 2025-12-03

### Added
- Initial development release
- Basic neurobrutalist styling for Django forms
- Integration with django-crispy-forms
- CC BY-NC 4.0 License

[Unreleased]: https://github.com/JhonatanRian/crispy_neurobrutalist/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/JhonatanRian/crispy_neurobrutalist/releases/tag/v0.1.0
