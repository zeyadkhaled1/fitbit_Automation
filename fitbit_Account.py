from playwright.sync_api import sync_playwright, Playwright, TimeoutError as PlaywrightTimeoutError
import random
import string
from discord import SyncWebhook, Embed


def Discord_webhook_Account_Creation(email, password, first_name, last_name, year, centimeters, pounds,webhook_url,country) -> None:
    webhook = SyncWebhook.from_url(webhook_url)
    embed = Embed(title=f"FitBot{country}", color=0xFF5733)
    embed.add_field(name="Account Creation", value='', inline=False)
    embed.add_field(name="Email", value=email, inline=True)
    embed.add_field(name="Password", value=password)
    embed.add_field(name="First name", value=first_name, inline=True)
    embed.add_field(name="Last name", value=last_name)
    embed.add_field(name="Year", value=str(year))
    embed.add_field(name="Height", value=str(centimeters))
    embed.add_field(name="Weight", value=str(pounds))
    # Send a message to the server
    webhook.send(embed=embed)

def generate_password(length=10):
    password = []
    characters = string.ascii_letters + string.digits + string.punctuation
    for _ in range(length):
        password.append(random.choice(characters))
    return "".join(password)

def generate_English_name() -> str:
    names = [
        "Oliver","Harry","Jack","Charlie","Craig","Crane","Crawford",
        "George","Noah","William","James","Alfie","Leo","Henry","Oscar","Alexander","Ethan","Arthur","Freddie","Max","Isaac","Jacob","Adam",
        "Liam","Thomas","Sebastian","Lucas","Mason","Harrison","Samuel","Mohammed","Benjamin",
        "Daniel","Elijah","Joseph","Mohammed","Dylan","Muhammad","Edward","Jude","Jenson",
        "Toby","Theo","Louis","Elliott","Riley","Felix","Archie","Finlay","Finley","Harvey",
        "Hayden","Aiden","Connor","Zachary","Evan","Ryan","Luke","Matthew","Jayden","Jake",
        "Nathan","Caleb","Callum","Jameson","Logan","Adam","Teddy","Theodore","Albert","Albie",
        "Alfred","Alistair","Andrew","Angus","Anthony","Arnold","Aston","Augustus","Austin",
        "Balthazar","Barnaby","Barry","Basil","Benedict","Benjamin","Bernard","Bertie",
        "Bertram","Bill","Billy","Blair","Blaise","Boris","Boston","Bradley","Braxton","Brayden",
        "Brendan","Brenton","Bret","Brett","Brian","Brice","Bridger","Brighton","Britton","Brock","Brodie",
        "Brody","Brooklyn","Bruce","Bruno","Bryan","Bryant","Bryce","Bryson","Byron","Cadby",
        "Caden","Caelan","Cai","Caiden","Cal","Calder","Caleb","Calum","Camden", "Cameron",
        "Campbell","Carl","Carlton","Carsen","Carson","Carter","Cary","Casey","Cash","Cason",
        "Caspian","Cassius","Castiel","Castor","Cato","Cavan","Cayden","Cedric","Cesar",
        "Chad","Chandler","Channing","Charles","Charley","Charlie","Charlotte","Chase",
        "Chauncey","Chester","Chevy","Chip","Chris","Christian","Christopher","Chuck",
        "Cian","Ciaran","Cillian","Clarence","Clark","Claud","Claude","Clay","Clayton",
        "Clement","Cliff","Clifford","Clifton","Clint","Clinton","Clyde","Cobie","Coby",
        "Codey","Coen","Cohan","Cohen","Colby","Cole","Colin","Collin","Colt","Colton","Conan",
        "Conner","Connor","Conor","Conrad","Cooper","Copen","Corbin","Corey","Cormac","Cornelius","Cornell","Cortez","Cory","Cosmo",
        "Cristian","Cristobal","Crosby","Cruz","Cullen","Curt","Curtis","Cuthbert","Cyril",
        "Cyrus",  "Daniel",    "David",    "Edward",    "Elijah",    "Ethan",    "Finley",    "Frankie",    "Freddie",    "Gabriel",    "George",    "Harvey",    "Henry",    "Isaac",    "Jack",    "Jacob",    "James",    "Jayden",    "John",    "Jonathan",    "Joseph",    "Joshua",    "Leo",    "Lewis",    "Liam",    "Logan",    "Lucas",    "Mason",    "Max",    "Mohammed",    "Muhammad",    "Noah",    "Oliver",    "Oscar",    "Owen",    "Parker",    "Reggie",    "Rhys",    "Riley",    "Robert",    "Roman",    "Rory",    "Ruben",    "Ryan",    "Samuel",    "Sebastian",    "Sonny",    "Theo",    "Thomas",    "Toby",    "Tommy",    "Tyler",    "William",    "Wyatt"]

    return random.choice(names)

