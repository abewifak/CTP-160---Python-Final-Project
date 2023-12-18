'''
Final Project that encodes and decodes text using cipherValue using input and distance also encodes and decodes binary and hex
Ibrahim Wifak
'''
import tkinter as tk
import tkinter.font as font
from functools import partial
from tkinter import messagebox, ttk
import webbrowser

class EncoderDecoderGUI:
    def __init__(self):
        #creating the window
        self.window = tk.Tk()
        self.window.geometry('500x600')
        self.window.title('Encoder and Decoder')
        self.window.configure(bg='grey')

        #creating the fonts
        self.f1 = font.Font(family='helvetica', size='30')
        self.f2 = font.Font(family='helvetica', size='15')
        self.f3 = font.Font(family='helvetica', size='20')
        self.f4 = font.Font(family='helvetica', size='10')

        #the textvariables
        self.code = tk.StringVar()
        self.distance = tk.StringVar()

        self.create_widgets()
        self.window.mainloop()

    def create_widgets(self):
        self.create_main_label()
        self.create_from_label()
        self.create_main_combobox()
        self.create_to_label()
        self.create_from_combobox()
        self.create_distance_entry()
        self.create_entry()
        self.create_result_label()
        self.create_convert_button()
        self.create_art_label()
        self.link()

    def create_main_label(self):
        main = tk.Label(self.window, text='Encoder/Decoder', bg="grey", fg='white')
        main['font'] = self.f1
        main.place(relx='0.50', rely='0.1', anchor='center')

    def create_from_label(self):
        unit = tk.Label(self.window, text='Encode/Decode:', bg='grey')
        unit['font'] = self.f2
        unit.place(relx='0.10', rely='0.28')
    
    def create_main_combobox(self):
        n = tk.StringVar()
        self.unitdd = ttk.Combobox(self.window, width='25', textvariable=n)
        self.unitdd['values'] = ('Encode', 'Decode',)
        self.unitdd.place(relx='0.57', rely='0.3', anchor='center')
        self.unitdd.current()
        self.unitdd.bind('<<ComboboxSelected>>', self.fromfunc)

    #creates the text for to
    def create_to_label(self):
        label_to = tk.Label(self.window, text='Type:', bg='grey')
        label_to['font'] = self.f2
        label_to.place(relx='0.11', rely='0.37')

    #creates the drop down menu for from
    def create_from_combobox(self):
        f = tk.StringVar()
        self.fromdd = ttk.Combobox(self.window, width='25', textvariable=f)
        self.fromdd['values'] = ('Encode', 'Decode')
        self.fromdd.place(relx='0.57', rely='0.39', anchor='center')
        self.fromdd.current()
        self.fromdd.bind('<<ComboboxSelected>>', self.tofunc)

    #creates the box to enter distance
    def create_distance_entry(self):
        distanceText = tk.Label(self.window, text='Distance: ', bg='grey')
        distanceText['font'] = self.f2
        distanceText.place(relx='0.11', rely='0.43')

        distance_entry = tk.Entry(self.window, width=10, textvariable=self.distance)
        distance_entry.place(relx='0.5', rely='0.45', anchor='center')

    def create_entry(self):
        code = tk.Entry(self.window, width=40, textvariable=self.code)
        code.place(relx='0.15', rely='0.50')

    #creates the text and box for the results
    def create_result_label(self):
        self.result = tk.Label(self.window, text='', bg='white', width=28, height=5)
        self.result['font'] = self.f3
        self.result.place(relx='0.05', rely='0.58')

    #creates the button
    def create_convert_button(self):
        convert_btn = tk.Button(self.window, text='Convert', command=self.convert, bg='red', fg='white')
        convert_btn['font'] = self.f2
        convert_btn.place(relx='0.75', rely='0.5', anchor='center')

    #creates art with my name at the button
    def create_art_label(self):
        art = tk.Label(self.window, text='By: Abe Wifak', bg='grey', fg='white')
        art.place(relx='0.5', rely='0.95', anchor='center')

    '''
    Link Function that creates a button and uses webbrowser that leads to my linkedIn
    '''
    def link(self):
        def open_link():
            webbrowser.open_new("https://www.linkedin.com/in/ibrahim-wifak")
    
        #button_linked = tk.Button(self.window, text="LinkedIn", command=open_link, bg='light blue')
        button_linked = tk.Button(self.window, text="LinkedIn", command=open_link, font=self.f4, bd=0, relief="solid", bg="#0077B5", fg="white")
        #button_linked['font'] = self.f4
        button_linked.place(relx='0.65', rely='0.95', anchor='center')
        #button_linked.place(relx='0.65', rely='0.95', anchor='center')
        button_linked.config(width=6, height=1, borderwidth=2, padx=3, pady=4, activebackground="#00669E", activeforeground="white")

    #fromfunc that chooses whether youll be encoding or decoding
    def fromfunc(self, event):
        if self.unitdd.get() == 'Encode':
            self.fromdd['values'] = ('Binary', 'Hexadecimal', 'Text')
            self.fromdd.current(0)
        elif self.unitdd.get() == 'Decode':
            self.fromdd['values'] = ('Binary', 'Hexadecimal', 'Text')
            self.fromdd.current(2)

    '''
    choses whether youll be encoding/decoding to what
    2 parameters
    '''
    def tofunc(self, event):
        if self.fromdd.get() == 'Binary':
            self.code.set('Enter Binary')
        elif self.fromdd.get() == 'Hexadecimal':
            self.code.set('Enter Hexadecimal')
        elif self.fromdd.get() == 'Text':
            self.code.set('Enter Text')

    #convert button and its options, when the options are chosen, it then takes a selection
    def convert(self):
        from_value = self.fromdd.get()
        to_value = self.unitdd.get()

        if from_value == 'Binary' and to_value == 'Encode':
            result = self.encode_binary(self.code.get(), int(self.distance.get()))
        elif from_value == 'Binary' and to_value == 'Decode':
            result = self.decode_binary(self.code.get(), int(self.distance.get()))
        elif from_value == 'Hexadecimal' and to_value == 'Encode':
            result = self.encode_hexadecimal(self.code.get(), int(self.distance.get()))
        elif from_value == 'Hexadecimal' and to_value == 'Decode':
            result = self.decode_hexadecimal(self.code.get(), int(self.distance.get()))
        elif from_value == 'Text' and to_value == 'Encode':
            result = self.encode_text(self.code.get(), int(self.distance.get()))
        elif from_value == 'Text' and to_value == 'Decode':
            result = self.decode_text(self.code.get(), int(self.distance.get()))
        else:
            messagebox.showerror('Error', 'Invalid input')
            return

        self.result.configure(text=result)

    def encode_binary(self, code, distance):
        result = ''
        for c in code:
            if c == ' ':
                result += ' '
            else:
                result += bin((ord(c) + distance) % 256)[2:].zfill(8)
        return result #returns the encoded binary

    def decode_binary(self, code, distance):
        result = ''
        for i in range(0, len(code), 8):
            if code[i:i+8] == ' ':
                result += ' '
            else:
                result += chr((int(code[i:i+8], 2) - distance) % 256)
        return result #returns the decoded binary

    def encode_hexadecimal(self, code, distance):
        result = ''
        for c in code:
            if c == ' ':
                result += ' '
            else:
                result += hex((ord(c) + distance) % 256)[2:]
        return result #returns the result

    def decode_hexadecimal(self, code, distance):
        result = ''
        for i in range(0, len(code), 2):
            if code[i:i+2] == ' ':
                result += ' '
            else:
                result += chr((int(code[i:i+2], 16) - distance) % 256)
        return result #returns the result
    
    def encode_text(self, code, distance):
        result = ''
        for c in code:
            if c == ' ':
                result += ' '
            else:
                result += chr((ord(c) + distance) % 256)
        return result #returns the result

    def decode_text(self, code, distance):
        result = ''
        for c in code:
            if c == ' ':
                result += ' '
            else:
                result += chr((ord(c) - distance) % 256)
        return result #returns the reults


if __name__ == '__main__':
    app = EncoderDecoderGUI() #calls the app to run
    app.run()