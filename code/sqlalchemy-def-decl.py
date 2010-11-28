Base = declarative_base()
metadata = Base.metadata

# Klassen, Tabellen und Relationen definieren
class Author(Base):
    __tablename__ = 'authors'
    # Spalten
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, index=True)

    def __repr__(self):
        return "<Author(%r, '%s')>" % (self.id, self.name)

class Book(Base):
    __tablename__ = 'books'
    # Spalten
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer,
        ForeignKey('authors.id', onupdate='CASCADE', ondelete='CASCADE'),
        nullable=False)
    title = Column(String, nullable=False, index=True)
    # Relationen
    author = relationship(Author, backref='books')
    tags = relationship('Tag', secondary='tags2books',
        backref=backref('books', lazy=False))

    def __repr__(self):
        return "<Book(%r, '%s')>" % (self.id, self.title)

class Tag(Base):
    __tablename__ = 'tags'
    # Spalten
    id = Column(Integer, primary_key=True)
    tag = Column(String, index=True, unique=True, nullable=False)

    def __repr__(self):
        return "<Tag(%r, '%s')>" % (self.id, self.tag)

# Die Assoziationstabelle wird klassisch definiert da sie nicht gemappt wird.
Table('tags2books', metadata,
    Column('tag_id', Integer,
        ForeignKey('tags.id', onupdate='CASCADE', ondelete='CASCADE'),
        primary_key=True),
    Column('book_id', Integer,
        ForeignKey('books.id', onupdate='CASCADE', ondelete='CASCADE'),
        primary_key=True)
)
