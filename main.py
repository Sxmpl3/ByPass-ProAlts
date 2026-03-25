import requests
import pyfiglet
import re, time, json


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from colorama import Fore, Style
from tqdm import tqdm

banner = pyfiglet.figlet_format("ProAlts ByPass", font="slant")

def get_token():
    url = "https://proalts.com/core/nordvpn/generate"

    cookies = {
        "version": "lite"
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:148.0) Gecko/20100101 Firefox/148.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Referer": "https://proalts.com/nordvpn",
    }

    url = "https://proalts.com/core/nordvpn/generate"
    r = requests.get(url, headers=headers, cookies=cookies)

    token = re.findall(r"\?ssid=([^&]+)", r.url)
    
    return token[0]

def skip_steps(token):
    url = f"https://scholarships.lalaloot.com/api/session/{token}/step/increment"

    cookies = {
        "cf_clearance": "10TQS89IhufVaOZuy9GF7e6Ut0IgjHZVD4GZVIoKyRI-1774470963-1.2.1.1-asvvpv7C4GAYWeEfeEPb5.SUSErxQ5x4oVAuuUjTndTFG35pL7RUoMJTgJJwZkCb52Sy.BB9kSFvvo9j0akptPx9ikH2up9Ra9LWSssli3vC0TSaRWNQ.kB_.6.ISAJPxsY0l.OCNqRSDHcfe9ABkyFLJ29y6U.BV_9fxZDc4QOMfXrI4kJf99JnEs1uUoqPO87Rg8uc3X5e_rqQ.6FprZb7ro_DCxQmYPXAO41vBb8",
        "_ga_4JJHZBNFXH": "GS2.1.s1774469724$o1$g1$t1774471035$j46$l0$h0",
        "_ga": "GA1.1.1132171408.1774469725",
        "_gid": "GA1.2.1276470726.1774469725",
        "version": "lite"
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:148.0) Gecko/20100101 Firefox/148.0",
        "Accept": "*/*",
        "Accept-Language": "es-ES,es;q=0.9,en-US;q=0.8,en;q=0.7",
        "Accept-Encoding": "gzip, deflate",
        "Referer": "https://scholarships.lalaloot.com/top-7-best-health-insurance-companies-in-the-usa-2026/",
        "Content-Type": "application/json",
        "Origin": "https://scholarships.lalaloot.com",
        "Te": "trailers",
    }
    
    while True:
        r = requests.patch(url, headers=headers, cookies=cookies)

        json_response = json.loads(r.text)
        final_url = json_response.get("session", {}).get("finalDestination")

        if final_url:
            return final_url

def get_data(final_url):
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    driver.get(final_url)

    for _ in tqdm(range(10), desc=f"{Fore.GREEN} [+] Saltando ads y obteniendo cuenta...{Style.RESET_ALL}"):
        time.sleep(1)

    user = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "mail"))
    ).get_attribute("value")

    password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "pass"))
    ).get_attribute("value")

    print(f"\n  - {Fore.BLUE}User: {Fore.WHITE}{user}")
    print(f"  - {Fore.BLUE}Password: {Fore.WHITE}{password}")

if __name__ == "__main__":
    print(Fore.MAGENTA + banner + Style.RESET_ALL)
    print(f"{Fore.MAGENTA}> By: https://github.com/Sxmpl3{Style.RESET_ALL}\n")

    token = get_token()
    for _ in tqdm(range(5), desc=f"{Fore.GREEN} [+] Obteniendo token...{Style.RESET_ALL}"):
        time.sleep(1)
    final_url = skip_steps(token)
    get_data(final_url)