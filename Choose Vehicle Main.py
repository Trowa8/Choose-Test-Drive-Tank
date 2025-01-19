from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import font
import os

directory = os.getcwd()

nation_full_names = {
    "us": "USA",
    "germ": "Germany",
    "ussr": "USSR",
    "uk": "United Kingdom",
    "jp": "Japan",
    "cn": "China",
    "it": "Italy",
    "fr": "France",
    "sw": "Sweden",
    "il": "Israel",
    "md": "Mad Thunder"
}

def select_directory():
    global WT_directory
    WT_directory = filedialog.askdirectory()
    if WT_directory:
        print(f"Selected directory: {WT_directory}")
        change()

def change():
    root1.destroy()
    create_second_window()

def create_second_window():
    global root2
    root2 = Tk()
    root2.geometry('450x180')  
    root2.resizable(False, False)  
    root2.title('Choose The Vehicle You Want To Test Drive')

    def read_tanks(nation):
        with open(fr'{directory}\Tanks\{nation}_tanks.txt', 'r') as f:
            tanks = [line.strip() for line in f.readlines()]
        return [name for tank in tanks for name in tank.split(',')]

    Nations = ["us", "germ", "ussr", "uk", "jp", "cn", "it", "fr", "sw", "il", "md"]

    selected_Nation = tk.StringVar(root2)
    selected_Nation.set(Nations[0])  

    selected_Tank = tk.StringVar(root2)
    selected_TankDefault = "<Choose Vehicle>"

    tanks = {nation: read_tanks(nation) for nation in Nations}
    
    def update_tank_menu(*args):
        selected_Tank.set(selected_TankDefault)
        for tank in tanks[selected_Nation.get()]:
            tank_menu['values'] = tuple(tank for tank in tanks[selected_Nation.get()])
            tank_menu.current(0)  
        aka_label.config(text=f"aka {nation_full_names[selected_Nation.get()]}")
        
    buttonUrl = tk.Button(root2, text="Youtube", command=lambda: open_website("https://www.youtube.com/@Ask3lad"))
    buttonUrl.place(x=10, y=10)

    faction_label = tk.Label(root2, text="Nation:")
    faction_label.pack()
    faction_menu = tk.OptionMenu(root2, selected_Nation, *Nations, command=update_tank_menu)
    faction_menu.pack()

    aka_font = font.Font(weight='bold', size=12)
    aka_label = tk.Label(root2, text="", font=aka_font)
    aka_label.place(x=260, y=24)

    tank_label = tk.Label(root2, text="Vehicle:")
    tank_label.pack(pady=7)
    
    tank_menu = ttk.Combobox(root2, textvariable=selected_Tank, width=30)
    tank_menu.state(['readonly'])
    tank_menu.pack()

    selected_Tank.set(selected_TankDefault)
    for tank in tanks[selected_Nation.get()]:
       tank_menu['values'] = tuple(tank for tank in tanks[selected_Nation.get()])
       tank_menu.current(0)  

    selected_Nation.trace('w', update_tank_menu)

    with open(f'{WT_directory}\\UserMissions\\Ask3lad\\ask3lad_testdrive.blk', 'r') as f:
        lines = f.readlines()

    CurrentTank = lines[171]
    print("Current Tank: " + CurrentTank)

    def take_input():
        if selected_Tank.get() == selected_TankDefault or selected_Tank.get() == '':
            print("Default Value Shall Not Pass")
        else:
            ChosenTank = "{}_{}".format(selected_Nation.get(), selected_Tank.get())
            lines[171] = 'weapons:t="{}_default"\n'.format(ChosenTank)
            with open(f'{WT_directory}\\UserMissions\\Ask3lad\\ask3lad_testdrive.blk', 'r') as f:
                file_contents = f.readlines()
            file_contents[171] = lines[171]
            with open(f'{WT_directory}\\UserMissions\\Ask3lad\\ask3lad_testdrive.blk', 'w') as f:
                f.writelines(file_contents)
            print(lines[171])
            lines[1] = 'include "#/develop/gameBase/gameData/units/tankModels/{}_{}.blk"'.format(selected_Nation.get(), selected_Tank.get())
            with open(f'{WT_directory}\\content\\pkg_local\\gameData\\units\\tankModels\\userVehicles\\us_m2a4.blk', 'w') as f:
                f.writelines(lines[1])
                print(lines[1])

    calculate_button = tk.Button(root2, text="Pick Vehicle", command=take_input)
    calculate_button.pack(pady=10)

    root2.mainloop()

root1 = Tk()
root1.geometry('500x200')  
root1.resizable(False, False)  
root1.title('Choose The Directory Of War Thunder')

folder_image = tk.PhotoImage(file="folder.png")
folder_image = folder_image.subsample(10, 10)

def browse_button():
    global WT_directory
    WT_directory = filedialog.askdirectory(title="Choose The Directory Of War Thunder")
    print(WT_directory)
    start_button.config(state='normal')

browse_button = tk.Button(root1, command=browse_button, image=folder_image, compound=tk.LEFT, width=100, height=100)
browse_button.place(x=188, y=20)

start_button = tk.Button(root1, text="Continue", command=change)
start_button.config(state='disabled')
start_button.place(x=210, y=130)

label = tk.Label(root1, text="Choose The Directory Of  War Thunder(Main Folder Named War Thunder)")
label.place(x=40, y=170)

root1.mainloop()


#Hello Person, i hope you like this little thing i made in 5 hours.
