from playwright.sync_api import Playwright, expect
import pytest
from pages.login_page import Login
@pytest.fixture(scope="session")
def set_up(playwright: Playwright):
    login_url = "https://demo-01.wge.dev.weave.works/sign_in"
    browser = playwright.chromium.launch(headless=False, slow_mo=3000)
    context = browser.new_context()
    page = context.new_page()
    page.wait_for_load_state("networkidle")
    page.goto(login_url)
    page.set_default_timeout(5000)
    yield page
    page.close()
    context.close()
    browser.close()
@pytest.fixture(scope="session")
def login_set_up(set_up):
    login_username = "wego-admin"
    login_password = ">ch2yU5@]F8U6IZkX?Q#"
    login_success_url = "https://demo-01.wge.dev.weave.works/clusters/list"
    page = set_up
    login_page = Login(page)
    login_page.get_username().fill(login_username)
    login_page.get_password().fill(login_password)
    login_page.get_continue_btn().click()
    expect(page).to_have_url(login_success_url)
    yield page
    login_page.get_account_settings().click()
    login_page.get_logout_btn().click()
