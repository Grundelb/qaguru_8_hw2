import pytest
from selene.support.shared import browser
from selene import be, have

@pytest.fixture(scope='function')
def setup_browser():
    browser.driver.maximize_window()
    browser.open('https://google.com')


def test_search_text_should_be_found(setup_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    assert browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser ... - GitHub'))

def test_search_text_should_be_not_found(setup_browser):
    browser.element('[name="q"]').should(be.blank).type('!!1234567890thistextsouldntbefound').press_enter()
    assert browser.element('[id="result-stats"]').should(have.text('About 0 results '))
