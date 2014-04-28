def captcha_field(request=request):
    from gluon.tools import Recaptcha
    w = lambda x,y: Recaptcha(request,
                              '6LeIK_ISAAAAABlEm6gH7NRcbCLIV_H6e8eEYfvD',
                              '6LeIK_ISAAAAAE-tUY4tCUeAYm5FKizTRroqSHRX')
 
    return Field('captcha', 'string', label=T('Verify'), widget=w, default='ok')