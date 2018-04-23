import sendgrid
from sendgrid.helpers.mail import *
import datetime
import os
import traceback
import sys

try:
    import acereporter
except Exception as e:
    tracebackStr = '<br>'.join([str(tb_line).replace('\n', '<br>') for tb_line in traceback.format_tb(e.__traceback__)])

    print('########### ERROR ###########')
    traceback.print_exc()

    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('ACEREPORT_SENDGRID_API_KEY'))
    from_email = Email(os.environ.get('EMAIL_SENDER_ADDR'), os.environ.get('EMAIL_SENDER_NAME'))
    subject = "ACE Report Job Error Notification"

    args = sys.argv

    data = {
        'datetime': str(datetime.datetime.now()),
        'args': str(args),
        'traceback': tracebackStr,
        'hostname': os.uname().nodename,
        'error': str(e)
    }
    contentHtml = """
        <p>An error has occurred while running the ACE Report job as at {data[datetime]}.</p>
        <p><b>Host:</b> {data[hostname]}</p>
        <p><b>Arguments:</b><pre>{data[args]}</pre></p>
        <p><b>Error:</b><pre>{data[error]}</pre></p>
        <p><b>Traceback:</b><pre>{data[traceback]}</pre></p>
    """.format(data=data)

    content = Content("text/html", contentHtml)

    mail = Mail()
    personalization = Personalization()
    personalization.add_to(Email(os.environ.get('ADMIN_EMAIL')))

    mail.from_email = from_email
    mail.subject = subject
    mail.add_personalization(personalization)
    mail.add_content(content)

    response = sg.client.mail.send.post(request_body=mail.get())
    #print('ttbbb: ', data['traceback'])

    print("Error notification email sent!")
    print(response.status_code)
    print(response.body)
    print(response.headers)
