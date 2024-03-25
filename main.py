from customtkinter import *
import encrypt
from tkinter import filedialog
import os

#Create and place the GUI
app = CTk()
app.geometry('600x435+800+350')
app.title('Foulanguage')
set_appearance_mode('dark')
app.iconbitmap(os.curdir+"\\fl.ico")


def encryption():
# Encrypting message
    message=str(txten.get('1.0','end'))
    lmessage=list(message)

    if keyen.get('1.0','end-1c') != '':
        try:
            key=list(keyen.get('1.0','end'))
            get_key = encrypt.key_binder(key)
            for i in range(len(lmessage)):
                for l in range(len(letters)):
                    if lmessage[i]==letters[l]:
                        lmessage[i]=get_key[l]

            mssg = ''.join(lmessage)
            k  = ''.join(key)
            return mssg,k
        except:
            return 'Wrong key','Clear the key'

    else:
        encrpt = encrypt.encrypt_message()
        for i in range(len(lmessage)):
            for l in range(len(letters)):
                if lmessage[i]==letters[l]:
                    lmessage[i]=encrpt[l]


        mssg = ''.join(lmessage)
        k = ''.join(encrpt)

    if txten.get(1.0,'end-1c')!='':
        return mssg, k

    else:
        return '',''

def decryption():
# Decrypting message
    try:
        message = str(txten.get('1.0','end'))
        key=list(keyen.get('1.0','end-1c'))
        get_key=encrypt.key_binder(key)
        lmessage = list(message)
        nlist=[]
        main_list=[]
        count=0
        last=0
        for i in range((len(lmessage)//3)):
            last=last+3
            for l in range(count,last):
                nlist.append(lmessage[l])
            main_list.append(''.join(nlist))
            nlist.clear()
            count = count + 3
        for i in range(len(main_list)):
            for l in range(len(get_key)):
                if main_list[i]==get_key[l]:
                    main_list[i]=letters[l]

        dcmsg = ''.join(main_list)


    except:
        dcmsg ='Wrong Input'

    return dcmsg

letters=encrypt.letters

mssg = CTkLabel(master=app, text='Enter Message:')
keymsg = CTkLabel(master=app, text='Enter key:')
mssg.place(relx=.07,rely=.175)
keymsg.place(relx=.07,rely=.605)

txten = CTkTextbox(master=app, height=150)
keyen = CTkTextbox(master=app, height=50)
txten.place(relx=.4, rely=.42, anchor=E)
keyen.place(relx=.4, rely=.73, anchor=E)

txt = txten.get('1.0','end-1c')
keytxt = keyen.get('1.0','end-1c')

class out():
#Place the encrypted of decrypted output
    def __init__(self):
        self.out = CTkTextbox(master=app, height=200)
        self.txt = CTkTextbox(master=app, height=150, font=('arial', 11))
        self.key = CTkTextbox(master=app, height=50, font=('arial', 11))
        self.outmsg = CTkLabel(master=app, text='Encrypted Message:  ')
        self.outkey = CTkLabel(master=app, text='Encryption key:  ')

    def enout(self):
        self.txt.delete(1.0,'end')
        self.key.delete(1.0,'end')
        msg,k = encryption()
        self.out.place_forget()
        self.txt.insert(1.0,msg)
        self.key.insert(1.0,k)

        self.outmsg.place(relx=.6, rely=.175)
        self.outkey.place(relx=.6, rely=.605)
        self.txt.place(relx=.6, rely=.415, anchor=W)
        self.key.place(relx=.6, rely=.725, anchor=W)
        self.outmsg.configure(text='Encrypted Message:  ')
        save.configure(state=NORMAL,command=ensave)

    def dout(self):
        self.out.delete(1.0,'end')
        self.txt.place_forget()
        self.key.place_forget()
        self.outkey.place_forget()


        dcmsg = decryption()
        self.out.insert(1.0,dcmsg)
        self.outmsg.place(relx=.6, rely=.175)
        self.out.place(relx=.6, rely=.48, anchor=W)
        self.outmsg.configure(text='Message:  ')
        save.configure(state=NORMAL,command=dcsave)

#Create an output object to use in generate button
output = out()

arro = CTkLabel(master=app, text='-------→')

def en():
# Encryption button's work
    arro.place(relx=.5, rely=.45, anchor=CENTER)

    encbtn.configure(state=DISABLED)
    decbtn.configure(state=NORMAL)
    gnrtbtn.configure(command=output.enout,state=NORMAL)
    txten.delete('1.0','end')
    keymsg.configure(text='Enter Key(Optional):')

def dc():
# Decryption button's work
    arro.place(relx=.5, rely=.45, anchor=CENTER)

    decbtn.configure(state=DISABLED)
    encbtn.configure(state=NORMAL)
    gnrtbtn.configure(command=output.dout,state=NORMAL)
    txten.delete('1.0', 'end')
    keymsg.configure(text='Enter Key:')

# Encrypt and Decrypt buttons
encbtn = CTkButton(master=app,text='Encrypt',command=en, fg_color='#35bd70',text_color='#303030',hover_color='#2d734b',text_color_disabled='#6e6e6e')
decbtn = CTkButton(master=app,text='Decrypt',command=dc, fg_color='#35bd70',text_color='#303030',hover_color='#2d734b',text_color_disabled='#6e6e6e')
encbtn.place(relx=.3,rely=.05,anchor= N)
decbtn.place(relx=.7,rely=.05,anchor= N)

def sho():
    pass

def choosefile():
    file = filedialog.askopenfilename(title='Select file',filetypes=(('Text file','*.txt'),))
    return file

def store():
    global file
    file = choosefile()

def dcsave():
# Save decrypted message as txt file
    with open('Decrypted.txt','w') as file:
        file.write(f'Decrypted Message:\n{output.out.get(1.0, "end")}')

def ensave():
# Save encrypted message as txt file
    with open('Encrypted.txt','w') as file:
        file.write(f'Encrypted Message:\n{output.txt.get(1.0, "end")}\n\nkey:\n{output.key.get(1.0, "end")}')

# Generate and save buttons
gnrtbtn = CTkButton(master=app, text='Generate', command= sho, state=DISABLED)
gnrtbtn.place(relx=.5,rely=.9, anchor= CENTER)

save = CTkButton(master=app,text='Save file',command=sho,state=DISABLED)
save.place(relx=.68, rely=.9, anchor=W)

app.mainloop()