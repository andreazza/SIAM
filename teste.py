# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 15:27:45 2019

@author: carlo
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json

from siam import *

#options = Options()
chrome_options = webdriver.ChromeOptions()

options = Options()
options.add_experimental_option("prefs", {
  "download.default_directory": r'C:\Users\carlo\downloads\Selenium',
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True,
  "plugins.plugins_disabled": ["Chrome PDF Viewer"],
  "plugins.always_open_pdf_externally": True
})

browser = webdriver.Chrome(executable_path=r'C:\temp\chrome-driver\chromedriver.exe',
                          chrome_options=options)

lista_dados = [{'ii':'1820820', 'dv':'7'},
               {'ii':'1820821', 'dv':'5'},
               {'ii':'1820822', 'dv':'3'},
               {'ii':'1820823', 'dv':'1'},
               {'ii':'1820824', 'dv':'9'}]

browser.get('https://novoportal.smf.rio.rj.gov.br')
#driver.get('https://www.google.com.br')

print('tecle ENTER')
input()
browser.switch_to.window(browser.window_handles[1])

usuario = '2649317'
senha = 'pwd200'

login = Login_SIAM(browser)

login.preenche_usuario_senha(usuario, senha)
login.entrar()

fcis1 = FCIS1_Seq(browser, lista_dados, 2, 2015, 2020)

fcis1.realizar_operacao()