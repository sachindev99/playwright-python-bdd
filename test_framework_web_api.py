import json

import pytest
from playwright.sync_api import Playwright, expect

from pageObjects.dashboard import Dashboard
from pageObjects.login import Login
from pageObjects.orderHistory import OrdersHistory
from utils.apiBase import APIUtils

with open('data/credentials.json') as f:
    test_data = json.load(f)

    user_credentials_list = test_data['user_credentials']


@pytest.mark.smoke
@pytest.mark.parametrize('user_credentials',user_credentials_list)
def test_e2e_web_api(playwright:Playwright,user_credentials,select_browser):
    api_utils = APIUtils()
    order_id = api_utils.createOrders(playwright,user_credentials)


    username = user_credentials["user_email"]
    password = user_credentials["password"]

    #select browser return page
    login_page = Login(select_browser)
    login_page.navigateToLoginPage()
    login_page.loginOperation(username, password)

    dashboard = Dashboard(select_browser)
    dashboard.click_order()

    orders_history = OrdersHistory(select_browser,order_id)
    orders_history.click_order()
    orders_history.verify_order_confirmation()











