class Policies:
    def __init__(self, page):
        self.page = page
    def open_policies(self):
        self.page.get_by_role("link", name="Policies").click()
    def open_policy_details(self):
        self.page.get_by_role("link", name="Containers Minimum Replica Count").click()
#add new test