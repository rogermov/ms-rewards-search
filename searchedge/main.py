from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time

# Inicializar o driver do Microsoft Edge
edge_options = webdriver.EdgeOptions()
edge_options.use_chromium = True
edge_options.add_argument("start-maximized")
driver = webdriver.Edge(options=edge_options)

# Navegar até a página de login do Microsoft
driver.get("https://login.live.com/")

# Preencher o campo de email
email_field = driver.find_element("loginfmt")
email_field.send_keys("roger.bthe@gmail.com")
email_field.send_keys(Keys.RETURN)

time.sleep(2) # Aguardar um tempo para carregar a próxima página

# Preencher o campo de senha
password_field = driver.find_element("passwd")
password_field.send_keys("T9c7x2j9.")
password_field.send_keys(Keys.RETURN)

time.sleep(5) # Aguardar um tempo para carregar a página após o login

# Navegar até o Bing
driver.get("https://www.bing.com/")

# Adicionar cookie de login
cookie = {'name': 'MSPAuth', 'value': driver.get_cookie('MSPAuth')['value'], 'domain': '.bing.com'}
driver.add_cookie(cookie)

# Lista de consultas de pesquisa
search_queries = ['arroz', 'feijao', 'macarrao', 'batata', 'cenoura', 'tomate', 'cebola', 'alho', 'azeite', 'sal', 'pimenta', 'limao', 'laranja', 'abacaxi', 'morango', 'melancia', 'uva', 'kiwi', 'lima', 'abacate', 'banana', 'laranja', 'manga', 'pimentao', 'beterraba', 'berinjela', 'couve', 'alface', 'espinafre', 'salsinha']

# Realiza a pesquisa 30 vezes com consultas aleatórias
for i in range(30):
    # Escolhe uma consulta aleatória da lista
    search_query = random.choice(search_queries)

    # Encontra o campo de pesquisa e insere a consulta
    search_box = driver.find_element('name', 'q')
    search_box.send_keys(search_query)

    # Envia o formulário de pesquisa
    search_box.send_keys(Keys.RETURN)

    # Espera a página carregar
    driver.implicitly_wait(10)

    # Volta para a página inicial do Bing
    driver.get('https://www.bing.com/')

# Fecha o navegador
driver.quit()
