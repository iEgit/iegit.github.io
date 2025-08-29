#!/usr/bin/env python3
"""
Simple Jupyter Notebook to Jekyll Post Converter

This script helps convert basic Jupyter notebook content to Jekyll markdown
format with our custom notebook styling.

Usage:
    python convert_notebook.py input.ipynb output.md

Note: This is a basic converter. For complex notebooks with plots and rich outputs,
manual conversion may be needed.
"""

import json
import sys
import re
from datetime import datetime

def convert_cell(cell, cell_index):
    """Convert a single notebook cell to HTML/markdown format."""
    cell_type = cell.get('cell_type', '')
    source = ''.join(cell.get('source', []))
    
    if cell_type == 'code':
        # Code cell
        execution_count = cell.get('execution_count') or cell_index
        outputs = cell.get('outputs', [])
        
        html = f'<div class="cell code-cell">\n'
        html += f'<div class="cell-input">\n'
        html += f'<div class="prompt in-prompt" data-count="{execution_count}"></div>\n'
        html += f'<pre><code class="language-python">{source}</code></pre>\n'
        html += f'</div>\n'
        
        # Process outputs
        for output in outputs:
            output_type = output.get('output_type', '')
            if output_type == 'stream':
                text = ''.join(output.get('text', []))
                html += f'<div class="cell-output text-output">\n'
                html += f'<div class="prompt out-prompt" data-count="{execution_count}"></div>\n'
                html += f'<pre>{text}</pre>\n'
                html += f'</div>\n'
            elif output_type == 'execute_result' or output_type == 'display_data':
                data = output.get('data', {})
                if 'text/plain' in data:
                    text = ''.join(data['text/plain'])
                    html += f'<div class="cell-output text-output">\n'
                    html += f'<div class="prompt out-prompt" data-count="{execution_count}"></div>\n'
                    html += f'<pre>{text}</pre>\n'
                    html += f'</div>\n'
                if 'text/html' in data:
                    html_content = ''.join(data['text/html'])
                    html += f'<div class="cell-output html-output">\n'
                    html += html_content
                    html += f'</div>\n'
        
        html += f'</div>\n\n'
        return html
        
    elif cell_type == 'markdown':
        # Markdown cell
        html = f'<div class="cell markdown-cell">\n'
        html += f'<div class="cell-input">\n'
        html += source
        html += f'</div>\n'
        html += f'</div>\n\n'
        return html
    
    return ''

def convert_notebook(input_file, output_file):
    """Convert a Jupyter notebook to Jekyll markdown format."""
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            notebook = json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        return False
    except json.JSONDecodeError:
        print(f"Error: '{input_file}' is not a valid JSON file.")
        return False
    
    cells = notebook.get('cells', [])
    
    # Extract title from first markdown cell or use filename
    title = input_file.replace('.ipynb', '').replace('_', ' ').replace('-', ' ').title()
    first_cell = cells[0] if cells else None
    if first_cell and first_cell.get('cell_type') == 'markdown':
        source = ''.join(first_cell.get('source', []))
        match = re.search(r'^#\s+(.+)$', source, re.MULTILINE)
        if match:
            title = match.group(1).strip()
    
    # Generate Jekyll front matter
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S +0000')
    filename_date = datetime.now().strftime('%Y-%m-%d')
    
    front_matter = f"""---
layout: notebook
title: "{title}"
date: {date}
categories: data-science python jupyter
author: Your Name
excerpt: "A notebook post converted from Jupyter notebook."
notebook_url: "https://github.com/your-repo/{input_file}"
---

# {title}

*This post was converted from a Jupyter notebook.*

"""
    
    # Convert cells
    content = front_matter
    for i, cell in enumerate(cells[1:], 1):  # Skip first cell if it's the title
        content += convert_cell(cell, i)
    
    # Write output
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Successfully converted '{input_file}' to '{output_file}'")
        print(f"Suggested filename: {filename_date}-{title.lower().replace(' ', '-')}.md")
        return True
    except IOError:
        print(f"Error: Could not write to '{output_file}'")
        return False

def main():
    if len(sys.argv) != 3:
        print("Usage: python convert_notebook.py input.ipynb output.md")
        print("\nExample:")
        print("  python convert_notebook.py my_analysis.ipynb _posts/2024-12-19-my-analysis.md")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    if not input_file.endswith('.ipynb'):
        print("Error: Input file must be a .ipynb file")
        sys.exit(1)
    
    if not output_file.endswith('.md'):
        print("Error: Output file must be a .md file")
        sys.exit(1)
    
    success = convert_notebook(input_file, output_file)
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()