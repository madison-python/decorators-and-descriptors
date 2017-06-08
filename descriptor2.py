from bs4 import BeautifulSoup

class HTMLEmail:

    _subject = None
    _body = None
    _body_plain = None

    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, text):
        soup = BeautifulSoup(text, 'html.parser')
        self._subject = soup.text

    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, text):
        soup = BeautifulSoup(text, 'html.parser')
        self._body = soup

    @property
    def body_plain(self):
        return self._body_plain

    @body_plain.setter
    def body_plain(self, text):
        soup = BeautifulSoup(text, 'html.parser')
        self._body_plain = soup.text


html = "<p><b>Wow!<b></p><p>A great email from Dan.</p>"
email = HTMLEmail()
email.subject = 'An email from Dan'
email.body = html
email.body_plain = html

print('subject:', email.subject)
print('body:   ', email.body)
print('plain:  ', email.body_plain)
