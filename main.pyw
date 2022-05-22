import tkinter.messagebox
from time import sleep
from tkinter import *
from forge import *

root = Tk()

promo_val = IntVar(root, 1)
radio_dict = {"0": "latest", "1": "recommended"}
dropdown_val = StringVar(root, value="1.18.2")


def startGeneration(info=ProjectInfo):
    if not checkValidModId(info):
        tkinter.messagebox.showinfo("Invalid ModId!", "Please enter a valid modid!")
        return

    zippath = downloadForgeZip(info)
    sleep(1)
    unzipFileAtPath(zippath)
    createNewDomain(info)
    changeTomlInfo(info)
    editMainModFile(info)

    tkinter.messagebox.showinfo("Success!", "Successfully generated project!")


def createWindow():
    root.title("Project Generator")
    #root.iconbitmap("app.ico")
    root.geometry('350x350')
    root.resizable(False, True)

    topFrame = Frame(root)
    topFrame.pack(side=TOP)

    projectInfoFrame = Frame(root)
    projectInfoFrame.pack(side=TOP)

    radioFrame = Frame(root)
    radioFrame.pack(side=TOP, pady=10)

    bottomFrame = Frame(root)
    bottomFrame.pack(side=BOTTOM)
    #
    #
    #
    ver_lab = Label(topFrame, text="Game Version:")
    ver_lab.pack(anchor=W, side=LEFT)

    mc_vers = OptionMenu(topFrame, dropdown_val, "1.18.2", "1.18.1", "1.16.5", "1.16.4", "1.16.3", "1.16.2", "1.16.1")
    mc_vers.pack()
    #
    #
    #
    name_lab = Label(projectInfoFrame, text="Mod Name:")
    name_lab.pack()
    modname_in = Entry(projectInfoFrame)
    modname_in.pack()

    modid_lab = Label(projectInfoFrame, text="Mod Identifier:")
    modid_lab.pack()
    modid_in = Entry(projectInfoFrame)
    modid_in.pack()

    author_lab = Label(projectInfoFrame, text="Mod Author:")
    author_lab.pack()
    author_in = Entry(projectInfoFrame)
    author_in.pack()

    license_lab = Label(projectInfoFrame, text="Mod License:")
    license_lab.pack()
    license_in = Entry(projectInfoFrame)
    license_in.pack()

    description_lab = Label(projectInfoFrame, text="Mod Description (may want to edit properly):")
    description_lab.pack()
    description_in = Entry(projectInfoFrame)
    description_in.pack()

    domain_lab = Label(projectInfoFrame, text="Domain (com.example.examplemod):")
    domain_lab.pack()
    domain_in = Entry(projectInfoFrame)
    domain_in.pack()
    #
    #
    #
    promo_lab = Label(radioFrame, text="Promotion:")
    promo_lab.pack(anchor=W, side=LEFT)

    latestradio = Radiobutton(radioFrame, variable=promo_val, text="Latest", justify=LEFT, value=0)
    latestradio.pack(anchor=W, side=LEFT)

    recommendedradio = Radiobutton(radioFrame, variable=promo_val, text="Recommended", justify=LEFT, value=1)
    recommendedradio.pack(anchor=E, side=RIGHT)
    #
    #
    #
    generate_button = Button(bottomFrame, command=lambda: startGeneration(
        ProjectInfo(
            dropdown_val.get(),
            radio_dict.get(str(promo_val.get())),
            name=modname_in.get(), modid=modid_in.get(), author=author_in.get(), license=license_in.get(),
            description=description_in.get(), domain=domain_in.get()
        )
    ), text="Generate!")
    generate_button.pack()

    root.mainloop()


createWindow()
