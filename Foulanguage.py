letters=[]
for i in range(32,123):
    letters.append(chr(i))
# List of alphabets

def encrypt_message():
    # Create an encryption key list
    import random
    tools=['!','@','$','%','&','^','*','0','1','2','3','4','5','6','7','8','9']
    ele=[]
    enc=[]

    for i in range(0,len(letters)):
        for l in range(3):
            x=random.randint(0,len(tools)-1)
            ele.append(tools[x])
        # for j in enc:
        if ele in enc:
            ele.clear()
            continue
        else:
            enc.append(''.join(ele))
            ele.clear()
    return enc


def key_binder(keyword):
    # Join individual keys to create the code
    num1 = 0
    num2 = 0
    mylist=[]
    key_list=[]
    for i in range(len(letters)):
        num2 = num2 + 3
        for l in range(num1,num2):
            mylist.append(keyword[l])
        key_list.append(''.join(mylist))
        mylist.clear()
        num1 = num1 + 3
    return key_list


def encryption():
    message=str(input("Write your message:\n"))
    lmessage=list(message)
    keyornot=int(input("To give a specific key press 1 otherwise enter any number to continue\n"))

    if keyornot==1:
        key=list(input('Enter the key:\n'))
        get_key = key_binder(key)
        for i in range(len(lmessage)):
            for l in range(len(letters)):
                if lmessage[i]==letters[l]:
                    lmessage[i]=get_key[l]
        print(f"Encrypted message:\n{''.join(lmessage)}\n\nKEY:\n{''.join(key)}")

    else:
        for i in range(len(lmessage)):
            for l in range(len(letters)):
                if lmessage[i]==letters[l]:
                    lmessage[i]=encrpt[l]
        print(f"Encrypted message:\n{''.join(lmessage)}\n\nKEY:\n{''.join(encrpt)}")

def decryption():
    message = str(input('Enter the encrypted message:\n'))
    key=list(input('Enter the key:\n'))
    get_key=key_binder(key)
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

    print(f"Decrypted message:\n{''.join(main_list)}")

encrpt=encrypt_message()


select=int(input('Press 1 to encrypt message and 2 to decrypt message:\n'))
if select==1:
    encryption()
elif select==2:
    decryption()
else:
     print('Wrong input')