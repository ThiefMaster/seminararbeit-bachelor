def post(self):
    # [...]
    # Check for duplicate request
    pending = self.data.session.query(TrustRequest) \
        .filter_by(ip=form.value('ip'), status=TR_OPEN) \
        .count()
    if pending:
        form.set_error('ip', 'Please do not submit ' + \
            'multiple trust requests for the same IP.')
        self.write({'errors': form.errors()})
        return
    request = TrustRequest()
    request.ip = form.value('ip')
    request.count = form.value('count')
    request.duration = form.value('duration')
    request.accountid = self.session.accountid
    request.accountname = self.session.account
    request.user_ip = self.request.remote_ip
    request.reason = form.value('reason')
    request.comments = form.value('comments')
    # Check for identd response
    self.check_identd(request.ip, self.post_identd,
        request, form)

def post_identd(self, success, response, request, form):
    request.identd = success
    request.identd_reply = response
    # Resolve IP
    self.gethostbyaddr(request.ip, self.post_resolved, request)

def post_resolved(self, hosts, request):
    if hosts:
        request.host = hosts[0]
    self.data.session.add(request)
    self.data.commit()
    self.write({})
