
import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By

# WhatsApp Web bağlantısı
driver = webdriver.Chrome(executable_path="/path/to/chromedriver")  # Burada doğru path'i kullan
driver.get("https://web.whatsapp.com")

# WhatsApp'a giriş yaptıktan sonra, beklemek için bir süre tanıyın
time.sleep(15)  # 15 saniye kadar bekleyebilirsiniz

# WhatsApp grubunu bulmak için grubun adı
group_name = "Siz Beni Dışlıyorsunuz😭😭"  # Burada grup adını gir

# Mesaj gönderme işlevi
def send_message(message):
    group = driver.find_element(By.XPATH, f'//span[@title="{group_name}"]')
    group.click()
    time.sleep(2)
    message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"]')
    message_box.send_keys(message)
    message_box.send_keys(u'\ue007')  # Enter tuşu

# Günlük mesaj gönderme
def daily_message():
    # YKS'ye kalan gün sayısı
    today = datetime.date.today()
    target_date = datetime.date(2025, 6, 5)  # YKS tarihi
    days_left = (target_date - today).days

    # Motivasyon mesajını internetten al
    motivation_message = f"YKS'ye {days_left} gün kaldı. Hedefe doğru ilerlemeye devam et!"

    # Gruba mesajı gönder
    send_message(motivation_message)

# Botun her gün 08:00'de çalışması için bir zamanlayıcı
while True:
    now = datetime.datetime.now()
    if now.hour == 8 and now.minute == 0:
        daily_message()
        time.sleep(60)  # 1 dakika bekle, tekrar aynı saatte çalışmasın
    time.sleep(30)  # Her 30 saniyede bir zamanı kontrol et
