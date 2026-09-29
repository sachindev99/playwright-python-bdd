
from playwright.sync_api import Page, expect


class PaymentDetails:

    def __init__(self,page:Page):
        self.page = page

    def add_payment_details(self):
        self.page.locator("input[value='4542 9931 9292 2293']").clear()
        self.page.locator("input[value='4542 9931 9292 2293']").fill("4522 5643 1231")

        self.page.locator(".input.ddl").nth(0).select_option("09")
        self.page.locator(".input.ddl").nth(1).select_option("24")

        cvv = self.page.locator(".field.small").filter(has_text='CVV CODE')
        cvv.locator("input").fill("341")

        name = self.page.locator(".field").filter(has_text="Name on Card ")
        name.locator("input").fill("John")


        country = self.page.get_by_placeholder("Select Country")

        country.click()
        country.press_sequentially("India")

        self.page.get_by_text("India", exact=True).click()


        place_order = self.page.get_by_text("Place Order", exact=True)
        expect(place_order).to_be_visible()
        place_order.click()

