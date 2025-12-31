# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-01-01

### Added
- Initial release of ARB Metadata Tools
- `add_arb_metadata.py` - Adds empty metadata blocks to ARB files
- `add_descriptions_intelligently.py` - Generates contextual descriptions
- Pattern-based description generation for common key types
- Support for multiple ARB files
- Comprehensive README with usage examples
- MIT License
- Publishing guide for contributors

### Features
- Zero external dependencies (Python standard library only)
- Intelligent pattern recognition for:
  - Labels, hints, and descriptions
  - Action buttons (send, create, confirm, etc.)
  - Status messages (successful, failed, error, warning)
  - Validation messages
  - Screen and section titles
  - Bilingual keys (e.g., `*Bn` for Bengali)
- Preserves existing metadata with placeholders
- UTF-8 encoding support for international characters
- Proper JSON formatting with indentation

### Documentation
- Comprehensive README with installation and usage
- Code documentation with docstrings
- Publishing guide for open-source distribution
- MIT License for free use and modification

## [Unreleased]

### Planned
- Command-line arguments for custom file paths
- Configuration file support (`.arbrc`)
- Batch processing for large projects
- Custom pattern definitions
- Integration with CI/CD pipelines
- VS Code extension
- Support for other localization formats (JSON, XML)
- Unit tests
- GitHub Actions workflow

---

[1.0.0]: https://github.com/JehadurRE/arb-metadata-tools/releases/tag/v1.0.0
