from playwright.sync_api import sync_playwright, Playwright, TimeoutError as PlaywrightTimeoutError
import time
import json

from discord import SyncWebhook, Embed


def automation_process(playwright: Playwright, list):
    x = 0
    while True:
        try:
            first_name = list[0]
            last_name = list[1]
            address_line_1 = list[2]
            address_line_2 = list[3]
            postal_code = list[4]
            city = list[5]
            state = list[6]
            fitbit_email = list[7]
            paypal_email = list[8]
            phone_number = list[9]
            address_to_search = list[10]
            page.goto("https://www.fitbitionic.expertinquiry.com/")
            page.get_by_label("Country").select_option(value='JP')
            with page.expect_popup() as page1_info:
                page.get_by_role("link", name="Register").click()
            page1 = page1_info.value
            page1.get_by_role(
                "textbox", name="<input type=\"text\" class=\"form-control\" data-bind=\"value:Answer, attr:{maxlength: $root.getMaxLength(MaxLength), 'aria-label': Label, 'aria-required': Required}, event:{keydown: $root.validateTab}\" autocomplete=\"nothing\" aria-labelledby=\"TextTemplate\" />").first.click()
            page1.get_by_role(
                "textbox", name="<input type=\"text\" class=\"form-control\" data-bind=\"value:Answer, attr:{maxlength: $root.getMaxLength(MaxLength), 'aria-label': Label, 'aria-required': Required}, event:{keydown: $root.validateTab}\" autocomplete=\"nothing\" aria-labelledby=\"TextTemplate\" />").first.fill(first_name)
            page1.get_by_role(
                "textbox", name="<input type=\"text\" class=\"form-control\" data-bind=\"value:Answer, attr:{maxlength: $root.getMaxLength(MaxLength), 'aria-label': Label, 'aria-required': Required}, event:{keydown: $root.validateTab}\" autocomplete=\"nothing\" aria-labelledby=\"TextTemplate\" />").nth(1).click()
            page1.get_by_role(
                "textbox", name="<input type=\"text\" class=\"form-control\" data-bind=\"value:Answer, attr:{maxlength: $root.getMaxLength(MaxLength), 'aria-label': Label, 'aria-required': Required}, event:{keydown: $root.validateTab}\" autocomplete=\"nothing\" aria-labelledby=\"TextTemplate\" />").nth(1).fill(last_name)
            page1.get_by_placeholder("Enter Address Here to Search").click()
            page1.get_by_placeholder(
                "Enter Address Here to Search").fill(address_to_search)
            page1.get_by_placeholder("Address Line 1").click()
            page1.get_by_placeholder("Address Line 1").fill(address_line_1)
            page1.get_by_placeholder("Address Line 2").click()
            page1.get_by_placeholder("Address Line 2").fill(address_line_2)
            page1.get_by_placeholder("Post Code").click()
            page1.get_by_placeholder("Post Code").fill(postal_code)
            page1.get_by_placeholder("City").click()
            page1.get_by_placeholder("City").fill(city)
            page1.get_by_placeholder("State").click()
            page1.get_by_placeholder("State").fill(state)
            page1.get_by_placeholder("Email Address", exact=True).click()
            page.wait_for_timeout(3000)
            page1.get_by_placeholder("Email Address", exact=True).type(
                fitbit_email)
            page1.get_by_placeholder(
                "Confirm Email Address", exact=True).click()
            page.wait_for_timeout(3000)
            page1.get_by_placeholder("Confirm Email Address", exact=True).type(
                fitbit_email)
            page1.get_by_role("button", name="Next").click()
            page.wait_for_timeout(3000)
            page1.get_by_placeholder("Email Address", exact=True).click()
            page.wait_for_timeout(3000)
            page1.get_by_placeholder(
                "Email Address", exact=True).type(fitbit_email)
            page1.get_by_placeholder("Confirm Email Address").click()
            page.wait_for_timeout(2000)
            page1.get_by_placeholder(
                "Confirm Email Address").type(fitbit_email)
            page1.get_by_role(
                "combobox", name="United States: +1").get_by_text("+1").click()
            page1.get_by_role("option", name="Japan (日本)+81").click()
            page.wait_for_timeout(2000)
            page1.get_by_placeholder("__-____-____").click()
            page.wait_for_timeout(2000)
            page1.get_by_placeholder("__-____-____").type(phone_number)
            page1.get_by_role(
                "combobox", name="Preferred method of reimbursement").click()
            page1.get_by_role("option", name="PayPal").click()
            page1.locator("#email_RefundEmail").click()
            page.wait_for_timeout(2000)
            page1.locator("#email_RefundEmail").type(paypal_email)
            page1.locator("#confirm_RefundEmail").click()
            page.wait_for_timeout(2000)
            page1.locator("#confirm_RefundEmail").type(paypal_email)
            page1.get_by_text("Yes").click()
            page1.get_by_text("I Agree").click()
            page1.get_by_role("button", name="Next").click()
            page.wait_for_timeout(10000)
            page1.locator("#top-submit").click()
            page.wait_for_timeout(10000)
            # Create a new webhook
            webhook = SyncWebhook.from_url(
                'https://discord.com/api/webhooks/1068436993559777390/jnpU5fL_qs182ARxvqeRzSR1Ywpg9mhiWdxhSc1jMAewTNFJNWCo8SClRcpxEv2m0wPe')
            refrence = page1.locator(
                '//*[@id="pageContainer"]/div[5]/div/div/div/div[4]/div[1]/span[2]').inner_text()
            embed = Embed(title="FitBotJP", color=0xFF5733)
            embed.add_field(name="Submitted Form", value='', inline=False)
            embed.add_field(name="Email", value=fitbit_email, inline=True)
            embed.add_field(name="Ref", value=refrence)
            embed.add_field(name="First name", value=first_name, inline=True)
            embed.add_field(name="Last name", value=last_name)
            embed.add_field(name="Address", value=address_line_1)
            embed.add_field(name="phone", value=phone_number)
            embed.add_field(name="Paypal Email", value=paypal_email)
            embed.add_field(name="State", value=state)
            embed.add_field(name="City", value=city)
            # Send a message to the server
            webhook.send(embed=embed)
            page1.close()
            break
        except PlaywrightTimeoutError:
            x += 1
            if (x == 2):
                print("Timeout! Break")
                break
            else:
                print("Timeout! Retry")
            continue


#
start = time.time()

playwright = sync_playwright().start()
browser = playwright.chromium.launch(
    headless=False)
ua = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/69.0.3497.100 Safari/537.36"
)
page = browser.new_page(user_agent=ua)
# Reading Data From Json
f = open('data.json')
data = json.load(f)
for val in data["all_entries"]:
    data_arr = []
    for value in val.values():
        data_arr.append(value)
    automation_process(playwright, data_arr)

end = time.time()
x = end-start
playwright.stop()
print(
    f"Finished in {int(x/3600)} hours ,{int(((x/3600)-int((x/3600)))*60)} minutes")
