import turtle
import random

def simulazione(n,r,p,g,m,h,v,c,d):
    turtle.setup(width=2*r,height=2*r)
    tart=[]
    età=[random.randint(5,70) for i in range(n)]
    tart_mal=[]
    tart_sane=[]
    tart_morte=[]
    tart_vive=[]
    tart_imm=[]
    tart_asi=[]
    tart_nonasi=[]
    bordo=turtle.Turtle()
    bordo.penup()
    bordo.setpos(-r,-r)
    bordo.pendown()
    for k in range(4):
        bordo.forward(2*r)
        bordo.left(90)
    bordo.hideturtle()
    muro=turtle.Turtle()
    muro.color("blue")
    muro.penup()
    muro.setpos(-100,-r)
    muro.pendown()
    muro.goto(-100,r)
    muro.hideturtle()
    posti_spec=turtle.Turtle()
    posti_spec.color("purple")
    posti_spec.penup()
    posti_spec.setpos(175,250)
    posti_spec.pendown()
    posti_spec.right(90)
    posti_spec.forward(75)
    posti_spec.left(90)
    posti_spec.forward(75)
    posti_spec.hideturtle()
    
    for numtart in range(n):
        alex=turtle.Turtle()
        alex.speed(0)
        alex.penup()
        alex.setpos(random.random()*2*r-r,random.random()*2*r-r)
        alex.pendown()
        tart.append(alex)
        prob=random.random()
        if prob<=p:
            alex.color("red")
            tart_mal.append(alex)
            #asintomatici:
            if random.random()<0.5:
                alex.color("yellow")
                tart_asi.append(alex)
            else:
                tart_nonasi.append(alex)
        else:
            alex.color("green")
            tart_sane.append(alex)
        
            
            
    day_mal=[0 for z in range(n)]    
    for day in range(1,g+1):
        if day%2==0:
            turtle.bgcolor("light yellow")
        else:
            turtle.bgcolor("light blue")
        for x in tart_nonasi:
            prob_morte=random.random()
            if prob_morte<=m:
                x.color("black")
                tart_nonasi.remove(x)
                tart_mal.remove(x)
                tart_morte.append(x)
        for pos in range(n):
            if tart[pos] in tart_mal:
                day_mal[pos]=day_mal[pos]+1
                if day_mal[pos]==h:
                    tart[pos].color("green")
                    tart_mal.remove(tart[pos])
                    if tart[pos] in tart_asi:
                        tart_asi.remove(tart[pos])
                    else:
                        tart_nonasi.remove(tart[pos])
                    tart_sane.append(tart[pos])
                    #anticorpi:
                    tart[pos].color("light green")
                    tart_imm.append(tart[pos])
                    
        #malati stanno fermi:
        tart_vive=tart_sane+tart_asi
        for v in range(1,v+1):
            T=tart_vive[random.randint(0,len(tart_vive)-1)]
            coordT=T.pos() 
            intx=(coordT[0]-d,coordT[0]+d)
            inty=(coordT[1]-d,coordT[1]+d)
            x=random.random()*(intx[1]-intx[0])+intx[0]
            y=random.random()*(inty[1]-inty[0])+inty[0]
            if x<-r:
                x=-r
            if x>r:
                x=r
            if y<-r:
                y=-r
            if y>r:
                y=r
            #movimenti manhattan:
            #muro:
            if coordT[0]<(-100) and x<(-100):
                T.goto(x,coordT[1])
                T.goto(x,y)
            if coordT[0]>(-100) and x>(-100):
                T.goto(x,coordT[1])
                T.goto(x,y)
            if coordT[0]>(-100) and x<(-100):
                x=random.random()*(100+coordT[0])-99
                T.goto(x,coordT[1])
                T.goto(x,y)
            if coordT[0]<(-100) and x>(-100):
                x=random.random()*(coordT[0]+99)+coordT[0]
                T.goto(x,coordT[1])
                T.goto(x,y)

            #posti speciali:
            if T not in tart_imm and T in tart_sane and x>=175 and x<=250 and y>=175 and y<=250:
                T.color("red")
                tart_sane.remove(T)
                tart_mal.append(T)
                #asintomatici:
                if random.random()<0.5:
                    T.color("yellow")
                    tart_asi.append(T)
                else:
                    tart_nonasi.append(T)
                        
            if T in tart_mal:
                indice_T=tart.index(T)
                for i in tart_sane:
                    #dipendenza dall'età:
                    indice=tart.index(i)
                    pos_i=i.pos()
                    if pos_i[0]<(-100) and coordT[0]<(-100) or pos_i[0]>(-100) and coordT[0]>(-100):
                        if età[indice]>50 or età[indice_T]>50:
                            if i not in tart_imm and pos_i[0]>=(x-2*c) and pos_i[0]<=(x+2*c) and pos_i[1]>=(y-2*c) and pos_i[1]<=(y+2*c):
                                i.color("red")
                                tart_sane.remove(i)
                                tart_mal.append(i)
                                #asintomatici:
                                if random.random()<0.5:
                                    i.color("yellow")
                                    tart_asi.append(i)
                                else:
                                    tart_nonasi.append(i)
                        elif età[indice]<=50 or età[indice_T]<=50:
                            if i not in tart_imm and pos_i[0]>=(x-c) and pos_i[0]<=(x+c) and pos_i[1]>=(y-c) and pos_i[1]<=(y+c):
                                i.color("red")
                                tart_sane.remove(i)
                                tart_mal.append(i)
                                #asintomatici:
                                if random.random()<0.5:
                                    i.color("yellow")
                                    tart_asi.append(i)
                                else:
                                    tart_nonasi.append(i)
                        
            if T in tart_sane:
                indice_T=tart.index(T)
                for j in tart_mal:
                    pos_j=j.pos()
                    indice=tart.index(j)
                    if pos_j[0]<(-100) and coordT[0]<(-100) or pos_j[0]>(-100) and coordT[0]>(-100):
                        if età[indice]>50 or età[indice_T]>50:
                            if T in tart_sane and T not in tart_imm and pos_j[0]>=(x-2*c) and pos_j[0]<=(x+2*c) and pos_j[1]>=(y-2*c) and pos_j[1]<=(y+2*c):
                                T.color("red")
                                tart_sane.remove(T)
                                tart_mal.append(T)
                                #asintomatici:
                                if random.random()<0.5:
                                    T.color("yellow")
                                    tart_asi.append(T)
                                else:
                                    tart_nonasi.append(T)
                        elif età[indice]<=50 or età[indice_T]<=50:
                            if T in tart_sane and T not in tart_imm and pos_j[0]>=(x-c) and pos_j[0]<=(x+c) and pos_j[1]>=(y-c) and pos_j[1]<=(y+c):
                                T.color("red")
                                tart_sane.remove(T)
                                tart_mal.append(T)
                                #asintomatici:
                                if random.random()<0.5:
                                    T.color("yellow")
                                    tart_asi.append(T)
                                else:
                                    tart_nonasi.append(T)
                    

        #malati random ogni giorno:
        if len(tart_sane)!=0:
            T_rand=tart_sane[random.randint(0,len(tart_sane)-1)]
            #anticorpi:
            if len(tart_sane)!=len(tart_imm):
                while T_rand in tart_imm:
                    T_rand=tart_sane[random.randint(0,len(tart_sane)-1)]
                T_rand.color("red")
                tart_sane.remove(T_rand)
                tart_mal.append(T_rand)
                if random.random()<0.5:
                    T_rand.color("yellow")
                    tart_asi.append(T_rand)
                else:
                    tart_nonasi.append(T_rand)
                
            
            
    
        print("Giorno: ",day)                
        print("Numero persone morte: ",(len(tart_morte)))            
        print("Numero persone sane: ",(len(tart_sane)))
        print("Numero persone malate: ",(len(tart_mal))) 
        print("---------------------------")
    turtle.clearscreen()
    
print(simulazione(50,250,0.2,60,0.01,15,20,10,10))

def simVaryingP():
    for p in (0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9):
        print(simulazione(50,250,p,30,0.01,15,20,10,10))

def simVaryingD():
    for d in (1,3,6,12,25,50,100,200):
        print(simulazione(50,250,0.2,30,0.01,15,20,10,d))

def simVaryingV():
    for v in (5,10,20,40):
        print(simulazione(50,250,0.2,30,0.01,15,v,10,10))

def simVaryingM():
    for m in (0.01,0.05,0.1,0.2,0.5):
        print(simulazione(50,250,0.2,30,m,15,20,10,10))

def simVaryingC():
    for c in (1,10,20,40):
        print(simulazione(50,250,0.2,30,0.01,15,20,c,10))


