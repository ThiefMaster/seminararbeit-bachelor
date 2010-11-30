# Query zusammenbauen
q = session.query(Author)
q = q.options(joinedload_all(Author.books, Book.tags))
q = q.filter_by(name='John Resig')
# Query ausführen; es muss genau eine Zeile gefunden werden
john = q.one()
# Daten ausgeben ohne dass eine zusätzliche Query gesendet wird
print john.name
for book in john.books:
    print book
    print book.tags
