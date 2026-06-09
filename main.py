from models import Book, BookManager
from storage import ensure_storage, load_books, save_books


def read_required_text(label):
    while True:
        value = input(f"{label}: ").strip()
        if value:
            return value
        print(f"Error: {label.lower()} cannot be empty.")


def read_year():
    while True:
        try:
            year = int(input("Publication year: ").strip())
            return Book.validate_year(year)
        except ValueError as error:
            print(f"Error: {error}")


def add_book(manager):
    try:
        title = read_required_text("Title")
        author = read_required_text("Author")
        year = read_year()
        manager.add_book(Book(title, author, year))
        save_books(manager.get_all_books())
        print("Book was added.")
    except (TypeError, ValueError) as error:
        print(f"Error: {error}")


def show_books(manager):
    books = manager.get_all_books()
    print("\n--- Book List ---")
    if not books:
        print("No books yet.")
        return
    for index, book in enumerate(books, start=1):
        print(f"{index}. {book}")


def search_book(manager):
    title = read_required_text("Enter title to search")
    print("\n--- Search Result ---")
    try:
        results = manager.search_by_title(title)
    except ValueError as error:
        print(f"Error: {error}")
        return

    if not results:
        print("Book was not found.")
        return
    for book in results:
        print(book)


def main():
    ensure_storage()
    manager = BookManager(load_books())

    while True:
        print("\n=== Book Manager ===")
        print("1. Add book")
        print("2. Show all books")
        print("3. Search book")
        print("4. Exit")

        choice = input("Choose: ").strip()
        if choice == "1":
            add_book(manager)
        elif choice == "2":
            show_books(manager)
        elif choice == "3":
            search_book(manager)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Error: choose 1-4.")


if __name__ == "__main__":
    main()
