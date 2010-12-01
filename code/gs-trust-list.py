trustreq = aliased(TrustRequest)
ip_reqs = select([func.count('*')]) \
    .where(trustreq.ip == TrustRequest.ip)
user_reqs = select([func.count('*')]) \
    .where(trustreq.accountid == TrustRequest.accountid)

requests = self.data.session.query(TrustRequest,
    ip_reqs.as_scalar(), user_reqs.as_scalar()) \
    .filter_by(status=TR_OPEN) \
    .order_by(TrustRequest.request_time)

for request, ip_reqs, user_reqs in requests:
    # [...]
