from playwright.sync_api import sync_playwright
import winsound
import time

def sesli_uyari():
    winsound.Beep(1000, 800)

def kontrol_et():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.tcdd.gov.tr/")
        print("Sayfa açıldı, test başarılı!")
        sesli_uyari()
        browser.close()

while True:
    kontrol_et()
    print("Tekrar denenecek...")
    time.sleep(60)  
