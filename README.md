# 06 Book Manager OOP

Console book management application written in Python with object-oriented design.

## Features

- Add a book with title, author, and publication year.
- Show all saved books.
- Search books by title using case-insensitive partial matching.
- Validate empty text, invalid years, and corrupted saved records.
- Save books in `data/books.json`.

## OOP Structure

- `LibraryItem` is an abstract base class.
- `Book` inherits from `LibraryItem`, encapsulates title, author, and year, and validates its own state.
- `BookManager` manages a private list of `Book` objects and exposes methods for adding, listing, and searching.

## Run

```powershell
python main.py
```

## Example

```text
=== Book Manager ===
1. Add book
2. Show all books
3. Search book
4. Exit
Choose: 1
Title: Clean Code
Author: Robert C. Martin
Publication year: 2008
Book was added.

Choose: 2
--- Book List ---
1. Clean Code - Robert C. Martin (2008)

Choose: 3
Enter title to search: clean
--- Search Result ---
Clean Code - Robert C. Martin (2008)

Choose: 4
Goodbye!
```
