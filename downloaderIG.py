from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
import os, glob


opt = webdriver.ChromeOptions()
opt.binary_location = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
chromedriver_exe_location = os.path.join(os.getcwd(), 'F:\Lavoro\Python\seleniumDriver\chromedriver.exe')
profile_path = r'C:\Users\liamm\AppData\Local\Google\Chrome\User Data'  # path minus last folder
opt.add_argument('--user-data-dir={}'.format(profile_path))
opt.add_argument('--profile-directory={}'.format('Profile 3'))  # last folder name
driver = webdriver.Chrome(chromedriver_exe_location, options=opt, service_args='')



for i in range (1,2):
     for n in range (1,5):
       driver.get('https://www.instagram.com/pampam.mp4/reels/')

       time.sleep(7)



       driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/div[3]/div/div/div/div[" + str(i) + "]/div[" + str(n) + "]/div/a").click()

       time.sleep(4)

       url = driver.current_url
       driver.get('https://snapinsta.app/instagram-photo-download')
       time.sleep(4)
       driver.find_element(By.ID,"url").send_keys(url)
       time.sleep(2)
       driver.find_element(By.ID,"send").click()
       time.sleep(15)
       driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/section/div/div/div/div[2]/a").click()




driver.close()