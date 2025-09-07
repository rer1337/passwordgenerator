from customtkinter import *
from random import *

def symbols(value):
    global symbolsamnt
    symbolsamnt = int(value)
    count_password_chars_label.configure(text=f'{int(value)}')
    
def passgen():
    global symbolsamnt
    chars = [char for char in 'qwertyuiopasdfghjklzxcvbnm']
    spec_chars = [char for char in '!@#$%^&*()_+']
    avalable_value = []
    result = ''
    if l_chars_btn.get():
        avalable_value += chars
    if up_chars_btn.get():
        avalable_value += [char.upper() for char in chars]
    if spec_chars_btn.get():
        avalable_value += spec_chars
    if number_chars_btn.get():
        avalable_value += [str(i) for i in range(0,10)]
    for i in range(symbolsamnt):
        result += choice(avalable_value)
    passwordentry.delete('0', 'end')
    passwordentry.insert(0, result)
    
symbolamnt = 12
window = CTk()
window.title('passgen')
passwordentry = CTkEntry(window, width=110)
passwordentry.grid(row=0,column=0,padx=5,pady=5)

btn = CTkButton(window, text='GENERATE', command=passgen)
btn.grid(row=0,column=1,padx=10)

settings_frame_left = CTkFrame(window, width=50)
settings_frame_left.grid(row=1,column=0)

l_chars_btn = CTkCheckBox(settings_frame_left, text="a", width=70)
l_chars_btn.pack(pady=2.5)

up_chars_btn = CTkCheckBox(settings_frame_left, text="A", width=70)
up_chars_btn.pack(pady=2.5)

spec_chars_btn = CTkCheckBox(settings_frame_left, text="!", width=70)
spec_chars_btn.pack(pady=2.5)

number_chars_btn = CTkCheckBox(settings_frame_left, text="1", width=70)
number_chars_btn.pack(pady=2.5)

settings_frame_right = CTkFrame(window)
settings_frame_right.grid(row=1,column=1)

count_password_chars_slider = CTkSlider(settings_frame_right, from_=1, to=65536, orientation='vertical', command=symbols)
count_password_chars_slider.pack(side='right')

count_password_chars_label = CTkLabel(settings_frame_right,text='4',width=40)
count_password_chars_label.pack(side='left',padx=10)

window.mainloop()