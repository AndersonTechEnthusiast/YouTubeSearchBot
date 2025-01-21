from selenium import webdriver # Importa a biblioteca Selenium para automação do navegador
from selenium.webdriver.chrome.service import Service # Importa o serviço para iniciar o ChromeDriver
from selenium.webdriver.support.wait import WebDriverWait # Importa a funcionalidade de espera explícita
from selenium.webdriver.support import expected_conditions as EC # Importa as condições esperadas para verificar elementos no DOM
from selenium.webdriver.common.by import By # Importa opções de localização de elementos no DOM, como por ID, NAME, etc.
from selenium.webdriver.common.keys import Keys # Importa comandos de teclado, como ENTER, TAB, etc.
from selenium.webdriver.chrome.options import Options # Importa opções de configuração para o navegador Chrome
# Configuração de opções para o navegador Chrome
chrome_options = Options() # Cria uma instância de opções para o navegador Chrome, permitindo configurar parâmetros antes de iniciar o navegador
chrome_options.add_argument("--disable-gpu") # Desativa a aceleração gráfica por GPU, geralmente para resolver problemas de compatibilidade

import pyautogui # Biblioteca para automação de mouse e teclado
import time # Biblioteca para funções relacionadas ao tempo, como pausas e atrasos
import pygetwindow as variavel_janelas #cria sua variavel # Biblioteca para gerenciar janelas abertas do sistema

pedido = input("Iniciar Projeto ? (sim/não) \n ->")
if pedido.lower() == 'sim':
    query = input("digite o que quer Acessar no Youtube ? \n (ex: Como Aprender Python...) \n -> ")
    if query:

        caminho = "./chromedriver-win64/chromedriver-win64/chromedriver.exe" # pega o caminho do WebDriverChrome 

        servico = Service(caminho) # Adiciona o caminho para ser tratado pelo Service (serviço)

        drive = webdriver.Chrome(service=servico , options=chrome_options) # coloca o servico para ser rodado no chrome (webdriver.chrome = navegador chrome execute o servico do caminho)

        try: # tente

            time.sleep(1) # durma por 1 segundo

            pyautogui.click(x=1024 , y=126) # clica no (x) da notificação

            drive.get("https://youtube.com/") # o endereco do site

            drive.implicitly_wait(5) # espere 5 segundos 

            pesquisa = WebDriverWait(drive, 10).until( # pesquisa (variavel) , WebDriverWait(drive , 10) (Navegador Espere (Nevegador , 10 segundos)) -> isso serve para o sistema esperar o navegador carregar todos seus elementos , until -> até , ou seja lendo ficaria: WebDriverWait(drive,10).until -> significa: Espere O Navegador(Navegador , 10 segundos) até 
                EC.element_to_be_clickable((By.NAME , "search_query")) # EC é um atalho criado para expected_condicions (condições esperadas) , que condições ? elemento_to_to_clickable (elemento estar clicavel) , que elemento estar clicavel ? o elemento que tenha o name desejado , tipo , (By.NAME , "nome-do-elemento")
            )
            # esta clicavel ? , então passa as chaves para a pesquisa
            pesquisa.send_keys(query)
            # depois , a chave de ENTER
            pesquisa.send_keys(Keys.ENTER)

            video = WebDriverWait(drive , 10).until( # mesmo caso do de cima
                EC.presence_of_all_elements_located((By.XPATH , '//*[@id = "video-title"]')) # presence_of_all_elements_located (presenca de todos os elementos locados) , aqui estou puxando varios elementos (Array) pela o id deles , que seria By.XPATH , ou seja puxe todos que tenham esse caminho (XPATH) , "id-do-elemento-desejado" , "//*[@id = 'video-title']"
            )
            time.sleep(5)
            # janelas (variavel)
            # variavel_janelas (variavel criada no escopo)
            # .getWindowsWithTitle() (pegue Windows Com Titulo) - no caso "Chrome"
            # fica: pegue todos os Windows com o Titulo do Chrome (Array de Janelas)
            janelas = variavel_janelas.getWindowsWithTitle("Chrome") # pega todas em forma de Array getWindowsWithTitle (pegue Windows com Titulo)
            list = [] # cria uma Array
            for janela in janelas: # percorre todas as janelas 
                list.append(janela.title) # adiciona apenas os titulos na Array

            escolhida = janelas[0] # escolhida (variavel) , aloca a primeira janela
            
            time.sleep(5) 
            
            escolhida.minimize() # minimiza a janela

            # verifica se o video existe
            if video:
                print("Qual dos videos Deseja ?")

                print(f"Vídeos Encontrados: {len(video)} Vídeos Correspondem a sua Pesquisa !!!")

                for num in range(0 , len(video)): # percorre o a lenght (comprimento) da quantidade de videos com o mesmo id
                    print(f"clique: {num} para acessar o {num}° vídeo !") # mostra para o usuário a lista e os comandos
                
                quero_esse_video = input('Qual deseja assistir ?') # recebe o comando do usuario

                quero_esse_video = int(quero_esse_video) # transforma a variavel em um número inteiro

                while quero_esse_video > len(video): # verifica se o comando é maior que a quantidade
                    print("Vídeo Não Encontrado !!!") # se for , o video não existe
                    quero_esse_video = int(input('Qual deseja assistir ?')) # solicita novamente uma nova resposta do usuário

                while quero_esse_video < 0: # verifica se o comando é menor que zero , não existe (video com índice de -1)
                    print(f"por favor digite um número entre 0 e {len(video) - 1}") # então retorna para que ele mostre a mensagem de aviso
                    quero_esse_video = int(input('Qual deseja assistir ?')) # solicita novamente uma nova resposta do usuário
                
                escolhida.restore() # maximiza a pagina novamente

                video[quero_esse_video].click() # o comando dado ao usuario é adicionado para clicar no video selecionado pelo comando

                time.sleep(1)

                pyautogui.press("f") # pressiona "f" , para colocar o video em Tela Cheia
            else:
                print("Nenhum Vídeo foi Encontrado")
            input("pressione enter para fechar a Janela !!")
        except ValueError:
            print("Error , Teste Interrompido !!!")
        finally:
            drive.quit()
    else:
        print("digite algo por favor")
elif pedido.lower() in ['não' , 'nao']:
    print("Então , Tchau !!!")
else:
    print("Digie sua Resposta")