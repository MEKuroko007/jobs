import hashlib
import os
from pathlib import Path
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


directory = f"C:\\Users\\{os.getlogin()}\\Desktop\\Jobs"      
if not os.path.exists(directory):
    os.makedirs(directory)


options = webdriver.ChromeOptions()
options.headless = True
options.add_experimental_option("prefs", {
    "download.default_directory": directory,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True,
    "plugins.always_open_pdf_externally": True
})


driver = webdriver.Chrome(options=options)
links = []
driver.get("https://www.emploi-public.ma/FR/index.asp?p=1")
el = driver.find_elements(By.CSS_SELECTOR, "td a")
echelle_levels = ['Echelle 8','Echelle 9', 'Echelle 10', 'Echelle 11']
for e in el:
    for level in echelle_levels:
        if level in e.text:
            links.append(e.get_attribute("href")) 


for link in links:
    driver.get(link)
    try:
        download_button = driver.find_element(By.XPATH, "//a[@class='btn btn-block btn-social btn-down']")
        download_button.click()
        sleep(5) # Wait for file to download
    except:
        print("Could not download file from:", link)


file_path = f"C:\\Users\\{os.getlogin()}\\Desktop\\jobs"
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


sleep(10)
driver.quit()
