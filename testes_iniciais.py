# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import re


options = Options()
options.add_experimental_option("prefs", {
  "download.default_directory": r'C:\Users\carlo\downloads\Selenium',
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True,
  "plugins.plugins_disabled": ["Chrome PDF Viewer"],
  "plugins.always_open_pdf_externally": True
})

driver = webdriver.Chrome(executable_path=r'C:\temp\chrome-driver\chromedriver.exe',
                          options=options)

driver.get('https://novoportal.smf.rio.rj.gov.br')
print("Page Title is : %s" %driver.title)
input()
driver.switch_to.window(driver.window_handles[1])

ii1 = driver.find_element_by_id("ctl00_ePortalContent_listainscricao_UCLISTA_INTINSC1")
dv1 = driver.find_element_by_id("ctl00_ePortalContent_listainscricao_UCLISTA_INTDIG1")

ii2 = driver.find_element_by_id("ctl00_ePortalContent_listainscricao_UCLISTA_INTINSC2")
dv2 = driver.find_element_by_id("ctl00_ePortalContent_listainscricao_UCLISTA_INTDIG2")

ii1.send_keys('3135096')
dv1.send_keys('0')

ii2.send_keys('3135096')
dv2.send_keys('0')

add_intervalo = driver.find_element_by_id("ctl00_ePortalContent_listainscricao_UCLISTA_btaddintervalo")

#add_intervalo.click()

visualizar = driver.find_element_by_id("ctl00_ePortalContent_btVisualizarIntervalo")

visualizar.click()

ok_button = driver.find_element_by_id("popup_ok")

print('antes do ok')
ok_button.click()
print('depois do ok')

span = driver.find_element_by_id("ctl00_ePortalContent_StatusLine")

texto_messagem = span.text

regex = re.compile(f'(\w+)(\s*)\(V I S U A L I Z')
result = regex.search(texto_messagem)
pdf = result.group(1)+'.pdf'

url = 'https://pdfsiam.smf.rio.rj.gov.br/pdfs/DIPFSIAM/'+pdf
print(url)

print('antes do get')
driver.get(url)
print('depois do get  ')

print("Page Title is : %s" %driver.title)