from selenium import webdriver
from selenium.webdriver.edge.options import Options
from time import sleep


with open('path.txt', 'r') as arquivo:
    path = arquivo.read()

url = 'https://globoesporte.globo.com/futebol/futebol-internacional/futebol-ingles/'
driver = webdriver.Edge(executable_path=path)
driver.get(url)

sleep(3)

lista = []

for i in range(1, 21):
    team = driver.find_element_by_xpath(
        f'//*[@id="classificacao__wrapper"]/article/section[1]/div/table[1]/tbody/tr['+str(i)+']/td[2]/strong').text

    points = driver.find_element_by_xpath(
        '//*[@id="classificacao__wrapper"]/article/section[1]/div/table[2]/tbody/tr['+str(i)+']/td[1]').text

    games = driver.find_element_by_xpath(
        '//*[@id="classificacao__wrapper"]/article/section[1]/div/table[2]/tbody/tr['+str(i)+']/td[2]').text

    victories = driver.find_element_by_xpath(
        '//*[@id="classificacao__wrapper"]/article/section[1]/div/table[2]/tbody/tr['+str(i)+']/td[3]').text

    empates = driver.find_element_by_xpath(
        '//*[@id="classificacao__wrapper"]/article/section[1]/div/table[2]/tbody/tr['+str(i)+']/td[4]').text

    defeat = driver.find_element_by_xpath(
        '//*[@id="classificacao__wrapper"]/article/section[1]/div/table[2]/tbody/tr['+str(i)+']/td[5]').text

    goals_scored = driver.find_element_by_xpath(
        '//*[@id="classificacao__wrapper"]/article/section[1]/div/table[2]/tbody/tr['+str(i)+']/td[6]').text

    conceded_goals = driver.find_element_by_xpath(
        '//*[@id="classificacao__wrapper"]/article/section[1]/div/table[2]/tbody/tr['+str(i)+']/td[7]').text

    goal_difference = driver.find_element_by_xpath(
        '//*[@id="classificacao__wrapper"]/article/section[1]/div/table[2]/tbody/tr['+str(i)+']/td[8]').text

    percentage_wins = driver.find_element_by_xpath(
        '//*[@id="classificacao__wrapper"]/article/section[1]/div/table[2]/tbody/tr['+str(i)+']/td[9]').text

    data = {
        'team': team,
        'points': points,
        'games': games,
        'victories': victories,
        'empates': empates,
        'defeat': defeat,
        'goals_scored': goals_scored,
        'conceded_goals': conceded_goals,
        'goal_difference': goal_difference,
        'percentage_wins': percentage_wins
    }
    lista.append(data)

with open('PremierLeague/data_premier.json', 'w') as archive_json:
    archive_json.write(str(lista).replace('\'', '\"'))
