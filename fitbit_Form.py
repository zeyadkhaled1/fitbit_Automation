from playwright.sync_api import sync_playwright, Playwright, TimeoutError as PlaywrightTimeoutError
import random

from discord import SyncWebhook, Embed

def generate_japanese_phone_number():
  area_code = str(random.randint(100, 999))
  first_part = str(random.randint(100, 999)).zfill(3)
  second_part = str(random.randint(1000, 9999)).zfill(4)
  return int(f"{area_code}{first_part}{second_part}")


def generate_uk_phone_number():
    first_part = str(random.randint(1000, 9999))
    second_part = str(random.randint(100000, 999999))
    phone_number = first_part + second_part
    return phone_number


def generate_uk_address():
    counties = [
        "Avon", "Bedfordshire", "Berkshire", "Borders", "Buckinghamshire",
        "Cambridgeshire", "Central", "Cheshire", "Cleveland", "Clwyd",
        "Cornwall", "Cumbria", "Derbyshire", "Devon", "Dorset", "Durham",
        "Dyfed", "East Sussex", "Essex", "Gloucestershire", "Greater London",
        "Greater Manchester", "Gwent", "Gwynedd County", "Hampshire", "Herefordshire",
        "Hertfordshire", "Highlands and Islands", "Humberside", "Isle of Wight",
        "Kent", "Lancashire", "Leicestershire", "Lincolnshire", "Merseyside",
        "Norfolk", "North Yorkshire", "Northamptonshire", "Northumberland",
        "Nottinghamshire", "Oxfordshire", "Powys", "Rutland", "Shropshire",
        "Somerset", "South Glamorgan", "South Yorkshire", "Staffordshire",
        "Strathclyde", "Suffolk", "Surrey", "Tayside", "Tyne and Wear",
        "Warwickshire", "West Glamorgan", "West Midlands", "West Sussex",
        "West Yorkshire", "Wiltshire"
    ]

    cities = [
        "Belfast", "Birmingham", "Bradford", "Brighton", "Bristol", "Cambridge",
        "Canterbury", "Carlisle", "Chelmsford", "Chester", "Chichester",
        "Coventry", "Derby", "Durham", "Ely", "Exeter", "Gloucester",
        "Hereford", "Kingston upon Hull", "Lancaster", "Leeds", "Leicester",
        "Lichfield", "Lincoln", "Liverpool", "City of London", "Manchester",
        "Newcastle upon Tyne", "Norwich", "Nottingham", "Oxford", "Peterborough",
        "Plymouth", "Portsmouth", "Preston", "Ripon", "Salford", "Salisbury",
        "Sheffield", "Southampton", "St Albans", "Stoke-on-Trent", "Sunderland",
        "Truro", "Wakefield", "Wells", "Westminster", "Winchester", "Wolverhampton",
        "Worcester", "York"
    ]

    streets = [
        "Main St", "High St", "Park Ave", "Maple St", "Oak St", "Pine Ave",
        "Cedar Blvd", "Elm St", "Washington Ave", "Madison St", "Jefferson Ave",
        "Lincoln St", "Adams St", "Roosevelt Ave"
    ]
    
    county = random.choice(counties)
    city = random.choice(cities)
    street = random.choice(streets)
    house_number = str(random.randint(1, 999))
    address_line_1 = house_number + ' ' + street
    address_line_2 = city + ', ' + county
    zip_code = str(random.randint(10000, 99999))
    return  address_line_1,address_line_2,zip_code,city,county



def generate_japanese_address():
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

def Discord_webhook_Form_Filling(webhook_url,refrence,address_line_1,first_name,last_name, address_line_2, postal_code, city, state,fitbit_email,paypal_email,phone_number) ->None:
            webhook = SyncWebhook.from_url(webhook_url)
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


