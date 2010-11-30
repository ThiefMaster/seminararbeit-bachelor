def get_author(cursor, quote_char, name):
    return cursor.execute("SELECT id, name FROM authors WHERE name = " + quote_char, (name,)).fetchone()

pg_conn = psycopg2.connect('')
sl_conn = sqlite3.connect('test.sqlite')
print get_author(pg_conn.cursor(), '%s', 'Knuth')
print get_author(sl_conn.cursor(), '?', 'Knuth')
sl_conn.close()
pg_conn.close()
