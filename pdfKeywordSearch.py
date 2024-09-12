import os
import fitz  # PyMuPDF


def search_keyword_in_pdf(pdf_path, keyword):
    """
    Search for a keyword in a PDF document.
    
    Args:
        pdf_path (str): The path to the PDF file.
        keyword (str): The keyword to search for.
    
    Returns:
        bool: True if the keyword is found, False otherwise.
    """
    try:
        doc = fitz.open(pdf_path)
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text = page.get_text("text")
            if keyword.lower() in text.lower():
                return True
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
        return False
    return False


def search_in_folder(folder_path, keyword):
    """
    Search for a keyword in all PDF files within a folder.
    
    Args:
        folder_path (str): The path to the folder containing PDFs.
        keyword (str): The keyword to search for.
    """
    found_files = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".pdf"):
                pdf_path = os.path.join(root, file)
                if search_keyword_in_pdf(pdf_path, keyword):
                    found_files.append(pdf_path)
    
    if found_files:
        print(f"Keyword '{keyword}' found in the following files:")
        for file in found_files:
            print(file)
    else:
        print(f"Keyword '{keyword}' not found in any PDF files in the folder.")


if __name__ == "__main__":
    folder_path = input("Enter the folder path containing PDF files: ")
    keyword = input("Enter the keyword to search for: ")
    
    search_in_folder(folder_path, keyword)
