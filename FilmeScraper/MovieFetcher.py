from requests_html import HTMLSession
import smtplib
from smtplib import SMTPException

if __name__ == "__main__":
    url = 'http://tuebinger-kinos.de/index.php?id=9&cinema_id=2'
    session = HTMLSession()
    cinemaHTML = session.get(url)
    cinemaHTML.html.render()
    ids = cinemaHTML.html.find('#program_teaser')
    message = ""

    for id in ids:
        message += id.full_text + "\n"
    subject = 'Kino-Newsletter'

    messageFinal = 'Subject: {}\n\n{}'.format(subject, message)

    try:
        smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtpObj.login('maxpersonalmailer@gmail.com', '')
        smtpObj.sendmail("maxpersonalmailer@gmail.com", "maximilian.schmidt@gmx.de", messageFinal)
        smtpObj.quit()
        print("Successfully sent email")
    except SMTPException as e:
        print("Error: unable to send email: " + str(e))