from .errors import NotEnoughItemsError, InvalidCommandType
from .command import Command

from getch import getch
import sys
import os
import shutil

class SelectionMenu:
    def __init__(self, *items, **kwargs):
        self.items = list(items)
        self.count = len(items) + 1
        self.index = 0
        self.activated_child = None
        self.parent = None
        self.is_prev = False

        self.title = kwargs.get("title")
        self.exit_cmd = True
        
        if kwargs.get("exit_cmd") == False and kwargs.get("exit_cmd") != None:
            self.count -= 1
            self.exit_cmd = False


        if self.count == 0:
            raise NotEnoughItemsError("Not enough items provided")

        for x in self.items:
            if not isinstance(x, Command) and not isinstance(x, SelectionMenu):
                raise InvalidCommandType(f"Item {self.items.index(x)} is type {type(x)} and is not a Command or SelectionMenu.")

            if isinstance(x, SelectionMenu):
                x.parent = self
                x.is_prev = True
        
        if self.exit_cmd: self.items.append(Command("Exit", self._exit))
        

    def _clear(self):
        if sys.platform == "win32":
            os.system("cls")
            return

        os.system("clear")

    def _select(self):
        if isinstance(self.items[self.index], Command):
            self._clear()
            self.items[self.index]._execute()
            return

        if isinstance(self.items[self.index], SelectionMenu):
            self.activated_child = self.items[self.index]

    def _menu_up(self):
        if self.index == 0:
            self.index = self.count - 1
            return
        
        self.index -= 1

    def _menu_down(self):
        if self.index == self.count - 1:
            self.index = 0
            return

        self.index += 1

    def _get_input(self):
        a = getch()

        if a == b'\x03':
            raise KeyboardInterrupt()

        if a == b'\x1a':
            raise EOFError()

        if a == b'\r':
            self._select()
            return

        if a == b'\x00' or b'\xe0':
            b = getch()

            if b == b'H': # Up
                self._menu_up()

            elif b == b'P': # Down
                self._menu_down()

            """elif b == b'K': # Left
                pass

            elif b == b'M': # Right
                pass"""

    def _print_title(self):
        x = f" {self.title} ".center(shutil.get_terminal_size().columns, "#") if self.title else "#"*shutil.get_terminal_size().columns
        print(x)

    def _exit(self):
        if self.parent:
            self.parent.activated_child = None
            return
        
        self._clear()
        sys.exit(0)

    def __str__(self):
        return self.title

    def run(self):
        while True:
            self._clear()
            self._print_title()
            if not self.activated_child:
                for i, item in enumerate(self.items):
                    if i == self.index:
                        print(f"> {item}")
                        continue
                    
                    print(f"  {item}")

                print("#"*shutil.get_terminal_size().columns)

                self._get_input()
            else:
                for i, item in enumerate(self.activated_child.items):
                    if i == self.activated_child.index:
                        print(f"> {item}")
                        continue
                    
                    print(f"  {item}")

                print("#"*shutil.get_terminal_size().columns)

                self.activated_child._get_input()

                
        