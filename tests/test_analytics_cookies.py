import pytest
from playwright.sync_api import sync_playwright


@pytest.mark.parametrize("browser_type", ["chromium", "firefox", "webkit"])
def test_analytics_cookies(browser_type):
    with sync_playwright() as p:
        browser = getattr(p, browser_type).launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        context.clear_cookies()

        page.goto("https://www.ing.pl")
        page.wait_for_load_state("networkidle")

        print(page.url)
        print(page.content())


        page.wait_for_selector("div.cookie-policy-content", timeout=120000)
        print(page.url)
        page.wait_for_load_state("load")
        page.click("button.js-cookie-policy-main-settings-button")
        page.wait_for_selector("div.js-checkbox[name='CpmAnalyticalOption']")
        toggle_button = page.query_selector("div.js-checkbox[name='CpmAnalyticalOption']")
        toggle_button.click()
        page.click("button.js-cookie-policy-settings-decline-button")

        cookies = context.cookies()
        cookie_policy_accepted = any(
            cookie['name'] == 'cookiePolicyINCPS' and cookie['value'] == 'true'
            for cookie in cookies
        )
        analytics_consent_given = any(
            cookie['name'] == 'cookiePolicyGDPR' and cookie['value'] == '3'
            for cookie in cookies
        )
        assert cookie_policy_accepted, "The 'cookiePolicyINCPS' cookie was not saved."
        assert analytics_consent_given, "The 'cookiePolicyGDPR' cookie does not have a value of 3."
        browser.close()
