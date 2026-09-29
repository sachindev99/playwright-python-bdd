import pytest
from playwright.sync_api import Playwright


orders_payload= {"orders":[{"country":"India","productOrderedId":"6960eae1c941646b7a8b3ed3"}]}


class APIUtils:
    def getToken(self,playwright:Playwright,user_credentials):
        api_request_context= playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response= api_request_context.post("/api/ecom/auth/login",data={"userEmail":user_credentials["user_email"],"userPassword":user_credentials["password"]})
        assert response.ok
        token = response.json()["token"]
        api_request_context.dispose()
        return token





    def createOrders(self,playwright:Playwright,user_credentials):
        token  = self.getToken(playwright,user_credentials)
        api_request_context=playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/order/create-order",data=orders_payload,
                                 headers={"Authorization":token,
                                          "Content-Type":"application/json"}

                                )

        print(response.json())


        return token,response.json()["orders"][0]

    def deleteOrders(self,playwright:Playwright,order_id,token):
        api_request_context=playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.delete(f"/api/ecom/order/delete-order/{order_id}",
                                              headers={"Authorization":token,
                                                       "Content-type":"application/json"}
                                            )
        print(response.json())
        return response.json()







