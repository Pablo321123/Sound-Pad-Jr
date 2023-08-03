import tkinter as tk
from tkinter import ttk

import sys
import os

# Obtém o caminho absoluto para a pasta_principal
pasta_principal_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(pasta_principal_path)


def create_card(root, item_name):
     # Criar um Frame que representa o card
    card_frame = ttk.Frame(root, relief="raised", borderwidth=2)
    card_frame.pack(padx=10, pady=10)

    # Adicionar a imagem de fundo usando o Canvas
    canvas = tk.Canvas(card_frame, width=300, height=200)
    canvas.grid(row=0, column=0)

    # Carregar a imagem de fundo
    filePath = "view\\build\\assets\\frame0\\card\\image_1.png"
    item_image = tk.PhotoImage(file=filePath)
    imagem_card = canvas.create_image(0, 0, anchor=tk.NW, image=item_image)

    # Adicionar rótulo ao card
    card_label = ttk.Label(card_frame, text=item_name)
    card_label.grid(row=1, column=0, padx=(0, 5), sticky=tk.W)

    # Adicionar botão ao card
    button = ttk.Button(
        card_frame,
        text="Botão",
        command=lambda: print(f"{item_name} clicked"),
    )
    button.grid(row=1, column=1, padx=(0, 5))

    # Adicionar botão de opção (Radio button) ao card
    card_radio_button = ttk.Radiobutton(card_frame, text=item_name)
    card_radio_button.grid(row=1, column=2, padx=(0, 5))


def main():
    items = [
        "Item 1",
        "Item 2",
        "Item 3",
        "Item 4",
        "Item 5",
        "Item 6",
        "Item 7",
        "Item 8",
        "Item 9",
        "Item 10",
        "Item 11",
        "Item 12",
        "Item 13",
        "Item 14",
        "Item 15",
        "Item 16",
        "Item 17",
        "Item 18",
        "Item 19",
        "Item 20",
    ]

    root = tk.Tk()
    root.title("Tkinter CardView Example")

    # Import the tcl file
    root.tk.call("source", "themes\Forest-ttk-theme-master/forest-light.tcl")

    # Set the theme with the theme_use method
    style = ttk.Style(root)
    style.theme_use("forest-light")

    # Criação do Canva
    canvas = tk.Canvas(root)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # ScrollBar
    scrollbar = ttk.Scrollbar(root, command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # Configuração da Scroll Bar no Frame
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind(
        "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    # adição do frame dentro do containner
    frame_container = tk.Frame(canvas, bg="white")
    canvas.create_window((0, 0), window=frame_container, anchor="nw")

    for item_name in items:
        create_card(frame_container, item_name)

    root.mainloop()


if __name__ == "__main__":
    main()
