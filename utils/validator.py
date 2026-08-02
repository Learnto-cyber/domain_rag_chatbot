import os

ALLOWED_EXTENSIONS = [".pdf"]


def is_pdf(filename):
    """
    Check whether the uploaded file is a PDF.
    """
    _, extension = os.path.splitext(filename)
    return extension.lower() in ALLOWED_EXTENSIONS


def get_file_size(file):
    """
    Return uploaded file size in bytes.
    """
    file.seek(0, os.SEEK_END)
    size = file.tell()
    file.seek(0)
    return size