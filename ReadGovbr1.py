import certifi
import urllib3
from bs4 import BeautifulSoup

http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())

print('starting....')
r = http.urlopen('GET', 'https://www.gov.br/cvm/pt-br/assuntos/protecao/alertas/deliberacoes-cvm-alertas-de-suspensao')
# print(r.data)
html = r.data
soup = BeautifulSoup(html, 'html.parser')
table = soup.find('table', class_='listing')
dados = []
linhas = table.find_all('tr')
for linha in linhas:
    celulas = linha.find_all('td')
    if celulas:
        suspensao = celulas[0].text.strip()
        atuacao = celulas[1].text.strip()
        deliberacao = celulas[2].text.strip()
        data = celulas[3].text.strip()
        dados.append([suspensao, atuacao, deliberacao, data])
for dado in dados:
    print('Suspensão:', dado[0])
    print('Atuação Irregular:', dado[1])
    print('Deliberação CVM:', dado[2])
    print('Data:', dado[3])
    print()
    
    
