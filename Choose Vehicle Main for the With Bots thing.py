from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import font
import os

directory = os.getcwd()

#All the decoded Nation names
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

#Event that selects the WT directoryS
def select_directory():
    global WT_directory
    WT_directory = filedialog.askdirectory()
    if WT_directory:
        print(f"Selected directory: {WT_directory}")
        change()

#Thing that destroys the first window
def change():
    root1.destroy()
    create_second_window()

#Thing that creates the second(Main) window
def create_second_window():
    global root2
    root2 = Tk()
    root2.geometry('450x180')  
    root2.resizable(False, False)  
    root2.title('Choose The Vehicle You Want To Test Drive')

    # Function to read tanks from a file
    def read_tanks(nation):
        with open(fr'{directory}\Tanks\{nation}_tanks.txt', 'r') as f:
            tanks = [line.strip() for line in f.readlines()]
        return [name for tank in tanks for name in tank.split(',')]

    # All the Nations
    Nations = ["us", "germ", "ussr", "uk", "jp", "cn", "it", "fr", "sw", "il", "md"]

    selected_Nation = tk.StringVar(root2)
    selected_Nation.set(Nations[0])  

    selected_Tank = tk.StringVar(root2)
    selected_TankDefault = "<Choose Vehicle>"

    # Create a dictionary to store the tanks for each Nation
    tanks = {nation: read_tanks(nation) for nation in Nations}
    
    #Function that makes sure there are no tanks from one nation in the other nation like tanks fron the USA With tanks from Sweden
    def update_tank_menu(*args):
        # Clear the tank menu
        selected_Tank.set(selected_TankDefault)
        # Add the tanks for the selected faction
        for tank in tanks[selected_Nation.get()]:
            tank_menu['values'] = tuple(tank for tank in tanks[selected_Nation.get()])
            tank_menu.current(0)  
        aka_label.config(text=f"aka {nation_full_names[selected_Nation.get()]}")
        
    #Creates button That sends you to Ask3lad's youtube :Pog:
    buttonUrl = tk.Button(root2, text="Youtube", command=lambda: open_website("https://www.youtube.com/@Ask3lad"))
    buttonUrl.place(x=10, y=10)

    # Create a Label and an OptionMenu for the Nation selector
    faction_label = tk.Label(root2, text="Nation:")
    faction_label.pack()
    faction_menu = tk.OptionMenu(root2, selected_Nation, *Nations, command=update_tank_menu)
    faction_menu.pack()

    #The Aka "Decoded Nation" Label
    aka_font = font.Font(weight='bold', size=12)
    aka_label = tk.Label(root2, text="", font=aka_font)
    aka_label.place(x=260, y=24)

    # Create a label and OptionMenu for the Vehicle selector
    tank_label = tk.Label(root2, text="Vehicle:")
    tank_label.pack(pady=7)
    
    tank_menu = ttk.Combobox(root2, textvariable=selected_Tank, width=30)
    tank_menu.state(['readonly'])
    tank_menu.pack()

    selected_Tank.set(selected_TankDefault)
    # Add the tanks for the selected faction
    for tank in tanks[selected_Nation.get()]:
       tank_menu['values'] = tuple(tank for tank in tanks[selected_Nation.get()])
       tank_menu.current(0)  

    # Update the tank menu whenever the selected faction is changed
    selected_Nation.trace('w', update_tank_menu)

    #Reads the file with weapon:t=...
    with open(f'{WT_directory}\\UserMissions\\Ask3lad\\ask3lad_testdrive_With_Moving_Bots.blk', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    #Prints the current Vehicle
    CurrentTank = lines[253]
    print("Current Tank: " + CurrentTank)

    #All the action when you press the Pick Vehicle Button
    def take_input():
        if selected_Tank.get() == selected_TankDefault or selected_Tank.get() == '':   #if the tank = nothing or the default value do nothing
            print("Default Value Shall Not Pass")
        else:                                                                           #if the tank = proper value change the value in documents
            ChosenTank = "{}_{}".format(selected_Nation.get(), selected_Tank.get())
            lines[253] = 'weapons:t="{}_default"\n'.format(ChosenTank)
            with open(f'{WT_directory}\\UserMissions\\Ask3lad\\ask3lad_testdrive_With_Moving_Bots.blk', 'r', encoding='utf-8') as f:
                file_contents = f.readlines()
            file_contents[253] = lines[253]
            with open(f'{WT_directory}\\UserMissions\\Ask3lad\\ask3lad_testdrive_With_Moving_Bots.blk', 'w', encoding='utf-8') as f:
                f.writelines(file_contents)
            print(lines[253])
            lines[1] = 'include "#/develop/gameBase/gameData/units/tankModels/{}_{}.blk"'.format(selected_Nation.get(), selected_Tank.get())
            with open(f'{WT_directory}\\content\\pkg_local\\gameData\\units\\tankModels\\userVehicles\\us_m2a4.blk', 'w', encoding='utf-8') as f:
                f.writelines(lines[1])
                print(lines[1])

    #Pick Vehicle Button
    calculate_button = tk.Button(root2, text="Pick Vehicle", command=take_input)
    calculate_button.pack(pady=10)

    root2.mainloop()

#The First Window
root1 = Tk()
root1.geometry('500x200')  
root1.resizable(False, False)  
root1.title('Choose The Directory Of War Thunder')

# Load the folder image
folder_image = tk.PhotoImage(file="folder.png")
folder_image = folder_image.subsample(10, 10)

# Create a button with the folder image and open file dialogue when clicked
def browse_button():
    global WT_directory
    WT_directory = filedialog.askdirectory(title="Choose The Directory Of War Thunder")
    print(WT_directory)
    start_button.config(state='normal')

#Button that triggers the browse_button event(I am too lazy to change it to a different name lol)
browse_button = tk.Button(root1, command=browse_button, image=folder_image, compound=tk.LEFT, width=100, height=100)
browse_button.place(x=188, y=20)

#And The Continue Button(That I also am too lazy to change the name of :) )
start_button = tk.Button(root1, text="Continue", command=change)
start_button.config(state='disabled')  #Makes the button disabled untill you choose the directory
start_button.place(x=210, y=130)

#The label of info
label = tk.Label(root1, text="Choose The Directory Of  War Thunder(Main Folder Named War Thunder)")
label.place(x=40, y=170)

root1.mainloop()


#Hello Person, i hope you like this little thing i made in 5 hours.
#If you find any bugs or anything else you want me to change or implement,
#message me at discordapp.com/users/916389301472882719 or just @trowa8 on discord in the ask3lad's server
