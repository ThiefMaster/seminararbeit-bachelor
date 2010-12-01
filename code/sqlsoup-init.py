# Verbindung zur Datenbank herstellen
engine = sqlalchemy.create_engine('postgresql:///test')
db = SqlSoup(engine)

# Relationen definieren
db.books.relate('author', db.authors, backref='books')
db.books.relate('tags', db.tags,
    secondary=db.tags2books._table,
    backref=backref('books', lazy=False))
