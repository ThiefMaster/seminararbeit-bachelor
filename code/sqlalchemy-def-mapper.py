# Metadata-Collection erstellen
metadata = sqlalchemy.MetaData()

# Tabellen definieren
authors_table = Table('authors', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False, index=True)
)

books_table = Table('books', metadata,
    Column('id', Integer, primary_key=True),
    Column('author_id', Integer,
        ForeignKey('authors.id', onupdate='CASCADE', ondelete='CASCADE'),
        nullable=False),
    Column('title', String, nullable=False, index=True)
)

tags_table = Table('tags', metadata,
    Column('id', Integer, primary_key=True),
    Column('tag', String, index=True, unique=True, nullable=False)
)

tags2books_table = Table('tags2books', metadata,
    Column('tag_id', Integer,
        ForeignKey('tags.id', onupdate='CASCADE', ondelete='CASCADE'),
        primary_key=True),
    Column('book_id', Integer,
        ForeignKey('books.id', onupdate='CASCADE', ondelete='CASCADE'),
        primary_key=True)
)

# Klassen zum Mappen der Tabellen definieren
class Author(object):
    def __repr__(self):
        return "<Author(%r, '%s')>" % (self.id, self.name)

class Book(object):
    def __repr__(self):
        return "<Book(%r, '%s')>" % (self.id, self.title)

class Tag(object):
    def __repr__(self):
        return "<Tag(%r, '%s')>" % (self.id, self.tag)

# Tabellen auf die Klassen mappen
mapper(Author, authors_table)
mapper(Book, books_table, properties={
    'author': relationship(Author, backref='books'),
    'tags': relationship(Tag, secondary=tags2books_table,
        backref=backref('books', lazy=False))
})
mapper(Tag, tags_table)
