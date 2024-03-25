# List of alphabets
letters=[chr(i) for i in range(32,123)]

def encrypt_message():
    # Create an encryption key list
    import random
    tools=['!','@','$','%','&','^','*','0','1','2','3','4','5','6','7','8','9']
    enc=[]
    while len(enc) <= len(letters):
        x = random.sample(tools,3)
        if ''.join(x) in enc:
            continue
        else:
            enc.append(''.join(x))
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


