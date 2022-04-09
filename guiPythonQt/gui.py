# gui.py
import PySimpleGUI as sg

layout = [
        [sg.Text("Hello from PySimpleGUI")],
        [sg.Button("Ok")]
        ]

window = sg.Window("Demo", layout)


while True:
    event, values = window.read()
    if event == "Ok" or event == sg.WIN_ClOSED:
        break

window.close()
