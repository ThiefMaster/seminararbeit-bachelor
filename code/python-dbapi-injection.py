# Falsch: Der Parameter wird in die Abfrage eingebettet
cursor.execute("SELECT * FROM authors WHERE name = '"+name+"'")

# Falsch: Der Parameter wird ebenfalls eingebettet, da der
# %-Operator den Parameter wie bei printf in den String einfügt
cursor.execute("SELECT * FROM authors WHERE name = '%s'" % name)

# Korrekt: Der Parameter wird separat übergeben
cursor.execute("SELECT * FROM authors WHERE name = %s", (name,))
