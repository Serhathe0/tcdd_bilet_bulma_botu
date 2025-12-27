import time
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import winsound

# Log ayarları
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def alert_sound():
    """Windows sistem sesi ile uyarı verir"""
    for _ in range(3):
        winsound.MessageBeep()
        time.sleep(0.5)

def check_available_tickets(driver):
    """Sayfadaki trenlerde boş koltuk olup olmadığını kontrol eder"""
    try:
        sefer_listesi = driver.find_element(By.ID, "seferListScroll")
        html = sefer_listesi.get_attribute("innerHTML")

        if any(keyword in html for keyword in ["Boş", "Koltuk Var", "Satışa Açık"]):
            logging.info("💥 Boş koltuk bulundu! 💥")
            alert_sound()
        else:
            logging.warning("😔 Henüz boş koltuk yok.")
    except Exception as e:
        logging.error(f"Hata oluştu: {e}")

def main():
    # Chrome başlat
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # TCDD sayfasını aç
    logging.info("TCDD e-bilet sayfası açılıyor...")
    driver.get("https://ebilet.tcddtasimacilik.gov.tr/view/eybis/tnmGenel/tcddWebContent.jsf")

    logging.info("Lütfen 'Nereden', 'Nereye' ve 'Tarih' alanlarını manuel doldur ve 'Ara' butonuna bas.")
    input("➡️ Tren listesi yüklendikten sonra ENTER’a bas: ")

    while True:
        check_available_tickets(driver)
        logging.info("⏳ 60 saniye bekleniyor...")
        time.sleep(60)

        driver.refresh()
        logging.info("🔄 Sayfa yenilendi, tekrar kontrol ediliyor...")

if __name__ == "__main__":
    main()
