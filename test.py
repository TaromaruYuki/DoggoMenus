import doggomenus

x = 0

def atx():
    global x
    x += 1

def aatx():
    am = input("Amount > ")

    try:
        am = int(am)
    except ValueError:
        print("Not a number!")
        return

    global x
    x += am
    print("Done!")

def stuck():
    return

def select():
    print("Selected!")

def move():
    print("move!")

var1 = doggomenus.Command("Add +1 to x", atx)
var2 = doggomenus.Command("Add a amount to x", aatx, pause=True)
showvar = doggomenus.Command("Show x", lambda: print(x), pause=True)
menuvar = doggomenus.SelectionMenu(var1, var2, showvar, title="Variable Testing")

stuckcmd = doggomenus.Command("You are stuck... Have fun :)", stuck)
stuckmenu = doggomenus.SelectionMenu(stuckcmd, title="???", exit_cmd=False)

menu = doggomenus.SelectionMenu(menuvar, stuckmenu, title="Example menu")
menu.run(on_select=select, on_move=move)