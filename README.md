# PDF Page Splitter

A Python script to split a single long PDF page into multiple equal-sized pages. This tool is particularly useful for splitting long scrollable PDFs into standard-sized pages.

## Features

- Split one long PDF page into multiple equal-sized pages
- Automatically maintains aspect ratio
- Supports custom number of output pages
- Preserves original PDF quality
- Command-line interface with multiple input options

## Prerequisites

- Python 3.6 or higher
- PyPDF2 library

## Installation

1. Clone this repository or download the `pdf_splitter.py` file

2. Install the required dependency:
```bash
pip install PyPDF2
```

## Usage

The script can be used in several ways:

### Basic Usage
```bash
python pdf_splitter.py input.pdf -p 5
```
This will split `input.pdf` into 5 equal pages and save as `input_split.pdf`

### Specify Output File
```bash
python pdf_splitter.py input.pdf -o output.pdf -p 3
```
This will split `input.pdf` into 3 pages and save as `output.pdf`

### Alternative Input Format
```bash
python pdf_splitter.py -i input.pdf --pages 4
```
This will split `input.pdf` into 4 pages

### Command Line Arguments

- `input.pdf`: Input PDF file (positional argument)
- `-i, --input`: Input PDF file (alternative way)
- `-o, --output`: Output PDF file (optional)
- `-p, --pages`: Number of pages to split into (default: 2)
- `-h, --help`: Show help message

## Examples

1. Split a PDF into 2 pages (default):
```bash
python pdf_splitter.py document.pdf
```

2. Split a PDF into 5 pages with custom output name:
```bash
python pdf_splitter.py document.pdf -o split_document.pdf -p 5
```

3. Using named input argument:
```bash
python pdf_splitter.py -i document.pdf --pages 3
```

## Limitations

- The script only works with PDFs that have a single page
- The input PDF must be accessible and readable
- You need write permissions in the output directory

## Error Handling

The script includes error handling for common issues:
- Input file not found
- Permission errors
- Multi-page PDF input
- Processing errors

## Output

The script will:
1. Show the original page dimensions
2. Display progress for each section being processed
3. Indicate where the output file is saved
4. Show total processing time

## Troubleshooting

If you encounter errors:

1. Ensure your PDF has only one page
2. Check file permissions
3. Verify PyPDF2 is installed correctly
4. Make sure the input PDF is not corrupted
5. Check if you have write access to the output location

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
