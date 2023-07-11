from playwright.sync_api import Playwright, sync_playwright, expect
from pages.workspaces_page import Workspaces
import pytest


@pytest.mark.usefixtures("login_set_up")
class TestWorkspaces:
    @pytest.fixture(autouse=True)
    def _obj(self, login_set_up):
        self.page = login_set_up
        self.workspaces_page = Workspaces(self.page)

    def test_open_workspaces_page(self):
        self.workspaces_page.open_workspaces_page()
        expect(self.page).to_have_url("https://demo-01.wge.dev.weave.works/workspaces")

    def test_open_workspaces_details_page(self):
        self.workspaces_page.open_workspaces_details_page()
        expect(self.page).to_have_url("https://demo-01.wge.dev.weave.works/workspaces/details/serviceAccounts?clusterName=management&workspaceName=dev-team")

    def test_verify_workspaces_service_accounts(self):
        self.workspaces_page.open_workspaces_service_accounts()
        expect(self.page.get_by_role("cell", name="dev-team")).to_be_visible()

    def test_verify_workspaces_roles(self):
        self.workspaces_page.open_workspaces_roles()
        expect(self.page).to_have_url("https://demo-01.wge.dev.weave.works/workspaces/details/roles?clusterName=management&workspaceName=dev-team")



    def test_verify_workspaces_role_bindings(self):
        self.workspaces_page.open_workspaces_role_bindings()
        expect(self.page).to_have_url("https://demo-01.wge.dev.weave.works/workspaces/details/roleBindings?clusterName=management&workspaceName=dev-team")
        expect(self.page.get_by_role("cell", name="dev-team", exact=True)).to_be_visible()



    def test_verify_workspaces_policies(self):
        self.workspaces_page.open_workspaces_policies()
        expect(self.page).to_have_url("https://demo-01.wge.dev.weave.works/workspaces/details/policies?clusterName=management&workspaceName=dev-team")
        expect(self.page.get_by_role("link", name="dev-team allowed repositories")).to_be_visible()


