disk_size_mb = 1.44  # Объем дискеты в Мб
pages_per_book = 100  # Количество страниц в книге
lines_per_page = 50  # Число строк на странице
chars_per_line = 25  # Количество символов в строке
bytes_per_char = 4  # Объем одного символа в байтах
disk_size_bytes = disk_size_mb * 1024 * 1024
# Вычисляем количество символов в одной книге
chars_per_book = pages_per_book * lines_per_page * chars_per_line
# Вычисляем объем одной книги в байтах
book_size_bytes = chars_per_book * bytes_per_char
# Вычисляем количество книг, помещающихся на дискету
books_on_disk = disk_size_bytes // book_size_bytes
print("Количество книг, помещающихся на дискету:", int(books_on_disk))