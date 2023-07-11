class Login:
    def __init__(self, page):
        self.page = page
    def get_username(self):
        return self.page.get_by_placeholder("Username")
    def get_password(self):
        return self.page.get_by_placeholder("Password")
    def get_continue_btn(self):
        return self.page.get_by_role("button", name="CONTINUE")
    def get_account_settings(self):
        return self.page.locator(".UserSettings-sc-1x073xj-2 > button")
    def get_logout_btn(self):
        return self.page.get_by_role("menuitem", name="Logout")