from pathlib import Path

# Project Root
BASE_DIR = Path(__file__).resolve().parent

# Documents Folder
DOCUMENTS_DIR = BASE_DIR / "documents"

# Allowed File Types
ALLOWED_EXTENSIONS = [".pdf"]

# Maximum File Size (20 MB)
MAX_FILE_SIZE = 20 * 1024 * 1024

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DOCUMENTS_DIR = BASE_DIR / "documents"

EXTRACTED_TEXT_DIR = BASE_DIR / "extracted_text"

DOCUMENTS_DIR.mkdir(exist_ok=True)

EXTRACTED_TEXT_DIR.mkdir(exist_ok=True)