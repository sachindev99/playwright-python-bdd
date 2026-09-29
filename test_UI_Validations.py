import time

from playwright.sync_api import Page, expect


def test_UI_ValidationsDyanmicScript(page: Page):
    # iphoneX, Nokia Edge -> verify 2 items are showing in cart.
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username").fill("rahulshettyacademy")
    page.get_by_label("Password").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").click()
    page.get_by_role("button", name="Sign In").click()
    iphoneLocator=page.locator("app-card").filter(has_text="iphone X")
    edge = page.locator("app-card").filter(has_text="Nokia Edge")
    iphoneLocator.get_by_role("button").click()
    edge.get_by_role("button").click()
    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)

def test_Child_Window_Handle(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    with page.expect_popup() as new_Page:
        page.locator(".blinkingText[href='https://rahulshettyacademy.com/documents-request']").click()
        child_page = new_Page.value

        text= child_page.locator(".red").text_content()
        #complete text: Please email us at mentor@rahulshettyacademy.com with below template to receive response

        split_text=text.split("at ") # split_text[0]= Please email us split_text[1]=mentor@rahulshettyacademy.com with below template to receive response
        extract_email=split_text[1].split(" ") #extract_email[0]=mentor@rahulshettyacademy.com, extract_email[1]=with, extract_email[2]=below.....
        #print(extract_email[0]) #mentor@rahulshettyacademy.com
        assert extract_email[0]=="mentor@rahulshettyacademy.com"


