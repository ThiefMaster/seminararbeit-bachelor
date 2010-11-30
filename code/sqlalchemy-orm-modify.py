js_tag = session.query(Tag).filter_by(tag='javascript').one()
book.tags.append(js_tag)
book.tags.append(Tag(tag='new-release'))
session.commit()
