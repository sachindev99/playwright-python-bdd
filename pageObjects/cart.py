import time

from playwright.sync_api import expect

class Cart:
    def __init__(self, page):
        self.page = page

    def verify_order_is_present(self):
        cart = self.page.locator('.cart')
        expect(cart).to_contain_text('ADIDAS ORIGINAL')

    def verify_items_are_added_to_cart(self,expected_items):
        cart = self.page.locator('.cartWrap')

        #Find all .cartWrap elements, filter them to the one containing this product name, and verify exactly one exists.
        for item in expected_items.values():
            expect(cart.filter(has_text=item)).to_have_count(1)

    def remove_product(self,items):

        for item in items:
            cart_item = self.page.locator('.cartWrap').filter(has_text=item)
            cart_item.locator('.btn-danger').click()

    def verify_order_is_displayed(self,items):
         expect(self.page.locator('.cart')).to_contain_text(items)

    def checkout_button_is_clicked(self):
        self.page.get_by_role("button",name="Checkout").click()



    def verify_item_is_not_present(self,items):
        expect(self.page.locator('.cart')).to_contain_text(items)

    def continue_shopping(self):
        self.page.locator("button",has_text="Continue Shopping").click()











