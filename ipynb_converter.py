import json
import os
import argparse
from functools import reduce

def process_cell(cell):
    if cell['cell_type'] == 'markdown':
        return ''.join(f"# {line}" for line in cell.get('source', [])) + "\n\n"    # If cell_type = markdown save it as a comment
    elif cell['cell_type'] == 'code':
        return ''.join(cell.get('source', [])) + "\n\n"    # If cell_type = code save it as python code
    return ''

def convert_ipynb_to_py(file_path):
    """
    Converts a Jupyter notebook (.ipynb) file to a Python (.py) file.
    Markdown cell content is converted to comments, and code cells are kept as code.
    Counts the number of "# Ćwiczenie" in the provided file.
    
    Parameters:
        ipynb_path (str): Path to the input .ipynb file.
    """
    
    if file_path.endswith(".ipynb") == False:
        print("Provide a ipynb file!")    # Check if the given file is in proper format
        
    print(f"Converting {file_path} to py")

    # Create the path to the python file we're creating
    py_path = os.path.splitext(file_path)[0] + '.py'

    # Read the data from the ipynb (json) file
    with open(file_path, 'r', encoding='utf-8') as in_file:
        notebook_data = json.load(in_file)

    # Extract cells and using "process_cell" convert them into proper format in the python file
    cells = notebook_data.get('cells', [])
    py_lines = list(map(process_cell, cells))

    # Write the lines into the python file
    with open(py_path, 'w') as out_file:
            print(*py_lines, file=out_file, sep='')
            
    print(f"Success! Saved to {py_path}")

    # Using reduce count the number of markdown cells with "# Ćwiczenie"
    count = reduce(
        lambda acc, cell: acc + (
            1 if cell['cell_type'] == 'markdown' and '# Ćwiczenie' in cell.get('source', [])[0] else 0
        ),
        notebook_data.get('cells', []), 0
    )

    # Print the final count
    print("Liczba ćwiczeń: "+ str(count))
    return

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert .ipynb to .py with Markdown as comments and code cells as code.")
    parser.add_argument("filepath", type=str, help="Path to the input .ipynb file")
    args = parser.parse_args()
    
    convert_ipynb_to_py(args.filepath)

