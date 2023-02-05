from playwright.sync_api import sync_playwright, Playwright, TimeoutError as PlaywrightTimeoutError
import random

from discord import SyncWebhook, Embed

def generate_japanese_phone_number():
  area_code = str(random.randint(100, 999))
  first_part = str(random.randint(100, 999)).zfill(3)
  second_part = str(random.randint(1000, 9999)).zfill(4)
  return int(f"{area_code}{first_part}{second_part}")


def generate_address():
    prefectures = ['Hokkaido', 'Aomori', 'Iwate', 'Miyagi', 'Akita', 'Yamagata',               'Fukushima', 'Ibaraki', 'Tochigi', 'Gunma', 'Saitama', 'Chiba',               'Tokyo', 'Kanagawa', 'Niigata', 'Toyama', 'Ishikawa', 'Fukui',               'Yamanashi', 'Nagano', 'Gifu', 'Shizuoka', 'Aichi', 'Mie',               'Shiga', 'Kyoto', 'Osaka', 'Hyogo', 'Nara', 'Wakayama', 'Tottori',               'Shimane', 'Okayama', 'Hiroshima', 'Yamaguchi', 'Tokushima', 'Kagawa',               'Ehime', 'Kochi', 'Fukuoka', 'Saga', 'Nagasaki', 'Kumamoto', 'Oita',               'Miyazaki', 'Kagoshima', 'Okinawa']

    cities = ['Tokyo', 'Yokohama', 'Osaka', 'Nagoya', 'Sapporo', 'Kobe', 'Kyoto',          'Fukuoka', 'Sendai', 'Shizuoka', 'Hiroshima', 'Kawasaki', 'Saitama',          'Yonago', 'Hamamatsu', 'Matsuyama', 'Okayama', 'Fukushima', 'Asahikawa']

    streets = ['Main St', 'High St', 'Park Ave', 'Maple St', 'Oak St', 'Pine Ave',           'Cedar Blvd', 'Elm St', 'Washington Ave', 'Madison St', 'Jefferson Ave',           'Lincoln St', 'Adams St', 'Roosevelt Ave']
    
    prefecture = random.choice(prefectures)
    city = random.choice(cities)
    street = random.choice(streets)
    house_number = str(random.randint(1, 999))
    address_line_1 = street + ' ' + house_number
    address_line_2 = city + ', ' + prefecture
    zip_code = str(random.randint(10000, 99999))
    return  address_line_1,address_line_2,zip_code,city,prefecture

def Discord_webhook_Form_Filling(webhook,refrence,address_line_1,first_name,last_name, address_line_2, postal_code, city, state,fitbit_email,paypal_email,phone_number) ->None:
            webhook = SyncWebhook.from_url(
                'https://discordapp.com/api/webhooks/1068494626769621022/wlKEYJjzbxgVkwIyHZgE6D9lEoFTbiP9BSnEtxxByCauPa5PXHEwgOK555YpYZyTysl7')
            embed = Embed(title="FitBotJP", color=0xFF5733)
            embed.add_field(name="Submitted Form", value='', inline=False)
            embed.add_field(name="Email", value=fitbit_email, inline=True)
            embed.add_field(name="Ref", value=refrence)
            embed.add_field(name="First name", value=first_name, inline=True)
            embed.add_field(name="Last name", value=last_name)
            embed.add_field(name="Address", value=address_line_1)
            embed.add_field(name="Address2", value=address_line_2)
            embed.add_field(name="phone", value=phone_number)
            embed.add_field(name="Paypal Email", value=paypal_email)
            embed.add_field(name="State", value=state)
            embed.add_field(name="City", value=city)
            embed.add_field(name="Zip_code", value=postal_code)
            # Send a message to the server
            webhook.send(embed=embed)


def run(playwright: Playwright, first_name, last_name, address_line_1, address_line_2, postal_code, city, state,fitbit_email,paypal_email,phone_number,address_to_search) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    x = 0
    while True:
        try:
            page.goto("https://www.fitbitionic.expertinquiry.com/")
            page.get_by_label("Country").select_option(value='JP')
            with page.expect_popup() as page1_info:
                page.get_by_role("link", name="Register").click()
            page1 = page1_info.value
            page1.get_by_role(
                "textbox", name="<input type=\"text\" class=\"form-control\" data-bind=\"value:Answer, attr:{maxlength: $root.getMaxLength(MaxLength), 'aria-label': Label, 'aria-required': Required}, event:{keydown: $root.validateTab}\" autocomplete=\"nothing\" aria-labelledby=\"TextTemplate\" />").first.click(timeout=1200000)
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
            Discord_webhook_Form_Filling(webhook,refrence,address_line_1,first_name,last_name,address_line_2,postal_code,city,state,fitbit_email,paypal_email,phone_number)
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
def main_fill_form(first_name, last_name, address_line_1, address_line_2, postal_code, city, state,fitbit_email,paypal_email,phone_number,address_to_search):
   with sync_playwright() as playwright:
        run(playwright, first_name, last_name, address_line_1, address_line_2, postal_code, city, state,fitbit_email,paypal_email,phone_number,address_to_search)
