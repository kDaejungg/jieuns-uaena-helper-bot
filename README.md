# Jieun's Uaena Helper (v1.2.0)

IU hayranları için tasarlanmış, modern Discord arayüz özelliklerini (Buttons, Slash Commands) kullanan interaktif bir asistan botu.

---
# Kurulum

Kullandığınız İS'ye göre adımları uygulayınız.
## Linux

Linux sistemlerde Python genellikle yüklü gelir. Terminalinizi açın ve şu adımları izleyin:

1. **Depoyu Klonlayın:**
   ```bash
   git clone https://github.com/kDaejungg/jieuns-uaena-helper-bot.git
    cd jieuns-uaena-helper-bot
   ```
2. **Sanal Ortam Oluşturun:**
   ```bash
   python3 -m venv venv
   ```
3. **Sanal Ortamı Aktifleştirin:**
   ```bash
   source venv/bin/activate
   ```
4. **Gereksinimleri Yükleyin:**
   ```bash
   pip install -r requirements.txt
   ```
5. **Botu Çalıştırın:**
   ```bash
   python3 bot.py
   ```

---

## Windows

Windows'ta PowerShell veya Komut İstemi (CMD) kullanabilirsiniz. Python'ın sistem yoluna (PATH) ekli olduğundan emin olun.

1. **Depoyu Klonlayın:**
   ```powershell
   git clone https://github.com/kDaejungg/jieuns-uaena-helper-bot.git
cd jieuns-uaena-helper-bot
   ```
2. **Sanal Ortam Oluşturun:**
   ```powershell
   python -m venv venv
   ```
3. **Sanal Ortamı Aktifleştirin:**
   ```powershell
   .\venv\Scripts\activate
   ```
4. **Gereksinimleri Yükleyin:**
   ```powershell
   pip install -r requirements.txt
   ```
5. **Botu Çalıştırın:**
   ```powershell
   python bot.py
   ```

---

## macOS

Mac kullanıcıları Terminal uygulamasını kullanarak aşağıdaki adımları takip edebilir:

1. **Depoyu Klonlayın:**
   ```bash
   git clone https://github.com/kDaejungg/jieuns-uaena-helper-bot.git
cd jieuns-uaena-helper-bot
   ```
2. **Sanal Ortam Oluşturun:**
   ```bash
   python3 -m venv venv
   ```
3. **Sanal Ortamı Aktifleştirin:**
   ```bash
   source venv/bin/activate
   ```
4. **Gereksinimleri Yükleyin:**
   ```bash
   pip install -r requirements.txt
   ```
5. **Botu Çalıştırın:**
   ```bash
   python3 bot.py
   ```

---

## 📂 Dosya Yapısı ve İçerik

- `bot.py`: Ana bot motoru ve Discord komutları.
- `iu_data.json`: Şarkılar, karakterler ve mod verileri.
- `about.json`: Botun kimlik bilgileri (Sürüm, Geliştirici).
- `requirements.txt`: Gerekli Python kütüphaneleri
- `.gitignore`: Token ve gereksiz dosyaların GitHub'a gitmesini engelleyen liste.

## ⚠️ Önemli Güvenlik Notu
`bot.py` dosyasındaki `TOKEN` kısmına kendi bot anahtarınızı girmelisiniz. Projeyi GitHub'da herkese açık (Public) paylaşmadan önce bu token'ı sildiğinizden veya `.env` dosyasına taşıdığınızdan emin olun.

---
*Made with 💜 for Uaenas by kDaejungg*
