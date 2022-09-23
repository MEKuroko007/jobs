from msilib.schema import Directory
from ssl import Options
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome, ChromeOptions
import os
import hashlib
from pathlib import Path
#//////////////////////////////////////////////////
#This is  a job search script on the "emploi public"
################ ESSALHI {kUROKO007} ##############
#//////////////////////////////////////////////////
directory=f"C:\\Users\\{os.getlogin()}\\Desktop\\Jobs"
if not os.path.exists(directory):
    os.makedirs(directory)
######################################################
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
  "download.default_directory": directory,
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
    if "Echelle 11" in e.text : # if you want to search for another level,only change number 11 EX:'TS:9,lp:10.....'
      links.append(e.get_attribute("href")) 
for link in links:
    driver.get(link)
    driver.find_element(By.XPATH,"//a[@class='btn btn-block btn-social btn-down']").click()

##############################################################
#################Remove duplicate Files#######################
##############################################################
file_path =f"C:\\Users\\{os.getlogin()}\\Desktop\\jobs"
list_files = os.walk(file_path)
unique_files = dict()
for root, folders, files in list_files:
    for file in files:
        file_path = Path(os.path.join(root, file))
        Hash_file = hashlib.md5(open(file_path, 'rb').read()).hexdigest()
        if Hash_file not in unique_files:
            unique_files[Hash_file] = file_path
        else:
            os.remove(file_path)
sleep(100)
driver.quit()
