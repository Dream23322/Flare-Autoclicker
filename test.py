from optparse import Values
from tabnanny import check
import tkinter
from tkinter.tix import IMAGE
import customtkinter
import sys
import pyautogui
import keyboard
import mouse
right_click = False
double_click = True


customtkinter.set_appearance_mode("light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme('green')  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("380x620")
app.title("Flare Autoclicker")


def change_appearance_mode():
    #sets mode to dark
    app.set_appearance_mode('dark')
    frame_1.set_appearance_mode('dark')
    label_1.set_appearance_mode('dark')
    label_3.set_appearance_mode('dark')
    label_2.set_appearance_mode('dark')
    button_1.set_appearance_mode('dark')
    lightmode.set_appearance_mode('dark')
    darkmode.set_appearance_mode("dark")
    slider_1.set_appearance_mode('dark')
    switch_1.set_appearance_mode('dark')
    checkbox_1.set_appearance_mode('dark')
    visual_frame.set_appearance_mode('dark')
    settings_frame.set_appearance_mode('dark')
    optionmenu_1.set_appearance_mode('dark')
    

def light_mode_toggle():
    #sets mode to light
    app.set_appearance_mode('light')
    frame_1.set_appearance_mode('light')
    label_1.set_appearance_mode('light')
    label_3.set_appearance_mode('light')
    label_2.set_appearance_mode('light')
    button_1.set_appearance_mode('light')
    lightmode.set_appearance_mode('light')
    darkmode.set_appearance_mode('light')
    slider_1.set_appearance_mode('light')
    switch_1.set_appearance_mode('light')
    checkbox_1.set_appearance_mode('light')
    settings_frame.set_appearance_mode('light')
    visual_frame.set_appearance_mode('light')
    optionmenu_1.set_appearance_mode('light')
    

toggled = False

        

def main_toggle():
    while True:
        if right_click == True:
            pyautogui.rightClick()
        if keyboard.is_pressed("TAB"):
            break
        else:
            pyautogui.leftClick

def adc_toggle():
    double_click == True
       
def rightClickToggle():
    right_click == True


def button_callback():
    slider_1.set(5)

def dark_mode_toggle():
    customtkinter.set_appearance_mode('dark')

def update():
    while True:
        if mouse.is_pressed(button='left') and double_click == True:
            print("It Should Be Working")
            pyautogui.leftClick()
        while toggled == True:
            pyautogui.leftClick()

        if keyboard.is_pressed("F6"):
            toggled == True
        print("Running")    


def change(val):

    data = (str(val))
    


frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=25, padx=40, fill="both", expand=True)

settings_frame = customtkinter.CTkFrame(master=frame_1)
settings_frame.pack(pady=30, padx=28, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(master=settings_frame, text='Autoclicker Settings', justify=tkinter.LEFT)
label_1.pack(pady=12, padx=10)


button_1 = customtkinter.CTkButton(master=settings_frame, text='reset', command=button_callback)
button_1.pack(pady=12, padx=10)

slider_1 = customtkinter.CTkSlider(master=settings_frame, command=change, from_=0, to=10)
slider_1.pack(pady=12, padx=10)
slider_1.set(5)

label_2 = customtkinter.CTkLabel(master=settings_frame, text='5')

label_2.pack(pady=12, padx=10)



optionmenu_1 = customtkinter.CTkButton(settings_frame, text='Right Click', command=rightClickToggle)
optionmenu_1.pack(pady=12, padx=10)


checkbox_1 = customtkinter.CTkCheckBox(master=settings_frame, text='random')
checkbox_1.set_appearance_mode('on')
checkbox_1.pack(pady=12, padx=10)

checkbox_2 = customtkinter.CTkButton(master=settings_frame, text='Auto Double Click', command=adc_toggle)
checkbox_2.pack()

radiobutton_var = tkinter.IntVar(value=1)


#switch_1 = customtkinter.CTkSwitch(master=settings_frame, text='Toggle', command=main_toggle)
switch_1 = customtkinter.CTkButton(master=settings_frame, text='Toggle', command=main_toggle)
switch_1.pack(pady=12, padx=10)

update_sys = customtkinter.CTkSwitch(master=settings_frame, text='Update Checks', command=update)
update_sys.pack()

visual_frame = customtkinter.CTkFrame(master=frame_1)
visual_frame.pack(pady=3, padx=29, fill="both")


label_3 = customtkinter.CTkLabel(master=visual_frame, text='Visual')
label_3.pack(pady=1, padx=10)

darkmode = customtkinter.CTkButton(master=visual_frame, text='dark mode', command=change_appearance_mode)
darkmode.pack(pady=1, padx=1)

lightmode = customtkinter.CTkButton(master=visual_frame, text='light mode', command=light_mode_toggle)
lightmode.pack(pady=1, padx=10)





app.mainloop()
