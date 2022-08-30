#binary
import discord as dis
from discord.ext import commands
from selenium import webdriver
import requests
import time
from googletrans import Translator
import random
from keep_alive import keep_alive
client = commands.Bot(command_prefix='`')

def check_id(id):
    if(id[3] != 1):
        return 0

@client.event
async def on_ready():
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))
       
@client.command('say')
async def say(ctx):
   await ctx.send("hi")
  
#gg dich
@client.command()
async def ggdich(ctx,word:str):
  trans = Translator()
  t = trans.translate(word,src="en",dest="vi")
  await ctx.send(t.text)
#meme
@client.command("meme")
async def imgmeo(ctx):
    data = requests.get('https://api.imgflip.com/get_memes').json()['data']['memes']
    images = [{'name':image['name'],'url':image['url'],'id':image['id']} for image in data]
    #List all the memes
    print('Here is the list of available memes : \n')
    imgurl = random.choice(images)
    await ctx.send(imgurl['url'])
  
#meo
@client.command("meo")
async def imgg(ctx):
    res = requests.get('https://api.thecatapi.com/v1/images/search?breed_ids=beng&include_breeds=true').json()
    img = [{'url':image['url']} for image in res]
    await ctx.send(img[0]['url'])
#dog 
@client.command("dog")
async def dog(ctx):
    res = requests.get('https://dog.ceo/api/breeds/image/random').json()
  
    await ctx.send(res['message'])
#thoi khoa bieu
@client.command()
async def tkb(ctx,user:str,pas:str):
  def login(user,pas):
      driver = webdriver.ChromeOptions()
      driver.add_argument('--no-sandbox')
      driver.add_argument('--disable-dev-shm-usage')
      prefs = {
         "profile.managed_default_content_settings.images": 2
      }
      driver.add_experimental_option("prefs", prefs)
      driver = webdriver.Chrome(options=driver)
      driver.get("https://lichhoc-lichthi.tdtu.edu.vn")
      time.sleep(2)
      driver.execute_script('document.querySelector("#txtUser").value="{}"'.format(user))
      driver.execute_script('document.querySelector("#txtPass").value="{}"'.format(pas))
      time.sleep(1)
      driver.execute_script('document.querySelector("#btnLogIn").click()')
      time.sleep(2)
      driver.get('https://lichhoc-lichthi.tdtu.edu.vn')
      time.sleep(2)
      driver.execute_script("document.querySelector('#ThoiKhoaBieu1_cboHocKy').value='116'")
      time.sleep(1)
      driver.execute_script('document.querySelector("#ThoiKhoaBieu1_btnTuanHienTai").click()')
      time.sleep(2)
      driver.execute_script('document.querySelector("#ThoiKhoaBieu1_pnTKBTheoTuan > div:nth-child(5)")')
      time.sleep(2)
      data = driver.find_element_by_id('ThoiKhoaBieu1_pnTKBTheoTuan')
      tkb_html = (data.get_attribute('innerHTML'))
      url = "https://htmlcsstoimage.com/demo_run"
      s = requests.Session()
      html = {
         "html": tkb_html
      }
      res = s.post(url,data=html)
      return res.json()['url']
  await ctx.send((login(user,pas)))

#titok
@client.command()
async def top(ctx,url_input:str):
  driver = webdriver.ChromeOptions()
  prefs = {
      "profile.managed_default_content_settings.images": 2
  }
  driver.add_experimental_option("prefs", prefs)
  driver = webdriver.Chrome('./Chromedriver', options=driver)
  driver.get(url_input)
  elem = driver.find_element_by_tag_name('video').get_attribute('src')
  data = requests.get(elem)
  f = open("a.mp4","wb")
  f.write(data.content)
  f.close
  area = ctx.message.channel
  try:  
      await area.send(file = dis.File("./a.mp4"))
  except:
      await ctx.send("Nộp VIP để up file trên 8Mb")
keep_alive()
client.run("OTg4MTMwNDcyNzkyMDUxODM0.Go7KdD.zpHnK17YIyGnGnDMltolvRQsRaTk-AC8kWaH9k")


# thoi khoa bieu


