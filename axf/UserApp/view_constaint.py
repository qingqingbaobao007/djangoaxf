from django.core.mail import send_mail
from django.template import loader


def send_email(name,email,token):
    subject = '红浪漫洗浴'
    message = '充值1000送免费洗澡一次'

    context = {
        'name': name,
        'url': 'http://106.53.5.6/axfuser/activeAccount/?token='+str(token)
    }

    html_message = loader.get_template('active.html').render(context=context)
    from_email = '738613409@qq.com'
    recipient_list = [email]

    send_mail(subject=subject, html_message=html_message, message=message, from_email=from_email,
              recipient_list=recipient_list)
