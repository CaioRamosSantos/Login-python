from PySimpleGUI import PySimpleGUI as sg
import time

sg.theme('Reddit')

layout = [
    [sg.Text('Usuário(Login)', size=(15, 1)), sg.Input(key='usuario')],
    [sg.Text('Senha', size=(15, 1)), sg.Input(key='senha', password_char='*')],
    [sg.Checkbox('Lembrar senha')],
    [sg.Button('Entrar')],
]

janela = sg.Window('Tela login', layout)

while True:
    eventos, credenciais = janela.read()
    
    if eventos == sg.WINDOW_CLOSED:
        break
    
    if eventos == 'Entrar':
        if credenciais['usuario'] == 'Caio' and credenciais['senha'] == '123':
            time.sleep(1)
            sg.popup('Seja bem-vindo!', title='Sucesso')
            break  
        else:
            sg.popup_error('Credênciais inválidas', title='Falha')

janela.close()
