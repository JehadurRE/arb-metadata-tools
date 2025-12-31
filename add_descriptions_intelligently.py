#!/usr/bin/env python3
"""
Intelligent ARB Description Generator
======================================

Automatically generates contextual descriptions for Flutter ARB localization
file metadata based on key names and values.

This tool uses pattern recognition and natural language processing to generate
meaningful descriptions for ARB metadata, making your localization files more
maintainable and developer-friendly.

Author: Md. Jehadur Rahman Emran
License: MIT
Repository: https://github.com/JehadurRE/arb-metadata-tools
"""

import json
import re
import sys
from pathlib import Path
from typing import Dict, Any, Tuple


# Mapping of key patterns to description templates
DESCRIPTION_PATTERNS = {
    # Labels
    r'.*Label$': 'Label for {field} input field',
    r'.*Hint$': 'Placeholder or hint text for {field} field',
    r'.*Desc$': 'Description text for {field}',
    r'.*Bn$': 'Bengali translation for {field}',
    
    # Actions/Buttons
    r'^send.*': 'Button text to send {action}',
    r'^resend.*': 'Button text to resend {action}',
    r'^enter.*': 'Placeholder text to enter {field}',
    r'^please.*': 'Validation or instruction message',
    r'^confirm.*': 'Confirmation action or dialog',
    r'^create.*': 'Action to create {item}',
    r'^go.*': 'Navigation action',
    r'^continue.*': 'Button to continue to next step',
    
    # Status/Messages
    r'.*Successful$': 'Success message when {action} completes successfully',
    r'.*Failed$': 'Error message when {action} fails',
    r'.*Error$': 'Error message for {issue}',
    r'.*Warning$': 'Warning message about {issue}',
    r'.*Note$': 'Informational note about {topic}',
    r'.*Message$': 'Message displayed to user',
    
    # Validation
    r'^.*Must.*': 'Validation error message',
    r'^invalid.*': 'Validation error for invalid {field}',
    
    # Screens/Sections
    r'.*Dashboard$': 'Dashboard screen or section title',
    r'.*Screen$': 'Screen title or heading',
    r'.*Management$': 'Management section or feature title',
    r'.*History$': 'History or past records section',
    r'.*Details$': 'Detailed information section',
    r'.*Information$': 'Information display section',
}


def camel_case_to_words(text: str) -> str:
    """
    Convert camelCase or PascalCase to space-separated words.
    
    Args:
        text: The camelCase string
        
    Returns:
        Space-separated lowercase words
    """
    # Insert space before uppercase letters
    words = re.sub(r'([A-Z])', r' \1', text).strip().lower()
    return words


def generate_description(key: str, value: str) -> str:
    """
    Generate a contextual description based on key name and value.
    
    Args:
        key: The ARB key name
        value: The localized text value
        
    Returns:
        A contextual description for the metadata
    """
    # Check if it's already a good description based on value
    if value and len(value) > 10 and not value.startswith('{'):
        # Use the value itself as basis for description
        if '?' in value:
            return f"Question: {value[:50]}..."
        elif value.endswith('!'):
            return f"Exclamation or emphasis: {value[:50]}..."
        elif value.endswith(':'):
            return f"Label: {value[:50]}..."
    
    # Extract meaningful parts from key name
    words = camel_case_to_words(key)
    
    # Check patterns
    for pattern, template in DESCRIPTION_PATTERNS.items():
        if re.match(pattern, key, re.IGNORECASE):
            # Extract context from key name
            field = words.replace('label', '').replace('hint', '').replace('desc', '').strip()
            action = words.replace('send', '').replace('resend', '').strip()
            item = words.replace('create', '').strip()
            issue = words.replace('error', '').replace('warning', '').strip()
            topic = words.replace('note', '').strip()
            
            desc = template.format(
                field=field or 'input',
                action=action or 'action',
                item=item or 'item',
                issue=issue or 'issue',
                topic=topic or 'topic'
            )
            return desc
    
    # Default: use the value or key as description
    if value and len(value) < 100:
        return f"Text: '{value}'"
    else:
        return f"Localization key for {words}"


def add_descriptions(file_path: str, verbose: bool = True) -> int:
    """
    Add intelligent descriptions to ARB file metadata.
    
    Args:
        file_path: Path to the ARB file
        verbose: Whether to print progress for each key
        
    Returns:
        Number of descriptions added
        
    Raises:
        FileNotFoundError: If the ARB file doesn't exist
        json.JSONDecodeError: If the ARB file is not valid JSON
    """
    path = Path(file_path)
    
    if not path.exists():
        raise FileNotFoundError(f"ARB file not found: {file_path}")
    
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    updated_count = 0
    
    # Process each key
    keys_to_process = [k for k in data.keys() 
                      if not k.startswith('@') and not k.startswith('@@')]
    
    for key in keys_to_process:
        metadata_key = f'@{key}'
        value = data[key]
        
        # Check if metadata exists and has empty description
        if metadata_key in data:
            if 'description' in data[metadata_key] and data[metadata_key]['description'] == '':
                # Generate and add description
                description = generate_description(key, value)
                data[metadata_key]['description'] = description
                updated_count += 1
                
                if verbose:
                    print(f"  {key}: {description[:60]}...")
    
    # Write back
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    return updated_count


def main():
    """Main entry point for the script."""
    # Configure these paths for your project
    arb_files = [
        'lib/l10n/app_en.arb',
        'lib/l10n/app_bn.arb'
    ]
    
    print("Intelligent ARB Description Generator")
    print("=" * 50)
    print()
    
    total_updated = 0
    
    for arb_file in arb_files:
        try:
            print(f"Processing: {arb_file}")
            count = add_descriptions(arb_file, verbose=False)
            total_updated += count
            print(f"✓ Updated {count} descriptions")
            print()
        except FileNotFoundError as e:
            print(f"✗ Error: {e}")
            sys.exit(1)
        except json.JSONDecodeError as e:
            print(f"✗ Invalid JSON in {arb_file}: {e}")
            sys.exit(1)
        except Exception as e:
            print(f"✗ Unexpected error: {e}")
            sys.exit(1)
    
    print("=" * 50)
    print(f"✓ Complete! Updated {total_updated} descriptions total")


if __name__ == '__main__':
    main()
