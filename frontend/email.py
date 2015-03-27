import requests

__author__ = 'niels-ole'


def send_confirmation_message(order):
    return requests.post(
        "https://api.mailgun.net/v2/sandbox3488da64f0db4f36b0eebcb6aa2f5a01.mailgun.org/messages",
        auth=("api", ""),
        data={"from": "Mailgun Sandbox <postmaster@sandbox3488da64f0db4f36b0eebcb6aa2f5a01.mailgun.org>",
              "to": "Niels-Ole Kuehl <nielsole.kuehl@gmail.com>",
              "subject": "Paid {0}".format(order.id),
              "text": "Name: {0}, Address: {1}, E-Mail: {2}".format(order.name, order.address, order.email)})

def send_interest_message(order):
    return requests.post(
        "https://api.mailgun.net/v2/sandbox3488da64f0db4f36b0eebcb6aa2f5a01.mailgun.org/messages",
        auth=("api", ""),
        data={"from": "Mailgun Sandbox <postmaster@sandbox3488da64f0db4f36b0eebcb6aa2f5a01.mailgun.org>",
              "to": "Niels-Ole Kuehl <nielsole.kuehl@gmail.com>",
              "subject": "Interest {0}".format(order.id),
              "text": "Name: {0}, Address: {1}, E-Mail: {2}".format(order.name, order.address, order.email)})