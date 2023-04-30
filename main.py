# set up

import PySimpleGUI as sg
import os

sg.theme("DarkGrey6")

layout = [ [sg.Text("ADBtools")],
           [sg.Text('')],
           [sg.Text("Run commands"), sg.Button("adb devices"), ],
           [sg.Text("Custom adb command:"), sg.Text("adb"), sg.InputText(), sg.Button("Send")],
           [sg.Button("close ADBtools")] ]



# add explanation

print("This is the output window.")
print("Everything that would normally be printed into a terminal goes here.")
print('')

# create window
window = sg.Window("ADBtools", layout, margins=(25,25))

# create loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "adb devices":
        os.chdir("adb")
        os.system("adb devices")

    elif event == "close ADBtools":
        print("ADBtools closed")
        break

    elif event == sg.WIN_CLOSED:
        print("ADBtools closed")
        break

window.close()
