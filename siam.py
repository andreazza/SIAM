#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 16:41:56 2019

@author: carlos
"""

# import winsound
import os
from selenium import webdriver
import time
import datetime
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import re
import random
from pandas import DataFrame

class Tela (object):
    """ 
        superclasse Tela
        define os atributos e métodos compartilhados por todas as telas
    """
    def __init__(self, browser): # falta achar o tipo do driver
        """
        Args:
            path do arquivo do driver
        """
        self.__browser = browser
        self.ids: dict = {#tela de login
                          'usuario' : 'ctl00_ePortalContent_USUARIO',
                          'senha' : 'ctl00_ePortalContent_SENHA',
                          'botao_entrar' : 'ctl00_ePortalContent_btEntrar',
                          
                          #tela compi
                          'atalho': 'ctl00_ATALHO',
                          'botao_ir': 'ctl00_lnkIr', 
                          'ii':'ctl00_ePortalContent_UCINSCRICAO_INSCRICAO',
                          'dv':'ctl00_ePortalContent_UCINSCRICAO_DIGITO',
                          'status': 'ctl00_ePortalContent_STATUS', 
                          'status_opcoes':'ctl00_ePortalContent_drpSTATUS',
                          # tem que testar se o self.limpa_elemento
                          # funciona para um combo                             
                          'pa1':'ctl00_ePortalContent_UCPROCESSO_PROCESSO1',
                          'pa2':'ctl00_ePortalContent_UCPROCESSO_PROCESSO2',
                          'pa3':'ctl00_ePortalContent_UCPROCESSO_PROCESSO3',
                          'pa4':'ctl00_ePortalContent_UCPROCESSO_PROCESSO4',
                          'logradouro': 'ctl00_ePortalContent_TRECHOMSG',
                          'cl':'ctl00_ePortalContent_UCCODLOGRAD_CODLOGRAD',
                          'numero':'ctl00_ePortalContent_NR',
                          'trecho':'ctl00_ePortalContent_TRECHO',
                          'comp1':'ctl00_ePortalContent_COMPLEND',
                          'comp2':'ctl00_ePortalContent_COMPLEND2',
                          'comp3':'ctl00_ePortalContent_COMPLEND3',
                          'comp4':'ctl00_ePortalContent_COMPLEND4',
                          'comp5':'ctl00_ePortalContent_COMPLEND5',
                          'comp6':'ctl00_ePortalContent_COMPLEND6',
                          'lote':'ctl00_ePortalContent_LOTE',
                          'quadra':'ctl00_ePortalContent_QUADRA',
                          'pal':'ctl00_ePortalContent_LOTEAM',
                          
                          'compmigrado': 'ctl00_ePortalContent_COMPLMIGRADO',
                          
                          # radio
                          'apagar_radio':'ctl00_ePortalContent_rblAPAGARCOMPLMIGR_0',
                          # radio
                          'benf_radio_sim':'ctl00_ePortalContent_rblBENF_0',
                          'benf_radio_nao':'ctl00_ePortalContent_rblBENF_1',
                            
                          # combo
                          'ri_opcoes':'ctl00_ePortalContent_drpRI',
                             
                          'matricula':'ctl00_ePortalContent_MATRICULA',
                          'condicao':'ctl00_ePortalContent_CONDICAO',
                          
                          # radio
                          'cpf_radio':'ctl00_ePortalContent_rbCPFT',
                          # radio 
                          'cnpf_radio':'ctl00_ePortalContent_rbCNPJT',
                          # radio
                          'sequencial_radio':'ctl00_ePortalContent_rbSEQUENCIALT',
                             
                          'cpf1':'ctl00_ePortalContent_CPFCGCT1',
                          'cpf2':'ctl00_ePortalContent_CPFCGCT2',
                          'cpf3':'ctl00_ePortalContent_CPFCGCT3',
                          'tipologia':'ctl00_ePortalContent_ESPECIE',
                          # combo
                          'tipologia_opcoes':'ctl00_ePortalContent_drpESPECIE',
                          # combo
                          'utilizacao_opcoes':'ctl00_ePortalContent_drpATIVIDADE',
                          'posicao':'ctl00_ePortalContent_POSICAO',
                          # combo
                          'posicao_opcoes':'ctl00_ePortalContent_drpPOSICAO',
                          'fracao_fiscal':'ctl00_ePortalContent_FRFISCAL',
                          'fracao_ideal':'ctl00_ePortalContent_FRIDEAL',
                          'idade':'ctl00_ePortalContent_IDADE',
                          'area_edificada':'ctl00_ePortalContent_AREAEDIF',
                          'qtd_tcl':'ctl00_ePortalContent_QTDTCL',
                          'ano_desd':'ctl00_ePortalContent_ANODESD',
                          'id_terreno':'ctl00_ePortalContent_IDTERRENO',
                          'area_terreno':'ctl00_ePortalContent_AREATERR',
                          'testada':'ctl00_ePortalContent_TESTREAL',
                          'qtd_testadas':'ctl00_ePortalContent_QTTESTDCAD',
                          'id_condom':'ctl00_ePortalContent_IDCONDOM',
                             
                          # radio
                          'sim_radio':'ctl00_ePortalContent_rbSIM',
                          # radio
                          'nao_radio':'ctl00_ePortalContent_rbNAO',
                             
                          'vig_inicial':'ctl00_ePortalContent_VIGINICIAL',
                          'vig_final':'ctl00_ePortalContent_VIGFINAL',
                          
                          # na tela CALC EM GRUPO, esses campos têm nome diferente
                          'vig_inicial_CALC':'ctl00_ePortalContent_VIG_INICIAL',
                          'vig_final_CALC':'ctl00_ePortalContent_VIG_FINAL',
                          
                          'incluir_botao':'ctl00_ePortalContent_btIncluir',
                          'alterar_botao':'ctl00_ePortalContent_btAlterar',
                          'consultar_botao':'ctl00_ePortalContent_btConsultar',
                          
                          'radio_NAO': 'ctl00_ePortalContent_rbNAO',
                          
                          'botao_limpar': 'ctl00_btLimpar',
                          
                          'ok': 'popup_ok',
                          # mensagem de sucesso ou de erro após a operacao
                          'status_line':'ctl00_ePortalContent_StatusLine',
                          #botao visualizar da FCIS1
                          'botao_visualizar':'ctl00_ePortalContent_btVisualizar',
                          #anoI na tela FCIS1
                          'ano_inicial':'ctl00_ePortalContent_ANOI',
                          #anoF na tela FCIS1
                          'ano_final':'ctl00_ePortalContent_ANOF',
                          'link': 'link',
                          
                          #tela CALC EM GRUPO
                          'botao_processar':'ctl00_ePortalContent_btIncluir',
                          
                          #tela REAGI 
                          'exercicio':'ctl00_ePortalContent_EXERC',
                          'guia': 'ctl00_ePortalContent_GUIA',
                          'botao_reativar': 'ctl00_ePortalContent_btReativar',
                          
                          #tela cancelar em grupo SEQ38                          
                          # 'Operacao nao permitida'
                          # FIM NORMAL
                          'exer1': 'ctl00_ePortalContent_EXERCICIO',
                          'exer2': 'ctl00_ePortalContent_EXERCICIO2',
                          'guia1': 'ctl00_ePortalContent_GUIA',
                          'guia2': 'ctl00_ePortalContent_GUIA2',
                          'radio_imprimir': 'ctl00_ePortalContent_chbIMPRIMIRGUIA',
                          # botao_processar é o mesmo da tela CALC em grupo
                          
                          #tela RVLAN
                          'check1': 'ctl00_ePortalContent_chkSel1',
                          'check2': 'ctl00_ePortalContent_chkSel2',
                          'check3': 'ctl00_ePortalContent_chkSel3',
                          'check4': 'ctl00_ePortalContent_chkSel4',
                          'check5': 'ctl00_ePortalContent_chkSel5',
                          'check6': 'ctl00_ePortalContent_chkSel6',
                          'lote1': 'ctl00_ePortalContent_LOTE1',
                          'lote2': 'ctl00_ePortalContent_LOTE2',
                          'lote3': 'ctl00_ePortalContent_LOTE3',
                          'lote4': 'ctl00_ePortalContent_LOTE4',
                          'lote5': 'ctl00_ePortalContent_LOTE5',
                          'lote6': 'ctl00_ePortalContent_LOTE6',
                          'base1': 'ctl00_ePortalContent_BASE1',
                          'base2': 'ctl00_ePortalContent_BASE2',
                          'base3': 'ctl00_ePortalContent_BASE3',
                          'base4': 'ctl00_ePortalContent_BASE4',
                          'base5': 'ctl00_ePortalContent_BASE5',
                          'base6': 'ctl00_ePortalContent_BASE6',
                          'iptu1': 'ctl00_ePortalContent_IPTU1',
                          'iptu2': 'ctl00_ePortalContent_IPTU2',
                          'iptu3': 'ctl00_ePortalContent_IPTU3',
                          'iptu4': 'ctl00_ePortalContent_IPTU4',
                          'iptu5': 'ctl00_ePortalContent_IPTU5',
                          'iptu6': 'ctl00_ePortalContent_IPTU6',
                          'tcl1': 'ctl00_ePortalContent_VALOR1',
                          'tcl2': 'ctl00_ePortalContent_VALOR2',
                          'tcl3': 'ctl00_ePortalContent_VALOR3',
                          'tcl4': 'ctl00_ePortalContent_VALOR4',
                          'tcl5': 'ctl00_ePortalContent_VALOR5',
                          'tcl6': 'ctl00_ePortalContent_VALOR6',
                          'botao_incluir_compor': 'ctl00_ePortalContent_btIncluir2',
                          
                          # tela GRGUI
                          # botões incluir e alterar são os mesmos da COMPI
                          
                          # tela FINAL
                          # botão alterar é o mesmo da COMPI
                          'total_guia': 'ctl00_ePortalContent_TOTAL_GUIA1',
                          'botao_efetivar': 'ctl00_ePortalContent_btEfetivar',
                          'valor_quitado': 'ctl00_ePortalContent_VALOR_QUITADO1',
                          'imprimir_guias': 'ctl00_ePortalContent_chkImprimirGuias',
                          'final_mensagem': 'ctl00_ePortalContent_mensagemnaoexistem',
                          
                          # tela CANC em grupo
                          'check_imprimir': 'ctl00_ePortalContent_chbIMPRIMIRGUIA',
                          
                          # tela CVQUI
                          'guia_cvqui': 'ctl00_ePortalContent_PRXGUIA',
                          
                          'guia_0': 'ctl00_ePortalContent_array_CVQUI_View_ctl02_GUIA_Item_',
                          'sp0': 'ctl00_ePortalContent_array_CVQUI_View_ctl02_SP_Item_',
                          'sc0': 'ctl00_ePortalContent_array_CVQUI_View_ctl02_SC_Item_',
                          'valor0': 'ctl00_ePortalContent_array_CVQUI_View_ctl02_VALORGUIA_Item_',
                          'quitado0': 'ctl00_ePortalContent_array_CVQUI_View_ctl02_VALORQUITADO_Item_',
                          'quitou0': 'ctl00_ePortalContent_array_CVQUI_View_ctl02_STATUS_Item_',
                          
                          
                          'guia_1': 'ctl00_ePortalContent_array_CVQUI_View_ctl03_GUIA_Item_',
                          'sp1': 'ctl00_ePortalContent_array_CVQUI_View_ctl03_SP_Item_',
                          'sc1': 'ctl00_ePortalContent_array_CVQUI_View_ctl03_SC_Item_',
                          'valor1': 'ctl00_ePortalContent_array_CVQUI_View_ctl03_VALORGUIA_Item_',
                          'quitado1': 'ctl00_ePortalContent_array_CVQUI_View_ctl03_VALORQUITADO_Item_',
                          'quitou1': 'ctl00_ePortalContent_array_CVQUI_View_ctl03_STATUS_Item_',
                          
                          'guia_2': 'ctl00_ePortalContent_array_CVQUI_View_ctl04_GUIA_Item_',
                          'sp2': 'ctl00_ePortalContent_array_CVQUI_View_ctl04_SP_Item_',
                          'sc2': 'ctl00_ePortalContent_array_CVQUI_View_ctl04_SC_Item_',
                          'valor2': 'ctl00_ePortalContent_array_CVQUI_View_ctl04_VALORGUIA_Item_',
                          'quitado2': 'ctl00_ePortalContent_array_CVQUI_View_ctl04_VALORQUITADO_Item_',
                          'quitou2': 'ctl00_ePortalContent_array_CVQUI_View_ctl04_STATUS_Item_',
                          
                          'guia_3': 'ctl00_ePortalContent_array_CVQUI_View_ctl05_GUIA_Item_',
                          'sp3': 'ctl00_ePortalContent_array_CVQUI_View_ctl05_SP_Item_',
                          'sc3': 'ctl00_ePortalContent_array_CVQUI_View_ctl05_SC_Item_',
                          'valor3': 'ctl00_ePortalContent_array_CVQUI_View_ctl05_VALORGUIA_Item_',
                          'quitado3': 'ctl00_ePortalContent_array_CVQUI_View_ctl05_VALORQUITADO_Item_',
                          'quitou3': 'ctl00_ePortalContent_array_CVQUI_View_ctl05_STATUS_Item_',
                          
                          'guia_4': 'ctl00_ePortalContent_array_CVQUI_View_ctl06_GUIA_Item_',
                          'sp4': 'ctl00_ePortalContent_array_CVQUI_View_ctl06_SP_Item_',
                          'sc4': 'ctl00_ePortalContent_array_CVQUI_View_ctl06_SC_Item_',
                          'valor4': 'ctl00_ePortalContent_array_CVQUI_View_ctl06_VALORGUIA_Item_',
                          'quitado4': 'ctl00_ePortalContent_array_CVQUI_View_ctl06_VALORQUITADO_Item_',
                          'quitou4': 'ctl00_ePortalContent_array_CVQUI_View_ctl06_STATUS_Item_',
                          
                          'guia_5': 'ctl00_ePortalContent_array_CVQUI_View_ctl07_GUIA_Item_',
                          'sp5': 'ctl00_ePortalContent_array_CVQUI_View_ctl07_SP_Item_',
                          'sc5': 'ctl00_ePortalContent_array_CVQUI_View_ctl07_SC_Item_',
                          'valor5': 'ctl00_ePortalContent_array_CVQUI_View_ctl07_VALORGUIA_Item_',
                          'quitado5': 'ctl00_ePortalContent_array_CVQUI_View_ctl07_VALORQUITADO_Item_',
                          'quitou5': 'ctl00_ePortalContent_array_CVQUI_View_ctl07_STATUS_Item_',
                          
                          'guia_6': 'ctl00_ePortalContent_array_CVQUI_View_ctl08_GUIA_Item_',
                          'sp6': 'ctl00_ePortalContent_array_CVQUI_View_ctl08_SP_Item_',
                          'sc6': 'ctl00_ePortalContent_array_CVQUI_View_ctl08_SC_Item_',
                          'valor6': 'ctl00_ePortalContent_array_CVQUI_View_ctl08_VALORGUIA_Item_',
                          'quitado6': 'ctl00_ePortalContent_array_CVQUI_View_ctl08_VALORQUITADO_Item_',
                          'quitou6': 'ctl00_ePortalContent_array_CVQUI_View_ctl08_STATUS_Item_',
                          
                          'guia_7': 'ctl00_ePortalContent_array_CVQUI_View_ctl09_GUIA_Item_',
                          'sp7': 'ctl00_ePortalContent_array_CVQUI_View_ctl09_SP_Item_',
                          'sc7': 'ctl00_ePortalContent_array_CVQUI_View_ctl09_SC_Item_',
                          'valor7': 'ctl00_ePortalContent_array_CVQUI_View_ctl09_VALORGUIA_Item_',
                          'quitado7': 'ctl00_ePortalContent_array_CVQUI_View_ctl09_VALORQUITADO_Item_',
                          'quitou7': 'ctl00_ePortalContent_array_CVQUI_View_ctl09_STATUS_Item_',
                          # PRECISA INCLUIR ATÉ A guia_14 (15 guias por EX)
                          
                          # REMIT
                          # o botão consultar na REMIT tem nome diferente
                          'consultar_remit': 'ctl00_ePortalContent_btnConsultar',
                          'iptu_1': 'ctl00_ePortalContent_chbREMIPTU1',
                          'tcl_1': 'ctl00_ePortalContent_chbREMTCL1',
                          'iptu_2': 'ctl00_ePortalContent_chbREMIPTU2',
                          'tcl_2': 'ctl00_ePortalContent_chbREMTCL2',
                          'iptu_3': 'ctl00_ePortalContent_chbREMIPTU3',
                          'tcl_3': 'ctl00_ePortalContent_chbREMTCL3',
                          'iptu_4': 'ctl00_ePortalContent_chbREMIPTU4',
                          'tcl_4': 'ctl00_ePortalContent_chbREMTCL4',
                          'iptu_5': 'ctl00_ePortalContent_chbREMIPTU5',
                          'tcl_5': 'ctl00_ePortalContent_chbREMTCL5',
                          'exercicio_remit': 'ctl00_ePortalContent_EXERCICIO',
                          
                          #GRDVA
                          'exer1_grdva': 'ctl00_ePortalContent_EXERCICIO',
                          'exer2_grdva': 'ctl00_ePortalContent_EXERCICIO_FINAL',
                          'guia_gerar': 'ctl00_ePortalContent_GUIAGERA',
                          'cancelar_grdva': 'ctl00_ePortalContent_btCancelar',
                          'gerar_grdva': 'ctl00_ePortalContent_btGerar',       
                          
                          #DESIN
                          'desinibir_botao': 'ctl00_ePortalContent_btAlterar',
                          
                          #DEPO2
                          'deposito_disponivel': 'ctl00_ePortalContent_DISPONIVEL',
                          'exercicio_DEPO2': 'ctl00_ePortalContent_EXERCICIO',                          
                          
                          #CVQUI
                          'apropriar_botao': 'ctl00_ePortalContent_btApropriar',
                          
                          #EA2
                          'imprime_guia': 'ctl00_ePortalContent_chbIMPRIMEGUIA',
                          
                          #VVDEC
                          'consultar_vvdec': 'ctl00_ePortalContent_btnConsultar',
                          'excluir_vvdec': 'ctl00_ePortalContent_btExcluir',
                          'apartirde': 'ctl00_ePortalContent_APARTIRDE',
                          'origem': 'ctl00_ePortalContent_EXERCORIGEM',
                          'judical': 'ctl00_ePortalContent_rblTIPODECISAO_1',
                          'vvdec': 'ctl00_ePortalContent_VLVENALDECLARADO',
                          
                          #IMGUI
                          'imprimir_botao': 'ctl00_ePortalContent_btIMPRIMIR',
                          'impressora': 'ctl00_ePortalContent_IMPRESSORA',
                          
                          }
    
    def ir_para_tela(self, nome_tela: str):
        """
            vai para a tela nome_tela
        """
        # preenche caixa de atalho com nome_tela
        self.preenche_caixa_de_texto('atalho', nome_tela)
        # clica no botao do atalho para ir para nome_tela
        self.click('botao_ir')
    
    def click(self, id_elemento: str):
        """
            encontra o elemento pelo id e clica
        """
        
        elemento = self.__browser.find_element_by_id(self.ids[id_elemento])
        elemento.click()
        
    def force_click(self, id_elemento: str):
        """
            encontra o elemento pelo id e clica
        """
        
        elemento = self.__browser.find_element_by_id(self.ids[id_elemento])
        self.__browser.execute_script("arguments[0].click();", elemento)
    
    def click_link(self, link: str):
        """
            encontra o elemento pelo id e clica
        """
        
        link = self.__browser.find_element_by_link_text('link')
        link.click()
           
    
    def marcar_radio(self, id_elemento: str):
        """
            encontra o elemento radio pelo id e clica
        """
        
        radio = self.__browser.find_element_by_id(self.ids[id_elemento])
        self.__browser.execute_script("arguments[0].checked = true;", radio)
    
    def desmarcar_radio(self, id_elemento: str):
        """
            encontra o elemento radio pelo id e clica
        """
        
        radio = self.__browser.find_element_by_id(self.ids[id_elemento])
        self.__browser.execute_script("arguments[0].checked = false;", radio)
    
    def limpa_elemento(self, id_elemento: str):
        """
            encontra caixa de texto pelo id e limpa
        """
        caixa = self.__browser.find_element_by_id(self.ids[id_elemento])
        caixa.clear()
    
    def desmarcar(self, id_elemento: str):
        """
            
        """
        check = self.__browser.find_element_by_id(self.ids[id_elemento])
        
        if check.get_attribute('checked'):
            check.click()
    
    def limpa_varios_elementos(self, ids: [str]):
        """
            limpa as caixas de texto indicadas na lista ids
        """
        for id_elemento in ids:
            self.limpa_elemento(id_elemento)
    
    def preenche_caixa_de_texto(self, id_elemento: str, texto: str):
        """
            encontra caixa de texto pelo id e preenche com texto
        """
        caixa = self.__browser.find_element_by_id(self.ids[id_elemento])
        caixa.send_keys(texto)
    
    def preenche_caixa_de_texto_1a1(self, id_elemento: str, texto: str):
        """
            encontra caixa de texto pelo id e preenche com texto
        """
        caixa = self.__browser.find_element_by_id(self.ids[id_elemento])
        for letra in texto:
            caixa.send_keys(letra)
    
    def preenche_varias_caixas(self, ids_dict: dict):
        """
            preenche as caixas de texto indicadas em id_valor_dict
        """
        for id_elemento, texto in ids_dict.items():
            self.preenche_caixa_de_texto(id_elemento, texto)
    
    def get_span_texto(self, id_elemento: str) -> str:
        """
            pega o texto de um span
        """
        elemento = self.__browser.find_element_by_id(self.ids[id_elemento])
        return elemento.text
    
    def get_texto(self, id_elemento: str) -> str:
        """
            pega o texto
        """
        elemento = self.__browser.find_element_by_id(self.ids[id_elemento])
        return elemento.get_attribute('value')
    
    def get_varios_textos(self, id_elementos: [str]) -> [str]:
        """
            pega varios textos
        """
        
        return [self.get_texto(id_ele) for id_ele in id_elementos]
    
    def preenche_PA(self, p1: str, p2: str, p3: str, p4: str):
        """ preenche processo """
        self.preenche_caixa_de_texto('pa1', p1)
        self.preenche_caixa_de_texto('pa2', p2)
        self.preenche_caixa_de_texto('pa3', p3)
        self.preenche_caixa_de_texto('pa4', p4)
    
    def preenche_ii_e_dv(self, ii: str, dv: str):
        """ preenche ii e dv """
        self.preenche_caixa_de_texto('ii', ii)
        self.preenche_caixa_de_texto('dv', dv)
        
    def limpa_ii_e_dv(self):
        """ limpa ii e dv """
        self.limpa_elemento('ii')
        self.limpa_elemento('dv')
    
    def clicar_ok(self):
        """ clica no botao ok """
        self.click('ok')
        
    def clicar_botao_limpar(self):
        """ clica no botao limpar """
        self.click('botao_limpar')        
    
    def executar_script(self, script: str):
        """ executa script """
        self.__browser.execute_script(script)
        
    def salvar_html(self, nome: str):  
        """ salva html / PRECISA INFORMAR SE FUNCIONOU """
        with open(nome, "w", encoding="utf-8") as f:
            f.write(self.__browser.page_source)
    
    def get_status_line(self) -> str:
        """ pega a mensagem após a operacao """
        status_line = self.__browser.find_element_by_id(self.ids['status_line'])
        return status_line.text
    
    def tem_texto_na_status_line(self, texto:str) -> bool:
        """ verifica se tem texto na status_line """
        status_line = self.get_status_line()
        
        return not (status_line.find(texto) == -1)
    
    def esperar_elem(self, elem:str, tempo: int):
        WebDriverWait(self.__browser, tempo).until(
            EC.presence_of_element_located((By.ID, 
                                            self.ids[elem])))
    
    def espera_implicita(self, tempo: int):
        self.__browser.implicitly_wait(tempo)
    
    def screen_shot(self, nome_arq):
        self.__browser.get_screenshot_as_file(nome_arq)
        
    def preenche_select_combo(self, elem: str, opcao: str):
        id = self.ids[elem]
        self.__browser.find_element_by_xpath(f'//select[@id=\'{id}\']/option[text()=\'{opcao}\']').click()
        

class Login_SIAM(Tela):
    """
        classe para fazer operacoes na de login
    """    
    def __init__(self, browser): # falta achar o tipo do driver
        """
        Args:
            path do arquivo do driver
        """
        super().__init__(browser)
        
    
    def preenche_usuario_senha(self, usuario: str, senha: str):
        """ preenche ii e dv """
        self.preenche_caixa_de_texto('usuario', usuario)
        self.preenche_caixa_de_texto('senha', senha)
    
    def entrar(self):
        """ clica no botao entrar """
        self.click('botao_entrar')

class Compi(Tela):
    """
        classe para fazer operacoes na COMPI
    """    
    def __init__(self, browser): # falta achar o tipo do driver
        """
        Args:
            path do arquivo do driver
        """
        super().__init__(browser)
        
    
    def ir_para_COMPI(self): 
        self.ir_para_tela('COMPI')
    
    def consultar(self):
        """ clica no botao consultar """
        self.click('consultar_botao')
        
    def alterar(self):
        """ clica no botao alterar """
        self.click('alterar_botao')
        
    def clicar_radio_sim(self):
        """ clica no radio sim """
        self.marcar_radio('sim_radio')
        
    def marcar_radio_apagar_comp_migrado(self):
        """ marcar radio apagar complemento migrado """
        self.marcar_radio('apagar_radio')
      
    def marcar_radio_benf_nao(self):
        """ marcar radio benf_radio_nao """
        self.marcar_radio('benf_radio_nao')        
    
    def marcar_radio_benf_sim(self):
        """ marcar radio benf_radio_sim """
        self.marcar_radio('benf_radio_sim')        
        
    def preenche_vigencia(self, inicio, fim):
        """ preenche vigencia inicial e final """
        self.preenche_caixa_de_texto('vig_inicial', inicio)
        self.preenche_caixa_de_texto('vig_final', fim)
        
    def alterar_ri(self, ri:str):
        self.preenche_select_combo('ri_opcoes', ri)
        
    def verifica_se_alterou(self):
        """ 
            retorna True se alterou com sucesso
            pode lançar uma exceção caso a visualização seja um insucesso
            captura e encerra o processo
        """
        
        return self.tem_texto_na_status_line('êxito')

class CVDEP(Tela):
    """
        classe para fazer operacoes na CVDEP
    """    
    def __init__(self, browser): # falta achar o tipo do driver
        """
        Args:
            path do arquivo do driver
        """
        super().__init__(browser)
        
    
    def ir_para_CVDEP(self): 
        self.ir_para_tela('CVDEP')
    
    def consultar(self):
        """ clica no botao consultar """
        self.click('consultar_botao')
        
    def preenche_ex_guia(self, exercicio: int, guia: int):
        """ preenche exercicio e guia """
        self.preenche_caixa_de_texto('exer1', exercicio)
        self.preenche_caixa_de_texto('guia', guia)
        
    def apropriar(self):
        """ clica no botao alterar """
        self.click('apropriar_botao')
        
    def verifica_se_apropriou(self): 
        """ 
            retorna True se a apropriação foi successful
        """
              
        return self.tem_texto_na_status_line('EFETUADA')
    
class EA2(Tela):
    """
        classe para fazer operacoes na EA2
    """    
    def __init__(self, browser): # falta achar o tipo do driver
        """
        Args:
            path do arquivo do driver
        """
        super().__init__(browser)
        
    
    def ir_para_EA2(self): 
        self.ir_para_tela('EA2')
    
    def consultar(self):
        """ clica no botao consultar """
        self.click('consultar_botao')
        
    def incluir(self):
        """ clica no botao incluir """
        self.click('incluir_botao')
        
    def preenche_ex_guia(self, exercicio: int, guia: int):
        """ preenche exercicio e guia """
        self.preenche_caixa_de_texto('exer1', exercicio)
        self.preenche_caixa_de_texto('guia', guia)
        
    def desmarcar_radio_imprime(self):
        """ desmarca radio para imprimir relatório """
        self.desmarcar_radio('imprime_guia')
        
    def verifica_se_incluiu(self): 
        """ 
            retorna True se a inclusão foi successful
        """
              
        return self.tem_texto_na_status_line('êxito')
        
class RVLAN(Tela):
    """
        classe para fazer operacoes na RVLAN
    """    
    def __init__(self, browser): # falta achar o tipo do driver
        """
        Args:
            path do arquivo do driver
        """
        super().__init__(browser)        
    
    def ir_para_RVLAN(self): 
        self.ir_para_tela('RVLAN')
    
    def alterar(self):
        """ clica no botao alterar """
        self.click('alterar_botao')
        
    def incluir_e_compor(self):
        """ clica no botao inluir e compor """
        self.click('botao_incluir_compor')     
        
    def martela_vv(self, vvs):
        """ martela o valor venal
            vvs: lista de valor venal
        """        
        for i in vvs.keys():
            # precisa refatorar isso aqui
            # o while ou recursao deve ficar em preenche_caixa_de_texto_1a1
            # para evitar repetição
            while True:
                self.limpa_elemento(f'base{i}')
                self.preenche_caixa_de_texto_1a1(f'base{i}', vvs[i])
                base = self.get_texto(f'base{i}')
                
                if base == vvs[i]:
                    break
    
    def martela_iptu(self, iptus):
        """ martela o iptu
            iptus: lista de iptus
        """        
        for i in iptus.keys():
            # precisa refatorar isso aqui
            # o while ou recursao deve ficar em preenche_caixa_de_texto_1a1
            # para evitar repetição
            while True:
                self.limpa_elemento(f'iptu{i}')
                self.preenche_caixa_de_texto_1a1(f'iptu{i}', iptus[i])
                iptu = self.get_texto(f'iptu{i}')
                
                if iptu == iptus[i]:
                    break
    
    def martela_tcl(self, tcls):
        """ martela a tcl
            tcls: lista de tcls
        """        
        for i in tcls.keys():
            # precisa refatorar isso aqui
            # o while ou recursao deve ficar em preenche_caixa_de_texto_1a1
            # para evitar repetição            
            while True:
                self.limpa_elemento(f'tcl{i}')
                self.preenche_caixa_de_texto_1a1(f'tcl{i}', tcls[i])
                tcl = self.get_texto(f'tcl{i}')
                
                if tcl == tcls[i]:
                    break
    
    def clica_ckecks(self, num_anos):
        """
            clica nos checks para alterar
            num_anos: número de exercícios
        """
        
        for i in range(num_anos):
            self.force_click(f'check{i+1}')
    
    def pega_vv_iptu_tcl(self, ii, dv, inicio, fim):
        """
            retorna simulacao de vv, iptu e tcl
        """
        simulacao = {'ii': ii, 'dv': dv}
        num_anos = fim-inicio+1
        for i in range(num_anos):
            simulacao[f"vv{fim-i}"] = \
                self.get_texto(f"base{i+1}")
            simulacao[f"iptu{fim-i}"] = \
                self.get_texto(f"iptu{i+1}")
            simulacao[f"tcl{fim-i}"] = \
                self.get_texto(f"tcl{i+1}")
            
        return simulacao    

class GRGUI(Tela):
    """
        classe para fazer operacoes na GRGUI
    """    
    def __init__(self, browser): # falta achar o tipo do driver
        """
        Args:
            path do arquivo do driver
        """
        super().__init__(browser)
        
    
    def ir_para_GRGUI(self): 
        self.ir_para_tela('GRGUI')
    
    def alterar(self):
        """ clica no botao alterar """
        self.click('alterar_botao')
        
    def incluir(self):
        """ clica no botao alterar """
        self.click('incluir_botao')  

class FINAL(Tela):
    """
        classe para fazer operacoes na FINAL
    """    
    def __init__(self, browser): # falta achar o tipo do driver
        """
        Args:
            path do arquivo do driver
        """
        super().__init__(browser)        
    
    def ir_para_FINAL(self): 
        self.ir_para_tela('GRGUI')
    
    def alterar(self):
        """ clica no botao alterar """
        self.click('alterar_botao')
        
    def efetivar(self):
        """ clica no botao efetivar """
        self.click('botao_efetivar') 
        
    def total_guia(self):
        """ retorna o valor total da guia """
        return self.get_span_texto('total_guia').strip()
    
    def foi_sucesso(self):
        """ 
            retorna True se alterou com sucesso
            lança uma exceção caso a visualização seja um insucesso
            captura e encerra o processo
        """
        mensagem = self.get_span_texto('final_mensagem')
        regex = re.compile(f'(\w+)(\s*)FIM NORMAL')
        result = regex.search(mensagem)
        
        return result != None   
    
    
    def preenche_valor_quitado(self, valor_quitado):
        """ limpa e preenche o valor quitado """
                
        while True:
            # precisa refatorar isso aqui
            # o while ou recursao deve ficar em preenche_caixa_de_texto_1a1
            # para evitar repetição
            self.limpa_elemento('valor_quitado')
            self.preenche_caixa_de_texto_1a1('valor_quitado', valor_quitado)
            vq = self.get_texto('valor_quitado')
            
            if vq == valor_quitado:
                break
    
    def clica_imprimir_guias(self):
        """ clica no imprimir guias para não imprimir """
        self.click('imprimir_guias')

class Calc_Seq(Tela):
    """
        Classe para fazer operações na Calculo em Grupo
    """
    def __init__(self, browser): # falta achar o tipo do driver
        """
        Args:
            path do arquivo do driver
        """
        super().__init__(browser)        
    
    def ir_para_calc_seq(self): 
        self.ir_para_tela('SEQ31')
    
    def limpar_ii_dv(self):
        """ limpa ii e dv """
        self.preenche_caixa_de_texto('ii', '')
        self.preenche_caixa_de_texto('dv', '')
        
    def processar(self):
        """ clica no botao consultar """
        self.click('botao_processar')
        
    def clicar_radio_NAO(self):
        """ clica no botao consultar """
        self.click('radio_NAO')
        
    def preenche_vigencia(self, inicial: int, final: int):
        """ preenche vigencia inicial e final """
        
        self.preenche_caixa_de_texto('vig_inicial_CALC', inicial)
        self.preenche_caixa_de_texto('vig_final_CALC', final)
        
    def operacao_ok(self) -> bool:
        """ verifica se a operacao foi realizada com sucesso """
        
        return self.tem_texto_na_status_line('FINAL OK')

class Canc_Grupo(Tela):
    """
        Classe para fazer operações na Cancelar em Grupo
    """
    def __init__(self, browser): # falta achar o tipo do driver
        """
        Args:
            path do arquivo do driver
        """
        super().__init__(browser)        
    
    def limpar_form(self):
       """
         Tive que fazer essa função específica porque
         o botão limpar não funciona direito nesta tela

        Returns
        -------
        None.

        """
       # TO-DO usa a função específica; não repete isso aqui 
       for elem in ['ii', 'dv','pa1', 'pa2', 'pa3', 'pa4', 'exer1', 'exer2',
                      'guia1', 'guia2']:
            self.limpa_elemento(elem)   

       self.desmarcar('check_imprimir')                      
    
    def ir_para_canc_seq(self): 
        self.ir_para_tela('SEQ38')
    
    def processar(self):
        """ clica no botao consultar """
        self.click('botao_processar')
        
    def desmarcar_radio_imprime(self):
        """ desmarca radio para imprimir relatório """
        self.desmarcar_radio('radio_imprimir')
        
    def preenche_exercicios(self, ex1: int, ex2: int):
        """ preenche exercícios """
        
        self.preenche_caixa_de_texto('exer1', ex1)
        self.preenche_caixa_de_texto('exer2', ex2)
        
    def preenche_guias(self, guia1: int, guia2: int):
        """ preenche guias """
        
        self.preenche_caixa_de_texto('guia1', guia1)
        self.preenche_caixa_de_texto('guia2', guia2)     
        
    def operacao_ok(self) -> bool:
        """ verifica se a operacao foi realizada com sucesso """
        return self.tem_texto_na_status_line('FIM NORMAL')
 
class FCIS1(Tela):
    """
       classe para fazer operacoes na FCIS1
    """
    def __init__(self, browser, url_dir: str): # falta achar o tipo do driver
        """
        Args:
            browser
            url_dir: diretorio dos relatorios
        """
        super().__init__(browser)
        self.url_dir = url_dir
    
    def preenche_ano_inicial(self, ano_inicial: int):
        """ preenche ano inicial """
        self.preenche_caixa_de_texto('ano_inicial', ano_inicial)
    
    def preenche_ano_final(self, ano_final: int):
        """ preenche final """
        self.preenche_caixa_de_texto('ano_final', ano_final)
        
    def clicar_visualizar(self):
        """ clica no botao Visualizar Impressão """
        self.click('botao_visualizar')
        
    def pega_url_pdf(self):
        """ 
            retorna o nme do pdf 
            pode lançar uma exceção caso a visualização seja um insucesso
            captura e encerra o processo
        """
        status_line = self.get_status_line()
        regex = re.compile(f'(\w+)(\s*)\(V I S U A L I Z')
        result = regex.search(status_line)
        pdf = result.group(1)+'.pdf'
        
        url = self.url_dir+pdf
        
        return url
    
    def ir_para_FCIS1(self): 
        self.ir_para_tela('FCIS1')

class IMGUI(Tela):
    """
       classe para fazer operacoes na IMGUI
    """
    def __init__(self, browser): # falta achar o tipo do driver
        """
        Args:
            browser
            url_dir: diretorio dos relatorios
        """
        super().__init__(browser)
    
    def preenche_ano(self, ano: int):
        """ preenche ano """
        self.preenche_caixa_de_texto('exer1', ano)
    
    def preenche_guia(self, guia: int):
        """ preenche guia """
        self.preenche_caixa_de_texto('guia', guia)
        
    def preenche_impressora(self, impressora: str):
        """ preenche guia """
        self.preenche_caixa_de_texto('impressora', impressora)
        
    def clicar_imprimir(self):
        """ clica no botao Visualizar Impressão """
        self.click('imprimir_botao')
            
    def ir_para_IMGUI(self): 
        self.ir_para_tela('IMGUI')
        
    def verifica_exito(self):
        """ 
            retorna True se alterou com sucesso
            pode lançar uma exceção caso a visualização seja um insucesso
            captura e encerra o processo
        """
        status_line = self.get_status_line()
                
        return status_line.find('êxito') != -1

class REAGI(Tela):
    """
        classe para fazer operacoes na REAGI
    """
    def __init__(self, browser): # falta achar o tipo do driver
        """
        Args:
            browser
        """
        super().__init__(browser)
    
    def preenche_ex_guia(self, exercicio: int, guia: int):
        """ preenche exercicio e guia """
        self.preenche_caixa_de_texto('exercicio', exercicio)
        self.preenche_caixa_de_texto('guia', guia)
    
    def consultar(self):
        """ clica no botao consultar """
        self.click('consultar_botao')
        
    def reativar(self):
        """ clica no botao reativar """
        self.click('botao_reativar')
        
    def ir_para_REAGI(self): 
        self.ir_para_tela('REAGI')
    
    def verifica_se_reativou(self):
        """ 
            retorna True se alterou com sucesso
            pode lançar uma exceção caso a visualização seja um insucesso
            captura e encerra o processo
        """
        status_line = self.get_status_line()
        regex = re.compile(f'(\w+)(\s*)êxito')
        result = regex.search(status_line)
        result.group(1)
        
        return True
   
class CVQUI(Tela):
    """
        classe para fazer operacoes na REAGI
    """
    def __init__(self, browser): # falta achar o tipo do driver
        """
        Args:
            browser
        """
        super().__init__(browser)
    
    def preenche_ex_guia(self, exercicio: int, guia: int):
        """ preenche exercicio e guia """
        self.preenche_caixa_de_texto('exercicio', exercicio)
        self.preenche_caixa_de_texto('guia_cvqui', guia)
    
    def consultar(self):
        """ clica no botao consultar """
        self.click('consultar_botao')
        
    def ir_para_CVQUI(self): 
        self.ir_para_tela('CVQUI')
    
    def get_primeira_guia(self):
        return int(self.get_span_texto(id_elemento='guia_0'))
    
    def get_status_proc(self, guia: int):
        return self.get_span_texto(id_elemento=f'sp{guia}')
    
    def get_status_cob(self, guia: int):
        return self.get_span_texto(id_elemento=f'sc{guia}')
    
    def get_valor(self, guia: int):
        valor = self.get_span_texto(
            id_elemento=f'valor{guia}').strip().replace(',', '.', 1)
        
        valor = 0.0 if valor == '' else float(valor)
        
        return valor
    
    def get_quitado(self, guia: int):
        quitado = self.get_span_texto(
            id_elemento=f'quitado{guia}').strip().replace(',', '.', 1)
        
        quitado = 0.0 if quitado == '' else float(quitado)
        
        return quitado
    
    def get_quitou(self, guia: int):
        quitou = self.get_span_texto(id_elemento=f'quitou{guia}')
        
        return 'SIM' if quitou.strip() == 'Quitada' else 'NAO'
    
    def tem_guia_no_exercicio(self):
        status_line = self.get_status_line()
        
        return status_line.find('Nao existe') == -1
        
    
    def get_info_guias(self, ii:str, dv:str):
        """
            pega as informações sobre as guias exibidas na tela atual
            
            Returns
            -------
            Retorna um dict com a informação
            {'g_0_sproc': 'I', 'g_0_scob': 'S', 'g_0_valor': 236.0, 'g_0_quitado': '0.0', 'g_0_quitou':'S',
             'g_0_sproc': 'I', 'g_1_scob': 'S', 'g_1_valor': 77.0, 'g_1_quitado': '20.0', 'g_1_quitou':'N',
             ...}
    
        """
        info_linha = {}
        info_linha['ii'] = ii+'-'+dv
                            
        try:
            # pega a primeira guia emitida no exercício
            guia = self.get_primeira_guia()
            # precisei criar essa variável porque no html o contador de 
            # guias sempre começa com 0. Quando o exercício não tem guia
            # 0 gera erro        
            cont_guia = 0
            
            while True:
                sp = self.get_status_proc(guia=cont_guia)
                sc = self.get_status_cob(guia=cont_guia)
                valor = self.get_valor(guia=cont_guia)
                quitado = self.get_quitado(guia=cont_guia)
                quitou = self.get_quitou(guia=cont_guia)
                
                info_linha[f'g_{guia}_sproc'] = sp
                info_linha[f'g_{guia}_scob'] = sc
                info_linha[f'g_{guia}_valor'] = valor
                info_linha[f'g_{guia}_quitado'] = quitado
                info_linha[f'g_{guia}_quitou'] = quitou
                
                guia += 1
                cont_guia += 1
        except: 
            pass
        
        return info_linha
 
class REMIT(Tela):
    """
        classe para fazer operacoes na REAGI
    """
    def __init__(self, browser): # falta achar o tipo do driver
        """
        Args:
            browser
        """
        super().__init__(browser)
    
    def preenche_ex_guia(self, exercicio: int, guia: int):
        """ preenche exercicio e guia """
        self.preenche_caixa_de_texto('exercicio_remit', exercicio)
        self.preenche_caixa_de_texto('guia', guia)
    
    def consultar(self):
        """ clica no botao consultar """
        self.click('consultar_remit')
        
    def processar(self):
        """ clica no botao reativar """
        self.click('botao_processar')
        
    def ir_para_REMIT(self): 
        self.ir_para_tela('REMIT')
        
    def marcar_checks(self, num_exs:int):
        for i in range(1, num_exs+1):
            self.marcar_radio(f'iptu_{i}')
            self.marcar_radio(f'tcl_{i}')    
            
    def tem_guia_no_exercicio(self):
        """ 
            retorna True se tem guia no exercício
        """
        status_line = self.get_status_line()
        
        return status_line.find('nao existe') == -1
    
    def verifica_se_remitiu(self):
        """ 
            retorna True se alterou com sucesso
            pode lançar uma exceção caso a visualização seja um insucesso
            captura e encerra o processo
        """
        status_line = self.get_status_line()
        
        return status_line.find('êxito') != -1
 
class GRDVA(Tela):
    """
        classe para fazer operacoes na GRDVA
    """
    def __init__(self, browser): # falta achar o tipo do driver
        """
        Args:
            browser
        """
        super().__init__(browser)
    
    def preenche_ex_guia(self, ex1: int, ex2: int, 
                         guia: int):
        """ preenche exercicio e guia """
        self.preenche_caixa_de_texto('exer1_grdva', ex1)
        self.preenche_caixa_de_texto('exer2_grdva', ex2)
        self.preenche_caixa_de_texto('guia', guia)
    
    def cancelar(self):
        """ clica no botao cancelar """
        self.click('cancelar_grdva')
        
    def gerar(self):
        """ clica no botao gerar """
        self.click('gerar_grdva')
        
    def ir_para_GRDVA(self): 
        self.ir_para_tela('GRDVA')
        
    def cancelar_novamente(self):
        """ 
            retorna True se o SIAM solicitou cancelar novamente
        """
                
        return self.tem_texto_na_status_line('Clique novamente')
    
    def cancelar_ok(self):
        """ 
            retorna True se cancelou ok
        """
                
        return self.tem_texto_na_status_line('EXITO')
    
class CNDEB(Tela):
    """
        classe para fazer operacoes na CNDEB
    """
    def __init__(self, browser): # falta achar o tipo do driver
        """
        Args:
            browser
        """
        super().__init__(browser)
        
    def ir_para_CNDEB(self): 
        self.ir_para_tela('CNDEB')
    
    def preenche_ex_guia(self, exercicio: int, guia: int):
        """ preenche exercicio e guia """
        self.preenche_caixa_de_texto('exercicio', exercicio)
        self.preenche_caixa_de_texto('guia', guia)
    
    def consultar(self):
        """ clica no botao consultar """
        self.click('consultar_botao')
        
class DEPO2(Tela):
    """
        classe para fazer operacoes na DEPO2
    """
    def __init__(self, browser): # falta achar o tipo do driver
        """
        Args:
            browser
        """
        super().__init__(browser)
        
    def ir_para_DEPO2(self): 
        self.ir_para_tela('DEPO2')
        
    def limpa_DEPO2(self):
        self.limpa_varios_elementos(['ii', 'dv', 'exercicio_DEPO2', 'guia'])
    
    def preenche_ex_guia(self, exercicio: int, guia: int):
        """ preenche exercicio e guia """
        self.preenche_caixa_de_texto('exercicio_DEPO2', exercicio)
        self.preenche_caixa_de_texto('guia', guia)
    
    def consultar(self):
        """ clica no botao consultar """
        self.click('consultar_botao')
        
    def get_deposito(self):
        """
        

        Returns
        -------
        Depósito disponível (float)

        """
        
        deposito = 0.00
        
        try:
            deposito = self.get_span_texto('deposito_disponivel').strip()
        
            if deposito == '':
                deposito = 0.00
            else: deposito = float(deposito.replace(',', '.', 1))
        except: pass
        
        return deposito
  
class DESIN(Tela):
    """
        classe para fazer operacoes na DESIN
    """    
    def __init__(self, browser): # falta achar o tipo do driver
        """
        Args:
            path do arquivo do driver
        """
        super().__init__(browser)
        
    
    def ir_para_DESIN(self): 
        self.ir_para_tela('DESIN')
    
    def consultar(self):
        """ clica no botao consultar """
        self.click('consultar_botao')
        
    def desinibir(self):
        """ clica no botao alterar """
        self.click('desinibir_botao')
        
    def preenche_ex_guia(self, exercicio: int, guia: int):
        """ preenche exercicio e guia """
        self.preenche_caixa_de_texto('exercicio', exercicio)
        self.preenche_caixa_de_texto('guia', guia)
        
    def verifica_se_desinibiu(self):
        """ 
            retorna True se alterou com sucesso
            pode lançar uma exceção caso a visualização seja um insucesso
            captura e encerra o processo
        """
        status_line = self.get_status_line()
                
        return status_line.find('êxito') != -1      
  
class VVDEC(Tela):
    """
        classe para fazer operacoes na DESIN
    """    
    def __init__(self, browser): # falta achar o tipo do driver
        """
        Args:
            path do arquivo do driver
        """
        super().__init__(browser)
        
    
    def ir_para_VVDEC(self): 
        self.ir_para_tela('VVDEC')
    
    def consultar(self):
        """ clica no botao consultar """
        self.click('consultar_vvdec')
        
    def incluir(self):
        """ clica no botao incluir """
        self.click('incluir_botao')
        
    def excluir(self):
        """ clica no botao excluir """
        self.click('excluir_vvdec')
        
    def preenche(self, apartirde: int, origem: int,
                 vvdec: int, vig_inicial: int, 
                 vig_final:int):
        """ preenche exercicio e guia """
        self.preenche_caixa_de_texto('apartirde', apartirde)
        self.preenche_caixa_de_texto('origem', origem)
        self.preenche_caixa_de_texto('vvdec', vvdec)
        self.preenche_caixa_de_texto('vig_inicial', vig_inicial)
        self.preenche_caixa_de_texto('vig_final', vig_final)
   
    def clicar_radio_Judicial(self):
        """ clica no botao consultar """
        self.click('judical')    
        
    def verifica_exito(self):
        """ 
            retorna True se alterou com sucesso
            pode lançar uma exceção caso a visualização seja um insucesso
            captura e encerra o processo
        """
        status_line = self.get_status_line()
                
        return status_line.find('êxito') != -1          
  
class Op_Sequencial(object):
    """ 
        superclasse Op_Sequencial
        define os atributos e métodos compartilhados por todas as
        operações sequenciais
        
        atributos:
            self.browser
            self.lista_dados_op: cada operacao passa um dict com os dados necessarios
            self.op_atual: informa a operacao atual
    """
    def __init__(self, browser, lista_dados_op:list, 
                 max_delay: int): # falta achar o tipo do driver
        """
        Args:
            browser
            lista_dados_op: lista de dicts; cada dict possui os dados necessarios
            a cada operação
            max_delay: tempo máximo de delay entre operações
            dir_download: diretorio de download sem o \ no fim
        """
        self.browser = browser
        self.lista_dados_op:list[dict] = lista_dados_op        
        self.op_atual = 0 
        self.max_delay = max_delay     
    
    def avancar_op(self):
        """ avanca à próxima operacao """
        self.op_atual += 1
    
    def recuar_op(self):
        """ recua à operacao anterior """
        self.op_atual -= 1
    
    def get_dados_op_atual(self) -> dict:
        """ returna o dict da posicao self.op_atual """
        return self.lista_dados_op[self.op_atual]
    
    def realizar_operacao(self):
        pass  

class FCIS1_Seq(Op_Sequencial):
    """
        subclasse de Op_Sequencial
        
        download de várias inscrições
    """
    def __init__(self, browser, lista_dados_op:list, 
                 max_delay: int,
                 ano_inicial: int,
                 ano_final: int,
                 url_dir: str): # falta achar o tipo do driver
        """
        Args:
            browser
            lista_dados_op: esta classe considera que o dict possui duas chaves:
                'ii' e 'dv'
        """
        super().__init__(browser, lista_dados_op, max_delay)
        
        self.ano_inicial = ano_inicial
        self.ano_final = ano_final
        self.url_dir = url_dir
    
    def realizar_operacao(self):
        """ realiza operacao """
        
        fcis1 = FCIS1(self.browser, self.url_dir)
        
        fcis1.ir_para_FCIS1()
        
        while(len(self.lista_dados_op)-1 >= self.op_atual):
            try:
                # limpa dados da FCIS1
                fcis1.clicar_botao_limpar()
                # pega os dados da operacao atual
                dados = self.get_dados_op_atual()
                # nesse caso, os dados são inscrição (ii) e dig verificador (dv)
                ii, dv = dados['ii'], dados['dv']
                
                fcis1.preenche_ii_e_dv(ii, dv)
                fcis1.preenche_ano_inicial(self.ano_inicial)
                fcis1.preenche_ano_final(self.ano_final)
                
                fcis1.clicar_visualizar()
                time.sleep(0.4)
                fcis1.clicar_ok()
                
                #url = fcis1.pega_url_pdf()
                
                #self.browser.get(url)
                fcis1.click_link('link')
                
                self.avancar_op()
                
                delay = self.max_delay*random.random()
                
                time.sleep(delay)
                
                print("Inscrição {}-{} ok!".format(ii, dv))
            except Exception as e:
                print(e)
                self.recuar_op() 
                # winsound.Beep(frequency=750, duration=3000)
                os.system(f'play -nq -t alsa synth {3} sine {440}')
                break
    
class IMGUI_Seq(Op_Sequencial):
    """
        subclasse de Op_Sequencial
        
        IMPRIMIR GUIAS EM SEQUENCIA
    """
    def __init__(self, browser, lista_dados_op:list, 
                 max_delay: int,
                 impressora: str): # falta achar o tipo do driver
        """
        Args:
            browser
            lista_dados_op: esta classe considera que o dict possui duas chaves:
                'ii' e 'dv'
        """
        super().__init__(browser, lista_dados_op, max_delay)
        
        self.impressora = impressora
    
    def realizar_operacao(self):
        """ realiza operacao """
        
        imgui = IMGUI(self.browser)
        
        imgui.ir_para_IMGUI()
        
        while(len(self.lista_dados_op)-1 >= self.op_atual):
            try:
                # limpa dados da FCIS1
                imgui.clicar_botao_limpar()
                # pega os dados da operacao atual
                dados = self.get_dados_op_atual()
                # nesse caso, os dados são inscrição (ii) e dig verificador (dv)
                ii, dv = dados['ii'], dados['dv']
                ano, guia = dados['ano'], dados['guia']
                
                imgui.preenche_ii_e_dv(ii, dv)
                imgui.preenche_ano(ano=ano)
                imgui.preenche_guia(guia=guia)
                imgui.preenche_impressora(impressora=self.impressora)
                
                imgui.clicar_imprimir()
                
                time.sleep(0.4)
                
                imgui.clicar_ok()
                
                self.avancar_op()
                
                delay = self.max_delay*random.random()
                
                time.sleep(delay)
                
                if not imgui.verifica_exito():
                    erro = imgui.get_status_line()
                    raise Exception(f'erro na operação: {erro}')

                print("Inscrição {}-{} ok!".format(ii, dv))
            except Exception as e:
                print(e)
                self.recuar_op() 
                # winsound.Beep(frequency=750, duration=3000)
                os.system(f'play -nq -t alsa synth {3} sine {440}')
                break    
    
class COMPI_ALT_Seq(Op_Sequencial):
    """
        subclasse de Op_Sequencial
        
        realiza alterações em sequência na COMPI
        
        a lista de dados deve conter obrigatoriamente ii e dv
        ademais, deve indicar os campos a alterar
    """
    def __init__(self, browser, lista_dados_op:list, 
                 max_delay: int, processo:str,
                 benfeitoria: str,
                 apagar_comp_mig=False): # falta achar o tipo do driver
        """
        Args:
            browser
            lista_dados_op: esta classe considera que o dict possui 
            duas chaves obrigattórias: 'ii' e 'dv'
            
            as demais são os campos a alterar
        """
        super().__init__(browser, lista_dados_op, max_delay)
        
         # separa os 4 componentes do processo
        lista_processo = processo.split('-')
        
        self.p1 = lista_processo[0]
        self.p2 = lista_processo[1]
        self.p3 = lista_processo[2]
        self.p4 = lista_processo[3]
        self.apagar_comp_mig = apagar_comp_mig     
        self.benfeitoria = benfeitoria
       
    def realizar_operacao(self):
        """ realiza operacao """
        
        compi = Compi(self.browser)
        
        compi.ir_para_COMPI()
        
        while(len(self.lista_dados_op)-1 >= self.op_atual):
            try:
                # limpa dados da FCIS1
                compi.clicar_botao_limpar()
                # pega os dados da operacao atual
                dados = self.get_dados_op_atual()
                # nesse caso, os dados são inscrição (ii) e dig verificador (dv)
                ii, dv = dados['ii'], dados['dv']
                
                compi.preenche_ii_e_dv(ii, dv)
                
                compi.consultar()
                
                dados.pop('ii')
                dados.pop('dv')
                
                compi.preenche_PA(self.p1, self.p2, self.p3, self.p4)
                
                try:
                    ri = dados['ri_opcoes']
                    
                    compi.alterar_ri(ri)
                    
                    dados.pop('ri_opcoes', None)
                except KeyError: pass
                
                # limpa os dados a alterar
                compi.limpa_varios_elementos(dados)
                
                # preenche os dados a alterar
                compi.preenche_varias_caixas(dados)
                
                if self.apagar_comp_mig:
                    compi.marcar_radio_apagar_comp_migrado()
                    
                if self.benfeitoria == 'sim':
                    compi.marcar_radio_benf_sim()
                elif self.benfeitoria == 'nao':
                    compi.marcar_radio_benf_nao()
                else: pass # None
                        
                compi.alterar()                       
                compi.clicar_ok()
                
                compi.verifica_se_alterou()
                
                self.avancar_op()
                
                delay = self.max_delay*random.random()
                
                time.sleep(delay)
                
                print("Inscrição {}-{} ok!".format(ii, dv))
            except Exception as e:
                print(e)
                self.recuar_op()                  
                # winsound.Beep(frequency=750, duration=3000)
                os.system(f'play -nq -t alsa synth {3} sine {440}')
                break
            
class Martelar_Seq(Op_Sequencial):
    """
        subclasse de Op_Sequencial
        
        realiza alterações em sequência na COMPI-RVLAN-GRGUI-FINAL
        
        a lista de dados deve conter obrigatoriamente ii e dv
        ademais, deve indicar os valores a martelar
    """
    def __init__(self, browser, lista_dados_op:list, 
                 max_delay: int,
                 processo:str,
                 inicio: int,
                 fim: int,
                 descontinuo: bool = False,
                 amortiza: bool = False,
                 martela_vv: bool = False,
                 martela_iptu: bool = True,
                 martela_tcl: bool = False,
                 martela_idx: [int] = []): # falta achar o tipo do driver
        """
        Args:
            browser
            lista_dados_op: esta classe considera que o dict possui 
            duas chaves obrigattórias: 'ii' e 'dv'
            
            as demais são os campos a martelar
            
            martela_idx indica o índice correto para martelar
                varia de 1 a 6
                1 -> corresponde ao exercício mais recente
                6 -> ao menos recente
                exemplo:
                    2015 a 2020
                    2020 -> 1
                    2019 -> 2
                    2018 -> 3
                    2017 -> 4
                    2016 -> 5
                    2015 -> 6
            
            descontinuo: serve para designar intervalos descontínuos. Neste caso,
            incluem sempre o exercício atual e um outro intervalo. É obrigatório
            martelar os dados do exercício atual.
            
            Ex: 2021 e 2015 a 2019
            
            No exemplo acima, self.inicio=2015 e self.fim=2019
        """
        super().__init__(browser, lista_dados_op, max_delay)
        
         # separa os 4 componentes do processo
        lista_processo = processo.split('-')
        
        self.p1 = lista_processo[0]
        self.p2 = lista_processo[1]
        self.p3 = lista_processo[2]
        self.p4 = lista_processo[3]
        self.inicio = inicio
        self.fim = fim
        self.descontinuo = descontinuo
        self.amortiza = amortiza
        self.martela_vv = martela_vv
        self.martela_iptu = martela_iptu
        self.martela_tcl = martela_tcl
        
        self.martela_idx = martela_idx
        
       
    def dados_martelar(self, dados: dict):
        """
            retorna listas com dados para martelar
            se não é para martelar, returna []
        """
        vvs = {}
        iptus = {}
        tcls = {}
        
        if self.martela_vv:
            for i in self.martela_idx:
                vvs[f'{i}'] = dados[f'vv{i}']
        
        if self.martela_iptu:
            for i in self.martela_idx:
                iptus[f'{i}'] = dados[f'iptu{i}']
                
        if self.martela_tcl:
            for i in self.martela_idx:
                tcls[f'{i}'] = dados[f'tcl{i}']
                
        return vvs, iptus, tcls
  
    def realizar_operacao(self):
        """ realiza operacao """
        
        compi = Compi(self.browser)
        rvlan = RVLAN(self.browser) 
        grgui = GRGUI(self.browser) 
        final = FINAL(self.browser) 
        
        while(len(self.lista_dados_op)-1 >= self.op_atual):
            try:
                compi.ir_para_COMPI()
                # limpa dados da COMPI
                compi.clicar_botao_limpar()
                # pega os dados da operacao atual
                dados = self.get_dados_op_atual()
                # nesse caso, os dados são inscrição (ii) e dig verificador (dv)
                ii, dv = dados['ii'], dados['dv']
                
                compi.preenche_ii_e_dv(ii, dv)                
                compi.consultar()                
                compi.preenche_PA(self.p1, self.p2, self.p3, self.p4)
                
                if self.descontinuo:
                    ano_atual = datetime.datetime.now().year
                    
                    compi.clicar_radio_sim()
                    compi.preenche_vigencia(ano_atual, ano_atual)    
                    compi.alterar()                       
                    compi.clicar_ok()
                    
                    compi.ir_para_COMPI()
                    compi.clicar_botao_limpar()
                    
                    compi.preenche_ii_e_dv(ii, dv)                
                    compi.consultar()                
                    compi.preenche_PA(self.p1, self.p2, self.p3, self.p4)
                
                compi.clicar_radio_sim()
                compi.preenche_vigencia(self.inicio, self.fim)    
                compi.alterar()                       
                compi.clicar_ok()
                 
                num_anos = len(self.martela_idx)
                #num_anos = self.fim-self.inicio+1
                rvlan.clica_ckecks(num_anos)
                
                vvs, iptus, tcls = \
                    self.dados_martelar(dados)
                
                rvlan.martela_vv(vvs)
                rvlan.martela_iptu(iptus)
                rvlan.martela_tcl(tcls)
                 
                rvlan.alterar()
                rvlan.clicar_ok()
                    
                rvlan.incluir_e_compor()
                rvlan.clicar_ok()
                
                grgui.incluir()
                grgui.clicar_ok()                
                
                if self.amortiza != 'nao':
                    total_guia = ''
                    if self.amortiza == 'total': 
                        total_guia = final.total_guia()
                    elif self.amortiza == 'parcial':
                        total = float(final.total_guia().replace(',', '.'))
                        
                        parcial = float(dados['amortiza_parcial'].replace(',', '.'))
                        parcial = round(parcial)
                        
                        if parcial < round(total*0.93):                        
                            total_guia = str(dados['amortiza_parcial'])
                        else: total_guia = final.total_guia()
                    else: raise Exception('Opção incorreta')
                    final.preenche_valor_quitado(total_guia)
                    final.alterar()
                    final.clicar_ok()                    
                input()    
                # o check imprimir guias está 'checado'
                # é preciso clicar para não imprimir
                final.clica_imprimir_guias()
                final.efetivar()
                final.clicar_ok()
                
                if not final.foi_sucesso():
                    raise Exception('erro na operação!')
                
                self.avancar_op()
                
                delay = self.max_delay*random.random()
                
                time.sleep(delay)
                
                print("Inscrição {}-{} ok!".format(ii, dv))
            except Exception as e:
                print(e)
                self.recuar_op()                  
                # winsound.Beep(frequency=750, duration=3000)
                os.system(f'play -nq -t alsa synth {3} sine {440}')
                break
  
class Simulacao(Op_Sequencial):
    """
        subclasse de Op_Sequencial
        
        simula VV, IPTU e TCL
        
        a lista de dados deve conter obrigatoriamente ii e dv
        ademais, deve indicar os valores a martelar
    """
    def __init__(self, browser, lista_dados_op:list, 
                 max_delay: int,
                 processo:str,
                 inicio: int,
                 fim: int
                 ): # falta achar o tipo do driver
        """
        Args:
            browser
            lista_dados_op: esta classe considera que o dict possui 
            duas chaves obrigattórias: 'ii' e 'dv'
            
            as demais são os campos a martelar
        """
        super().__init__(browser, lista_dados_op, max_delay)
        
         # separa os 4 componentes do processo
        lista_processo = processo.split('-')
        
        self.p1 = lista_processo[0]
        self.p2 = lista_processo[1]
        self.p3 = lista_processo[2]
        self.p4 = lista_processo[3]
        self.inicio = inicio
        self.fim = fim
       
    def realizar_operacao(self):
        """ realiza operacao """
        
        compi = Compi(self.browser)
        rvlan = RVLAN(self.browser) 
        simulacoes = []
        
        while(len(self.lista_dados_op)-1 >= self.op_atual):
            try:
                compi.ir_para_COMPI()
                # limpa dados da COMPI
                compi.clicar_botao_limpar()
                # pega os dados da operacao atual
                dados = self.get_dados_op_atual()
                # nesse caso, os dados são inscrição (ii) e dig verificador (dv)
                ii, dv = dados['ii'], dados['dv']
                
                compi.preenche_ii_e_dv(ii, dv)
                
                compi.consultar()
                
                compi.preenche_PA(self.p1, self.p2, self.p3, self.p4)
                
                compi.clicar_radio_sim()
                compi.preenche_vigencia(self.inicio, self.fim)    
                compi.alterar()                       
                compi.clicar_ok()
                                
                simulacao = \
                    rvlan.pega_vv_iptu_tcl(ii, 
                                           dv, 
                                           self.inicio, 
                                           self.fim)
                
                simulacoes.append(simulacao)
               
                self.avancar_op()
                
                delay = self.max_delay*random.random()
                
                time.sleep(delay)
                
                print("Inscrição {}-{} ok!".format(ii, dv))
            except Exception as e:
                print(e)
                self.recuar_op()                  
                # winsound.Beep(frequency=750, duration=3000)
                os.system(f'play -nq -t alsa synth {3} sine {440}')
                break
        
        return simulacoes
    
class Rev_Lanc_Seq(Op_Sequencial):
    """
        subclasse de Op_Sequencial
        
        rever lançamentos para uma lista de inscricoes
    """
    def __init__(self, browser, lista_dados_op:list, 
                 max_delay: int,
                 processo:str,
                 calcula: bool,
                 ano_inicio: int,
                 ano_fim: int): # falta achar o tipo do driver
        """
        Args:
            browser
            lista_dados_op: esta classe considera que o dict possui duas chaves:
                'ii' e 'dv'
            processo: 99-99-999999-9999
            calcula: se True, calcula; caso contrário, não calcula
            ano_inicio e ano_fim são autoexplicáveis
        """
        super().__init__(browser, lista_dados_op, max_delay)
        
        # separa os 4 componentes do processo
        lista_processo = processo.split('-')
        
        self.p1 = lista_processo[0]
        self.p2 = lista_processo[1]
        self.p3 = lista_processo[2]
        self.p4 = lista_processo[3]
        
        self.calcula = calcula
        self.ano_inicio = ano_inicio
        self.ano_fim = ano_fim
    
    def realizar_operacao(self):
        """ realiza operacao """
        
        calc_seq = Calc_Seq(self.browser)
        calc_seq.ir_para_calc_seq()
        
        while(len(self.lista_dados_op)-1 >= self.op_atual):
            try:
                # pega os dados da operacao atual
                dados = self.get_dados_op_atual()
                # nesse caso, os dados são inscrição (ii) e dig verificador (dv)
                ii, dv = dados['ii'], dados['dv']
                
                calc_seq.clicar_botao_limpar()
                calc_seq.preenche_ii_e_dv(ii, dv)
                calc_seq.preenche_PA(self.p1, self.p2, self.p3, self.p4)
                calc_seq.preenche_vigencia(self.ano_inicio, self.ano_fim)
                
                if not self.calcula:
                    calc_seq.clicar_radio_NAO()
                                
                calc_seq.processar()
                calc_seq.clicar_ok()
                
                if not calc_seq.operacao_ok():
                    raise Exception('operacao com erro')
                
                self.avancar_op()
                
                delay = self.max_delay*random.random()
                
                time.sleep(delay)
                
                print("Inscrição {}-{} ok!".format(ii, dv))               
            except Exception as e:
                print(e)
                self.recuar_op() 
                os.system(f'play -nq -t alsa synth {3} sine {440}')
                break  
        
        os.system('play -nq -t alsa synth 2 sine 200')
    
class REAGI_Seq(Op_Sequencial):
    """
        subclasse de Op_Sequencial
        
        reativa guia de uma sequencia de inscrições
    """
    def __init__(self, browser, lista_dados_op:list, 
                 max_delay: int,
                 processo:str,
                 exercicio: int,
                 guia: int): # falta achar o tipo do driver
        """
        Args:
            browser
            lista_dados_op: esta classe considera que o dict possui duas chaves:
                'ii' e 'dv'
            processo: 99-99-999999-9999
           exercicio, guia a reativar
        """
        super().__init__(browser, lista_dados_op, max_delay)
        
        # separa os 4 componentes do processo
        lista_processo = processo.split('-')
        
        self.p1 = lista_processo[0]
        self.p2 = lista_processo[1]
        self.p3 = lista_processo[2]
        self.p4 = lista_processo[3]
        
        self.exercicio = exercicio
        self.guia = guia
    
    def realizar_operacao(self):
        """ realiza operacao """
        
        reagi = REAGI(self.browser)
        
        reagi.ir_para_REAGI()
        
        while(len(self.lista_dados_op)-1 >= self.op_atual):
            try:
                # pega os dados da operacao atual
                dados = self.get_dados_op_atual()
                # nesse caso, os dados são inscrição (ii) e dig verificador (dv)
                ii, dv = dados['ii'], dados['dv']
                
                reagi.clicar_botao_limpar()
                reagi.preenche_ii_e_dv(ii, dv)
                reagi.preenche_PA(self.p1, self.p2, self.p3, self.p4)
                reagi.preenche_ex_guia(self.exercicio, self.guia)
                
                reagi.consultar()
                time.sleep(0.1)
                reagi.reativar()
                time.sleep(0.4)
                reagi.clicar_ok()
                
                if not reagi.verifica_se_reativou():
                    raise Exception('operacao com erro')
                
                self.avancar_op()
                
                delay = self.max_delay*random.random()
                
                print("Inscrição {}-{} ok! Delay de {:.2f}s.".format(ii, dv, delay)) 
                
                time.sleep(delay)
            except Exception as e:
                print(e)
                self.recuar_op() 
                # winsound.Beep(frequency=750, duration=3000)
                os.system(f'play -nq -t alsa synth {3} sine {440}')
                break   

class Canc_Seq(Op_Sequencial):
    """
        subclasse de Op_Sequencial
        
        cancelar lançamentos em grupo
    """
    def __init__(self, browser, lista_dados_op:list, 
                 max_delay: int,
                 processo:str,
                 ano_inicio: int,
                 ano_fim: int,
                 guia1: int,
                 guia2: int): # falta achar o tipo do driver
        """
        Args:
            browser
            lista_dados_op: esta classe considera que o dict possui duas chaves:
                'ii' e 'dv'
            processo: 99-99-999999-9999
            ano_inicio e ano_fim são autoexplicáveis
            guia1 e guia2 também
        """
        super().__init__(browser, lista_dados_op, max_delay)
        
        # separa os 4 componentes do processo
        lista_processo = processo.split('-')
        
        self.p1 = lista_processo[0]
        self.p2 = lista_processo[1]
        self.p3 = lista_processo[2]
        self.p4 = lista_processo[3]
        
        self.ano_inicio = ano_inicio
        self.ano_fim = ano_fim
        self.guia1 = guia1
        self.guia2 = guia2
    
    def realizar_operacao(self):
        """ realiza operacao """
        
        canc_seq = Canc_Grupo(self.browser)
        canc_seq.ir_para_canc_seq()
        
        while(len(self.lista_dados_op)-1 >= self.op_atual):
            try:
                # pega os dados da operacao atual
                dados = self.get_dados_op_atual()
                # nesse caso, os dados são inscrição (ii) e dig verificador (dv)
                ii, dv = dados['ii'], dados['dv']
                
                # tive que fazer uma função específica porque
                # o botão limpar não funciona direito nesta tela
                canc_seq.limpar_form()
                
                canc_seq.preenche_ii_e_dv(ii, dv)
                canc_seq.preenche_PA(self.p1, self.p2, self.p3, self.p4)
                canc_seq.preenche_exercicios(self.ano_inicio, self.ano_fim)
                canc_seq.preenche_guias(self.guia1, self.guia2)
                # desmarcar a opção de imprimir
                              
                canc_seq.processar()
                canc_seq.clicar_ok()
                
                if not canc_seq.operacao_ok():
                    raise Exception('operacao com erro')
                
                self.avancar_op()
                
                delay = self.max_delay*random.random()
                
                time.sleep(delay)
                
                print("Inscrição {}-{} ok!".format(ii, dv))               
            except Exception as e:
                print(e)
                self.recuar_op() 
                os.system(f'play -nq -t alsa synth {3} sine {440}')
                return
        
        os.system('play -nq -t alsa synth 2 sine 200')

class CVQUI_Seq(Op_Sequencial):
    """
        subclasse de Op_Sequencial
        
        cancelar lançamentos em grupo
    """
    def __init__(self, browser, lista_dados_op:list, 
                 max_delay: int,
                 exercicio: int): # falta achar o tipo do driver
        """
        Args:
            browser
            lista_dados_op: esta classe considera que o dict possui duas chaves:
                'ii' e 'dv'
            processo: 99-99-999999-9999
            ano_inicio e ano_fim são autoexplicáveis
            guia1 e guia2 também
        """
        super().__init__(browser, lista_dados_op, max_delay)
        
        self.exercicio = exercicio
    
    def realizar_operacao(self):
        """ realiza operacao """
        
        cvqui = CVQUI(self.browser)
        
        try:
            cvqui.ir_para_CVQUI()
        except Exception as e:
            print(e)
            self.recuar_op() 
            os.system(f'play -nq -t alsa synth {3} sine {440}')
            return        
        
        # guarda dicts com informações sobre as guias
        # {'g_0_sproc': 'I', 'g_0_scob': 'S', 'g_0_valor': 236.0, 'g_0_quitado': '0.0',
        #  'g_0_sproc': 'I', 'g_1_scob': 'S', 'g_1_valor': 77.0, 'g_1_quitado': '20.0',
        #   ...}
        info_guias = []
        
        erro = False
        
        while(len(self.lista_dados_op)-1 >= self.op_atual):
            try:
                # pega os dados da operacao atual
                dados = self.get_dados_op_atual()
                # nesse caso, os dados são inscrição (ii) e dig verificador (dv)
                ii, dv = dados['ii'], dados['dv']
                
                cvqui.clicar_botao_limpar()
                cvqui.preenche_ii_e_dv(ii, dv)                
                cvqui.preenche_ex_guia(exercicio=self.exercicio,
                                       guia=0)
                cvqui.consultar()
                
                if not cvqui.tem_guia_no_exercicio():
                    raise Exception('Nao tem guia para o exercicio')
                
                info_guias.append(cvqui.get_info_guias(ii=ii,
                                                       dv=dv))
                                
                self.avancar_op()
                
                delay = self.max_delay*random.random()
                
                time.sleep(delay)
                
                print("Inscrição {}-{} ok!".format(ii, dv))               
            except Exception as e:
                print(e)
                self.recuar_op() 
                os.system(f'play -nq -t alsa synth {3} sine {440}')
                erro = True
                break
        
        if not erro:
            os.system('play -nq -t alsa synth 2 sine 200')
        
        return DataFrame(data=info_guias)
 
class DEPO2_Get_Depositos_Seq(Op_Sequencial):
    """
        subclasse de Op_Sequencial
        
        retorna deposito disponivel
    """
    def __init__(self, browser, lista_dados_op:list, 
                 max_delay: int,
                 exercicio: int,
                 guia: int): # falta achar o tipo do driver
        """
        Args:
            browser
            lista_dados_op: esta classe considera que o dict possui duas chaves:
                'ii' e 'dv'
            processo: 99-99-999999-9999
            ano_inicio e ano_fim são autoexplicáveis
            guia1 e guia2 também
        """
        super().__init__(browser, lista_dados_op, max_delay)
        
        self.exercicio = exercicio
        self.guia = guia
    
    def realizar_operacao(self):
        """ realiza operacao """
        
        depo2 = DEPO2(self.browser)
        
        try:
            depo2.ir_para_DEPO2()
        except Exception as e:
            print(e)
            self.recuar_op() 
            os.system(f'play -nq -t alsa synth {3} sine {440}')
            return        
        
        # guarda dicts com informações sobre os depositos
        # {'ii': '1234567', 'dv': '8', 'deposito': 1234567.00}
        info_depositos = []
        
        erro = False
        
        while(len(self.lista_dados_op)-1 >= self.op_atual):
            try:
                # pega os dados da operacao atual
                dados = self.get_dados_op_atual()
                # nesse caso, os dados são inscrição (ii) e dig verificador (dv)
                ii, dv = dados['ii'], dados['dv']
                
                depo2.limpa_DEPO2()
                depo2.preenche_ii_e_dv(ii, dv)                
                depo2.preenche_ex_guia(exercicio=self.exercicio,
                                       guia=self.guia)
                depo2.consultar()
                
                deposito = {'ii': ii, 'dv': dv, 
                            'deposito':depo2.get_deposito()}
                
                info_depositos.append(deposito)
                                
                self.avancar_op()
                
                delay = self.max_delay*random.random()
                
                time.sleep(delay)
                
                print("Inscrição {}-{} ok!".format(ii, dv))               
            except Exception as e:
                print(e)
                self.recuar_op() 
                os.system(f'play -nq -t alsa synth {3} sine {440}')
                erro = True
                break
        
        if not erro:
            os.system('play -nq -t alsa synth 2 sine 200')
        
        return DataFrame(data=info_depositos)    
 
class DEPO2_Copia_Tela_Seq(Op_Sequencial):
    """
        subclasse de Op_Sequencial
        
        copiar tela CNDEB
    """
    def __init__(self, browser, lista_dados_op:list, 
                 max_delay: int,
                 exercicio: int,
                 guia: int): # falta achar o tipo do driver
        """
        Args:
            browser
            lista_dados_op: esta classe considera que o dict possui duas chaves:
                'ii' e 'dv'
            processo: 99-99-999999-9999
            ano_inicio e ano_fim são autoexplicáveis
            guia1 e guia2 também
        """
        super().__init__(browser, lista_dados_op, max_delay)
        
        self.exercicio = exercicio
        self.guia = guia
    
    def print_idx(self, idx: int):
        tam = len(self.lista_dados_op)
        num_zeros = len(str(tam))
        num_digits = len(str(idx))
        
        return f'{"0"*(num_zeros-num_digits)}{idx}'        
    
    def realizar_operacao(self):
        """ realiza operacao """
        
        depo2 = DEPO2(self.browser)
        
        depo2.ir_para_DEPO2()
        
        idx = 0
        
        while(len(self.lista_dados_op)-1 >= self.op_atual):
            try:
                # pega os dados da operacao atual
                dados = self.get_dados_op_atual()
                # nesse caso, os dados são inscrição (ii) e dig verificador (dv)
                ii, dv = dados['ii'], dados['dv']
                
                depo2.limpa_DEPO2()
                depo2.preenche_ii_e_dv(ii, dv)                
                depo2.preenche_ex_guia(exercicio=self.exercicio,
                                       guia=self.guia)
                
                depo2.consultar()
                
                depo2.screen_shot(
                    f'saida/{self.print_idx(idx)}_{ii}_{dv}_{self.exercicio}_guia_{self.guia}.png')
                
                self.avancar_op()
                
                delay = self.max_delay*random.random()
                
                time.sleep(delay)
                
                print("Inscrição {}-{} ok!".format(ii, dv))   
                
                idx += 1
            except Exception as e:
                print(e)
                self.recuar_op() 
                os.system(f'play -nq -t alsa synth {3} sine {440}')
                return
        
        os.system('play -nq -t alsa synth 2 sine 200')    
 
class REMIT_Seq(Op_Sequencial):
    """
        subclasse de Op_Sequencial
        
        cancelar lançamentos em grupo
    """
    def __init__(self, browser, lista_dados_op:list, 
                 max_delay: int,
                 processo: str,
                 exercicio: int,
                 guia: int,
                 num_exs: int): # falta achar o tipo do driver
        """
        Args:
            browser
            lista_dados_op: esta classe considera que o dict possui duas chaves:
                'ii' e 'dv'
            processo: 99-99-999999-9999
            ano_inicio e ano_fim são autoexplicáveis
            guia1 e guia2 também
        """
        super().__init__(browser, lista_dados_op, max_delay)
        
        self.num_exs = num_exs
        self.guia = guia
        self.exercicio = exercicio
        
        # separa os 4 componentes do processo
        lista_processo = processo.split('-')
        
        self.p1 = lista_processo[0]
        self.p2 = lista_processo[1]
        self.p3 = lista_processo[2]
        self.p4 = lista_processo[3]
        
    
    def realizar_operacao(self):
        """ realiza operacao """
        
        remit = REMIT(self.browser)
        
        remit.ir_para_REMIT()
                
        while(len(self.lista_dados_op)-1 >= self.op_atual):
            try:
                # pega os dados da operacao atual
                dados = self.get_dados_op_atual()
                # nesse caso, os dados são inscrição (ii) e dig verificador (dv)
                ii, dv = dados['ii'], dados['dv']
                
                remit.clicar_botao_limpar()
                remit.preenche_ii_e_dv(ii, dv)                
                remit.preenche_ex_guia(exercicio=self.exercicio,
                                       guia=self.guia)
                remit.preenche_PA(self.p1, self.p2, self.p3, self.p4)
                remit.consultar()
                
                if not remit.tem_guia_no_exercicio():
                    raise Exception("Não tem guia no exercício")
                
                remit.marcar_checks(num_exs=self.num_exs)
                
                remit.processar()
                
                remit.clicar_ok()
                
                if not remit.verifica_se_remitiu():
                    raise Exception('Erro ao remitir') 
                
                self.avancar_op()
                
                delay = self.max_delay*random.random()
                
                time.sleep(delay)
                
                print("Inscrição {}-{} ok!".format(ii, dv))               
            except Exception as e:
                print(e)
                self.recuar_op() 
                os.system(f'play -nq -t alsa synth {3} sine {440}')
                return
        
        os.system('play -nq -t alsa synth 2 sine 200')
        
class GRDVA_Seq(Op_Sequencial):
    """
        subclasse de Op_Sequencial
        
        cancelar lançamentos em grupo
    """
    def __init__(self, browser, lista_dados_op:list, 
                 max_delay: int,
                 processo:str,
                 ano_inicio: int,
                 ano_fim: int,
                 guia: int,
                 operacao='cancelar'): # falta achar o tipo do driver
        """
        Args:
            browser
            lista_dados_op: esta classe considera que o dict possui duas chaves:
                'ii' e 'dv'
            processo: 99-99-999999-9999
            ano_inicio e ano_fim são autoexplicáveis
            guia1 e guia2 também
        """
        super().__init__(browser, lista_dados_op, max_delay)
        
        # separa os 4 componentes do processo
        lista_processo = processo.split('-')
        
        self.p1 = lista_processo[0]
        self.p2 = lista_processo[1]
        self.p3 = lista_processo[2]
        self.p4 = lista_processo[3]
        
        self.ano_inicio = ano_inicio
        self.ano_fim = ano_fim
        self.guia = guia
        self.operacao = operacao
    
    def realizar_operacao(self):
        """ realiza operacao """
        
        grdva = GRDVA(self.browser)
        grdva.ir_para_GRDVA()
        
        while(len(self.lista_dados_op)-1 >= self.op_atual):
            try:
                # pega os dados da operacao atual
                dados = self.get_dados_op_atual()
                # nesse caso, os dados são inscrição (ii) e dig verificador (dv)
                ii, dv = dados['ii'], dados['dv']
                
                grdva.clicar_botao_limpar()
                
                grdva.preenche_ii_e_dv(ii, dv)
                grdva.preenche_PA(self.p1, self.p2, self.p3, self.p4)
                grdva.preenche_ex_guia(ex1=self.ano_inicio, 
                                       ex2=self.ano_fim, 
                                       guia=self.guia)
                
                
                if self.operacao == 'cancelar':
                    grdva.cancelar()
                else: grdva.gerar()                
                
                grdva.clicar_ok()
                
                if not grdva.cancelar_novamente():
                    raise Exception('operacao com erro')
                    
                if self.operacao == 'cancelar':
                    grdva.cancelar()
                else: grdva.gerar()
                
                grdva.clicar_ok()
                    
                if not grdva.cancelar_ok():
                    raise Exception('operacao com erro')
                
                self.avancar_op()
                
                delay = self.max_delay*random.random()
                
                time.sleep(delay)
                
                print("Inscrição {}-{} ok!".format(ii, dv))               
            except Exception as e:
                print(e)
                self.recuar_op() 
                os.system(f'play -nq -t alsa synth {3} sine {440}')
                return
        
        os.system('play -nq -t alsa synth 2 sine 200')
 
class CNDEB_Seq(Op_Sequencial):
    """
        subclasse de Op_Sequencial
        
        copiar tela CNDEB
    """
    def __init__(self, browser, lista_dados_op:list, 
                 max_delay: int,
                 ano_inicio: int,
                 ano_fim: int,
                 num_vias: int,
                 guia: int): # falta achar o tipo do driver
        """
        Args:
            browser
            lista_dados_op: esta classe considera que o dict possui duas chaves:
                'ii' e 'dv'
            processo: 99-99-999999-9999
            ano_inicio e ano_fim são autoexplicáveis
            guia1 e guia2 também
        """
        super().__init__(browser, lista_dados_op, max_delay)
        
        self.ano_inicio = ano_inicio
        self.ano_fim = ano_fim
        self.num_vias = num_vias
        self.guia = guia
    
    def print_idx(self, idx: int):
        tam = len(self.lista_dados_op)*(self.ano_fim-self.ano_inicio+1)
        num_zeros = len(str(tam))
        num_digits = len(str(idx))
        
        return f'{"0"*(num_zeros-num_digits)}{idx}'        
    
    def realizar_operacao(self):
        """ realiza operacao """
        
        cndeb = CNDEB(self.browser)
        
        cndeb.ir_para_CNDEB()
        
        idx = 0
        
        while(len(self.lista_dados_op)-1 >= self.op_atual):
            try:
                # pega os dados da operacao atual
                dados = self.get_dados_op_atual()
                # nesse caso, os dados são inscrição (ii) e dig verificador (dv)
                ii, dv = dados['ii'], dados['dv']
                
                for ex in range(self.ano_inicio, self.ano_fim+1):
                    cndeb.clicar_botao_limpar()
                    cndeb.preenche_ii_e_dv(ii, dv)                
                    cndeb.preenche_ex_guia(exercicio=ex,
                                           guia=self.guia)
                    
                    for _ in range(1, self.num_vias+1):
                        cndeb.consultar()
                    
                    cndeb.screen_shot(
                        f'saida/{self.print_idx(idx)}_{ii}_{dv}_{ex}_guia_{self.guia}.png')
                
                self.avancar_op()
                
                delay = self.max_delay*random.random()
                
                time.sleep(delay)
                
                print("Inscrição {}-{} ok!".format(ii, dv))   
                
                idx += 1
            except Exception as e:
                print(e)
                self.recuar_op() 
                os.system(f'play -nq -t alsa synth {3} sine {440}')
                return
        
        os.system('play -nq -t alsa synth 2 sine 200')
 
class DESIN_Seq(Op_Sequencial):
    """
        subclasse de Op_Sequencial
        
        reativa guia de uma sequencia de inscrições
    """
    def __init__(self, browser, lista_dados_op:list, 
                 max_delay: int,
                 processo:str,
                 exercicio: int,
                 guia: int): # falta achar o tipo do driver
        """
        Args:
            browser
            lista_dados_op: esta classe considera que o dict possui duas chaves:
                'ii' e 'dv'
            processo: 99-99-999999-9999
           exercicio, guia a reativar
        """
        super().__init__(browser, lista_dados_op, max_delay)
        
        # separa os 4 componentes do processo
        lista_processo = processo.split('-')
        
        self.p1 = lista_processo[0]
        self.p2 = lista_processo[1]
        self.p3 = lista_processo[2]
        self.p4 = lista_processo[3]
        
        self.exercicio = exercicio
        self.guia = guia
    
    def realizar_operacao(self):
        """ realiza operacao """
        
        desin = DESIN(self.browser)
        
        desin.ir_para_DESIN()
        
        while(len(self.lista_dados_op)-1 >= self.op_atual):
            try:
                # pega os dados da operacao atual
                dados = self.get_dados_op_atual()
                # nesse caso, os dados são inscrição (ii) e dig verificador (dv)
                ii, dv = dados['ii'], dados['dv']
                
                desin.clicar_botao_limpar()
                desin.preenche_ii_e_dv(ii, dv)
                desin.preenche_PA(self.p1, self.p2, self.p3, self.p4)
                desin.preenche_ex_guia(self.exercicio, self.guia)
                
                desin.consultar()
                time.sleep(0.1)
                desin.desinibir()
                time.sleep(0.1)
                desin.clicar_ok()
                
                if not desin.verifica_se_desinibiu():
                    raise Exception('operacao com erro')
                
                self.avancar_op()
                
                delay = self.max_delay*random.random()
                
                print("Inscrição {}-{} ok! Delay de {:.2f}s.".format(ii, dv, delay)) 
                
                time.sleep(delay)
            except Exception as e:
                print(e)
                self.recuar_op() 
                # winsound.Beep(frequency=750, duration=3000)
                os.system(f'play -nq -t alsa synth {3} sine {440}')
                break      
 
class Compi_Inspecao(Op_Sequencial):
    """ 
        subclasse de Op_Sequencial
        
        consulta várias inscrições na COMPI e retorna elementos
    """
    def __init__(self, browser, lista_dados_op:list,
                 lista_elementos: [str],
                 max_delay: float): # falta achar o tipo do driver
        """
        Args:
            browser
            lista_dados_op: esta classe considera que o dict possui duas chaves:
                'ii' e 'dv'
        """
        super().__init__(browser, lista_dados_op, max_delay)
        self. lista_elementos = lista_elementos
    
    def realizar_operacao(self) -> DataFrame:
        """ realiza operacao """
        
        compi = Compi(self.browser)
        
        compi.ir_para_COMPI()
        
        # dict para construir DatFrame
        dict_elementos: dict = {}
        # iniciar dict com listas vazias
        for elemento in ['ii', 'dv']+self.lista_elementos:
            dict_elementos[elemento] = []
            
        # como o logradouro é um span, precisei criar uesta variável
        # pegar texto de span é diferente de edit (text input)
        # o mesmo para compmigrado
           
        spans = { 'logradouro' : False, 'compmigrado' : False }
        
        for key in spans.keys():
            if key in self.lista_elementos:
                self.lista_elementos.remove(key)
                spans[key] = True            
        
        while(len(self.lista_dados_op)-1 >= self.op_atual):
            try:
                # limpa dados da COMPI
                compi.clicar_botao_limpar()
                # pega os dados da operacao atual
                dados = self.get_dados_op_atual()
                # nesse caso, os dados são inscrição (ii) e dig verificador (dv)
                ii, dv = dados['ii'], dados['dv']
                
                dict_elementos['ii'].append(ii)
                dict_elementos['dv'].append(dv)
                
                compi.preenche_ii_e_dv(ii, dv)
                
                compi.consultar()
                
                for key in spans.keys():
                    if spans[key]:
                        dict_elementos[key].append(
                            compi.get_span_texto(key))
                
                lista_textos = compi.get_varios_textos(self.lista_elementos)
                
                for elem, texto in zip(self.lista_elementos, lista_textos):
                    dict_elementos[elem].append(texto)                   
                
                self.avancar_op()
                
                delay = self.max_delay*random.random()
                
                print(f'Inscrição {ii}-{dv} ok! Delay de {delay:.2f}s.') 
                
                time.sleep(delay)   
            except Exception as e:
                print(e)
                self.recuar_op() 
                break
            
        return DataFrame(data=dict_elementos)

class CVDEP_Apropriar_Seq(Op_Sequencial):
    """
        subclasse de Op_Sequencial
        
        Apropria o depósito em sequencia
    """
    def __init__(self, browser, lista_dados_op:list, 
                 max_delay: int,
                 processo:str,
                 exercicio: int,
                 guia: int): # falta achar o tipo do driver
        """
        Args:
            browser
            lista_dados_op: esta classe considera que o dict possui 
            as chaves 'ii' e 'dv'
            
            as demais são ignoradas
        """
        super().__init__(browser, lista_dados_op, max_delay)
        
        self.exercicio = exercicio
        self.guia = guia
        
         # separa os 4 componentes do processo
        lista_processo = processo.split('-')
        
        self.p1 = lista_processo[0]
        self.p2 = lista_processo[1]
        self.p3 = lista_processo[2]
        self.p4 = lista_processo[3]
        
       
    def realizar_operacao(self):
        """ realiza operacao """
        
        cvdep = CVDEP(self.browser)
        
        cvdep.ir_para_CVDEP()
        
        while(len(self.lista_dados_op)-1 >= self.op_atual):
            try:
                # limpa dados d tela
                cvdep.clicar_botao_limpar()
                # pega os dados da operacao atual
                dados = self.get_dados_op_atual()
                
                # nesse caso, os dados são inscrição (ii) e dig verificador (dv)
                ii, dv = dados['ii'], dados['dv']
                
                cvdep.preenche_ii_e_dv(ii, dv)
                cvdep.preenche_ex_guia(exercicio=self.exercicio, guia=self.guia)
                
                cvdep.consultar()
                
                cvdep.preenche_PA(self.p1, self.p2, self.p3, self.p4)
                
                cvdep.apropriar()
                cvdep.clicar_ok()
                
                cvdep.verifica_se_apropriou()
                
                self.avancar_op()
                
                delay = self.max_delay*random.random()
                
                time.sleep(delay)
                
                print("Inscrição {}-{} ok!".format(ii, dv))
            except Exception as e:
                print(e)
                self.recuar_op()                  
                # winsound.Beep(frequency=750, duration=3000)
                os.system(f'play -nq -t alsa synth {3} sine {440}')
                break
            
class EA2_Finalizar_Seq(Op_Sequencial):
    """
        subclasse de Op_Sequencial
        
        Finaliza guia em sequencia
    """
    def __init__(self, browser, lista_dados_op:list, 
                 max_delay: int,
                 processo:str,
                 exercicio: int,
                 guia: int): # falta achar o tipo do driver
        """
        Args:
            browser
            lista_dados_op: esta classe considera que o dict possui 
            as chaves 'ii' e 'dv'
            
            as demais são ignoradas
        """
        super().__init__(browser, lista_dados_op, max_delay)
        
        self.exercicio = exercicio
        self.guia = guia
        
         # separa os 4 componentes do processo
        lista_processo = processo.split('-')
        
        self.p1 = lista_processo[0]
        self.p2 = lista_processo[1]
        self.p3 = lista_processo[2]
        self.p4 = lista_processo[3]
        
       
    def realizar_operacao(self):
        """ realiza operacao """
        
        ea2 = EA2(self.browser)
        
        ea2.ir_para_EA2()
        
        while(len(self.lista_dados_op)-1 >= self.op_atual):
            try:
                # limpa dados d tela
                ea2.clicar_botao_limpar()
                # pega os dados da operacao atual
                dados = self.get_dados_op_atual()
                
                # nesse caso, os dados são inscrição (ii) e dig verificador (dv)
                ii, dv = dados['ii'], dados['dv']
                
                ea2.preenche_ii_e_dv(ii, dv)
                ea2.preenche_ex_guia(exercicio=self.exercicio, guia=self.guia)
                
                ea2.consultar()                
                ea2.preenche_PA(self.p1, self.p2, self.p3, self.p4)
                ea2.desmarcar_radio_imprime()                
                ea2.incluir()
                ea2.clicar_ok()
                
                ea2.verifica_se_incluiu()
                
                self.avancar_op()
                
                delay = self.max_delay*random.random()
                
                time.sleep(delay)
                
                print("Inscrição {}-{} ok!".format(ii, dv))
            except Exception as e:
                print(e)
                self.recuar_op()                  
                # winsound.Beep(frequency=750, duration=3000)
                os.system(f'play -nq -t alsa synth {3} sine {440}')
                break

class VVDEC_Seq(Op_Sequencial):
    """
        subclasse de Op_Sequencial
        
        reativa guia de uma sequencia de inscrições
    """
    
    def print_idx(self, idx: int):
        tam = len(self.lista_dados_op)
        num_zeros = len(str(tam))
        num_digits = len(str(idx))
        
        return f'{"0"*(num_zeros-num_digits)}{idx}'
    
    def __init__(self, browser, lista_dados_op:list, 
                 max_delay: int,
                 processo:str,
                 apartirde: int,
                 origem: int,
                 anoinicio: int,
                 anofim: int,
                 tipo_dec: str,
                 idx: int): # falta achar o tipo do driver
        """
        Args:
            browser
            lista_dados_op: esta classe considera que o dict possui duas chaves:
                'ii' e 'dv'
            processo: 99-99-999999-9999
           exercicio, guia a reativar
           
           idx é o valor inicial do indice. Em caso de erro
               precisa indicar o último índice
        """
        super().__init__(browser, lista_dados_op, max_delay)
        
        # separa os 4 componentes do processo
        lista_processo = processo.split('-')
        
        self.p1 = lista_processo[0]
        self.p2 = lista_processo[1]
        self.p3 = lista_processo[2]
        self.p4 = lista_processo[3]
        
        self.apartirde = apartirde
        self.origem = origem
        self.anoinicio = anoinicio
        self.anofim = anofim
        self.tipo_dec = tipo_dec
        self.idx = idx
    
    def realizar_operacao(self):
        """ realiza operacao """
        
        vvdec = VVDEC(self.browser)
        
        vvdec.ir_para_VVDEC()
        
        idx = self.idx
        
        while(len(self.lista_dados_op)-1 >= self.op_atual):
            try:
                # pega os dados da operacao atual
                dados = self.get_dados_op_atual()
                # nesse caso, os dados são inscrição (ii) e dig verificador (dv)
                ii, dv = dados['ii'], dados['dv']
                vv_declarado = dados['vvdec']
                
                vvdec.clicar_botao_limpar()                
                vvdec.preenche_PA(self.p1, self.p2, self.p3, self.p4)
                vvdec.preenche_ii_e_dv(ii, dv)
                vvdec.preenche(apartirde=self.apartirde,
                               origem=self.origem,
                               vvdec=vv_declarado,
                               vig_inicial=self.anoinicio,
                               vig_final=self.anofim)     
                
                if self.tipo_dec == 'judicial':
                    vvdec.clicar_radio_Judicial()
                
                vvdec.consultar()
                vvdec.incluir()
                
                vvdec.clicar_ok()
                
                if not vvdec.verifica_exito():
                    erro = vvdec.get_status_line()
                    raise Exception(f'operacao com erro: {erro}')
                
                vvdec.screen_shot(f'saida/{self.print_idx(idx)} - {ii}_{dv}.png')
                
                self.avancar_op()
                
                delay = self.max_delay*random.random()
                
                print(f'Inscrição {ii}-{dv} ok! Delay de {delay:.2f}s.') 
                
                idx = idx + 1
                
                time.sleep(delay)
            except Exception as e:
                print(e)
                self.recuar_op() 
                # winsound.Beep(frequency=750, duration=3000)
                os.system(f'play -nq -t alsa synth {3} sine {440}')
                break      

# NÃO FUNCIONOU IMP EM PDF
class Imprime_Compi(Op_Sequencial):
    """ 
        subclasse de Op_Sequencial
        
        consulta várias inscrições na COMPI e salva em pdf
    """
    def __init__(self, browser, lista_dados_op:list, 
                 tempo_entre_operacoes: float, dir_download: str): # falta achar o tipo do driver
        """
        Args:
            browser
            lista_dados_op: esta classe considera que o dict possui duas chaves:
                'ii' e 'dv'
        """
        super().__init__(browser, lista_dados_op, tempo_entre_operacoes,
             dir_download)
    
    def realizar_operacao(self):
        """ realiza operacao """
        
        compi = Compi(self.browser)
        
        compi.ir_para_COMPI()
        
        while(len(self.lista_dados_op)-1 >= self.op_atual):
            try:
                # limpa dados da COMPI
                compi.limpar_a_COMPI()
                # pega os dados da operacao atual
                dados = self.get_dados_op_atual()
                # nesse caso, os dados são inscrição (ii) e dig verificador (dv)
                ii, dv = dados['ii'], dados['dv']
                
                compi.preenche_ii_e_dv(ii, dv)
                
                compi.consultar()
                                
                self.avancar_op()
                
                time.sleep(self.tempo_entre_operacoes)                
            except Exception as e:
                print(e)
                self.recuar_op() 
                break
            
