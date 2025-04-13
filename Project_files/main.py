import os
import openai
import json
from docx import Document
from odf.opendocument import OpenDocumentText
from odf.text import P
import fitz  # PyMuPDF

# ----------- TXT ----------
def read_txt_file(filepath):
    content = [f"\n📄 TXT FILE: {filepath}\n"]
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            content.extend(file.readlines())
    except Exception as e:
        content.append(f"Error reading .txt file: {e}\n")
    return content

# ----------- DOCX ----------
def read_docx_file(filepath):
    content = [f"\n📄 DOCX FILE: {filepath}\n"]
    try:
        doc = Document(filepath)
        for para in doc.paragraphs:
            content.append(para.text + "\n")
    except Exception as e:
        content.append(f"Error reading .docx file: {e}\n")
    return content

# ----------- ODT ----------
def read_odt_file(filepath):
    content = [f"\n📄 ODT FILE: {filepath}\n"]
    try:
        textdoc = OpenDocumentText(filepath)
        for element in textdoc.text.childNodes:
            if isinstance(element, P) and element.firstChild:
                content.append(element.firstChild.data + "\n")
    except Exception as e:
        content.append(f"Error reading .odt file: {e}\n")
    return content

# ----------- PDF ----------
def read_pdf_file(filepath):
    content = [f"\n📄 PDF FILE: {filepath}\n"]
    try:
        doc = fitz.open(filepath)
        for page_num, page in enumerate(doc):
            content.append(f"\n--- Page {page_num + 1} ---\n")
            content.append(page.get_text() + "\n")
    except Exception as e:
        content.append(f"Error reading .pdf file: {e}\n")
    return content

# ----------- MAIN ----------
if __name__ == "__main__":
    print("Choose the file type to open:")
    print("1 - TXT\n2 - DOCX\n3 - ODT\n4 - PDF")
    choice = input("Enter a number (1-4): ").strip()

    file_base = input("Enter the base file name (without extension): ").strip()

    # Automatically append the right extension
    extension_map = {"1": ".txt", "2": ".docx", "3": ".odt", "4": ".pdf"}
    extension = extension_map.get(choice)

    if not extension:
        print("❌ Invalid choice.")
        exit()

    file_path = os.path.abspath(file_base + extension)

    print(f"\n🔎 Looking for file: {file_path}")

    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        exit()
    else:
        print(f"📂 File found: {file_path}")

    # Read and combine content
    full_content = []

    if choice == "1":
        full_content += read_txt_file(file_path)
    elif choice == "2":
        full_content += read_docx_file(file_path)
    elif choice == "3":
        full_content += read_odt_file(file_path)
    elif choice == "4":
        full_content += read_pdf_file(file_path)

    # Output file
    output_path = "combined_output.txt"

    try:
        with open(output_path, "w", encoding="utf-8") as out_file:
            out_file.writelines(full_content)
        print(f"\n✅ All content successfully written to: {output_path}")
    except Exception as e:
        print(f"\n❌ Failed to write to {output_path}: {e}")