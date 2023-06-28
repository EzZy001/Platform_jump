import random
import tkinter as tk

okno = tk.Tk()
okno.resizable(False, False)
canvas = tk.Canvas(okno, width=800, height=600, bg='black')

left = True    
left1 = False  
left2 = True   
counter1 = 0  
loose_inf = 0 
counter2 = 0

def pozadie():
    global ids
    ids = []
    for i in range(500):
        n_x = random.randint(0, 800)
        n_y = random.randint(0, 600)
        item_id = canvas.create_text(n_x, n_y, fill='yellow', text='*')
        ids.append(item_id)

def pohyb_pozadie():
    for item_id in ids:
        poz = canvas.coords(item_id)
        if poz[1] < 600.0:
            canvas.move(item_id, 0, 1)
        else:
            canvas.move(item_id, 0, -600)
    okno.after(10, pohyb_pozadie)

def loose():
    try:
        global counter2
        global loose_inf
        pos = canvas.coords('lopta')
        if pos[1] > 600:
            canvas.delete('lopta')
            canvas.create_text(400, 300, text = 'YOU LOST!', font = 'Arial 50 bold', fill = 'red', tag = 'prehra_text_1')
            canvas.create_text(400, 400, text = f'Your score was: {counter2}', font = 'Arial 10 bold', fill = 'white', tag = 'prehra_text_2')
            canvas.create_text(400, 550, text = 'Try again...', font = 'Arial 10 bold', fill = 'white')
            loose_inf = 1
            conter2 = 0
            canvas.after(5, loose)
        else:
            canvas.after(5, loose)
    except IndexError:
        pass

def platforma():
    canvas.create_rectangle(350, 200, 450, 220, fill = 'blue',tag = 'platforma1')
    canvas.create_rectangle(350, 350, 450, 370, fill = 'blue',tag = 'platforma2')
    canvas.create_rectangle(350, 490, 450, 510, fill = 'blue',tag = 'platforma3')
    
def lopta():
    canvas.create_oval(390, 460, 420, 490, fill = 'green', tag = 'lopta')
    
def lopta_movement_left(event):
    canvas.move('lopta', -6, 0)
    
def lopta_movement_right(event):
    canvas.move('lopta', 6, 0)

def score():
    global counter2
    canvas.delete('text9')
    canvas.create_text(400, 30, text = f'Score: {counter2}', fill = 'white',
                       font = 'Arial 16 bold', tag = 'text9')
    canvas.after(10, score)

def bounce1():
    lopta_c = canvas.coords('lopta')
    p1_coords = canvas.coords('platforma1')
    p2_coords = canvas.coords('platforma2')
    p3_coords = canvas.coords('platforma3')
    global counter1
    counter1 += 1    
    canvas.move('lopta', 0, -1)
    
    if counter1 == 180:
        canvas.after(5, bounce2)
    else:
        canvas.after(5, bounce1)

def bounce2():
    try:
        lopta_c = canvas.coords('lopta')
        p1_coords = canvas.coords('platforma1')
        p2_coords = canvas.coords('platforma2')
        p3_coords = canvas.coords('platforma3')
        global counter1
        global counter2

        canvas.move('lopta', 0, 1)
        if lopta_c[3] == p1_coords[1] and lopta_c[0] + 15 >= p1_coords[0] and lopta_c[2] - 15 <= p1_coords[2]:
            counter1 = 0
            counter2 += 1
            canvas.after(1, bounce1)
        elif lopta_c[3] == p2_coords[1] and lopta_c[0] + 15 >= p2_coords[0] and lopta_c[2] - 15 <= p2_coords[2]:
            counter1 = 0
            counter2 += 1
            canvas.after(1, bounce1)
        elif lopta_c[3] == p3_coords[1] and lopta_c[0] + 15 >= p3_coords[0] and lopta_c[2] - 15 <= p3_coords[2]:
            counter1 = 0
            counter2 += 1
            canvas.after(1, bounce1)
        else:
            canvas.after(1, bounce2)          
    except IndexError:
        pass

def pohyb_platforma_dole1():
    p1_coords = canvas.coords('platforma1')


    if p1_coords[1] <= 600.0:
        canvas.move('platforma1', 0, 1)
        
    else:
        canvas.move('platforma1', 0, -500)
        
        
    okno.after(10, pohyb_platforma_dole1)
    
def pohyb_platforma_dole2():
    p2_coords = canvas.coords('platforma2')

    if p2_coords[1] <= 600.0:
        canvas.move('platforma2', 0, 1)
        
    else:
        canvas.move('platforma2', 0, -500)
        
    okno.after(10, pohyb_platforma_dole2)
    
def pohyb_platforma_dole3():
    p3_coords = canvas.coords('platforma3')
    if p3_coords[1] <= 600.0:
        canvas.move('platforma3', 0, 1)
        
    else:
        canvas.move('platforma3', 0, -500)
                
    okno.after(10, pohyb_platforma_dole3)

def pohyb_platforma():
    global left
    global left1
    global left2
    p1_coords = canvas.coords('platforma1')
    p2_coords = canvas.coords('platforma2')
    p3_coords = canvas.coords('platforma3')

    if left:
        if p1_coords[2] < 750:
            canvas.move('platforma1', 1, 0)
        else:
            left = False
    else:
        if p1_coords[0] > 50:
            canvas.move('platforma1', -1, 0)
        else:
            left = True
    if left1:
        if p2_coords[2] < 750:
            canvas.move('platforma2', 1, 0)
        else:
            left1 = False
    else:
        if p2_coords[0] > 50:
            canvas.move('platforma2', -1, 0)
        else:
            left1 = True
    if left2:
        if p3_coords[2] < 750:
            canvas.move('platforma3', 1, 0)
        else:
            left2 = False
    else:
        if p3_coords[0] > 50:
            canvas.move('platforma3', -1, 0)
        else:
            left2 = True
            
    canvas.after(5, pohyb_platforma)

def game_restart(event):
    global loose_inf
    if loose_inf > 0:
        okno.destroy()

canvas.bind_all('<Left>', lopta_movement_left)
canvas.bind_all('<Right>', lopta_movement_right)
canvas.bind_all('<Key>', game_restart)


canvas.pack()
pozadie()
pohyb_pozadie()
platforma()
score()
pohyb_platforma()
lopta()
bounce1()
pohyb_platforma_dole1()
pohyb_platforma_dole2()
pohyb_platforma_dole3()
loose()

okno.mainloop()
