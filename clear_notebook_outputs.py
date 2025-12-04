#!/usr/bin/env python3
"""Clear all outputs from Jupyter notebooks to prevent sensitive data leaks."""

import json
import sys

def clear_notebook_outputs(notebook_path):
    """Clear all cell outputs from a Jupyter notebook."""
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    # Clear outputs from all code cells
    for cell in notebook.get('cells', []):
        if cell.get('cell_type') == 'code':
            cell['outputs'] = []
            cell['execution_count'] = None
    
    # Write back to file
    with open(notebook_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, ensure_ascii=False, indent=1)
    
    print(f"✅ Cleared outputs from: {notebook_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python clear_notebook_outputs.py <notebook_path>")
        sys.exit(1)
    
    notebook_path = sys.argv[1]
    clear_notebook_outputs(notebook_path)
