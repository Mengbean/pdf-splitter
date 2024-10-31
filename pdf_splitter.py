from PyPDF2 import PdfReader, PdfWriter
import time
import argparse
import os

def split_long_pdf(input_path, output_path=None, num_pages=2):
    """
    Split a single long PDF page into multiple equal-sized pages.
    
    Args:
        input_path (str): Path to the input PDF file
        output_path (str, optional): Path for the output PDF file. If not provided,
                                   will create in the same directory as input file
        num_pages (int): Number of pages to split the PDF into
    """
    # Validate input file exists
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    # Generate output path if not provided
    if output_path is None:
        file_name = os.path.splitext(input_path)[0]
        output_path = f"{file_name}_split.pdf"
    
    print(f"Starting PDF processing for: {input_path}")
    
    # Create PDF reader object
    pdf_reader = PdfReader(input_path)
    
    if len(pdf_reader.pages) != 1:
        raise ValueError("This script is designed for PDFs with a single long page. "
                        f"Your PDF has {len(pdf_reader.pages)} pages.")
    
    # Create PDF writer object
    pdf_writer = PdfWriter()
    
    # Get the first page
    page = pdf_reader.pages[0]
    
    # Get original page dimensions
    original_width = float(page.mediabox.width)
    original_height = float(page.mediabox.height)
    
    print(f"Original page dimensions: {original_width:.0f}x{original_height:.0f} points")
    
    # Calculate height for each new page
    page_height = original_height / num_pages
    print(f"Each new page will be {original_width:.0f}x{page_height:.0f} points")
    
    # Split the page
    for i in range(num_pages):
        print(f"Processing section {i+1} of {num_pages}...")
        
        try:
            # Create a new page by copying the original
            new_page = pdf_writer.add_page(page)
            
            # Calculate the crop box for this section
            lower_y = original_height - (i + 1) * page_height
            upper_y = original_height - i * page_height
            
            # Set the crop box to show only the relevant portion
            new_page.mediabox.lower_left = (0, lower_y)
            new_page.mediabox.upper_right = (original_width, upper_y)
            
        except Exception as e:
            print(f"Error processing section {i+1}: {str(e)}")
            continue
    
    print(f"Writing output to: {output_path}")
    # Write the output PDF file
    try:
        with open(output_path, 'wb') as output_file:
            pdf_writer.write(output_file)
    except PermissionError:
        raise PermissionError(f"Unable to write to {output_path}. Check file permissions.")
    except Exception as e:
        raise Exception(f"Error writing output file: {str(e)}")
            
    print(f"Successfully split into {num_pages} pages")
    print(f"Output saved to: {output_path}")

def main():
    # Create argument parser
    parser = argparse.ArgumentParser(
        description='Split a single long PDF page into multiple equal-sized pages.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python pdf_splitter.py input.pdf -p 5
    python pdf_splitter.py input.pdf -o output.pdf -p 3
    python pdf_splitter.py -i input.pdf --pages 4
        """
    )
    
    parser.add_argument('input', nargs='?', help='Input PDF file')
    parser.add_argument('--input', '-i', help='Input PDF file (alternative way)')
    parser.add_argument('--output', '-o', help='Output PDF file (optional)')
    parser.add_argument('--pages', '-p', type=int, default=2,
                       help='Number of pages to split into (default: 2)')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Get input file from either positional or named argument
    input_file = args.input if args.input else args.input
    
    if not input_file:
        parser.error("Please provide an input PDF file")
    
    try:
        start_time = time.time()
        split_long_pdf(input_file, args.output, args.pages)
        end_time = time.time()
        
        print(f"Total processing time: {end_time - start_time:.2f} seconds")
    except Exception as e:
        print(f"Error: {str(e)}")
        exit(1)

if __name__ == "__main__":
    main()