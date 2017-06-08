from bs4 import BeautifulSoup

class HTMLProperty:

    def __init__(self, name):
        self.name = f'_{name}'

    def __get__(self, instance, type=None):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        soup = BeautifulSoup(value, 'html.parser')
        setattr(instance, self.name, soup)


class PlainTextProperty:

    def __init__(self, name):
        self.name = f'_{name}'

    def __get__(self, instance, type=None):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        soup = BeautifulSoup(value, 'html.parser')
        setattr(instance, self.name, soup.text)


class HTMLEmail:

    subject = PlainTextProperty('subject')
    body = HTMLProperty('body')
    body_plain = PlainTextProperty('body_plain')


html = "<p><b>Wow!<b></p><p>A great email from Dan.</p>"
email = HTMLEmail()
email.subject = 'An email from Dan'
email.body = html
email.body_plain = html

print('subject:', email.subject)
print('body:   ', email.body)
print('plain:  ', email.body_plain)
