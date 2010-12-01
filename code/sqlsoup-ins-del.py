test = db.authors.insert(name='Test')
db.commit()
db.delete(test)
db.commit()
