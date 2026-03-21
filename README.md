# Jieun's Uaena Helper (v1.2.0)

IU (Lee Ji-eun) hayranları için sayfalandırılmış diskografi, ruh haline göre şarkı önerileri ve eğlenceli mini oyunlar içeren etkileşimli bir Discord asistanı. (Sadece Türkçe olarak mevcuttur)

## ⚠️Sadece botu sunucunuza eklemek istiyorsanız bu bağlantıyı kullanın ve aşağıda belirtilen adımları göz ardı edin: [![Discord Invite](https://img.shields.io/badge/Discord-Botu_Sunucuna_Ekle-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.com/oauth2/authorize?client_id=1484879171183443978&permissions=5066929685518400&integration_type=0&scope=bot)

---
# Kurulum

Kullandığınız İS'ye göre adımları uygulayınız.

## Yapılandırma
Kurulum kısmında bulunan birinci adımdan sonra aşağıdaki adımları uygulayın:

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
   ```


   ⚠️DAHA ÖNCE BELİRTİLEN YAPILANDIRMA ADIMLARINI TAKİP EDİN


   ```bash
    cd jieuns-uaena-helper-bot
   ```
   
1. **Sanal Ortam Oluşturun:**
   ```bash
   python3 -m venv venv
   ```
2. **Sanal Ortamı Aktifleştirin:**
   ```bash
   source venv/bin/activate
   ```
3. **Gereksinimleri Yükleyin:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Botu Çalıştırın:**
   ```bash
   python3 bot.py
   ```

---

## Windows

Windows'ta PowerShell veya Komut İstemi (CMD) kullanabilirsiniz. Python'ın sistem yoluna (PATH) ekli olduğundan emin olun.

1. **Depoyu Klonlayın:**
   ```powershell
   git clone https://github.com/kDaejungg/jieuns-uaena-helper-bot.git
   ```

   ⚠️DAHA ÖNCE BELİRTİLEN YAPILANDIRMA ADIMLARINI TAKİP EDİN

   
   ```powershell
   cd jieuns-uaena-helper-bot
   ```
1. **Sanal Ortam Oluşturun:**
   ```powershell
   python -m venv venv
   ```
2. **Sanal Ortamı Aktifleştirin:**
   ```powershell
   .\venv\Scripts\activate
   ```
3. **Gereksinimleri Yükleyin:**
   ```powershell
   pip install -r requirements.txt
   ```
4. **Botu Çalıştırın:**
   ```powershell
   python bot.py
   ```

---

## macOS

Mac kullanıcıları Terminal uygulamasını kullanarak aşağıdaki adımları takip edebilir:

1. **Depoyu Klonlayın:**
   ```bash
   git clone https://github.com/kDaejungg/jieuns-uaena-helper-bot.git
   ```


   ⚠️DAHA ÖNCE BELİRTİLEN YAPILANDIRMA ADIMLARINI TAKİP EDİN


   ```bash
    cd jieuns-uaena-helper-bot
   ```
1. **Sanal Ortam Oluşturun:**
   ```bash
   python3 -m venv venv
   ```
2. **Sanal Ortamı Aktifleştirin:**
   ```bash
   source venv/bin/activate
   ```
3. **Gereksinimleri Yükleyin:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Botu Çalıştırın:**
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
