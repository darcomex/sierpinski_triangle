from tkinter import *

def reset():
    global point_a, point_b, point_c,point_a_sub,point_b_sub,point_c_sub
    point_a = [-1, -1]
    point_b = [-1, -1]
    point_c = [-1, -1]
    point_a_sub = [250, 250]
    point_b_sub = [250, 250]
    point_c_sub = [250, 250]
    can.delete(ALL)
    point_b_endroit.place_forget()
    point_c_endroit.place_forget()
    bouton_confirmer.place_forget()
    bouton_recommencer.place_forget()
    bouton_suivant.place_forget()
    bouton_precedent.place_forget()
    bouton_actualiser.place_forget()
    entree_etape.place_forget()
    entree_etape.delete(0, END)
    entree_etape.insert(0, '0')
    texte_placer_point.config(text = 'Veuillez placer le point A :')
    texte_placer_point.place(x = 175, y = 2)
    point_a_endroit.place(x=250,y=250)
def demarrage():

    global point_a, point_b, point_c
    point_a_endroit.place_forget()
    point_b_endroit.place_forget()
    point_c_endroit.place_forget()
    sierpinski(0, point_a, point_b, point_c)
    bouton_confirmer.place_forget()
    bouton_recommencer.place_forget()
    bouton_precedent.place(x = 0, y = 475)
    entree_etape.place(x = 64, y = 475)
    bouton_suivant.place(x = 90, y = 475)
    bouton_recommencer.place(x = 413, y = 475)
    bouton_actualiser.place(x = 200, y = 475)

def placer_point(event):
    global point_a, point_b, point_c, point_a_sub, point_b_sub, point_c_sub
    if(point_a[0] == -1 and point_a[1] == -1):
        point_a = point_a_sub
        texte_placer_point.config(text = 'Veuillez placer le point B : ') 
        point_a_endroit.place(x = point_a[0], y = point_a[1])
        point_b_endroit.place(x = 250, y = 250)
    elif(point_b[0] == -1 and point_b[1] == -1): 
        point_b = point_b_sub
        texte_placer_point.config(text = 'Veuillez placer le point C : ') 
        point_b_endroit.place(x = point_b[0], y = point_b[1])
        point_c_endroit.place(x = 250, y = 250)
    elif(point_c[0] == -1 and point_c[1] == -1): 
        point_c = point_c_sub
        point_c_endroit.place(x = point_c[0], y = point_c[1])
        texte_placer_point.place_forget()
        bouton_recommencer.place(x = 0, y = 475)
        bouton_confirmer.place(x = 435, y = 475)
        
def deplacer_croix_left(event):
    print('ta gauche')
    global point_a, point_b, point_c, point_a_sub, point_b_sub, point_c_sub
    if(point_a[0] == -1 and point_a[1] == -1):
        if(point_a_sub[1] <= 500):
            point_a_sub = [point_a_sub[0]-10, point_a_sub[1]]
            point_a_endroit.place(x = point_a_sub[0], y = point_a_sub[1])
    elif(point_b[0] == -1 and point_b[1] == -1):
        if(point_b_sub[1] <= 500):
            point_b_sub = [point_b_sub[0]-10, point_b_sub[1]]
            point_b_endroit.place(x = point_b_sub[0], y = point_b_sub[1])
    elif(point_c[0] == -1 and point_c[1] == -1):
        if(point_c_sub[1] <= 500):
            point_c_sub = [point_c_sub[0]-10, point_c_sub[1]]
            point_c_endroit.place(x = point_c_sub[0], y = point_c_sub[1])
    
def deplacer_croix_right(event):
    global point_a, point_b, point_c, point_a_sub, point_b_sub, point_c_sub
    if(point_a[0] == -1 and point_a[1] == -1):
        if(point_a_sub[1] <= 500):
            point_a_sub = [point_a_sub[0]+10, point_a_sub[1]]
            point_a_endroit.place(x = point_a_sub[0], y = point_a_sub[1])
    elif(point_b[0] == -1 and point_b[1] == -1):
        if(point_b_sub[1] <= 500):
            point_b_sub = [point_b_sub[0]+10, point_b_sub[1]]
            point_b_endroit.place(x = point_b_sub[0], y = point_b_sub[1])
    elif(point_c[0] == -1 and point_c[1] == -1):
        if(point_c_sub[1] <= 500):
            point_c_sub = [point_c_sub[0]+10, point_c_sub[1]]
            point_c_endroit.place(x = point_c_sub[0], y = point_c_sub[1])
def deplacer_croix_top(event):
    global point_a, point_b, point_c, point_a_sub, point_b_sub, point_c_sub
    if(point_a[0] == -1 and point_a[1] == -1):
        if(point_a_sub[1] <= 500):
            point_a_sub = [point_a_sub[0], point_a_sub[1]-10]
            point_a_endroit.place(x = point_a_sub[0], y = point_a_sub[1])
    elif(point_b[0] == -1 and point_b[1] == -1):
        if(point_b_sub[1] <= 500):
            point_b_sub = [point_b_sub[0], point_b_sub[1]-10]
            point_b_endroit.place(x = point_b_sub[0], y = point_b_sub[1])
    elif(point_c[0] == -1 and point_c[1] == -1):
        if(point_c_sub[1] <= 500):
            point_c_sub = [point_c_sub[0], point_c_sub[1]-10]
            point_c_endroit.place(x = point_c_sub[0], y = point_c_sub[1])

