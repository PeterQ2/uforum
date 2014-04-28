class pagination(DIV):
    items_per_page = 10
    records = 100

    def limitby(self):
        from gluon import current
        page = self.page=int(current.request.vars.page or 0)
        return (self.items_per_page*page, self.items_per_page*(page+1))

    def xml(self):
        from gluon import current
        pages, rem = divmod(self.records, self.items_per_page)
        if rem:
            pages += 1
        if self.page > 0:
            self.append(A(IMG(_title=T('First page'), _src=URL('static','icons',args='control_start_blue.png')), _href=URL(args=current.request.args,vars=dict(page=0))))
        if self.page > 1:
            self.append(A(IMG(_title=T('Previous page'), _src=URL('static','icons',args='control_rewind_blue.png')), _href=URL(args=current.request.args,vars=dict(page=self.page-1))))
        if self.page<pages-2:
            self.append(A(IMG(_title=T('Next page'), _src=URL('static','icons',args='control_fastforward_blue.png')), _href=URL(args=current.request.args,vars=dict(page=self.page+1))))
        if self.page<pages-1:
            self.append(A(IMG(_title=T('Last page'), _src=URL('static','icons',args='control_end_blue.png')), _href=URL(args=current.request.args,vars=dict(page=pages-1))))
        return DIV.xml(self)