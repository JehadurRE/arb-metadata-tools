# ARB Metadata Tools for Flutter

<div align="center">

![PyPI version](https://img.shields.io/pypi/v/arb-metadata-tools.svg)
![PyPI downloads](https://img.shields.io/pypi/dm/arb-metadata-tools.svg)
![Python versions](https://img.shields.io/pypi/pyversions/arb-metadata-tools.svg)
![GitHub stars](https://img.shields.io/github/stars/JehadurRE/arb-metadata-tools?style=social)
![License](https://img.shields.io/github/license/JehadurRE/arb-metadata-tools)

</div>

A collection of Python scripts to automatically manage metadata in Flutter ARB (Application Resource Bundle) localization files.

## Problem

When using Flutter's localization with ARB files, the Google ARB VS Code extension shows warnings for keys without metadata. Manually adding metadata to hundreds of keys is tedious and time-consuming.

## Solution

These tools automatically add and manage metadata for your ARB files:

1. **add_arb_metadata.py** - Adds empty metadata blocks to all keys
2. **add_descriptions_intelligently.py** - Intelligently generates contextual descriptions based on key names and values

## Features

- ✅ Automatically adds metadata to all ARB keys
- ✅ Intelligently generates contextual descriptions
- ✅ Preserves existing metadata with placeholders
- ✅ Supports multiple ARB files
- ✅ Pattern-based description generation
- ✅ Handles bilingual keys (e.g., `*Bn` for Bengali)

## Installation

### Option 1: Install from PyPI (Recommended)

```bash
pip install arb-metadata-tools
```

### Option 2: Install from Source

```bash
# Clone the repository
git clone https://github.com/JehadurRE/arb-metadata-tools.git
cd arb-metadata-tools

# Install in development mode
pip install -e .

# Or install directly
pip install .
```

**Requirements:** Python 3.6+ (no external dependencies)

## Usage

After installation, you can use the command-line tools:

### Basic Metadata Addition

```bash
# If installed from PyPI
arb-metadata

# Or if running from source
python add_arb_metadata.py
```

This adds empty metadata blocks to all keys without metadata.

### Intelligent Description Generation

```bash
# If installed from PyPI
arb-descriptions

# Or if running from source
python add_descriptions_intelligently.py
```

This generates contextual descriptions based on:
- Key naming patterns (Label, Hint, Desc, etc.)
- Action verbs (send, create, confirm, etc.)
- Content analysis (questions, exclamations, labels)
- Context clues (Dashboard, Management, History, etc.)

## Examples

### Before
```json
{
  "loginButton": "Login",
  "enterPassword": "Enter your password"
}
```

### After
```json
{
  "loginButton": "Login",
  "@loginButton": {
    "description": "Button text to login to the application"
  },
  "enterPassword": "Enter your password",
  "@enterPassword": {
    "description": "Placeholder text to enter password field"
  }
}
```

## Configuration

### For Command-Line Usage

The tools look for ARB files in the standard Flutter location: `lib/l10n/`

### For Custom Paths

Edit the file paths in the scripts to match your project structure:

```python
arb_files = [
    'lib/l10n/app_en.arb',
    'lib/l10n/app_bn.arb',
    # Add more ARB files as needed
]
```

## Pattern Recognition

The intelligent description generator recognizes:

- **Labels**: `*Label` → "Label for {field} input field"
- **Hints**: `*Hint` → "Placeholder or hint text for {field}"
- **Actions**: `send*`, `create*`, `confirm*` → Action descriptions
- **Validation**: `please*`, `*Must*` → Validation messages
- **Status**: `*Successful`, `*Failed` → Status messages
- **Screens**: `*Dashboard`, `*Management` → Screen titles

## Requirements

- Python 3.6+
- No external dependencies

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - see LICENSE file for details

## 👨‍💻 Author

<div align="center">

### **Md. Jehadur Rahman Emran**
*Software Engineer • Researcher • Full-Stack Developer*

[![GitHub](https://img.shields.io/badge/GitHub-JehadurRE-black?style=flat&logo=github)](https://github.com/JehadurRE)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-jehadurre-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/jehadurre)
[![Twitter](https://img.shields.io/badge/Twitter-JehadurRE-blue?style=flat&logo=twitter)](https://x.com/JehadurRE)
[![Portfolio](https://img.shields.io/badge/Portfolio-jehadurre.icu-green?style=flat&logo=google-chrome)](https://portfolio.jehadurre.icu)
[![Email](https://img.shields.io/badge/Email-emran.jehadur@gmail.com-red?style=flat&logo=gmail)](mailto:emran.jehadur@gmail.com)

</div>

## Acknowledgments

Created to solve ARB metadata management for Flutter localization projects.

## Support

If you find this tool helpful, please ⭐ star the repository!

## Related

- [Flutter Internationalization](https://docs.flutter.dev/development/accessibility-and-localization/internationalization)
- [ARB Format Specification](https://github.com/google/app-resource-bundle)
