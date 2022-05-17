import tkinter as tk

window = tk.Tk()

verdrop = tk.StringVar(window).set("Enter Version")

promo_ver_type = tk.IntVar(window).set(1)

def setupWindowBasics():
    window.title("Forge Mod Project Generator")
    window.geometry('350x200')
    window.iconbitmap('app.ico')

    version_drop_down = tk.OptionMenu(window, verdrop, "")
    version_drop_down.pack()

    latest_radio = tk.Radiobutton(window, text="Latest", variable=promo_ver_type, value=0).pack()
    recommended_radio = tk.Radiobutton(window, text="Recommended", variable=promo_ver_type, value=1).pack()

    window.mainloop()


