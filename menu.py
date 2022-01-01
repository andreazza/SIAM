# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 10:07:48 2020

@author: carlo
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pandas import DataFrame
from siam import *
import os

def load_lista_dados(arq_nome: str) -> list:
    """    

    Parameters
    ----------
    arq_nome : str
        nome do arquivo

    Returns
    -------
    list[dict]
    
    Carrega o arquivo csv de dados para uma lista.
    O elemento da lista é um dict.
    Exemplo abaixo.
    
    [{'ii':'1820820', 'dv':'7'},
     {'ii':'1820821', 'dv':'5'},
     {'ii':'1820822', 'dv':'3'},
     {'ii':'1820823', 'dv':'1'},
     {'ii':'1820824', 'dv':'9'}]

    """
    
    header: list[str] # cabeçalho. exemple ['ii', 'dv']
    lista_de_dados: list[dict] = []
    
    with open(arq_nome, "r") as file:
        header = file.readline().strip().split('|')
        
        dado: dict # exemple: {'ii':'1820820', 'dv':'7'}
    
        for line in file:
            
            dado = {}
            
            itens = line.strip().split('|')
            
            for key, value in zip(header, itens):
                dado[key] = value
            
            lista_de_dados.append(dado)
    
    return lista_de_dados

def load_configuracoes(arq_nome: str) -> list:
    """    

    Parameters
    ----------
    arq_nome : str
        nome do arquivo

    Returns
    -------
    dict
    
    Carrega o arquivo csv de dados para um dict.
    Exemplo abaixo.
    
    { "processo" : "00-04-375102-2015",
      "ano_inicio": 2015,
      "ano_fim": 2020 }

    """
    
    with open(arq_nome, "r") as file:
        config: dict = {}
            
        for line in file:
            
            itens = line.strip().split('=')
            
            key, value = itens[0], itens[1]
            
            config[key] = value
    
    return config

def fazer_login(browser, usuario: str, senha: str):
    
    browser.switch_to.window(browser.window_handles[1])
    
    login = Login_SIAM(browser)

    login.preenche_usuario_senha(usuario, senha)
    login.entrar()    
    
def gerar_relatorios(browser, ano_inicial: int, ano_final: int,
                     lista_dados: list, tempo_entre_operacoes: int):
    fcis1 = FCIS1_Seq(browser, lista_dados, tempo_entre_operacoes, 
                      ano_inicial, ano_final)

    fcis1.realizar_operacao()

