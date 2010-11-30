q = session.query(Book)
q = q.join(Book.tags)
q = q.options(joinedload(Book.tags))
q = q.filter(Tag.tag == 'jquery')
for book in q:
    print book
    print book.tags
