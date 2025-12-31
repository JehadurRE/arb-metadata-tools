# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.1.0] - 2025-01-01

### Added
- Proper `--help` command-line argument support
- `--version` flag to display version information
- Command-line argument parsing with `argparse`
- Ability to specify custom ARB files as arguments
- `--verbose` flag for `arb-descriptions` to show each description being added
- Comprehensive help text with usage examples
- Better error messages and user guidance

### Changed
- Improved command-line interface with proper argument handling
- Enhanced documentation in help text
- Better user experience with informative help messages

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

---

[1.1.0]: https://github.com/JehadurRE/arb-metadata-tools/releases/tag/v1.1.0
[1.0.0]: https://github.com/JehadurRE/arb-metadata-tools/releases/tag/v1.0.0
