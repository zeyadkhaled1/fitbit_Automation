from playwright.sync_api import sync_playwright, Playwright, TimeoutError as PlaywrightTimeoutError
import random

from discord import SyncWebhook, Embed


def Discord_webhook_Account_Creation(email, password, first_name, last_name, year, centimeters, pounds) ->None:
    webhook = SyncWebhook.from_url(
                'https://discordapp.com/api/webhooks/1068494626769621022/wlKEYJjzbxgVkwIyHZgE6D9lEoFTbiP9BSnEtxxByCauPa5PXHEwgOK555YpYZyTysl7')
    embed = Embed(title="FitBotJP", color=0xFF5733)
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


def run(playwright: Playwright, email, password, first_name, last_name, year, centimeters, pounds) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://quik.email/en")
    page.wait_for_timeout(20000)
    email_test = page.locator("#trsh_mail").input_value()
    print(email)
    page1 = context.new_page()
    page1.goto(
        f"https://accounts.fitbit.com/signup?targetUrl=https%3A%2F%2Fwww.fitbit.com%2Fglobal%2Fjp%2Fhome")
    page1.get_by_placeholder("Your email address").click()
    page1.get_by_placeholder("Your email address").fill(email_test)
    page1.get_by_placeholder("Choose your password").click()
    page1.get_by_placeholder("Choose your password").fill(
        password)
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
    page1.get_by_placeholder("First name").fill(first_name)
    page.wait_for_timeout(2000)
    page1.get_by_placeholder("Last name").click()
    page.wait_for_timeout(2000)
    page1.get_by_placeholder("Last name").fill(last_name)
    page.wait_for_timeout(2000)
    page1.get_by_placeholder("Year").click()
    page.wait_for_timeout(2000)
    page1.get_by_placeholder("Year").fill(str(year))
    page.wait_for_timeout(2000)
    page1.get_by_role("button", name="Continue").click()
    page.wait_for_timeout(2000)
    page1.locator(
        "#height-system").get_by_role("combobox").select_option("METRIC")
    page1.get_by_placeholder("Centimeters").click()
    page.wait_for_timeout(2000)
    page1.get_by_placeholder("Centimeters").fill(str(centimeters))
    page.wait_for_timeout(2000)
    page1.get_by_placeholder("Pound").click()
    page.wait_for_timeout(2000)
    page1.get_by_placeholder("Pound").fill(str(pounds))
    page.wait_for_timeout(2000)
    page1.locator("#gender").get_by_role("combobox").select_option("MALE")
    page.wait_for_timeout(2000)
    page1.get_by_role("button", name="Create Account").click()
    page.wait_for_timeout(7000)
    Discord_webhook(email_test, password, first_name, last_name, year, centimeters, pounds)
    # ---------------------
    context.close()
    browser.close()


def main_account_creation(email, password, first_name, last_name, year, centimeters, pounds):
    with sync_playwright() as playwright:
        run(playwright, email, password, first_name,
            last_name, year, centimeters, pounds)
