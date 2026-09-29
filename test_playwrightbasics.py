import time
from threading import Thread

from playwright.sync_api import Page, expect


def test_playwright_basics(playwright):
    browser= playwright.chromium.launch(headless=False)
    context = browser.new_context() #just like opening a browser in incognito
    page = context.new_page()
    page.goto("https://www.google.com")


def test_playwright_shortcut(page: Page):
    page.goto("https://www.google.com")


def test_core_locators(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("username").fill("rahulshettyacademy")
    page.get_by_label("password").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("Consultant")
    page.get_by_role("link",name="terms and conditions").click()
    page.locator("#terms").check()
    page.get_by_role("button",name="Sign In").click()
    time.sleep(10)

def test_invalid_login(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("username").fill("rahulshettyacademy")
    page.get_by_label("password").fill("Learning@830$3mK3424")
    page.get_by_role("combobox").select_option("Consultant")
    page.get_by_role("button",name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password")).to_be_visible()
    time.sleep(10)