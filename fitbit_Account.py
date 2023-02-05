from playwright.sync_api import sync_playwright, Playwright, TimeoutError as PlaywrightTimeoutError
import random

# def automation_process():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(
#             headless=False)
#         ua = (
#             "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
#             "AppleWebKit/537.36 (KHTML, like Gecko) "
#             "Chrome/69.0.3497.100 Safari/537.36"
#         )
#         page = browser.new_page(user_agent=ua)
#         page.goto(
#             "http://agencies.monroecountypa.gov/monroepa_prod/search/commonsearch.aspx?mode=realprop", wait_until="load")


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
    # page.goto("https://quik.email/en")
    # page.wait_for_timeout(20000)
    # email = page.locator("#trsh_mail").input_value()
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
    page1.get_by_placeholder("Year").fill(year)
    page.wait_for_timeout(2000)
    page1.get_by_role("button", name="Continue").click()
    page.wait_for_timeout(2000)
    page1.locator(
        "#height-system").get_by_role("combobox").select_option("METRIC")
    page1.get_by_placeholder("Centimeters").click()
    page.wait_for_timeout(2000)
    page1.get_by_placeholder("Centimeters").fill(centimeters)
    page.wait_for_timeout(2000)
    page1.get_by_placeholder("Pound").click()
    page.wait_for_timeout(2000)
    page1.get_by_placeholder("Pound").fill(pounds)
    page.wait_for_timeout(2000)
    page1.locator("#gender").get_by_role("combobox").select_option("MALE")
    page.wait_for_timeout(2000)
    page1.get_by_role("button", name="Create Account").click()
    page.wait_for_timeout(7000)

    # ---------------------
    context.close()
    browser.close()


def main(email, password, first_name, last_name, year, centimeters, pounds):
    with sync_playwright() as playwright:
        run(playwright, email, password, first_name,
            last_name, year, centimeters, pounds)
