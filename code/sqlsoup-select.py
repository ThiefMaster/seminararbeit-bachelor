q = db.books
q = q.join(db.books.tags)
q = q.options(joinedload(db.books.tags))
q = q.filter(db.tags.tag == 'javascript')
for book in q:
    print book
    print book.tags