def generate_Japanese_name() -> str:
    names = ['Asahi', 'Akihiko', 'Akira', 'Aoki', 'Asa',
             'Botan', 'Benjiro', 'Chibi', 'Chiharu', 'Chikafusa', 'Chikao', 'Chiko', 'Chimon', "Dai", 'Doi', 'Daido', 'Daiki', 'Daisuke',
             'Danno', 'Danuja', 'Enmei', 'Fumihiro', 'Genkei', 'Giichi', 'Goku', 'Goro', 'Gou', 'Habiki', 'Hachi', 'Hachirou', 'Hakaku',
             'Hansuke', 'Harue', 'Hayate', 'Hekima', 'Hideo', 'Hiroto', 'Hiroshi', 'Hiroyuki', 'Hotaru', 'Ichiro', 'Itachi', 'Jiro', 'Jomei',
             'Jona', 'Junichiro', 'Junpei', 'Jurou', 'Kaede', 'Kaemon', 'Kage', 'Kaiyo', 'Kamaye', 'Kame', 'Kamin', 'Kazz', 'Kazumi', 'Keiji', 'Keisuke',
             'Keitaro', 'Ken', 'Kenji', 'Kiyoshi', 'Koji', 'Kota', 'Mako', 'Masashi', 'Minor', 'Miyo', 'Miyoko', 'Namiko', 'Nana', 'Nao', 'Naoki', 'Naoyuki',
             'Naozumi', 'Natsu', 'Noa', 'Noboru', 'Noburu', 'Noritaka', 'Notin', 'Oda', 'Ohta', 'Orochi', 'Reiji', 'Souta ', 'Sana ',
             'Takato', 'Takaya', 'Take', 'Takuma', 'Tamaki', 'Tamashini', 'Touma', 'Yamato', 'Yo', 'Yoshio', 'Akiara',
             'Akio', 'Akito', 'Aoki', 'Aoto', 'Aoi', 'Asahi', 'Fuji', 'Haru', 'Haruto', 'Haruki', 'Hideaki', 'Hikaru', 'Hinata',
             'Hiroaki', 'Hirohito', 'Hiroaki', 'Kouma', 'Minato', 'Katsumi', 'Katsuro', 'Kazu', 'Kazue', 'Kazuki', 'Kazumi', 'Kazuo', 'Kazuya', 'Kei', 'Kaito', 'Kane', 'Kenji', 'Itsuki', 'Minato', 'Naruhito', 'Nori', 'Osamu', 'Ren', 'Reiki', 'Reiko ',
             'Reo', 'Riku', 'Rin', 'Ringo', 'Souta', 'Sora', 'Sousuke', 'Souma', 'Taemon', 'Taichi', 'Taiga', 'Taiki', 'Taji', 'Takahiro', 'Takai', 'Takashi', 'Touma', 'Yuito', 'Yuuto', 'Yuusei', 'Yuuma', 'Arata', 'Asa', 'Asas', 'Chi', 'Chiyo', 'Haku', 'Daku', 'Eito',
             'Genkei', 'Giichi', 'Gin', 'Ginjiro', 'Hiromitsu', 'Hironori', 'Hironori', 'Hisahito', 'Ikuto', 'Isamu', 'Kai', 'Kaname',
             'Kanon', 'Kaoru', 'Kisho', 'Kiyoshi', 'Kuragari', 'Masao', 'Mitsuki', 'Naruto', 'Niko', 'Raiden', 'Ronin', 'Saburou',
             'Sana', 'Shiki', 'Syaoran', 'Tadashi', 'Tomiichi', 'Tomohiro', 'Tomoya', 'Youta']
    return random.choice(names)


def generate_year_of_birth():
    return random.randint(1984, 1999)


def generate_centimeters():
    return random.randint(160, 183)


def generate_pounds():
    return random.randint(100, 150)