def run(playwright: Playwright, first_name, last_name, address_line_1, address_line_2, postal_code, city, state,fitbit_email,paypal_email,phone_number,address_to_search,webhook_url,paymentMethod,country,headlessFlag) -> None:
    Flag=True if headlessFlag=='Yes' else False
    browser = playwright.chromium.launch(headless=Flag)
    context = browser.new_context()
    page = context.new_page()
    x = 0
    while True:
        try:
            page.goto("https://www.fitbitionic.expertinquiry.com/")
            if country=='Japan':
                page.get_by_label("Country").select_option(value='JP')
            elif country=='United Kingdom':    
                page.get_by_label("Country").select_option(value='GB')
            with page.expect_popup() as page1_info:
                page.get_by_role("link", name="Register").click()
            page1 = page1_info.value
            page1.get_by_role(
                "textbox", name="<input type=\"text\" class=\"form-control\" data-bind=\"value:Answer, attr:{maxlength: $root.getMaxLength(MaxLength), 'aria-label': Label, 'aria-required': Required}, event:{keydown: $root.validateTab}\" autocomplete=\"nothing\" aria-labelledby=\"TextTemplate\" />").first.click(timeout=12000000)
            page1.get_by_role(
                "textbox", name="<input type=\"text\" class=\"form-control\" data-bind=\"value:Answer, attr:{maxlength: $root.getMaxLength(MaxLength), 'aria-label': Label, 'aria-required': Required}, event:{keydown: $root.validateTab}\" autocomplete=\"nothing\" aria-labelledby=\"TextTemplate\" />").first.type(first_name)
            page1.get_by_role(
                "textbox", name="<input type=\"text\" class=\"form-control\" data-bind=\"value:Answer, attr:{maxlength: $root.getMaxLength(MaxLength), 'aria-label': Label, 'aria-required': Required}, event:{keydown: $root.validateTab}\" autocomplete=\"nothing\" aria-labelledby=\"TextTemplate\" />").nth(1).click()
            page1.get_by_role(
                "textbox", name="<input type=\"text\" class=\"form-control\" data-bind=\"value:Answer, attr:{maxlength: $root.getMaxLength(MaxLength), 'aria-label': Label, 'aria-required': Required}, event:{keydown: $root.validateTab}\" autocomplete=\"nothing\" aria-labelledby=\"TextTemplate\" />").nth(1).type(last_name)
            if country=='Japan':
                page1.get_by_placeholder("Enter Address Here to Search").click()
                page1.get_by_placeholder(
                    "Enter Address Here to Search").fill(address_to_search)
            page.wait_for_timeout(3000)
            page1.get_by_placeholder("Address Line 1").click()
            page1.get_by_placeholder("Address Line 1").fill(address_line_1)
            page1.get_by_placeholder("Address Line 2").click()
            page1.get_by_placeholder("Address Line 2").fill(address_line_2)
            page1.get_by_placeholder("Post Code").click()
            page1.get_by_placeholder("Post Code").fill(postal_code)
            if country=='Japan':
                page1.get_by_placeholder("City").click()
                page1.get_by_placeholder("City").fill(city)
                page1.get_by_placeholder("State").click()
                page1.get_by_placeholder("State").fill(state)
            elif country=='United Kingdom':
                page1.get_by_placeholder("Town").click()
                page1.get_by_placeholder("Town").fill(city)
            page1.get_by_placeholder("Email Address", exact=True).click()
            page.wait_for_timeout(3000)
            page1.get_by_placeholder("Email Address", exact=True).type(
                fitbit_email)
            page.wait_for_timeout(3000)
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
            page.wait_for_timeout(2000)
            page1.get_by_role(
                "combobox", name="United States: +1").get_by_text("+1").click()
            if country=='Japan':
                page1.get_by_role("option", name="Japan (日本)+81").click()
                page.wait_for_timeout(2000)
                page1.get_by_placeholder("__-____-____").click()
                page.wait_for_timeout(2000)
                page1.get_by_placeholder("__-____-____").type(phone_number)
            elif country=='United Kingdom':
                page1.get_by_role("option", name="United Kingdom+44").first.click()
                page.wait_for_timeout(2000)
                page1.get_by_placeholder("____ ______").click()
                page.wait_for_timeout(2000)
                page1.get_by_placeholder("____ ______").type(phone_number)
            page1.get_by_role(
                "combobox", name="Preferred method of reimbursement").click()
            page1.wait_for_timeout(2000)
            if paymentMethod=='PayPal':
                page1.get_by_role("option", name="PayPal").click()
                page1.locator("#email_RefundEmail").click()
                page1.wait_for_timeout(2000)
                page1.locator("#email_RefundEmail").type(paypal_email)
                page1.locator("#confirm_RefundEmail").click()
                page1.wait_for_timeout(2000)
                page1.locator("#confirm_RefundEmail").type(paypal_email)
            elif paymentMethod=='MasterCard Debit Card':
                 page1.get_by_role("option", name="Electronic MasterCard Debit Card").click()
            elif paymentMethod=='Google eGifts':
                page1.get_by_role("option", name="Google eGift").click()
            page1.wait_for_timeout(2000)
            page1.get_by_text("Yes").click()
            page1.get_by_text("I Agree").click()
            page1.get_by_role("button", name="Next").click()
            page.wait_for_timeout(10000)
            page1.locator("#top-submit").click()
            page.wait_for_timeout(10000)
            # Create a new webhook
            refrence = page1.locator(
                '//*[@id="pageContainer"]/div[5]/div/div/div/div[4]/div[1]/span[2]').inner_text()
            Discord_webhook_Form_Filling(webhook_url,refrence,address_line_1,first_name,last_name,address_line_2,postal_code,city,state,fitbit_email,paypal_email,phone_number)
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
        except:
            pass


#
def main_fill_form(first_name, last_name, address_line_1, address_line_2, postal_code, city, state,fitbit_email,paypal_email,phone_number,address_to_search,webhook_url,paymentMethod,country,headlessFlag):
   with sync_playwright() as playwright:
        run(playwright, first_name, last_name, address_line_1, address_line_2, postal_code, city, state,fitbit_email,paypal_email,phone_number,address_to_search,webhook_url,paymentMethod,country,headlessFlag)
