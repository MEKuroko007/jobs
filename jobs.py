from ssl import Options
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome, ChromeOptions
import os.path

#//////////////////////////////////////////////////
#this script is for serach job in 'emploi public'
#author ESSALHI MUSTAPHA {kUROKO007}
#//////////////////////////////////////////////////

#########################################33
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
  "download.default_directory": "D:\\Backup",
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True,
  "plugins.always_open_pdf_externally": True
})
####################################################
driver = webdriver.Chrome(options=options)
#####################################################33
links=[]
driver.get("https://www.emploi-public.ma/FR/index.asp?p=1")
el=driver.find_elements(By.CSS_SELECTOR,"td a")
for e in el:
    #if "Technicien" in e.text and "9" in e.text:
    if "Echelle 9"in e.text :
        links.append(e.get_attribute("href"))   
for link in links:
    driver.get(link)
    driver.find_element(By.XPATH,"//a[@class='btn btn-block btn-social btn-down']").click()
sleep(50)
driver.quit()