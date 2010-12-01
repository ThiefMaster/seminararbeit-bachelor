class News(Base):
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True, nullable=False)
    author = Column(String(30), nullable=False)
    perm_view = Column(String(32))
    title = Column(String(64), nullable=False)
    content = Column(Text, nullable=False)
    post_time = Column(DateTime, nullable=False,
        server_default=func.current_timestamp())
    translations = relationship('NewsTranslation',
        backref='news_rel',
        cascade='all, delete, delete-orphan',
        collection_class=attribute_mapped_collection('language'))

    def __repr__(self):
        return "<News(%r, '%s')>" % (self.id, self.title)

class NewsTranslation(Base):
    __tablename__ = 'news_translation'
    newsid = Column(Integer,
        ForeignKey('news.id', onupdate='CASCADE', ondelete='CASCADE'),
        primary_key=True, nullable=False)
    language = Column(String(16), primary_key=True, nullable=False)
    translator = Column(String(30), nullable=False)
    title = Column(String(64), nullable=False)
    content = Column(Text, nullable=False)
    # news_rel: backref from News

    def __repr__(self):
        return "<NewsTranslation(%r, '%s', '%s')>" % \
            (self.newsid, self.language, self.title)
