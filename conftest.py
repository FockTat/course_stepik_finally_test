import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None, help="Choose language: ru, en, es, etc.")

@pytest.fixture
def language(request):
    return request.config.getoption("language")

@pytest.fixture(scope="function")
def browser(language):
    print("\nStart Chrome browser...")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nQuit browser...")
    browser.quit()