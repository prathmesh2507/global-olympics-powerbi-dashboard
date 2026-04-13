from pathlib import Path
from datetime import datetime

def sort_by_type(file_path):
    return file_path.suffix[1:].upper() or "NO_EXTENSION"


def sort_by_date(file_path, date_format):
    timestamp = file_path.stat().st_mtime
    return datetime.fromtimestamp(timestamp).strftime(date_format)


