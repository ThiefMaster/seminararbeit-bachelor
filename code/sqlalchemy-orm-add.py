# Autor-Objekt erstellen
jresig = Author(name='John Resig')

# Tag-Objekt erstellen
jquery = Tag(tag='jquery')

# Buch-Objekt erstellen und Autor und Tags setzen
jsbook = Book(author=jresig)
jsbook.tags = [jquery]

# Titel vom ersten (und einzigen) Buch (also jsbook) mit dem jquery-Tag setzen
jquery.books[0].title = 'Secrets of the JavaScript Ninja'

# Tag-Objekt erstellen und der books-Relation das Buch hinzufügen
Tag(tag='javascript').books.append(jsbook)

# Buch-Objekt persistieren
session.add(jsbook)
session.commit()
