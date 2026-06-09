import json
from pathlib import Path

from models import Book


DATA_DIR = Path(__file__).parent / "data"
BOOKS_FILE = DATA_DIR / "books.json"


def ensure_storage():
    DATA_DIR.mkdir(exist_ok=True)
    if not BOOKS_FILE.exists():
        BOOKS_FILE.write_text("[]", encoding="utf-8")


def load_books():
    try:
        raw_books = json.loads(BOOKS_FILE.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return []
    except json.JSONDecodeError as error:
        print(f"Warning: books.json is not valid JSON. Starting with an empty list. ({error})")
        return []

    if not isinstance(raw_books, list):
        print("Warning: books.json must contain a list. Starting with an empty list.")
        return []

    books = []
    skipped_count = 0
    for item in raw_books:
        try:
            books.append(Book.from_dict(item))
        except (KeyError, ValueError, TypeError):
            skipped_count += 1

    if skipped_count:
        print(f"Warning: skipped {skipped_count} invalid saved book record(s).")

    return books


def save_books(books):
    ensure_storage()
    data = [book.to_dict() for book in books]
    BOOKS_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
