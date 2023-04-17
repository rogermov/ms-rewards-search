from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random

# lista de consultas de pesquisa
search_queries = ['arroz', 'feijao', 'macarrao', 'batata', 'cenoura', 'tomate', 'cebola', 'alho', 'azeite', 'sal', 'pimenta', 'limao', 'laranja', 'abacaxi', 'morango', 'melancia', 'uva', 'kiwi', 'lima', 'abacate', 'banana', 'laranja', 'manga', 'pimentao', 'beterraba', 'berinjela', 'couve', 'alface', 'espinafre', 'salsinha']

# cria uma instância do navegador Edge
edge = webdriver.Edge()

# abre a página do Bing
edge.get('https://www.bing.com/')

# realiza a pesquisa 30 vezes com consultas aleatórias
for i in range(30):
    # escolhe uma consulta aleatória da lista
    search_query = random.choice(search_queries)

    # encontra o campo de pesquisa e insere a consulta
    search_box = edge.find_element('name', 'q')
    search_box.send_keys(search_query)

    # envia o formulário de pesquisa
    search_box.send_keys(Keys.RETURN)

    # espera a página carregar
    edge.implicitly_wait(10)

    # volta para a página inicial do Bing
    edge.get('https://www.bing.com/')

# fecha o navegador
edge.quit()
