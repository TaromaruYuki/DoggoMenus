# DoggoMenus

A basic console menu system for Python!

## Command
This makes a command for a SelectionMenu
```python
import doggomenus

cmd = doggomenus.Command("Title / Name here", function_here)
# Optional Params
# Pause: Pause when command has finished executing
```

## SelectionMenu
The selection menu. Valid menu items are Command and SelectionMenu
```python
import doggomenus

cmd = doggomenus.Command("Say hi", lambda: print("Hello there!"), pause=True)

menu = doggomenus.SelectionMenu(cmd)
# Optional Params
# title - Set a title for the menu. This title will be used like a Command title if the SelectionMenu is a Selection menu item.
# exit_cmd - Toggle the exit option for the menu. Defaults to True.

menu.run()
```

## Example
```python
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

var1 = doggomenus.Command("Add +1 to x", atx)
var2 = doggomenus.Command("Add a amount to x", aatx, pause=True)
showvar = doggomenus.Command("Show x", lambda: print(x), pause=True)
menuvar = doggomenus.SelectionMenu(var1, var2, showvar, title="Variable Testing")

stuckcmd = doggomenus.Command("You are stuck... Have fun :)", stuck)
stuckmenu = doggomenus.SelectionMenu(stuckcmd, title="???", exit_cmd=False)

menu = doggomenus.SelectionMenu(menuvar, stuckmenu, title="Example menu")
menu.run()
```

# Build from source
On Windows you can run `install.bat` in cmd

On Linux and Mac you can run `install.sh` in a terminal