from time import sleep
from tkinter import *
from project import *
from forge import *

root = Tk()

promo_val = IntVar(root, 1)
radio_dict = {"0": "latest", "1": "recommended"}

dropdown_val = StringVar(root, value="1.18.2")

m_modname = ""
m_modid = ""
m_author = ""
m_license = ""
m_description = ""
m_domain = ""

def startGeneration():
    info = ProjectInfo (
        dropdown_val.get(),
        radio_dict.get(str(promo_val.get())),
        name=m_modname, modid=m_modid, author=m_author, license=m_license, description=m_description, domain=m_domain
    )
    zippath = downloadForgeZip(info)
    sleep(1)
    unzipFileAtPath(zippath)

def createWindow():
    root.title("Project Generator")
    root.iconbitmap("app.ico")
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
    name_lab = Label(projectInfoFrame, text = "Mod Name:")
    name_lab.pack()
    modname_in = Entry(projectInfoFrame)
    m_modname = modname_in.get()
    modname_in.pack()

    modid_lab = Label(projectInfoFrame, text = "Mod Identifier:")
    modid_lab.pack()
    modid_in = Entry(projectInfoFrame)
    m_modid = modid_in.get()
    modid_in.pack()

    author_lab = Label(projectInfoFrame, text = "Mod Author:")
    author_lab.pack()
    author_in = Entry(projectInfoFrame)
    m_author = author_in.get()
    author_in.pack()

    license_lab = Label(projectInfoFrame, text = "Mod License:")
    license_lab.pack()
    license_in = Entry(projectInfoFrame)
    m_license = license_in.get()
    license_in.pack()

    description_lab = Label(projectInfoFrame, text = "Mod Description (may want to edit properly):")
    description_lab.pack()
    description_in = Entry(projectInfoFrame)
    m_description = description_in.get()
    description_in.pack()

    domain_lab = Label(projectInfoFrame, text = "Domain (com.example.examplemod):")
    domain_lab.pack()
    domain_in = Entry(projectInfoFrame)
    m_domain = domain_in.get()
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
    generate_button = Button(bottomFrame, command=startGeneration, text="Generate!")
    generate_button.pack()

    root.mainloop()


createWindow()



    