def run(playwright: Playwright, email, password, first_name, last_name, year, centimeters, pounds,webhook,country,headlessFlag) -> None:
    Flag=True if headlessFlag=='Yes' else False
    try:
        browser = playwright.chromium.launch(headless=Flag)
        context = browser.new_context()
        # page = context.new_page()
        # page.goto("https://quik.email/en")
        # page.wait_for_timeout(20000)
        # email_test = page.locator("#trsh_mail").input_value()
        # print(email)
        page1 = context.new_page()
        page1.goto(
            f"https://accounts.fitbit.com/signup?targetUrl=https%3A%2F%2Fwww.fitbit.com%2Fglobal%2Fjp%2Fhome")
        page1.get_by_placeholder("Your email address").click()
        page1.get_by_placeholder("Your email address").fill(email)
        page1.get_by_placeholder("Choose your password").click()
        page1.get_by_placeholder("Choose your password").fill(
            password)
        page1.get_by_label(
            "I agree to the Fitbit Terms of Service. Please also read the Privacy Policy including the Cookie Use statement.").check()
        page1.get_by_role("button", name="Join Fitbit").click()
        # page1.wait_for_timeout(30000)
        # page.get_by_role("link", name="View").click()
        # with page.expect_popup() as page2_info:
        #     page.frame_locator("#myIframe").get_by_role(
        #         "link", name="Verify Your Email").click()
        # page2 = page2_info.value
        # page2.close()
        page1.wait_for_timeout(50000)
        page1.get_by_placeholder("First name").click()
        page1.wait_for_timeout(2000)
        page1.get_by_placeholder("First name").fill(first_name)
        page1.wait_for_timeout(2000)
        page1.get_by_placeholder("Last name").click()
        page1.wait_for_timeout(2000)
        page1.get_by_placeholder("Last name").fill(last_name)
        page1.wait_for_timeout(2000)
        page1.get_by_placeholder("Year").click()
        page1.wait_for_timeout(2000)
        page1.get_by_placeholder("Year").fill(str(year))
        page1.wait_for_timeout(2000)
        page1.get_by_role("button", name="Continue").click()
        page1.wait_for_timeout(2000)
        page1.locator(
            "#height-system").get_by_role("combobox").select_option("METRIC")
        page1.get_by_placeholder("Centimeters").click()
        page1.wait_for_timeout(2000)
        page1.get_by_placeholder("Centimeters").fill(str(centimeters))
        page1.wait_for_timeout(2000)
        page1.get_by_placeholder("Pound").click()
        page1.wait_for_timeout(2000)
        page1.get_by_placeholder("Pound").fill(str(pounds))
        page1.wait_for_timeout(2000)
        page1.locator("#gender").get_by_role("combobox").select_option("MALE")
        page1.wait_for_timeout(2000)
        page1.get_by_role("button", name="Create Account").click()
        page1.wait_for_timeout(7000)
        Discord_webhook_Account_Creation(
            email, password, first_name, last_name, year, centimeters, pounds,webhook,country)
        # ---------------------
        page1.goto("https://www.fitbit.com/settings/profile")
        page1.wait_for_timeout(2000)
        if country =='Japan':
            page1.get_by_role("combobox", name="COUNTRY").select_option("JP")
        elif country =='United Kingdom':
            page1.get_by_role("combobox", name="COUNTRY").select_option("GB")
        page1.wait_for_timeout(2000)
        page1.locator('//*[@id="language-by-region/country"]').click()
        page1.wait_for_timeout(2000)
        if country =='Japan':
            page1.get_by_role(
                "region", name="LANGUAGE BY REGION/COUNTRY").get_by_role("combobox").select_option("ja_JP")
        if country =='United Kingdom':
            page1.get_by_role(
                "region", name="LANGUAGE BY REGION/COUNTRY").get_by_role("combobox").select_option("en_GB")
        page1.wait_for_timeout(2000)
        page1.query_selector("h2#timezone").click()
        page1.wait_for_timeout(2000)
        if country=='Japan':
            page1.get_by_role("region", name="TIMEZONE").get_by_role(
                "combobox").select_option("Asia/Tokyo")
        elif country=='United Kingdom':
            page1.get_by_role("region", name="TIMEZONE").get_by_role(
                "combobox").select_option("Europe/London")
            
        page1.wait_for_timeout(2000)
        page1.get_by_role("button", name="Submit").click()
        page1.wait_for_timeout(2000)
        context.close()
        browser.close()
    except Exception as e:
        print(e)
        pass


def main_account_creation(email, password, first_name, last_name, year, centimeters, pounds,webhook,country,headlessFlag):
    with sync_playwright() as playwright:
        run(playwright, email, password, first_name,
            last_name, year, centimeters, pounds,webhook,country,headlessFlag)


# main_account_creation('mango','magolol123@de7k','bankai','minazuki','1996','170','200')
