import discord
from discord import app_commands
import random
from dotenv import load_dotenv
import os
import json

with open('iu_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
with open('about.json', 'r', encoding='utf-8') as f:
    ABOUT_DATA = json.load(f)

# Verilere Erişme
IU_COLOUR = int(data["iu_colour"], 16)
BIO = data["bio"]
DISCOGRAPHY = data["discography"]
FACTS = data["facts"]
SONGS_INFO = data["songs_info"]
CHARACTERS = data["characters"]
MOODS = data["moods"]

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

class IUBot(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()
        print("✅ Slash komutları senkronize edildi.")

class DiscographyView(discord.ui.View):
    def __init__(self, data_list, title):
        super().__init__(timeout=60)
        self.data_list = data_list
        self.title = title
        self.per_page = 10
        self.current_page = 0

    def create_embed(self):
        start = self.current_page * self.per_page
        end = start + self.per_page
        items = self.data_list[start:end]
        
        description = "\n".join(f"• {item}" for item in items)
        page_info = f"Sayfa {self.current_page + 1} / {((len(self.data_list)-1)//self.per_page) + 1}"
        
        embed = discord.Embed(title=self.title, description=description, color=IU_COLOUR)
        embed.set_footer(text=page_info)
        return embed

    @discord.ui.button(label="⬅️ Geri", style=discord.ButtonStyle.gray)
    async def previous(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.current_page > 0:
            self.current_page -= 1
            await interaction.response.edit_message(embed=self.create_embed(), view=self)
        else:
            await interaction.response.send_message("Zaten ilk sayfadasın!", ephemeral=True)

    @discord.ui.button(label="İleri ➡️", style=discord.ButtonStyle.gray)
    async def next(self, interaction: discord.Interaction, button: discord.ui.Button):
        if (self.current_page + 1) * self.per_page < len(self.data_list):
            self.current_page += 1
            await interaction.response.edit_message(embed=self.create_embed(), view=self)
        else:
            await interaction.response.send_message("Zaten son sayfadasın!", ephemeral=True)

class MoodView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=60)

    # Öneri gönderme yardımcı fonksiyonu
    async def send_recommendation(self, interaction: discord.Interaction, mood_key: str):
        songs = MOODS.get(mood_key, [])
        if songs:
            chosen_song = random.choice(songs)
            # JSON'daki SONGS_INFO'dan detay çekmeye çalışalım
            detail = SONGS_INFO.get(chosen_song.lower().strip(), "Bu parça için detaylı bilgi henüz eklenmedi.")
            
            embed = discord.Embed(
                title=f"✨ {mood_key.capitalize()} Modu Önerisi",
                description=f"Senin için seçtiğim şarkı: **{chosen_song}**\n\n{detail}",
                color=IU_COLOUR
            )
            await interaction.response.send_message(embed=embed, ephemeral=True)
        else:
            await interaction.response.send_message("Şarkı listesi yüklenemedi!", ephemeral=True)

    @discord.ui.button(label="Mutlu 🌸", style=discord.ButtonStyle.success)
    async def happy(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.send_recommendation(interaction, "mutlu")

    @discord.ui.button(label="Üzgün 🌧️", style=discord.ButtonStyle.primary)
    async def sad(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.send_recommendation(interaction, "uzgun")

    @discord.ui.button(label="Enerjik 🔥", style=discord.ButtonStyle.danger)
    async def energetic(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.send_recommendation(interaction, "enerjik")

    @discord.ui.button(label="Huzurlu 🌙", style=discord.ButtonStyle.secondary)
    async def peaceful(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.send_recommendation(interaction, "uykulu_huzurlu")

bot = IUBot()

def base_embed(title, description=None):
    embed = discord.Embed(title=title, description=description, color=IU_COLOUR)
    embed.set_footer(text="Jieun's Uaena Helper | Lee Ji-eun")
    return embed

@bot.tree.command(name="iu", description="Jieun's Uaena Helper ana menüsü")
async def iu(interaction: discord.Interaction):
    embed = base_embed("Jieun's Uaena Helper'a Hoş Geldin!")
    
    embed.add_field(
        name="📖 Bilgi Komutları", 
        value="`/bio` - IU'nun biyografisi\n`/disk` - Sayfalı diskografi\n`/sarki` - Şarkılar hakkında detaylı bilgi\n`/fact` - Rastgele IU bilgisi", 
        inline=False
    )
    
    embed.add_field(
        name="✨ Eğlence & Etkileşim", 
        value="`/karakter` - Hangi IU dizi karakterisin?\n`/oneri` - Moduna göre IU şarkısı önerisi", 
        inline=False
    )
    
    embed.set_footer(text="Uaena dünyasına hoş geldin! ✨")
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="bio", description="IU biyografisi")
async def bio(interaction: discord.Interaction):
    embed = base_embed("IU — Biyografi", BIO)
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="disk", description="IU diskografisini sayfalarla incele")
@app_commands.describe(tip="Hangi listeyi görmek istersin?")
@app_commands.choices(tip=[
    app_commands.Choice(name="Albümler", value="albuemler"),
    app_commands.Choice(name="Single'lar", value="singlelar")
])
async def disk(interaction: discord.Interaction, tip: str):
    data_list = DISCOGRAPHY.get(tip, [])
    
    if not data_list:
        await interaction.response.send_message("Liste boş veya bulunamadı.")
        return

    title = "IU — Albümler" if tip == "albuemler" else "IU — Single'lar"
    view = DiscographyView(data_list, title)
    await interaction.response.send_message(embed=view.create_embed(), view=view)

@bot.tree.command(name="sarki", description="Şarkı bilgisi")
@app_commands.describe(isim="Şarkı adı (örn: good day, lilac, eight)")
async def sarki(interaction: discord.Interaction, isim: str):
    key = isim.lower().strip()
    if key in SONGS_INFO:
        embed = base_embed("🎵 Şarkı Bilgisi", SONGS_INFO[key])
    else:
        matches = [k for k in SONGS_INFO if key in k]
        if matches:
            embed = base_embed("🎵 Şarkı Bilgisi", SONGS_INFO[matches[0]])
        else:
            await interaction.response.send_message(f"❌ `{isim}` bulunamadı. Mevcut: {', '.join(SONGS_INFO.keys())}")
            return
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="fact", description="Rastgele IU bilgisi")
async def fact(interaction: discord.Interaction):
    embed = base_embed("IU Hakkında Rastgele Bir Bilgi", random.choice(FACTS))
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="karakter", description="Hangi IU karakterisin?")
async def karakter(interaction: discord.Interaction):
    char, desc = random.choice(list(CHARACTERS.items()))
    embed = base_embed("Hangi IU Karakterisin?", f"Sen: **{char}**\n\n{desc}")
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="oneri", description="Şu anki moduna göre bir IU şarkısı önerisi al.")
async def oneri(interaction: discord.Interaction):
    embed = discord.Embed(
        title="🎭 Modun Nasıl?", 
        description="Şu an nasıl hissediyorsun? Aşağıdaki butonlardan birine bas, sana özel bir şarkı seçeyim!",
        color=IU_COLOUR
    )
    view = MoodView() 
    
    await interaction.response.send_message(embed=embed, view=view)

@bot.tree.command(name="hakkinda", description="Bot ve geliştirici hakkında bilgi al.")
async def hakkinda(interaction: discord.Interaction):
    embed = discord.Embed(
        title=f"✨ {ABOUT_DATA['bot_name']}",
        description=ABOUT_DATA['description'],
        color=IU_COLOUR
    )
    
    embed.add_field(name="Sürüm", value=ABOUT_DATA['version'], inline=True)
    embed.add_field(name="Geliştirici", value=ABOUT_DATA['developer'], inline=True)
    
    features_text = "\n".join(f"• {f}" for f in ABOUT_DATA['features'])
    embed.add_field(name="Özellikler", value=features_text, inline=False)
    
    embed.add_field(name="Not", value=ABOUT_DATA['credits'], inline=False)
    
    embed.set_footer(text="Uaena topluluğu için sevgiyle yapıldı✨")
    
    await interaction.response.send_message(embed=embed)

@bot.event
async def on_ready():
    print(f"✅ Bot aktif: {bot.user}")
    await bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.listening,
        name="IU dinliyor"
    ))

if __name__ == "__main__":
    TOKEN = os.getenv("DISCORD_TOKEN")
    if not TOKEN:
        print("❌ DISCORD_TOKEN bulunamadı. Lütfen .env dosyasına ekleyin.")
    else:
        bot.run(TOKEN)
