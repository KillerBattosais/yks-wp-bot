import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# YKS tarihi (22 Haziran)
yks_tarihi = datetime.date(2025, 6, 22)

# WhatsApp Web'e giriş yapacak fonksiyon
def send_whatsapp_message(group_name, message):
    # ChromeDriver'ı yükle ve başlat
    driver = webdriver.Chrome(ChromeDriverManager().install())
    
    # WhatsApp Web'i aç
    driver.get('https://web.whatsapp.com/')
    time.sleep(10)  # QR kodu taramak için bekleme süresi

    # Grup adını bul
    group = driver.find_element(By.XPATH, f"//span[@title='{group_name}']")
    group.click()

    # Mesaj kutusunu bul
    message_box = driver.find_element(By.XPATH, "//div[@contenteditable='true']")

    # Mesajı gönder
    message_box.send_keys(message)
    message_box.send_keys(Keys.RETURN)
 # İşlem tamamlandığında tarayıcıyı kapat
    time.sleep(5)
    driver.quit()

# Kalan gün sayısını hesaplayan fonksiyon
def get_days_until_yks():
    today = datetime.date.today()
    delta = yks_tarihi - today
    return delta.days

# Günlük mesajı hazırlayan fonksiyon
def create_message():
    days_left = get_days_until_yks()
    return f"YKS'ye {days_left} gün kaldı! Başarılar dilerim!"

# Ana fonksiyon
if _name_ == "_main_":
    group_name = "Siz Beni Dışlıyorsunuz😭😭"  # WhatsApp grubunun adı
    message = create_message()  # Mesajı oluştur
    send_whatsapp_message(group_name, message)  
