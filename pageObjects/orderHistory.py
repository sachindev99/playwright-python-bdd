from playwright.sync_api import expect


class OrdersHistory:
    def __init__(self,page,order_id):
        self.page = page
        self.order_id = order_id



    def click_order(self):
        row = self.page.locator("tr").filter(has_text=self.order_id)
        row.get_by_role("button", name="View").click()

    def verify_order_confirmation(self):
        expect(self.page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")

    def verify_order_is_not_present(self):
        row = self.page.locator("tr").filter(has_text=self.order_id)
        expect(row).not_to_be_visible()
