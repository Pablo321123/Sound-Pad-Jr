import sys
import os

# Obtém o caminho absoluto para a pasta_principal
pasta_principal_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.append(pasta_principal_path)

# Agora podemos importar o módulo Controller corretamente
from model.mediaPlayerModel import MediaPlayerModel

from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import ttk
from view.build.card_view import Card_View
from observer.observers import Observer

from ctypes import windll

GWL_EXSTYLE = -20
WS_EX_APPWINDOW = 0x00040000
WS_EX_TOOLWINDOW = 0x00000080


class MainView(Observer):
    def __init__(self) -> None:
        self.mpc = None
        self.fileControl = None
        self.cv: Card_View = None

    def startApp(self, controller, fileControl) -> None:
        self.mpc = controller
        self.fileControl = fileControl

        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path(
            r"D:\Projetos\Python\5 - SoundPad Jr\view\build\assets\frame0"
        )

        self.root = Tk()
        self.root.geometry("850x580")
        # Definindo o tamanho da barra de título como zero e tornando a janela transparente
        self.root.overrideredirect(1)
        self.root.wm_attributes("-transparentcolor", "blue")
        self.root.after(10, self.set_appwindow, self.root)

        # Definindo um ícone personalizado para a janela
        # icon_path = self.relative_to_assets("win_logo.ico")
        # self.root.iconbitmap(icon_path)

        # Definindo um ícone personalizado para a janela
        icon_photo = PhotoImage(file=self.relative_to_assets("win_logo.png"))
        self.root.iconphoto(False, icon_photo)
        # self.root.configure(bg="#138FFF")

        style = ttk.Style(self.root)
        # self.root.call("source", "forest-dark.tcl")
        # style.theme_use("dark-blue")

        frame = ttk.Frame(self.root)
        frame.pack()

        canvas = Canvas(
            self.root,
            bg="#138FFF",
            height=580,
            width=850,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )

        canvas.bind("<B1-Motion>", self.move_app)

        canvas.place(x=0, y=0)

        img_logo = PhotoImage(file=self.relative_to_assets(path="logo.png"))
        logo = canvas.create_image(85, 20, image=img_logo)

        image_image_1 = PhotoImage(file=self.relative_to_assets(path="image_1.png"))
        image_1 = canvas.create_image(425.0, 290.0, image=image_image_1)

        image_image_2 = PhotoImage(file=self.relative_to_assets("image_2.png"))
        image_2 = canvas.create_image(344.0, 290.0, image=image_image_2)

        # Carregar os Cards
        self.cv = Card_View(self.root)
        try:
            # card_data recebe a lista de sons salvos anteriormente
            card_data = fileControl.readFile()
            self.cv.create_card(self.mpc, card_data, image_image_2)
            self.mpc.loadSong(card_data)
        except FileNotFoundError as f:
            print("Arquivo de persistencia de dados não encontrado")
            print(f)

        button_image_5 = PhotoImage(file=self.relative_to_assets("button_5.png"))
        button_5 = Button(
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.exit_onClick(),
            relief="flat",
            activebackground="#117FE3",
        )
        button_5.place(x=811.0, y=11.0, width=30.0, height=30.0)

        # Pause Button
        button_image_1 = PhotoImage(file=self.relative_to_assets("button_2.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.mpc.pause(),
            relief="flat",
            activebackground="#117FE3",
        )
        button_1.place(x=615.0, y=209.0, width=161.0, height=41.0)

        # RESUME Button
        button_image_2 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.mpc.resume(),
            relief="flat",
            activebackground="#117FE3",
        )
        button_2.place(x=615.0, y=152.0, width=161.0, height=41.0)

        # ADD SONG BUTTON
        button_image_4 = PhotoImage(file=self.relative_to_assets("button_4.png"))
        button_4 = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.mpc.addMusic(),
            relief="flat",
            activebackground="#117FE3",
        )
        button_4.place(x=615.0, y=95.0, width=161.0, height=41.0)

        # Txt and Sound Mode
        button_sound = PhotoImage(file=self.relative_to_assets(path="sound.png"))
        button_txt = PhotoImage(file=self.relative_to_assets(path="txt.png"))
        self.img_button_mode = [button_sound, button_txt]
        currentImage = self.mpc.getMode()

        self.button_sound_1 = Button(
            image=self.img_button_mode[currentImage],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.changeMode(),
            relief="flat",
            activebackground="#117FE3",
        )
        self.button_sound_1.place(x=615.0, y=266.0, width=154.0, height=44.0)

        # -------------------------

        self.root.resizable(False, False)
        self.root.mainloop()

    def change_image(self):
        currentImage = self.mpc.getMode()
        print(currentImage)

        self.button_sound_1.destroy()
        self.button_sound_1 = Button(
            image=self.img_button_mode[currentImage],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.changeMode(),
            relief="flat",
            activebackground="#117FE3",
        )
        self.button_sound_1.place(x=615.0, y=266.0, width=154.0, height=44.0)
    
    def changeMode(self):
        self.mpc.changeMode()
        self.change_image()        

    def set_appwindow(self, root):
        hwnd = windll.user32.GetParent(root.winfo_id())
        style = windll.user32.GetWindowLongPtrW(hwnd, GWL_EXSTYLE)
        style = style & ~WS_EX_TOOLWINDOW
        style = style | WS_EX_APPWINDOW
        res = windll.user32.SetWindowLongPtrW(hwnd, GWL_EXSTYLE, style)
        # re-assert the new window style
        self.root.withdraw()
        self.root.after(10, root.deiconify)

    def exit_onClick(self):
        self.mpc.persistAddedSongs()
        self.root.quit()

    def move_app(self, e):
        self.root.geometry(f"+{e.x_root}+{e.y_root}")

    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    def update(self, mode=None):
        
        if mode is not None:
            self.change_image()
        else:
            image_image_2 = PhotoImage(file=self.relative_to_assets("image_2.png"))

            if self.cv.getCanvaFrame():
                self.cv.clearCards()
            self.cv.create_card(self.mpc, self.mpc.loadSong(), image_image_2)

        
