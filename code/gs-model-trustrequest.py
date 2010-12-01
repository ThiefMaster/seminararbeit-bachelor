class TrustRequest(Base):
    __tablename__ = 'trusts'
    id = Column(Integer, primary_key=True, nullable=False)
    request_time = Column(DateTime, nullable=False,
        server_default=func.current_timestamp())
    process_time = Column(DateTime)
    ip = Column(postgresql.INET, nullable=False)
    host = Column(String(64))
    count = Column(Integer, nullable=False)
    duration = Column(String(4), nullable=False)
    accountid = Column(BigInteger, nullable=False, index=True)
    accountname = Column(String(30), nullable=False)
    user_ip = Column(postgresql.INET, nullable=False)
    reason = Column(String(64), nullable=False)
    comments = Column(Text, nullable=False)
    identd = Column(Boolean, nullable=False,
        server_default='false')
    identd_reply = Column(Text)
    helper = Column(String(30))
    status = Column(SmallInteger, nullable=False, index=True,
        server_default='0')
    deny_reason = Column(String(256))

    def __repr__(self):
        return "<TrustRequest(%r, '%s', %u, '%s', '%s')>" % \
               (self.id, self.ip, self.count, self.duration,
                   self.accountname)