def deplacer_croix_down(event):
    global point_a, point_b, point_c, point_a_sub, point_b_sub, point_c_sub
    if(point_a[0] == -1 and point_a[1] == -1):
        if(point_a_sub[1] <= 450):
            point_a_sub = [point_a_sub[0], point_a_sub[1]+10]
            point_a_endroit.place(x = point_a_sub[0], y = point_a_sub[1])
    elif(point_b[0] == -1 and point_b[1] == -1):
        if(point_b_sub[1] <= 450):
            point_b_sub = [point_b_sub[0], point_b_sub[1]+10]
            point_b_endroit.place(x = point_b_sub[0], y = point_b_sub[1])
    elif(point_c[0] == -1 and point_c[1] == -1):
        if(point_c_sub[1] <= 450):
            point_c_sub = [point_c_sub[0], point_c_sub[1]+10]
            point_c_endroit.place(x = point_c_sub[0], y = point_c_sub[1])


point_a_sub = [250, 250]
point_b_sub = [250, 250]
point_c_sub = [250, 250]
point_a = [-1, -1]
point_b = [-1, -1]
point_c = [-1, -1]
    
    
def reculer_etape():
    nombre_etape = 0
    try: 
        nombre_etape = int(entree_etape.get())
    except: 
        entree_etape.delete(0, END)
        entree_etape.insert(0, '0')
    if(nombre_etape > 0): 
        entree_etape.delete(0, END)
        entree_etape.insert(0, str(nombre_etape-1))
        can.delete(ALL)
        sierpinski(nombre_etape-1, point_a, point_b, point_c)

def avancer_etape():

    nombre_etape = 0
    try:
        nombre_etape = int(entree_etape.get())
    except:
        entree_etape.delete(0, END)
        entree_etape.insert(0, '0')
    entree_etape.delete(0, END)
    entree_etape.insert(0, str(nombre_etape+1))
    can.delete(ALL)
    sierpinski(nombre_etape+1, point_a, point_b, point_c)

def actualiser():
    nombre_etape = 0
    try:
        nombre_etape = int(entree_etape.get())
    except:
        entree_etape.delete(0, END)
        entree_etape.insert(0, '0')
    if(nombre_etape >= 0): 
        can.delete(ALL)
        sierpinski(nombre_etape, point_a, point_b, point_c)
    else: 
        entree_etape.delete(0, END)
        entree_etape.insert(0, '0')

def milieu(point_1, point_2):

    return [(point_1[0]+point_2[0])/2, (point_1[1]+point_2[1])/2]

def sierpinski(etape, point_a, point_b, point_c):

    if(etape == 0):
        can.create_polygon(point_a, point_b, point_c, fill = "yellow")
        return etape
    else:
        point_d = milieu(point_a,point_b)
        point_e = milieu(point_b,point_c)
        point_f = milieu(point_c,point_a)
        
        sierpinski(etape-1, point_a, point_d, point_f) 
        sierpinski(etape-1, point_d, point_b, point_e) 
        sierpinski(etape-1, point_f, point_e, point_c)

fen = Tk()
fen.title("Triangle de Sierpinski (Marwan)")
can = Canvas(fen)
fen.config(width = 500, height = 500, bg = 'yellow')
can.config(width = 500, height = 473, bg = 'grey')
can.place(x = 0, y = 0)

texte_placer_point = Label(can, text = 'Veuillez placer le point A :', bg = 'grey', font = ("", 10, ""))
texte_placer_point.place(x = 175, y = 2)


point_a_endroit = Label(can, text = 'x', bg = 'grey')
point_b_endroit = Label(can, text = 'x', bg = 'grey')
point_c_endroit = Label(can, text = 'x', bg = 'grey')


bouton_confirmer = Button(fen, text = 'Confirmer',bg='grey', command = demarrage)
bouton_recommencer = Button(fen, text = 'Recommencer',bg='grey', command = reset)
bouton_precedent = Button(fen, text = 'Précédent',bg='grey', command = reculer_etape)
bouton_suivant = Button(fen, text = 'Suivant',bg='grey', command = avancer_etape)
bouton_actualiser = Button(fen, text = 'Actualiser',bg='grey', command = actualiser)
entree_etape = Entry(fen, width = 2, font = ('', 14, ''), bg = 'yellow')
entree_etape.insert(0, '0')

fen.bind('<Left>',deplacer_croix_left)
fen.bind('<Right>',deplacer_croix_right)
fen.bind('<Down>',deplacer_croix_down)
fen.bind('<Up>',deplacer_croix_top)
fen.bind('<Return>',placer_point)
fen.mainloop()