import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from typing import Dict, List, Union
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
import re

navegador = webdriver.Chrome(ChromeDriverManager().install())
navegador.maximize_window()

navegador.get("https://www.tripadvisor.com.br")
time.sleep(2)
navegador.find_element(By.XPATH,'//*[@id="lithium-root"]/main/div[3]/div/div/div/form/input[1]').click()
time.sleep(2)
navegador.find_element(By.XPATH,'//*[@id="lithium-root"]/main/div[3]/div/div/div/form/input[1]').send_keys("Congresso Nacional - Brasília")
time.sleep(2)
navegador.find_element(By.XPATH,'//*[@id="typeahead_results"]/a[1]').click()
time.sleep(2)
avaliacao= navegador.find_element(By.XPATH, '//*[@id="tab-data-qa-reviews-0"]/div/div[3]/span/div/div[1]/div[1]')
novo_num_avaliacao = navegador.find_element(By.XPATH, '//*[@id="tab-data-qa-reviews-0"]/div/div[3]/span/div/div[1]/div[2]/span')

num_avaliacao = novo_num_avaliacao.text.split(' ')

print('## Resultado da coleta de dados ##')
print(f'Avaliação do local: {avaliacao.text} de {num_avaliacao[0]} avaliações.')

