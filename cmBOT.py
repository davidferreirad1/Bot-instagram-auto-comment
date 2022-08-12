from tkinter.font import ITALIC, BOLD
from tkinter import *
import pyautogui
import PySimpleGUI as sg
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

wait = WebDriverWait(webdriver, 10, 1)

sg.theme('Black')
layout = [
    
    [sg.Text('USUÁRIO:',font=(ITALIC), text_color=('Red'), size=(50))],

    [sg.Input(key='usuario', size=(50), font=(BOLD))],
    [sg.Text('SENHA:', font=('BOLD'), text_color=('Red'), size=(50))],

    [sg.Input(key='senha',size=(50), font=(BOLD))],

    [sg.Text('DIGITE UMA HASHTAG:', font=('BOLD'), text_color=('Red'), size=(50))],
    [sg.Input(key='hashtag', size=(50), font=(BOLD))],

    [sg.Text('DIGITE SEU COMENTÁRIO:', font=('BOLD'), text_color=('Red'), size=(50))],
    [sg.Input(key='comentario', size=(50), font=(BOLD))],

    [sg.Button('INICIAR',button_color=('Blue'), size=(50))],
    
    [sg.Text('#########################################################',text_color=('Black'), size=(30))],

    [sg.Button('GITHUB',button_color=('Green'), size=(50))],

    [sg.Text('#########################################################',text_color=('Black'), size=(50))],
    

    [sg.Text('CREATED BY DAVID FERREIRA, @DAVU1D.', font=BOLD, text_color=('Green'), size=(50))],
]
window = sg.Window(
    'CMBOT',layout, font=BOLD,  size=(400, 389), finalize=True,
    )
while True:
    event, values = window.read()
    if event == 'GITHUB':
        drive = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))
        driver = drive
        driver.get('https://github.com/davidferreirad1')


        
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'INICIAR':
        usuario = values['usuario']
        senha = values['senha']
        hashtag = values['hashtag']
        comentario: object = values['comentario']
        pyautogui.alert('O cmBOT vai iniciar')
        break
window.close()

class InstagramBot:
    def __init__(self, username, password):
        self.username = usuario
        self.password = senha
        self.driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))

    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com')
        sleep(3)
        campo_usuario = driver.find_element("xpath", '//*[@name="username"]')
        campo_usuario.click()
        campo_usuario.clear()
        campo_usuario.send_keys(self.username)
        campo_senha = driver.find_element("xpath", '//*[@name="password"]')
        campo_senha.click()
        campo_senha.clear()
        campo_senha.send_keys(self.password)
        campo_senha.send_keys(Keys.RETURN)
        sleep(5)
        self.cnfcah(f'{hashtag}')

    def cnfcah(self,hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/"+ hashtag +"/")
        for i in range(1, 30):
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            sleep(2)
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            sleep(5)
        hrefs = driver.find_elements(By.TAG_NAME, "a")
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        [href for href in pic_hrefs if hashtag in href]
        sleep(12)
        print(hashtag + 'fotos: ' + str(len(pic_hrefs)))

        for pic_href in pic_hrefs:
            driver.get(pic_href)
            sleep(10)
            try:
                comentarios = (f'{comentario}')
                driver.find_element(By.CSS_SELECTOR, '._ablz').click()
                pyautogui.write(f'{comentarios}')
                sleep(60)
                pyautogui.press('ENTER')
            except Exception as e:
                print(e)
                sleep(10)


cmbot = InstagramBot(f'{usuario}', f'{senha}')
cmbot.login()



