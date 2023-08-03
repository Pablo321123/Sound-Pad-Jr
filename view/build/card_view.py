import tkinter as tk
from tkinter import ttk


class Card_View:
    def __init__(self, root) -> None:
        self.dic_card_data = {}
        self.lst_image = []
        self.imgContainer = None
        self.card_frame = None
        self.root = root

        self.root.tk.call("source", "themes\Forest-ttk-theme-master/forest-light.tcl")

        # Set the theme with the theme_use method
        style = ttk.Style(root)
        style.theme_use("forest-light")

    def on_click(self, songModel):
        modal = tk.Toplevel(self.root)
        modal.title("KeyBind")

        self.hotkey = None

        label = tk.Label(
            modal, text="Pressione a tecla desejada para definir o atalho:"
        )
        label.pack()

        # Função para tratar o evento de tecla pressionada e definir o atalho
        def on_key_press(event):
            self.hotkey = event.keysym
            print(f"Atalho escolhido: {self.hotkey}")
            modal.destroy()

        # Vincula a função on_key_press ao evento de tecla pressionada na janela modal
        modal.bind("<Key>", on_key_press)

        # Define o foco na janela modal ao clicar em qualquer local da tela
        modal.grab_set()

        # Espera até que a janela modal seja fechada
        modal.wait_window()

        if self.hotkey:
            self.mpc.createKeyBind(self.hotkey, songModel.name)           
        
        
        print(self.hotkey)

    def create_card(self, mpc, dic_card_data, imgContainer):
        image_width = 0
        image_height = 0
        self.dic_card_data = dic_card_data
        self.imgContainer = imgContainer
        self.mpc = mpc

        # Criar um Frame para o card
        self.card_frame = ttk.Frame(self.root)
        self.card_frame.pack(anchor="w", pady=103, padx=110)
        
        # Criar um Canvas para conter os cards
        canvasFrame = tk.Canvas(self.card_frame, highlightthickness=0)
        canvasFrame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Configuração da Scroll Bar no Frame
        scrollBar = ttk.Scrollbar(
            self.card_frame,
            orient="vertical",
            command=canvasFrame.yview,
            style="TScrollbar",
        )
        scrollBar.pack(side="right", fill="y")

        canvasFrame.configure(yscrollcommand=scrollBar.set)
        canvasFrame.bind(
            "<Configure>",
            lambda event: canvasFrame.configure(scrollregion=canvasFrame.bbox("all")),
        )

        # Frame que conterá os cards dentro do Canvas
        card_container = ttk.Frame(canvasFrame)
        canvasFrame.create_window((0, 0), window=card_container, anchor=tk.NW)

        for row, data in enumerate(self.dic_card_data):
            # Carregar a imagem
            bg_card_image = tk.PhotoImage(file=dic_card_data[data].bgimage_path)
            self.lst_image.append(bg_card_image)

            # Obter as dimensões da imagem
            image_width = bg_card_image.width()
            image_height = bg_card_image.height()

            # Criar um Canvas para o card com base no tamanho da imagem
            canvas = tk.Canvas(
                card_container,
                width=image_width,
                height=image_height,
                background="white",
                highlightthickness=0,
            )
            canvas.pack(anchor="w", pady=0, padx=0)

            # Adicionar a imagem ao Canvas
            image_widget = canvas.create_image(
                image_width // 2,
                image_height // 2,
                image=bg_card_image,
            )

            # Criar o botão
            button_image = tk.PhotoImage(
                file="view/build/assets/frame0/card/button_1.png"
            )
            button = tk.Button(
                canvas,
                image=button_image,
                borderwidth=0,
                highlightthickness=0,
                command=lambda songName=self.dic_card_data[data].name: mpc.play(
                    songName
                ),
                # command=lambda row=row: print(f"{row} button clicked"),
                relief="flat",
                activebackground="#138FFF",
            )
            button.image = button_image
            button.place(x=13, y=5, width=30, height=30)

            # Criar os textos
            canvas.create_text(
                50,
                12,
                anchor="nw",
                text=data,
                fill="#FFFFFF",
                font=("Inter Bold", 10),
            )
            canvas.create_text(
                300,
                12,
                anchor="nw",
                text=f"{float(dic_card_data[data].duration):.2f}",
                fill="#FFFFFF",
                font=("Inter Bold", 10),
            )

            entry_image_1 = tk.PhotoImage(
                file="view\\build\\assets\\frame0\card\entry_1.png"
            )
            self.lst_image.append(
                entry_image_1
            )  # Impedir que o garbage do python colete a imagem e não a mostre!
            entry_bg_1 = canvas.create_image(380, 20.0, image=entry_image_1)

            text = tk.StringVar()
            text.set(
                dic_card_data[data].keybind if dic_card_data[data].keybind else "Key"
            )
            entry = tk.Entry(
                canvas,
                textvariable=text,
                bg="#FFFFFF",
                border=0,
                highlightthickness=1,
                highlightcolor="#117fe3",
                foreground="#117fe3",
                readonlybackground="#FFFFFF",
                state="readonly",             
                justify="center"   
            )
            entry.place(x=365, y=10, width=30, height=20)
            # <FocusIn>
            entry.bind(
                "<Button-1>",
                lambda event, d=data: self.on_click(self.dic_card_data[d]),
            )
            
            button_image = tk.PhotoImage(
                file="view/build/assets/frame0/card/button_trash.png"
            )
            button = tk.Button(
                canvas,
                image=button_image,
                borderwidth=0,
                highlightthickness=0,
                command=lambda songName=data: mpc.deleteSong(
                    songName
                ),
                # command=lambda row=row: print(f"{row} button clicked"),
                relief="flat",
                activebackground="#138FFF",
            )
            button.image = button_image
            button.place(x=415, y=5, width=30, height=30)

        canvasFrame.config(width=image_width, height=self.imgContainer.height())

    def clearCards(self):
        self.card_frame.destroy()

    # retorna o container que contém os cards
    def getCanvaFrame(self):
        return self.card_frame
