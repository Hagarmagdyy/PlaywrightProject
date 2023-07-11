from playwright.sync_api import Playwright, expect
from pages.policies_page import Policies
import pytest
@pytest.mark.usefixtures("login_set_up")
class TestPolicies:
    @pytest.fixture(autouse=True)
    def _obj(self, login_set_up):
        self.page = login_set_up
        self.policies_page = Policies(self.page)
    def test_open_policies_page(self):
        self.policies_page.open_policies()
        expect(self.page).to_have_url("https://demo-01.wge.dev.weave.works/policies")
    def test_open_policy_details_page(self):
        self.policies_page.open_policy_details()
        expect(self.page).to_have_url("https://demo-01.wge.dev.weave.works/policy_details/details?clusterName=management&id=weave.policies.containers-minimum-replica-count&name=Containers%20Minimum%20Replica%20Count")
