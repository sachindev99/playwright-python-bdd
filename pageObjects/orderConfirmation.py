from playwright.sync_api import expect
from playwright.sync_api import Page


class OrderConfirmation:

    def __init__(self,page:Page):
        self.page = page



    def verify_order_is_completed(self):
        confirmation_text= self.page.locator("h1",has_text="Thankyou for the order.")
        expect(confirmation_text).to_be_visible()

    def sign_out(self):
        self.page.get_by_role("button",name="Sign Out").click()