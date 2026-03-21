# Jieun's Uaena Helper (v1.2.0)

IU hayranları için tasarlanmış, modern Discord arayüz özelliklerini (Buttons, Slash Commands) kullanan interaktif bir asistan botu.

---
# Kurulum

Kullandığınız İS'ye göre adımları uygulayınız.
## Yapılandırma 

Botun çalışması için bir "Discord Bot Token"ına ihtiyacınız var. Eğer nasıl alınacağını bilmiyorsanız [Discord Developer Portal](https://discord.com/developers/applications) üzerinden bir uygulama oluşturup "Bot" sekmesinden token'ınızı kopyalayabilirsiniz.

### Adım Adım Token Kurulumu:

1. **Gizli Dosyaları Görünür Yapın:**
   - **Windows:** Klasörde yukarıdaki "Görünüm" sekmesinden "Gizli Öğeler" kutucuğunu işaretleyin.
   - **Linux / macOS:** Klasör içindeyken `Ctrl + H` tuşlarına basarak `.env.example` dosyasını görünür yapın.

2. **Dosyayı Hazırlayın:**
   - `.env.example` dosyasının ismine sağ tıklayıp "Yeniden Adlandır" deyin.
   - Sondaki `.example` kısmını silin. Dosyanın yeni adı sadece `.env` olmalıdır.

3. **Token'ı Yapıştırın:**
   - Yeni oluşturduğunuz `.env` dosyasını Not Defteri veya herhangi bir metin düzenleyici ile açın.
   - `DISCORD_TOKEN=[addyourdiscordtokenhere]` satırındaki `[addyourdiscordtokenhere]` kısmını silip, kendi token'ınızı yapıştırın.
   - Dosyayı kaydedip kapatın.

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
*Made with 💜 for Uaenas by Enes Ramazan Whitelineage*
