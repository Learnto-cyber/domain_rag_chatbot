from pathlib import Path
from pypdf import PdfReader


class PDFLoader:

    def __init__(self):
        self.documents = []

    def load_pdf(self, pdf_path):

        print(f"\nOpening: {pdf_path}")

        reader = PdfReader(pdf_path)

        print(f"Total pages: {len(reader.pages)}")

        extracted_pages = []

        for page_number, page in enumerate(reader.pages, start=1):

            try:

                text = page.extract_text()

                print(f"\nPage {page_number}")
                print("Extracted Text:", repr(text))

                if not text:
                    print("No text found.")
                    continue

                extracted_pages.append({
                    "document": Path(pdf_path).name,
                    "page": page_number,
                    "text": text.strip()
                })

            except Exception as e:
                print(f"Error: {e}")

        print(f"Extracted {len(extracted_pages)} pages")

        return extracted_pages

    def load_all_documents(self, folder):

        folder = Path(folder)

        self.documents = []

        print(f"\nSearching PDFs in: {folder.resolve()}")

        pdf_files = list(folder.glob("*.pdf"))

        print(f"Found {len(pdf_files)} PDF(s)")

        for pdf_file in pdf_files:

            print(f"Processing {pdf_file.name}")

            pages = self.load_pdf(pdf_file)

            self.documents.extend(pages)

        return self.documents