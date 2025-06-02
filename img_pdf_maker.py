import os
import subprocess
from pypdf import PdfWriter


def create_pdfs_from_folders():
    cwd = os.getcwd()

    pdf_dir = os.path.join(cwd, 'PDFs')

    if os.path.exists(pdf_dir):
        if input("'PDFs' directory already exists and may contain generated PDFs. Do you want to continue? (Y/n)") == 'Y':
            os.makedirs(pdf_dir, exist_ok=True)
        else:
            print("Exiting...")
            exit(0)
    else:
        os.makedirs(pdf_dir, exist_ok=True)

    for dir in os.listdir(cwd):
    
        # Skip files
        if not os.path.isdir(dir):
            continue

        folder_path = os.path.join(cwd, dir)
        
        # Check for JPG or PNG files in the folder. If none, then skip.
        # If other file types are present, you may add the required code.
        jpg_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.jpg')]
        png_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.png')]
        if not jpg_files and not png_files:
            print(f"Skipping '{dir}' directory as it has no JPG or PNG images")
            continue

        pdf_name = os.path.join(pdf_dir, f"{dir}.pdf")
        if jpg_files:
            command = ["magick", f"{folder_path}/*.jpg", pdf_name]
        else:
            command = ["magick", f"{folder_path}/*.png", pdf_name]

        try:
            subprocess.run(command, check=True)
            print(f"PDF created for {dir}")
        except Exception as e:
            print(f"Could not create PDF: {e}")
            exit(1)

def combine_pdfs(pdf_dir):
    """
        Combines the generated PDFs into one PDF. This function can be used independently too.
    """
    pdfs = [f for f in os.listdir(pdf_dir) if f.endswith('.pdf')]
    merger = PdfWriter()
    for pdf in pdfs:
        merger.append(os.path.join(pdf_dir, pdf))
    merger.write("combined.pdf")
    merger.close()

if __name__ == "__main__":
    try:
        create_pdfs_from_folders()
        combine_pdfs(os.path.join(os.getcwd(), 'PDFs'))
    except Exception as e:
        print(f"ERROR: PDF could not be created properly. {e}")
