import keyboard
from Opcoes import Opcoes

class MainMenu:
    def __init__(self, *args, **kwargs):
        self.__selected = 1
        self.menu_options = { 1:"Novo Cliente", 2:"Apaga Cliente", 3:"Debita", 4:"Deposita", 5:"Saldo", 6:"Extrato", 7:"Sai"}

    def loop(self):
        while True:
            self.__get_selection()
            if self.__selected == 7:
                break
            else:
                self.__execute_action()
    
    def __get_selection(self):
        keyboard.add_hotkey('up', self.__up)
        keyboard.add_hotkey('down', self.__down)
        self.__show_menu()
        keyboard.wait('enter', True)
        keyboard.remove_all_hotkeys()

    def __show_menu(self):
        print("\n" * 100)
        print("Escolha uma opção e pressione Enter:")
        for key, value in self.menu_options.items():
            print("{4}{2}    {0} - {1}    {3}"
                  .format(  0 if key == 7 else key, value,
                         "->" if self.__selected == key else " ",
                         "<-" if self.__selected == key else " ",
                         "\n" if key == 7 else ""))

    def __up(self):
        if self.__selected == 1:
            return
        self.__selected -= 1
        self.__show_menu()

    def __down(self):
        if self.__selected == len(self.menu_options):
            return
        self.__selected += 1
        self.__show_menu()

    def __execute_action(self):
        Opcoes(self.__selected).execute_action()
  

MainMenu().loop()

