class Book:
    def __init__(self, book_id, title, author, year):
        self.id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = "Available"
        self.borrowed_by = None

    def display(self):
        return f"{self.id} {self.title} {self.author} {self.year} {self.status}"


class Reader:
    def __init__(self, reader_id, name):
        self.id = reader_id
        self.name = name
        self.borrowed_books = []

    def display(self):
        return f"{self.id} {self.name}"


class Library:
    def __init__(self):
        self.books = {}
        self.readers = {}

    def add_book(self, book):
        self.books[book.id] = book

    def add_reader(self, reader):
        self.readers[reader.id] = reader

    def borrow_book(self, reader_id, book_id):
        if reader_id in self.readers and book_id in self.books:
            reader = self.readers[reader_id]
            book = self.books[book_id]
            if book.status == "Available" and len(reader.borrowed_books) < 5:
                book.status = "Borrowed"
                book.borrowed_by = reader_id
                reader.borrowed_books.append(book_id)

    def return_book(self, reader_id, book_id):
        if reader_id in self.readers and book_id in self.books:
            reader = self.readers[reader_id]
            book = self.books[book_id]
            if book.status == "Borrowed" and book.borrowed_by == reader_id:
                book.status = "Available"
                book.borrowed_by = None
                if book_id in reader.borrowed_books:
                    reader.borrowed_books.remove(book_id)

    def display_books(self):
        result = []
        for book in self.books.values():
            result.append(book.display())
        return result

    def display_readers(self):
        result = []
        for reader in self.readers.values():
            result.append(reader.display())
        return result


def solve(data):
    """
    Ham giai bai toan chinh.
    - data: danh sach cac lenh da duoc doc tu input.
    - Tra ve: list chua cac dong ket qua (string).
    """
    library = Library()
    result = []
    
    for line in data:
        parts = line.strip().split()
        if not parts:
            continue
            
        command = parts[0]
        
        if command == "ADD_BOOK":
            book_id = parts[1]
            # Tim title va author trong dau ngoac kep
            line_str = line.strip()
            first_quote = line_str.find('"')
            second_quote = line_str.find('"', first_quote + 1)
            title = line_str[first_quote + 1:second_quote]
            
            remaining = line_str[second_quote + 1:].strip()
            third_quote = remaining.find('"')
            fourth_quote = remaining.find('"', third_quote + 1)
            author = remaining[third_quote + 1:fourth_quote]
            
            year_str = remaining[fourth_quote + 1:].strip()
            year = int(year_str)
            
            book = Book(book_id, title, author, year)
            library.add_book(book)
            
        elif command == "ADD_READER":
            reader_id = parts[1]
            # Tim name trong dau ngoac kep
            line_str = line.strip()
            first_quote = line_str.find('"')
            second_quote = line_str.find('"', first_quote + 1)
            name = line_str[first_quote + 1:second_quote]
            
            reader = Reader(reader_id, name)
            library.add_reader(reader)
            
        elif command == "BORROW_BOOK":
            reader_id = parts[1]
            book_id = parts[2]
            library.borrow_book(reader_id, book_id)
            
        elif command == "RETURN_BOOK":
            reader_id = parts[1]
            book_id = parts[2]
            library.return_book(reader_id, book_id)
            
        elif command == "DISPLAY_BOOKS":
            result.extend(library.display_books())
            
        elif command == "DISPLAY_READERS":
            result.extend(library.display_readers())
    
    return result


def main():
    data = []
    n = int(input().strip())  # so luong lenh
    for _ in range(n):
        line = input().strip()
        data.append(line)
    
    res = solve(data)
    if res:
        print("\n".join(map(str, res)))


if __name__ == "__main__":
    main()