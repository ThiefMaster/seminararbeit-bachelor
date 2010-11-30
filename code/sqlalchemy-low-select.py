from_obj = books_table
from_obj = from_obj.join(tags2books_table)
from_obj = from_obj.join(tags_table)
q = books_table.select(from_obj=[from_obj])
q = q.where(tags_table.c.tag == 'javascript')
res = q.execute()
for row in res:
    print row
