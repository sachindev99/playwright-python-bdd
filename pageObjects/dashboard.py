
class Dashboard:

    def __init__(self,page):
        self.page = page


    def click_order(self):
        self.page.get_by_role("button", name="ORDERS").click()

    def add_product(self):
       product_card = self.page.locator(".card").filter(has_text='ADIDAS ORIGINAL')
       product_card.get_by_role("button", name="Add To Cart").click()

    def click_cart(self):
       self.page.locator('button[routerlink="/dashboard/cart"]').click()

    def add_multiple_items_to_cart(self,item1,item2,item3):
        product_card1 = self.page.locator(".card").filter(has_text=item1)
        product_card1.get_by_role("button", name="Add To Cart").click()

        product_card2 = self.page.locator(".card").filter(has_text=item2)
        product_card2.get_by_role("button", name="Add To Cart").click()

        product_card3 = self.page.locator(".card").filter(has_text=item3)
        product_card3.get_by_role("button", name="Add To Cart").click()

    def add_products_to_cart(self,products):
        for product in products:
           item = self.page.locator(".card").filter(has_text=product)
           item.get_by_role("button", name="Add To Cart").click()










