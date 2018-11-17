from requests_html import HTMLSession
import smtplib
from smtplib import SMTPException

class FetchMovies:

    def getMovies(self):
        url = 'http://tuebinger-kinos.de/index.php?id=9&cinema_id=2'
        session = HTMLSession()
        cinemaHTML = session.get(url)
        cinemaHTML.html.render()
        ids = cinemaHTML.html.find('#program_teaser')
        message = ""
        for id in ids:
            message += id.full_text + "%0D%0A"
        try:
            smtpObj = smtplib.SMTP('localhost')
            smtpObj.sendmail("Server", "maximilian.schmidt@gmx.de", message)
            print
            "Successfully sent email"
        except SMTPException:
            print
            "Error: unable to send email"


if __name__ == "__main__":
    url = 'http://tuebinger-kinos.de/index.php?id=9&cinema_id=2'
    session = HTMLSession()
    cinemaHTML = session.get(url)
    cinemaHTML.html.render()
    ids = cinemaHTML.html.find('#program_teaser')
    for id in ids:
        print(id.full_text)
    try:
        smtpObj = smtplib.SMTP('localhost')
        smtpObj.sendmail(sender, receivers, message)
        print
        "Successfully sent email"
    except SMTPException:
        print
        "Error: unable to send email"