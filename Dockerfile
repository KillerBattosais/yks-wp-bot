#Python 3.8 tabanlı bir görüntü kullanıyoruz
FROM python:3.8-slim

# Çalışma dizini olarak /app belirliyoruz
WORKDIR /app

# requirements.txt dosyasını kopyalıyoruz
COPY requirements.txt .

# Bağımlılıkları yüklüyoruz
RUN pip install --no-cache-dir -r requirements.txt

# Proje dosyalarını kopyalıyoruz
COPY . .

# Botu çalıştırıyoruz
CMD ["python", "bot.py"]
