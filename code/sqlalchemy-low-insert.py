# Autor anlegen
res = authors_table.insert().execute(name='David Flanagan')
author_id = res.inserted_primary_key[0]

# Tag laden
where = tags_table.c.tag == 'javascript'
res = select([tags_table.c.id], where).execute()
tag_id = res.first()[0]

# Buch erstellen
ins = books_table.insert()
title = 'JavaScript - kurz und gut'
res = ins.execute(author_id=author_id, title=title)
book_id = res.inserted_primary_key[0]

# Tag zum Buch hinzufügen
ins = tags2books_table.insert()
ins.execute(book_id=book_id, tag_id=tag_id)
