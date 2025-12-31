#!/usr/bin/env python3
"""
ARB Metadata Generator
======================

Automatically adds empty metadata blocks to Flutter ARB localization files.

This tool solves the problem of Google ARB VS Code extension warnings about
missing metadata by adding empty metadata blocks to all keys that don't have them.

Author: Md. Jehadur Rahman Emran
License: MIT
Repository: https://github.com/JehadurRE/arb-metadata-tools
"""

import json
import sys
from pathlib import Path
from typing import Dict, Any


def add_metadata_to_arb(file_path: str) -> int:
    """
    Add empty metadata blocks to ARB file for keys without metadata.
    
    Args:
        file_path: Path to the ARB file
        
    Returns:
        Number of metadata blocks added
        
    Raises:
        FileNotFoundError: If the ARB file doesn't exist
        json.JSONDecodeError: If the ARB file is not valid JSON
    """
    path = Path(file_path)
    
    if not path.exists():
        raise FileNotFoundError(f"ARB file not found: {file_path}")
    
    # Read the file
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Create new ordered dict with metadata
    new_data: Dict[str, Any] = {}
    added_count = 0
    
    for key, value in data.items():
        # Add the key-value pair
        new_data[key] = value
        
        # If it's not a metadata key and doesn't have metadata, add empty metadata
        if not key.startswith('@') and not key.startswith('@@'):
            metadata_key = f'@{key}'
            if metadata_key not in data:
                # Add empty metadata block
                new_data[metadata_key] = {
                    "description": ""
                }
                added_count += 1
    
    # Write back to file with proper formatting
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(new_data, f, ensure_ascii=False, indent=2)
    
    return added_count


def main():
    """Main entry point for the script."""
    # Configure these paths for your project
    arb_files = [
        'lib/l10n/app_en.arb',
        'lib/l10n/app_bn.arb'
    ]
    
    print("ARB Metadata Generator")
    print("=" * 50)
    print()
    
    total_added = 0
    
    for arb_file in arb_files:
        try:
            print(f"Processing: {arb_file}")
            count = add_metadata_to_arb(arb_file)
            total_added += count
            print(f"✓ Added {count} metadata blocks")
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
    print(f"✓ Complete! Added {total_added} metadata blocks total")


if __name__ == '__main__':
    main()
