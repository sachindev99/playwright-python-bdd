import pytest
from playwright.sync_api import Playwright


@pytest.fixture(scope='session')
def user_credentials(request):
    print(request)
    return request.param

#pytest_addoption is a pytest hook. Pytest automatically calls it while setting itself up.
# It is used to register a custom command-line option. eg: --browser name firefox
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="select browser to use"
    )


@pytest.fixture
def browser(request):
    return request.config.getoption("--browser_name") #chrome or firefox

@pytest.fixture
def select_browser(browser,playwright:Playwright):
    if browser == "chrome":
        browser = playwright.chromium.launch(headless=False)

    elif browser == "firefox":
        browser = playwright.firefox.launch(headless=False)

    context = browser.new_context()
    page = context.new_page()

    yield page
    context.close()
    browser.close()
