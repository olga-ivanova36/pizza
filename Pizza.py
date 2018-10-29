import tkinter
import tkinter.ttk as ttk

root = tkinter.Tk()

P=dict()
P['Барбекю']={'Cостав':"Томатный соус, сыр моцарелла, бекон, свинина, цыплёнок, маринованный лук, шампиньоны",'size':{'S':"485", 'M':"595"}}
P['Карбонара']={'Состав': "Томатный соус, сыр моцарелла, бекон, яйцо",'size':{'S':"395", 'M':"545"}}
P['Мексиканская']={'Состав': "Сыр моцарелла, томатный соус, бекон, перец чили, цыплёнок, паприка, кукуруза, красный лук, зелень",'size':{'S':"485",'M':"545"}}

tkinter.Label(root, text='Выберите пиццу:', borderwidth=8).grid(row=0,column=0)
for i in range(len(list(P))):
    tkinter.Label(root, text=list(P)[i], borderwidth=8).grid(row=i+1,column=0)
   
tkinter.Label(root, text='Выберите размер:', borderwidth=8).grid(row=0,column=1)
sizes = [tkinter.StringVar() for i in range(len(list(P)))]
for i in range(len(list(P))):
    ttk.Combobox(root, values=list(P[list(P)[i]]['size'].keys()),textvariable=sizes[i]).grid(row=i+1,column=1)

tkinter.Label(root, text='Укажите количество:', borderwidth=8).grid(row=0,column=2)
numberofP=[tkinter.IntVar() for i in range(len(list(P)))]
for i in range(len(list(P))):
    tkinter.Spinbox(root, from_=0, to=20,textvariable=numberofP[i]).grid(row=i+1,column=2)

tkinter.Label(root, text='Выберите срок доставки:', borderwidth=8).grid(row=len(list(P))+1,column=0)
entry=ttk.Combobox(root, values=['Сегодня','Завтра'],textvariable=tkinter.StringVar())
entry.grid(row=len(list(P))+2,column=0)

tkinter.Label(root, text='Адрес доставки:', borderwidth=8).grid(row=len(list(P))+1,column=1)
entry1=tkinter.Entry(root)
entry1.grid(row=len(list(P))+2,column=1)

tkinter.Label(root, text='Ваш номер телефона:', borderwidth=8).grid(row=len(list(P))+1,column=2)
entry2=tkinter.Entry(root)
entry2.grid(row=len(list(P))+2,column=2)

button=tkinter.Button(root, text='Cтоимость',command=lambda:order(0),borderwidth=5).grid(row=len(list(P))+3,column=1)
button1=tkinter.Button(root, text='Заказать',command=lambda:order(1),borderwidth=5, bg='#b7f731').grid(row=len(list(P))+4,column=1)
button2=tkinter.Button(root, text='Выйти', command=root.destroy,borderwidth=5, bg='red').grid(row=len(list(P))+5,column=1)

def order(b):
    D=dict()
    number=sum([i.get() for i in numberofP])
    prices=[]
    pr1=[]
    for i in range(len(sizes)):
        if sizes[i].get()!='':
            priceofP=int(P[list(P)[i]]['size'][sizes[i].get()])
            #print("priceofP",priceofP)
            D[list(P)[i]]={priceofP}
            pr1.append(priceofP)
        else:
            priceofP=0
            pr1.append(100000)
        prices.append(priceofP)
    try:
        minP=prices.index(min(pr1))
    except:
        print("Выберите пиццу и укажите количество")

    sums=[]
    try:
        if entry.get()=='Сегодня':
            for i in range(len(prices)):
                if number<3:
                    sums.append(prices[i]*numberofP[i].get())
                else:
                    if i!=minP:
                        sums.append(prices[i]*numberofP[i].get())
                    else:
                        sums.append(prices[i]*(numberofP[i].get()-1))
                        print("При заказе от трёх пицц самая дешёвая пицца - бесплатно!")
            sumZ=sum(sums)
        if entry.get()=='Завтра':
            for i in range(len(prices)):
                sums.append(prices[i]*numberofP[i].get())
            sumZ=sum(sums)*0.95 
            print("Скидка 5% при заказе доставки на завтра.")

        orderS=tkinter.IntVar()   
        orderS.set(sumZ)
        label=tkinter.Label(root,textvariable=orderS).grid(row=len(list(P))+3,column=2)
    except:
        print("Выберите день доставки.")
    
    D['Время']={entry.get()}
    D['Адрес']={entry1.get()}
    D['Телефон']={entry2.get()}
    if b==0:
        b=0
    if b==1:
        print(D)

root.mainloop()
