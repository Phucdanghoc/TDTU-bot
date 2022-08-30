
import time
from webbrowser import get
from selenium import webdriver



def Id(driver):
   id = 7;
   while id == 7:
      print("Reading Noti ID:",id,'\n')
      driver.get('https://studentnews.tdtu.edu.vn/ChuDe/ThongBaoChuDe?TheLoaiID={}'.format(id))
      chose_page(driver,id)
      id = id +1
   
def read(driver,count):
            while (True):
               try:
                  driver.execute_script('document.querySelector("#div_lstThongBao > div.list.box.text-shadow > div:nth-child({}) > div > a").click()'.format(count))
                  time.sleep(1)
                  driver.switch_to.window(driver.window_handles[1])
                  driver.close()
                  driver.switch_to.window(driver.window_handles[0])
                  count = count + 1
                  print("Done noti ",count,'\n')
               except: 
                  print("Err")
                  break
               else:
                  continue
               
def chose_page(driver,id):
      page=1
      while(True):
         print(page,"\nPage is being Read")
         time.sleep(1)
         count = 1
         read(driver,count)
         print("Read Done !",page)
         page = page + 1
         try:
            driver.execute_script('document.querySelector("#div_lstThongBao > div:nth-child(3) > div.jplist-pagination > div.jplist-pagingprev > button.jplist-next").click()')
         except:
            print("Read Done notification ID: ",id,'\n')
            break
         else:
            continue
      
def login(user,pas):
      driver = webdriver.ChromeOptions()
      driver.add_argument('--no-sandbox')
      driver.add_argument('--disable-dev-shm-usage')
      prefs = {
         "profile.managed_default_content_settings.images": 2
      }
      driver.add_experimental_option("prefs", prefs)
      driver = webdriver.Chrome(options=driver)
      driver.get("https://studentnews.tdtu.edu.vn")
      time.sleep(2)
      driver.execute_script('document.querySelector("#txtUser").value="{}"'.format(user))
      driver.execute_script('document.querySelector("#txtPass").value="{}"'.format(pas))
      time.sleep(1)
      driver.execute_script('document.querySelector("#btnLogIn").click()')
      time.sleep(2)
      driver.get('https://studentnews.tdtu.edu.vn')
      Id(driver)
      
login("ID","Pass")

