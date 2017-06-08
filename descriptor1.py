from bs4 import BeautifulSoup

class HTMLEmail:

    _subject = None
    _body = None
    _body_plain = None

    def get_subject(self):
        return self._subject

    def set_subject(self, text):
        soup = BeautifulSoup(text, 'html.parser')
        self._subject = soup.text

    def get_body(self):
        return self._body

    def set_body(self, text):
        soup = BeautifulSoup(text, 'html.parser')
        self._body = soup

    def get_body_plain(self):
        return self._body_plain

    def set_body_plain(self, text):
        soup = BeautifulSoup(text, 'html.parser')
        self._body_plain = soup.text


html = "<p><b>Wow!<b></p><p>A great email from Dan.</p>"
email = HTMLEmail()
email.set_subject('An email from Dan')
email.set_body(html)
email.set_body_plain(html)

print('subject:', email.get_subject())
print('body:   ', email.get_body())
print('plain:  ', email.get_body_plain())
