import customtkinter

customtkinter.set_appearance_mode("system") #"dark", "ligth"
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350") #LxA


def login():
    print("test")


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)


label = customtkinter.CTkLabel(master=frame, text="Login System", font=("Roboto", 24))
label.pack(pady=12, padx=10)

fld_login = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
fld_login.pack(pady=12, padx=10)

fld_password = customtkinter.CTkEntry(
    master=frame, placeholder_text="Username", show="*"
)
fld_password.pack(pady=12, padx=10)

chk_remember = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
chk_remember.pack(pady=12, padx=10)

btn_login = customtkinter.CTkButton(master=frame, text="login", command=login)
btn_login.pack(pady=12, padx=10)

root.mainloop()