def mostra_menu():
    # guarda as configuracoes
    configs: dict = load_configuracoes('config')
    
    # chrome_options = webdriver.ChromeOptions()
    download_path = configs["download_path"]
    
    options_chrome = Options()
    options_chrome.add_experimental_option("prefs", {
        "download.default_directory": download_path,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": False,
        "plugins.plugins_disabled": ["Chrome PDF Viewer"],
        "plugins.always_open_pdf_externally": True
    })
    
    options_firefox = webdriver.FirefoxOptions()
    options_firefox.set_preference("download.default_directory", 
                                   download_path)
    options_firefox.set_preference("download.prompt_for_download", False)
    options_firefox.set_preference("download.directory_upgrade", True)
    options_firefox.set_preference("safebrowsing.enabled", True)
    options_firefox.set_preference("plugins.always_open_pdf_externally", True)
    options_firefox.set_preference("browser.download.useDownloadDir", True)
    options_firefox.set_preference("browser.helperApps.neverAsk.saveToDisk",
                                   "application/pdf")
    options_firefox.set_preference("pdfjs.disabled", True)
    options_firefox.set_preference("browser.download.dir", download_path)
                                   
    # armazena os dados das operacoes
    lista_dados: list = []
    
    # acesse o chrome com browser
    browser = None
        
    while True:
        print('1-abrir browser')
        print('2-fechar browser')
        print('3-carregar lista de dados')
        print('4-re-carregar configuracoes')
        print('5-fazer login')
        print('6-gerar relatorios pdf')
        print('7-alterar dados na COMPI')
        print('8-criar UA')
        print('9-lançamento sem remissão')
        print('10-reagi')
        print('11-pegar dados na COMPI')
        print('12-martelar')
        print('13-simulacao')
        print('14-cancelar guias')
        print('15-pegar dados das guias')
        print('16-remitir')
        print('17-cancelar ND')
        print('18-copiar tela CNDEB')
        print('19-gerar ND')
        print('20-desinibir guia')
        print('21-pegar depositos')
        print('22-copia da DEPO2')
        print('23-apropriar deposito')
        print('24-finalizar guia')
        print('25-valor venal declarado')
        print('26-imprimir guia')
        print('0-sair')
        print('')
        print('ATENÇÃO!!!')
        print('VERIFIQUE O PROCESSO!!')
        print('VERIFIQUE SE É RIO OU RIOTESTE!!')
        print('ATENÇÃO!!!')
        
        op = input()
        
        if op == '1': # ABRIR NAVEGADOR
            if configs['web_browser'] == 'chrome':
                browser = \
                    webdriver.Chrome(
                        executable_path=configs["chromedriver_path"],
                        options=options_chrome)
            else: # firefox
                browser = \
                    webdriver.Firefox(
                        executable_path=configs["firefoxdriver_path"],
                        options=options_firefox)
            
            #browser.get('https://novoportal.smf.rio.rj.gov.br')
            browser.get(configs["siam_url"])            
        elif op == '2': # FECHAR NAVEGADOR
            browser.quit()
        elif op == '3': # CARREGAR ARQUIVOS DE DADOS
            try:
                lista_dados = load_lista_dados(configs['arq_nome'])
            except:
                print("Arquivo arq_nome de config NÃO ENCONTRADO!!!")
            print(lista_dados)
        elif op == '4': # LOAD CONFIG
            configs = load_configuracoes('config')
           
            print('\nATENÇÃO!!!')
            print('\nArquivo config recarregado!\n')  
            
        elif op == '5': # LOGIN
            fazer_login(browser, configs['usuario'], configs['senha'])
        elif op == '6': # RELATÓRIOS
            inicio, fim = \
                int(configs["ano_inicio"]), int(configs["ano_fim"])
            
            print('\nATENÇÃO!!!\n')
            
            print(f'ano inicio={inicio}, ano fim={fim}')
            
            print('\nConfirma(s/n)?')        
            sn = input()
            
            if sn in ['S', 's']:            
                fcis1 = FCIS1_Seq(browser, lista_dados, int(configs["max_delay"]), 
                          inicio, fim, url_dir=configs["url_dir"])
    
                fcis1.realizar_operacao()
            else:
                print('\nOperação abortada!!\n')  
                
        elif op == '7': # ALTERAR DADOS COMPI          
            processo = configs['processo']        
            apagar_migrado = configs['apagar_comp_migrado']
            benfeitoria = configs['benfeitoria']
            
            print('\nATENÇÃO!!!\n')
            
            print(f'processo={processo}')
            print(f'benfeitoria={benfeitoria}')
            print(f'apagar complemento migrado={apagar_migrado}')
            
            print('\nConfirma(s/n)?')        
            sn = input()
            
            if sn in ['S', 's']:            
                benfeitoria = None if benfeitoria == 'none' else benfeitoria
                
                compi = COMPI_ALT_Seq(browser, lista_dados, 
                                      int(configs["max_delay"]),
                                      processo,
                                      benfeitoria=benfeitoria,
                                      apagar_comp_mig=apagar_migrado=='sim')
                
                compi.realizar_operacao()
            else:
                print('\nOperação abortada!!\n') 
                
        elif op == '8': # CRIAR UA
            processo = configs['processo']
            inicio, fim = \
                int(configs["ano_inicio"]), int(configs["ano_fim"])
            
            print('\nATENÇÃO!!!\n')
            
            print(f'processo={processo}')
            print(f'ano inicio={inicio}, ano fim={fim}')
            
            print('\nConfirma(s/n)?')        
            sn = input()
            
            if sn in ['S', 's']:   
                rev_lan = Rev_Lanc_Seq(browser, lista_dados, 
                                       int(configs["max_delay"]), 
                                       processo, 
                                       ano_inicio=inicio,
                                       ano_fim=fim,
                                       calcula=False)
                
                rev_lan.realizar_operacao()
            else:
                print('\nOperação abortada!!\n') 
        elif op == '9': # LANÇAMENTO SEM REMISSÃO
            processo = configs['processo']
            inicio, fim = \
                int(configs["ano_inicio"]), int(configs["ano_fim"])
            
            print('\nATENÇÃO!!!\n')
            
            print(f'processo={processo}')
            print(f'ano inicio={inicio}, ano fim={fim}')
            
            print('\nConfirma(s/n)?')        
            sn = input()
            
            if sn in ['S', 's']: 
                rev_lan = Rev_Lanc_Seq(browser, lista_dados, int(configs["max_delay"]), 
                                       processo, 
                                       ano_inicio=inicio,
                                       ano_fim=fim,
                                       calcula=True)
                
                rev_lan.realizar_operacao()
            else:
                print('\nOperação abortada!!\n')             
        elif op == '10': # REAGI
            processo = configs['processo']
            exercicio, guia = \
                int(configs["exercicio"]), int(configs["guia"])
            
            print('\nATENÇÃO!!!\n')
            
            print(f'processo={processo}')
            print(f'exercicio={exercicio}, guia={guia}')
            
            print('\nConfirma(s/n)?')        
            sn = input()
            
            if sn in ['S', 's']: 
                reagi_seq = REAGI_Seq(browser, lista_dados, 
                                      max_delay=int(configs["max_delay"]), 
                                      processo=processo, 
                                      exercicio=exercicio,
                                      guia=guia)                   
                
                reagi_seq.realizar_operacao() 
            else:
                print('\nOperação abortada!!\n')          
        elif op == '11': # PEGAR DADOS NA COMPI  
            processo = configs['processo']
                
            # elementos é componente do arquivo config
            # são os elementos a recuperar na COMPI
            lista_elementos = configs["elementos"].split(',')
            
            print('\nATENÇÃO!!!\n')
            
            print(f'processo={processo}')
            print(f'lista elementos={lista_elementos}')
            
            print('\nConfirma(s/n)?')        
            sn = input()
            
            if sn in ['S', 's']:
                compi_seq = Compi_Inspecao(browser, lista_dados, 
                                           lista_elementos,
                                           max_delay=int(configs["max_delay"]))               
                
                dados: DataFrame = compi_seq.realizar_operacao()
                file = f'saida/{configs["csv_saida"]}'
                dados.to_csv(file, index=False)
            else:
                print('\nOperação abortada!!\n')
        elif op == '12': # MARTELAR
            processo = configs['processo']            
            inicio, fim = \
                int(configs["ano_inicio"]), int(configs["ano_fim"])
            
            descontinuo = configs["descontinuo"]
            amortiza = configs["amortiza"]            
            martela_vv = configs["martela_vv"]
            martela_iptu = configs["martela_iptu"]
            martela_tcl = configs["martela_tcl"]
                
            indice = configs["martela_idx"].split(',')
            indice = list(map(int, indice))
            
            print('OPCAO MARTELAR\nATENÇÃO!!!\n')
            print('VERIFIQUE OS PARAMS, PRINCIPALMENTE DESCONTINUO!!!\n')
            print('O PARAM descontinuo=sim POSSUI COMPORTAMENTO!!!\n')
            print('BASTANTE DIFERENTE DO PARAM descontinuo=nao\n')
            
            print(f'processo={processo}')
            print(f'inicio={inicio}, fim={fim}')
            print(f'martela: vv={martela_vv}, iptu={martela_iptu}, tcl={martela_tcl}')
            print(f'amortiza={amortiza}')
            print(f'descontinuo={descontinuo}')
            print(f'indice martela={indice}')
            
            print('\nConfirma(s/n)?')        
            sn = input()
            
            if sn in ['S', 's']: 
                martelar = Martelar_Seq(browser, 
                                        lista_dados, 
                                        max_delay=int(configs["max_delay"]),
                                        processo=processo,
                                        inicio=inicio,
                                        fim=fim,
                                        descontinuo=descontinuo=='sim',
                                        amortiza=amortiza,
                                        martela_vv=martela_vv=='sim',
                                        martela_iptu=martela_iptu=='sim',
                                        martela_tcl=martela_tcl=='sim',
                                        martela_idx=indice)
                
                martelar.realizar_operacao()
            else:
                print('\nOperação abortada!!\n')                 
        elif op == '13': # SIMULAÇÃO
            processo = configs['processo']
            ano_inicio=int(configs["ano_inicio"])
            ano_fim=int(configs["ano_fim"])
                
            # elementos é componente do arquivo config
            # são os elementos a recuperar na COMPI
            lista_elementos = configs["elementos"].split(',')
            
            print('\nATENÇÃO!!!\n')
            
            print(f'processo={processo}')
            print(f'ano inicio={ano_inicio}')
            print(f'ano fim={ano_fim}')
            
            print('\nConfirma(s/n)?')        
            sn = input()
            
            if sn in ['S', 's']:
                simulador = Simulacao(browser, 
                                      lista_dados, 
                                      max_delay=int(configs["max_delay"]),
                                      processo=processo,
                                      inicio=ano_inicio,
                                      fim=ano_fim)                   
                
                dados = simulador.realizar_operacao()
                df_dados = DataFrame(data=dados)
                df_dados.to_csv(configs["csv_saida"], index=False)
            else:
                print('\nOperação abortada!!\n') 
        elif op == '14': # CANCELAR LANÇAMENTOS
            processo = configs['processo']
            ex1, ex2 = \
                int(configs["ano_inicio"]), int(configs["ano_fim"])
            guia1, guia2 = \
                int(configs["guia"]), int(configs["guia2"])
            
            print('\nATENÇÃO!!!\n')
            
            print(f'processo={processo}')
            print(f'exercicio 1={ex1}, exercicio 2={ex2}')
            print(f'guia 1={guia1}, guia 2={guia2}')
            
            print('\nConfirma(s/n)?')        
            sn = input()
            
            if sn in ['S', 's']: 
                canc_seq = Canc_Seq(browser, lista_dados, 
                                    max_delay=int(configs["max_delay"]), 
                                    processo=processo, 
                                    ano_inicio=ex1,
                                    ano_fim=ex2,
                                    guia1=guia1,
                                    guia2=guia2)                   
                
                canc_seq.realizar_operacao() 
            else:
                print('\nOperação abortada!!\n')
        elif op == '15': # PEGAR DADOS da CVQUI
            print('\nATENÇÃO!!!\n')
            
            print(f'exercicio={configs["exercicio"]}')
            print('\nImportante!!!\n')
            print('Preencha *exercicio* e *csv_saida* com o mesmo ano!')
                        
            print('\nConfirma(s/n)?')    
            
            sn = input()
            
            if sn in ['S', 's']: 
                cvqui_seq = CVQUI_Seq(browser, 
                                  lista_dados, 
                                  max_delay=int(configs["max_delay"]),
                                  exercicio=int(configs["exercicio"]))
            
                dados: DataFrame = cvqui_seq.realizar_operacao()
                dados.to_csv(configs["csv_saida"], index=False)
            else:
                print('\nOperação abortada!!\n')
        elif op == '16': # REMITIR
            print('\nATENÇÃO!!!\n')
            
            print(f'processo={configs["processo"]}')
            print(f'exercicio={configs["exercicio"]}')
            print(f'guia={configs["guia"]}')
            print(f'num_exs={configs["num_exs"]}')
                        
            print('\nConfirma(s/n)?')    
            
            sn = input()
            
            if sn in ['S', 's']: 
                remit_seq = REMIT_Seq(browser, 
                                  lista_dados, 
                                  max_delay=int(configs["max_delay"]),
                                  processo=configs["processo"],
                                  exercicio=int(configs["exercicio"]),
                                  guia=int(configs["guia"]),
                                  num_exs=int(configs["num_exs"]))
            
                remit_seq.realizar_operacao()
            else:
                print('\nOperação abortada!!\n')        
        elif op == '17': # CANCELAR ND
            processo = configs['processo']
            ex1, ex2 = \
                int(configs["ano_inicio"]), int(configs["ano_fim"])
            guia = int(configs["guia"])
            
            print('\nATENÇÃO!!!\n')
            
            print(f'processo={processo}')
            print(f'exercicio 1={ex1}, exercicio 2={ex2}')
            print(f'guia={guia}')
            
            print('\nConfirma(s/n)?')        
            sn = input()
            
            if sn in ['S', 's']: 
                grdva_seq = GRDVA_Seq(browser, lista_dados, 
                                    max_delay=int(configs["max_delay"]), 
                                    processo=processo, 
                                    ano_inicio=ex1,
                                    ano_fim=ex2,
                                    guia=guia,
                                    operacao='cancelar')                   
                
                grdva_seq.realizar_operacao() 
            else:
                print('\nOperação abortada!!\n') 
        elif op == '18': # copiar tela CNDEB
            print('\nATENÇÃO!!!\n')
            
            ex1, ex2 = \
                int(configs["ano_inicio"]), int(configs["ano_fim"])
            num_vias = int(configs["num_vias"])
            guia = int(configs["guia"])
            
            print(f'inicio={ex1}')
            print(f'fim={ex2}')
            print(f'guia={guia}')
            print(f'vias={num_vias}')
                        
            print('\nConfirma(s/n)?')    
            
            sn = input()
            
            if sn in ['S', 's']: 
                cndeb_seq = CNDEB_Seq(browser, 
                                  lista_dados, 
                                  max_delay=int(configs["max_delay"]),
                                  ano_inicio=ex1,
                                  ano_fim=ex2,
                                  num_vias=num_vias,
                                  guia=guia)
            
                cndeb_seq.realizar_operacao()
            else:
                print('\nOperação abortada!!\n')
        elif op == '19': # CANCELAR ND
            processo = configs['processo']
            ex1, ex2 = \
                int(configs["ano_inicio"]), int(configs["ano_fim"])
            guia = int(configs["guia"])
            
            print('\nATENÇÃO!!!\n')
            
            print(f'processo={processo}')
            print(f'exercicio 1={ex1}, exercicio 2={ex2}')
            print(f'guia={guia}')
            
            print('\nConfirma(s/n)?')        
            sn = input()
            
            if sn in ['S', 's']: 
                grdva_seq = GRDVA_Seq(browser, lista_dados, 
                                    max_delay=int(configs["max_delay"]), 
                                    processo=processo, 
                                    ano_inicio=ex1,
                                    ano_fim=ex2,
                                    guia=guia,
                                    operacao='gerar')                   
                
                grdva_seq.realizar_operacao() 
            else:
                print('\nOperação abortada!!\n') 
        elif op == '20': # DESIN
            processo = configs['processo']
            exercicio, guia = \
                int(configs["exercicio"]), int(configs["guia"])
            
            print('\nATENÇÃO!!!\n')
            
            print(f'processo={processo}')
            print(f'exercicio={exercicio}, guia={guia}')
            
            print('\nConfirma(s/n)?')        
            sn = input()
            
            if sn in ['S', 's']: 
                desin_seq = DESIN_Seq(browser, lista_dados, 
                                      max_delay=int(configs["max_delay"]), 
                                      processo=processo, 
                                      exercicio=exercicio,
                                      guia=guia)                   
                
                desin_seq.realizar_operacao() 
            else:
                print('\nOperação abortada!!\n')
        elif op == '21': # PEGAR depositos na DEPO2
            print('\nATENÇÃO!!!\n')
            
            print(f'exercicio={configs["exercicio"]}')
            print(f'guia={configs["guia"]}')
            
            print('\nImportante!!!\n')
            print('Preencha *exercicio* e *csv_saida* com o mesmo ano!')
                        
            print('\nConfirma(s/n)?')    
            
            sn = input()
            
            if sn in ['S', 's']: 
                depo2 = DEPO2_Get_Depositos_Seq(browser, 
                                  lista_dados, 
                                  max_delay=int(configs["max_delay"]),
                                  exercicio=int(configs["exercicio"]),
                                  guia=int(configs["guia"]))
            
                dados: DataFrame = depo2.realizar_operacao()
                dados.to_csv(configs["csv_saida"], index=False)
            else:
                print('\nOperação abortada!!\n')
        elif op == '22': # copia de tela DEPO2
            print('\nATENÇÃO!!!\n')
            
            print(f'exercicio={configs["exercicio"]}')
            print(f'guia={configs["guia"]}')
                        
            print('\nConfirma(s/n)?')    
            
            sn = input()
            
            if sn in ['S', 's']: 
                depo2 = DEPO2_Copia_Tela_Seq(browser, 
                                  lista_dados, 
                                  max_delay=int(configs["max_delay"]),
                                  exercicio=int(configs["exercicio"]),
                                  guia=int(configs["guia"]))
            
                depo2.realizar_operacao()
            else:
                print('\nOperação abortada!!\n')
       
        elif op == '23': # apropriar depósito
            processo = configs['processo']
            exercicio, guia = \
                int(configs["exercicio"]), int(configs["guia"])
            
            print('\nATENÇÃO!!!\n')
            
            print(f'processo={processo}')
            print(f'exercicio={exercicio}, guia={guia}')
            
            print('\nConfirma(s/n)?')        
            sn = input()
            
            if sn in ['S', 's']: 
                cvdep_seq = CVDEP_Apropriar_Seq(browser, lista_dados, 
                                      max_delay=int(configs["max_delay"]), 
                                      processo=processo, 
                                      exercicio=exercicio,
                                      guia=guia)                   
                
                cvdep_seq.realizar_operacao() 
            else:
                print('\nOperação abortada!!\n')    
        elif op == '24': # finalizar guia
            processo = configs['processo']
            exercicio, guia = \
                int(configs["exercicio"]), int(configs["guia"])
            
            print('\nATENÇÃO!!!\n')
            
            print(f'processo={processo}')
            print(f'exercicio={exercicio}, guia={guia}')
            
            print('\nConfirma(s/n)?')        
            sn = input()
            
            if sn in ['S', 's']: 
                ea2_seq = EA2_Finalizar_Seq(browser, lista_dados, 
                                      max_delay=int(configs["max_delay"]), 
                                      processo=processo, 
                                      exercicio=exercicio,
                                      guia=guia)                   
                
                ea2_seq.realizar_operacao() 
            else:
                print('\nOperação abortada!!\n')
        elif op == '25': # valor venal declarado
            processo = configs['processo']
            apartirde, origem = \
                int(configs["apartirde"]), int(configs["origem"])
                
            ex1, ex2 = \
                int(configs["ano_inicio"]), int(configs["ano_fim"])
            
            tipo_dec = configs["tipo_dec"]
            
            idx = int(configs["idx"])
            
            print('\nVALOR VENAL DECLARADO!!!\n')
            print('\nATENÇÃO!!!\n')            
            
            print(f'processo={processo}')
            print(f'apartirde={apartirde}, origem={origem}')
            print(f'de={ex1}, ate={ex2}')
            print(f'tipo de decisão={tipo_dec}')
            print(f'idx={idx}')
            
            print('\nConfirma(s/n)?')        
            sn = input()
            
            if sn in ['S', 's']: 
                vvdec_seq = VVDEC_Seq(browser, lista_dados, 
                                      max_delay=int(configs["max_delay"]), 
                                      processo=processo, 
                                      apartirde=apartirde,
                                      origem=origem,
                                      anoinicio=ex1,
                                      anofim=ex2,                                      
                                      tipo_dec=tipo_dec,
                                      idx=idx)                   
                
                vvdec_seq.realizar_operacao() 
            else:
                print('\nOperação abortada!!\n')
        elif op == '26': # IMGUI                
            impressora = configs["impressora"]
            
            print('\nIMGUI!!!\n')
            print('\nATENÇÃO!!!\n')            
            
            print(f'impressora={impressora}')
            
            print('\nConfirma(s/n)?')        
            sn = input()
            
            if sn in ['S', 's']: 
                imgui_seq = IMGUI_Seq(browser, lista_dados, 
                                      max_delay=int(configs["max_delay"]), 
                                      impressora=impressora)                   
                
                imgui_seq.realizar_operacao() 
            else:
                print('\nOperação abortada!!\n')        
        elif op == '0': # sair
            break        
        else: print('opção inválida')
        
mostra_menu()