books = input().split('&')

while True:
    command = input().split(' | ')

    if command[0] == 'Done':
        print(*books, sep=', ')
        break

    elif command[0] == 'Add Book':
        book_name = command[1]

        if book_name not in books:
            books.insert(0, book_name)

    elif command[0] == 'Take Book':
        book_name = command[1]

        if book_name in books:
            books.remove(book_name)

    elif command[0] == 'Swap Books':
        book1 = command[1]
        book2 = command[2]

        if book1 in books and book2 in books:
            book1_index = books.index(book1)
            book2_index = books.index(book2)

            books[book1_index], books[book2_index] = books[book2_index], books[book1_index]

    elif command[0] == 'Insert Book':
        book_name = command[1]

        if book_name not in books:
            books.append(book_name)

    elif command[0] == 'Check Book':
        index = int(command[1])

        if 0 <= index < len(books):
            print(books[index])
