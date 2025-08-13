import os

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
    Hàm giải bài toán chính.
    - data: danh sách các lệnh đã được đọc từ input.
    - Trả về: list chứa các dòng kết quả (string).
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
            # Tìm title và author trong dấu ngoặc kép
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
            # Tìm name trong dấu ngoặc kép
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


def prepare_working_dir():
    """
    Chuyển thư mục làm việc về nơi chứa script hiện tại.
    Tìm và trả về danh sách tất cả các file .in trong thư mục đó.
    """
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)
    in_files = [f for f in os.listdir(".") if f.lower().endswith(".in")]
    return in_files


def process_file(infile):
    """
    Xử lý một file .in và tạo file .out tương ứng.
    """
    outfile = infile.rsplit(".", 1)[0] + ".out"
    print(f"Đang xử lý {infile} -> {outfile} ...")
    with open(infile, "r", encoding="utf-8") as fin, open(outfile, "w", encoding="utf-8") as fout:
        # Đọc dữ liệu từ file input
        lines = fin.readlines()
        n = int(lines[0].strip())
        data = []
        for i in range(1, n + 1):
            data.append(lines[i].rstrip())
        
        # Gọi hàm giải
        res = solve(data)
        
        # Ghi kết quả ra file output
        if res:
            fout.write("\n".join(map(str, res)) + "\n")


def main():
    """
    Hàm chính: tìm các file input, xử lý từng file, tạo file output.
    """
    in_files = prepare_working_dir()
    if not in_files:
        print("Không tìm thấy file .in nào trong", os.getcwd())
        return
    for infile in sorted(in_files):
        process_file(infile)


if __name__ == "__main__":
    main()