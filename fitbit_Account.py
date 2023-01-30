from playwright.sync_api import sync_playwright, Playwright, TimeoutError as PlaywrightTimeoutError
import time
import json


def automation_process():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False)
        ua = (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/69.0.3497.100 Safari/537.36"
        )
        page = browser.new_page(user_agent=ua)
        page.goto(
            "http://agencies.monroecountypa.gov/monroepa_prod/search/commonsearch.aspx?mode=realprop", wait_until="load")


# def run(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://emailtemporanee.com/en")
#     page.wait_for_timeout(20000)
#     email = page.locator("#trsh_mail").inner_text()
#     print(email)
    # page1 = context.new_page()
    # page1.goto("https://accounts.fitbit.com/signup?targetUrl=https%3A%2F%2Fwww.fitbit.com%2Fglobal%2Fjp%2Fhome")
    # page1.get_by_placeholder("Your email address").click()
    # page1.get_by_placeholder("Your email address").fill("ikvppym684@lkop.me")
    # page1.get_by_placeholder("Choose your password").click()
    # page1.get_by_placeholder("Choose your password").fill("mypass@lol.com")
    # page1.get_by_label("I agree to the Fitbit Terms of Service. Please also read the Privacy Policy including the Cookie Use statement.").check()
    # page1.get_by_role("button", name="Join Fitbit").click()
    # page.get_by_role("link", name="Action required: Confirm Fitbit account email address").click()
    # page.frame_locator("iframe[name=\"aswift_9\"]").frame_locator("iframe[name=\"ad_iframe\"]").get_by_role("button", name="Close ad").click()
    # with page.expect_popup() as page2_info:
    #     page.frame_locator("#myIframe").get_by_role("link", name="Verify Your Email").click()
    # page2 = page2_info.value
    # page1.get_by_placeholder("First name").click()
    # page1.get_by_placeholder("First name").fill("ahmed")
    # page1.get_by_placeholder("Last name").click()
    # page1.get_by_placeholder("Last name").fill("mahmoud")
    # page1.get_by_placeholder("Year").click()
    # page1.get_by_placeholder("Year").fill("1996")
    # page1.get_by_role("button", name="Continue").click()
    # page1.get_by_placeholder("Inches").click()
    # page1.get_by_placeholder("Inches").fill("5")
    # page1.get_by_placeholder("Pounds").click()
    # page1.get_by_placeholder("Pounds").fill("250")
    # page1.locator("#gender").get_by_role("combobox").select_option("MALE")
    # page1.get_by_placeholder("Centimeters").fill("180")
    # page1.get_by_role("button", name="Create Account").click()

    # # ---------------------
    # context.close()
    # browser.close()


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://quik.email/en")
    page.wait_for_timeout(20000)
    email = page.locator("#trsh_mail").input_value()
    print(email)
    page1 = context.new_page()
    page1.goto(
        f"https://accounts.fitbit.com/signup?targetUrl=https%3A%2F%2Fwww.fitbit.com%2Fglobal%2Fjp%2Fhome")
    page1.get_by_placeholder("Your email address").click()
    page1.get_by_placeholder("Your email address").fill(email)
    page1.get_by_placeholder("Choose your password").click()
    page1.get_by_placeholder("Choose your password").fill(
        "mypass123@gmail.com")
    page1.get_by_label(
        "I agree to the Fitbit Terms of Service. Please also read the Privacy Policy including the Cookie Use statement.").check()
    page1.get_by_role("button", name="Join Fitbit").click()
    page.wait_for_timeout(30000)
    page.get_by_role("link", name="View").click()
    with page.expect_popup() as page2_info:
        page.frame_locator("#myIframe").get_by_role(
            "link", name="Verify Your Email").click()
    page2 = page2_info.value
    page2.close()
    page.wait_for_timeout(10000)
    page1.get_by_placeholder("First name").click()
    page.wait_for_timeout(2000)
    page1.get_by_placeholder("First name").fill("ahmed")
    page.wait_for_timeout(2000)
    page1.get_by_placeholder("Last name").click()
    page.wait_for_timeout(2000)
    page1.get_by_placeholder("Last name").fill("mahmoud")
    page.wait_for_timeout(2000)
    page1.get_by_placeholder("Year").click()
    page.wait_for_timeout(2000)
    page1.get_by_placeholder("Year").fill("1996")
    page.wait_for_timeout(2000)
    page1.get_by_role("button", name="Continue").click()
    page.wait_for_timeout(2000)
    page1.locator(
        "#height-system").get_by_role("combobox").select_option("METRIC")
    page1.get_by_placeholder("Centimeters").click()
    page.wait_for_timeout(2000)
    page1.get_by_placeholder("Centimeters").fill("160")
    page.wait_for_timeout(2000)
    page1.get_by_placeholder("Pound").click()
    page.wait_for_timeout(2000)
    page1.get_by_placeholder("Pound").fill("250")
    page.wait_for_timeout(2000)
    page1.locator("#gender").get_by_role("combobox").select_option("MALE")
    page.wait_for_timeout(2000)
    page1.get_by_role("button", name="Create Account").click()
    page.wait_for_timeout(7000)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
