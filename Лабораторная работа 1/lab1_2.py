# TODO Найдите количество книг, которое можно разместить на дискете
symbols_per_row=25
rows_per_page=50
pages_per_book=100
bytes_per_symbol=4
mbs_on_disk=1.44
kbs_per_mb=1024
bs_per_kb=1024
book_symbol_count=symbols_per_row*rows_per_page*pages_per_book
bytes_per_book=book_symbol_count*bytes_per_symbol
bytes_on_disk=mbs_on_disk*kbs_per_mb*bs_per_kb
books_on_disk=int(bytes_on_disk//bytes_per_book)
print("Количество книг, помещающихся на дискету:", books_on_disk)
