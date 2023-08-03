import tkinter as tk
from tkinter import ttk

def create_card(root, image_path, song_name, keyboard, duration, row, image_list):
    # Carregar a imagem
    item_image = tk.PhotoImage(file=image_path)
    image_list.append(item_image)  # Adicionando à lista para evitar que seja coletado pelo garbage collector

    # Obter as dimensões da imagem
    image_width = item_image.width()
    image_height = item_image.height()

    # Criar um Canvas para o card com base no tamanho da imagem
    canvas = tk.Canvas(root, width=image_width, height=image_height)  # Adicionar altura extra para acomodar textos
    canvas.grid(row=row, column=0, padx=10)

    # Adicionar a imagem ao Canvas
    image_widget = canvas.create_image(image_width // 2, image_height // 2, image=item_image)

    # Criar o botão
    button_image = tk.PhotoImage(file="view/build/assets/frame0/card/button_1.png")
    button = tk.Button(
        canvas,
        image=button_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print(f"{song_name} button clicked"),
        relief="flat",
        activebackground="#138FFF"
    )
    button.image = button_image
    button.place(x=13, y=5, width=30, height=30)

    # Criar os textos
    canvas.create_text(
        100, 8, anchor="nw", text=song_name, fill="#FFFFFF", font=("Inter Bold", 10)
    )
    canvas.create_text(
        200, 8, anchor="nw", text=keyboard, fill="#FFFFFF", font=("Inter Bold", 10)
    )
    canvas.create_text(
        300, 8, anchor="nw", text=duration, fill="#D4EBFF", font=("Inter Bold", 10)
    )

# Exemplo de uso
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x400")

    # Exemplo de dados para os cards
    card_data = [
        {
            "image_path": "view/build/assets/frame0/card/image_1.png",
            "song_name": "Song 1",
            "keyboard": "Keyboard 1",
            "duration": "Duration 1",
        },
        {
            "image_path": "view/build/assets/frame0/card/image_1.png",
            "song_name": "Song 2",
            "keyboard": "Keyboard 2",
            "duration": "Duration 2",
        },
        # Adicione mais dados para mais cards
    ]

    # Lista para armazenar os PhotoImage
    image_list = []

    # Criar os cards com base nos dados fornecidos
    for i, data in enumerate(card_data):
        create_card(
            root, data["image_path"], data["song_name"], data["keyboard"], data["duration"], row=i, image_list=image_list
        )

    root.mainloop()
