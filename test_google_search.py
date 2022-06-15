from selene.support.shared import browser
from selene import be, have


class TestGoogleSearch:

    def test_positive(self, setup):
        browser.open('https://google.com')
        browser.element('#L2AGLb').click()
        browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
        browser.element('[id="search"]').should(have.text('Selene'))

    def test_negative(self, setup):
        browser.open('https://google.com')
        browser.element('#L2AGLb').click()
        browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
        browser.element('[id="search"]').should(have.text('Seleneide'))
