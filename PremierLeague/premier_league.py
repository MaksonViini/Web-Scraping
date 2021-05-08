from selenium import webdriver
import os


with open('path.txt', 'r') as arquivo:
    path = arquivo.read()


driver = webdriver.Edge(executable_path=path)
driver.get('https://covid.saude.gov.br/')

