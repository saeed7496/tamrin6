
from asyncore import read
from itertools import product
from re import search
from tkinter import font
from pyfiglet import Figlet

produact=[]
moshakhasat=['id','mahsool', 'gheymat', 'mojoodi']
def load():
    l=open('tamrin6.txt', 'r')
    l_anbar=l.read()
    l.close()
    lst=l_anbar.split('\n')
    for i in range(len(lst)):
        my_dict={}
        lst_anbar=lst[i].split(',')
        my_dict['id']=lst_anbar[0]
        my_dict['mahsool']=lst_anbar[1]
        my_dict['gheymat']=lst_anbar[2]
        my_dict['mojoodi']=lst_anbar[3]
        produact.append(my_dict)

def show_list():
    load()
    for j in produact:
        print(j)

def show_menu():
    dict_menu={1:'Add product', 2:'Edit product', 3:'Delet product',
           4:'search', 5:'show list', 6:'buy', 7:'qrcode', 8:'exit'}

    for i,j in dict_menu.items():
        print(i,'=',j)

def serch():
    load()
    scan=input('lotfan id ya nam mahsool ra vared konid: ')
    for s in range(len(produact)):
        if produact[s]['id']==scan and int(produact[s]['mojoodi'])>0:
            print(produact[s])
            return s
        elif produact[s]['mahsool']==scan and int(produact[s]['mojoodi'])>0:
            print(produact[s])
            return s
        elif s ==len(produact)-1:
            return 'False'

def afzoodan():
    b=open('tamrin6.txt','a')
    b.write('\n')
    for i in moshakhasat:
        taghir=input(f'   {i} ra vared namaeed:')
        taghir+=','
        b.write(taghir)
    b.close()

def append():
    t=open('tamrin6.txt','w').close()
    for i in range(len(produact)):
        t=open('tamrin6.txt', 'a')
        for m in moshakhasat:
            st=str(produact[i][m])
            t.write(st)
            t.write(',')
        if i <= len(produact)-2:
            t.write('\n')
        t.close()

def kharid():
    while True:
        buy=int(input('1_taeed\n2_bargasht\n:'))
        if buy == 1:
            x=int(produact[s]['mojoodi'])
            x-=1
            produact[s]['mojoodi']=x
            append()
            f=open('tamrin7.txt', 'a')
            f.write('\n')
            f.write(str(produact[s]['mahsool']))
            f.write('\t')
            f.write(str(produact[s]['gheymat']))
            f.close()
            break
        elif buy == 2:
            break
    return 'chap factor'

def delet():
    while True:
        d=int(input('1_taeed\n2_bargasht:\n'))
        if d == 1:
            produact.pop(s)
            append()
            break
        elif d == 2:
            break

def edit():
    while True:
        edit=int(input('1_taeed\n2_bargasht\n'))
        if edit== 1:
            for i in moshakhasat:
                produact[s][i]=input(f'  {i} ra vared namaeed: ')
                append()
            break
        elif edit == 2:
            break

f=Figlet(font='standard')
print(f.renderText('s a e e d stor'))
show_menu()
while True:
    choos=int(input('chekar konam barat: '))
    if choos == 1:
        print('afzoodan:')
        afzoodan()
        
    elif choos ==2:
        print('edit:')
        s=serch()
        if s =='False':
            print('namojood')
        else:
            edit()        
    elif choos ==3:
        print('delet:')
        s=serch()
        if s =='False':
            print('namojood')
        else:
            delet()
    elif choos ==4:
        print('search')
        s=serch()
        if s =='False':
            print('namojood')        
    elif choos ==5:
        print('namayesh kalaha: ')
        show_list()

    elif choos ==6:
        print('kharid')
        s=serch()
        if s =='False':
            print('namojood')
        else:
            f=kharid()
            factor=open('tamrin7.txt', 'r')
            factor_moshtari=factor.read()

    elif choos==7:
        import qrcode
        s=serch()
        d=produact[s]
        img=qrcode.make(d)
        img.save(f'qrcod{s}.png')

    elif choos ==8:
        if f == 'chap factor':              #agar kharid dasht#
            print('factor=',factor_moshtari,'toman')
            f=open('tamrin7.txt','w').close()
        print('az kharid shoma motshakerim')
        exit()
    else:
        print('mojadad talah konid')








