class Login:

    def __init__(self,page):
        self.page = page


    def navigateToLoginPage(self):
        self.page.goto("https://rahulshettyacademy.com/client",wait_until="domcontentloaded",
    timeout=60000)
        self.page.locator("#login").wait_for(timeout=60000)

    def loginOperation(self,username,password):
        self.page.get_by_placeholder('email@example.com').fill(username)
        self.page.get_by_placeholder('enter your passsword').fill(password)
        self.page.locator('#login').click()




