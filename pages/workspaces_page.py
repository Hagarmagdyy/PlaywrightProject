class Workspaces:
    def __init__(self, page):
        self.page = page

    def open_workspaces_page(self):
        self.page.get_by_role("link", name="Workspaces").click()
    def open_workspaces_details_page(self):
        self.page.get_by_role("link", name="dev-team").click()
    def open_workspaces_service_accounts(self):
        self.page.get_by_role("tab", name="Service Accounts").click()

    def open_workspaces_roles(self):
        self.page.get_by_role("tab", name="Roles").click()
    def open_workspaces_role_bindings(self):
        self.page.get_by_role("tab", name="Role Bindings").click()
    def open_workspaces_policies(self):
        self.page.get_by_role("tab", name="Policies").click()
