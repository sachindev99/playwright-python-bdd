import time

import pytest
from pytest_bdd import given, when, then, parsers, scenarios
from playwright.sync_api import Page, Playwright
from conftest import user_credentials, select_browser
from pageObjects.cart import Cart
from pageObjects.dashboard import Dashboard
from pageObjects.login import Login
from pageObjects.orderConfirmation import OrderConfirmation
from pageObjects.orderHistory import OrdersHistory
from pageObjects.paymentDetails import PaymentDetails
from utils.apiBase import APIUtils

scenarios('../features/ordersTransaction.feature')

@pytest.fixture
def order_data():
    return {}



@pytest.fixture
def login_page(select_browser):
   return Login(select_browser)

@pytest.fixture
def orders_history(select_browser,order_data):
    return OrdersHistory(select_browser, order_data['order_id'])

@pytest.fixture
def order_confirmation(select_browser):
    return OrdersHistory(select_browser, None)

@pytest.fixture
def dashboard(select_browser):
    return Dashboard(select_browser)

@pytest.fixture
def api_utils():
    return APIUtils()

@pytest.fixture
def cart(select_browser):
    return Cart(select_browser)

@pytest.fixture
def cart_items():
    return {}

@pytest.fixture
def payment_details(select_browser):
    return PaymentDetails(select_browser)

@pytest.fixture
def order_confirmation(select_browser):
    return OrderConfirmation(select_browser)


@given(parsers.parse('place the item order with {username} and {password}'))
def place_item_order(playwright:Playwright,username,password,order_data,api_utils):
    #creating a dictionary
    user_credentials={}
    user_credentials['user_email'] = username
    user_credentials['password'] = password
    token,created_order_id = api_utils.createOrders(playwright, user_credentials)
    order_data['order_id']= created_order_id
    order_data['credentials']= user_credentials
    order_data['token'] = token


@given('user is on landing page')
def user_is_on_landing_page(select_browser:Page,login_page):
    login_page.navigateToLoginPage()

@given(parsers.parse('user logs in using {username} and {password}'))
def user_is_on_login_page(select_browser,login_page,username,password):
    login_page.navigateToLoginPage()
    login_page.loginOperation(username, password)


@when(parsers.parse('I login to portal with {username} and {password}'))
def login_to_portal(select_browser,login_page,username,password):
    login_page.loginOperation(username, password)

@when('navigate to orders page')
def navigate_to_orders_page(select_browser,dashboard):
    dashboard.click_order()

@when('select the orderId')
def select_orderId(select_browser,orders_history):
    orders_history.click_order()

@then('order message is successfully displayed')
def then_order_message(select_browser,orders_history):
    orders_history.verify_order_confirmation()

@when('the user removes product from the cart')
def remove_from_cart(playwright,api_utils,order_data):
    message= api_utils.deleteOrders(playwright,order_data['order_id'],order_data['token'])
    order_data['delete_message'] = message

@then('the cart should not contain the product')
def then_no_cart_message(select_browser,orders_history):
    orders_history.verify_order_is_not_present()

@when('user adds a product to the cart')
def add_to_cart(select_browser,dashboard):
    dashboard.add_product()

@then('the product should be displayed in the cart')
def then_the_product_is_displayed(select_browser,dashboard,cart):
    dashboard.click_cart()
    cart.verify_order_is_present()

@when(parsers.parse('user adds "{Item1}" "{Item2}" "{Item3}" to cart'))
def add_multiple_items_to_cart(select_browser,dashboard,Item1,Item2,Item3,cart_items):
    dashboard.add_multiple_items_to_cart(Item1,Item2,Item3)
    cart_items['item1']= Item1
    cart_items['item2']= Item2
    cart_items['item3']= Item3

    # cart_items = {
    #     'item1': 'ADIDAS ORIGINAL',
    #     'item2': 'ZARA COAT 3',
    #     'item3': 'iphone 13 pro'
    # }
@when('all the products should be displayed in the cart')
@then('all the products should be displayed in the cart')
def then_the_products_are_displayed(dashboard,cart,cart_items):
    dashboard.click_cart()
    cart.verify_items_are_added_to_cart(cart_items)

@when(parsers.parse('user removes "{Item1}" and "{Item3}" from the cart'))
def remove_from_cart(cart,Item1,Item3):
    cart.remove_product([Item1,Item3])


@then(parsers.parse('"{Item2}" should be displayed in the cart'))
def then_the_product_is_displayed(cart,Item2):
    cart.verify_order_is_displayed(Item2)

@then(parsers.parse('"{Item1}" should not be displayed in the cart'))
def remove_one_item_from_cart(cart,Item1):
    cart.verify_item_is_not_present(Item1)

@then(parsers.parse('"{Item2}" should not be displayed in the cart'))
def remove_one_item_from_cart(cart,Item2):
    cart.verify_item_is_not_present(Item2)

@then('checkout button is clicked')
def checkout_button_clicked(cart):
    cart.checkout_button_is_clicked()

@then('payment details are added')
def payment_details_added(payment_details):
    payment_details.add_payment_details()

@then('order is placed successfully')
def order_is_placed_successfully(order_confirmation):
    order_confirmation. verify_order_is_completed()

@when('user adds the following products to cart')
def add_products_to_cart(dashboard,datatable):
    products=[]


    for row in datatable:
        products.append(row[0])
        print(products)

    dashboard.add_products_to_cart(products)

@when('user continues shopping')
def continue_shopping(cart):
    cart.continue_shopping()

@then('user signs out')
def sign_out_page(order_confirmation):
    order_confirmation.sign_out()













































