#############################################
#
#  Schedule 1 - Cheat Menu
#  by logges aka gamingbee48
#
#  Key           Action
#  ------------  --------------------------------
#  F1            Show/Hide the Cheat Menu
#  Up/Down       Navigate the Menu
#  Left/Right    Change Option (if available)
#  Enter         Execute selected Command
#
#  Make sure the game console is active
#
#############################################


key = "~"


import tkinter as tk
import keyboard
import time

commands = [
    ("Free Camera", ["freecam"]),
    ("Save Game", ["save"]),
    ("Give Item", ["give baggie 20", "give jar 10", "give extralonglifesoil 10", "give highqualitypseudo 10", "give goldenskateboard"]),
    ("Give ingredient", ["give viagra 20", "give cuke 20", "give banana 20", "give paracetamol 20", "give donut 20", "give mouthwash 20", "give flumedicine 20", "give gasoline 20", "give energydrink 20", "give motoroil 20", "give megabean 20", "give chili 20", "give battery 20", "give iodine 20", "give addy 20", "give horsesemen 20"]),
    ("Give Drug", ["give ogkush 20", "give sourdiesel 20", "give greencrack 20", "give granddaddypurple 20", "give meth 20", "give cocaine 20"]),
    ("Give Weppon", ["give baseballbat", "give fryingpan", "give machete", "give revolver", "give m1911", "give revolverammo", "give m1911magazine"]),
    ("Give Seeds", ["give ogkushseed 10", "give sourdieselseed 10", "give greencrackseed 10", "give granddaddypurpleseed 10", "give cocaseed 10"]),
    ("Give Furniture", ["give suspensionrack", "give airpot", "give largestoragerack", "give bed","give brickpress", "give cauldron", "give chemistrystation", "give fullspectrumgrowlight", "give laboven", "give mixingstationmk2", "give packagingstationmk2"]),
    ("Clear Inventory", ["clearinventory"]),
    ("Change Cash", ["changecash 1000", "changecash 5000", "changecash 10000", "changecash 1000000"]),
    ("Change Balance", ["changebalance 1000", "changebalance 5000", "changebalance 10000", "changebalance 1000000"]),
    ("Add XP", ["addxp 100", "addxp 500", "addxp 1000"]),
    ("Teleport", ["teleport townhall", "teleport motel", "teleport warehouse", "teleport tacoticklers", "teleport dockswarehouse"]),
    ("Spawn Vehicle", ["spawnvehicle veeper", "spawnvehicle shitbox", "spawnvehicle bruiser", "spawnvehicle hounddog", "spawnvehicle cheetah", "spawnvehicle dinkler"]),
    ("Set Move Speed", ["setmovespeed 1", "setmovespeed 2", "setmovespeed 3"]),
    ("Set Jump Force", ["setjumpforce 1", "setjumpforce 2", "setjumpforce 3"]),
    ("Raise Wanted", ["raisewanted"]),
    ("Lower Wanted", ["lowerwanted"]),
    ("Clear Wanted", ["clearwanted"]),
    ("Set Health", ["sethealth 100", "sethealth 500", "sethealth 1000"]),
    ("Set Time", ["settime 0500", "settime 0800", "settime 1000", "settime 1200", "settime 1500", "settime 1800", "settime 2000", "settime 2300", "settime 0200"]),
    ("Set Time Scale", ["settimescale 1", "settimescale 2", "settimescale 3", "settimescale 5", "settimescale 10"]),
    ("Grow Plants", ["growplants"]),
    ("Clear Trash", ["cleartrash"]),
]

class ModMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Cheat Menu s1")
        self.root.geometry("400x400")
        self.root.attributes('-topmost', True)
        self.root.attributes('-alpha', 0.9)
        self.root.overrideredirect(True)

        self.current_index = 0
        self.option_indices = [0] * len(commands)

        self.canvas = tk.Canvas(self.root, highlightthickness=0)
        self.scrollable_frame = tk.Frame(self.canvas)

        self.scrollable_frame.bind(
    "<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        self.canvas.pack(side="left", fill="both", expand=True)

        self.labels = []
        self.create_menu()

        keyboard.on_press_key('up', lambda _: self.move_up())
        keyboard.on_press_key('down', lambda _: self.move_down())
        keyboard.on_press_key('left', lambda _: self.move_left())
        keyboard.on_press_key('right', lambda _: self.move_right())
        keyboard.on_press_key('enter', lambda _: self.select_command())
        keyboard.add_hotkey('f1', self.toggle_menu)

    def create_menu(self):
        tk.Label(self.scrollable_frame, text="Cheat Menu s1", font=("Arial", 20, "bold"), fg="white", bg="#222").pack(pady=10)

        for text, _ in commands:
            label = tk.Label(self.scrollable_frame, text=text, font=("Arial", 14), fg="#ccc", bg="#222")
            label.pack(anchor="w", padx=20)
            self.labels.append(label)

        self.update_selection()

    def update_selection(self):
        for idx, (label, (text, options)) in enumerate(zip(self.labels, commands)):
            option_idx = self.option_indices[idx]
            display_text = f"{text}: {options[option_idx]}"
            label.config(text=display_text)

            if idx == self.current_index:
                label.config(bg="black", fg="lime")
                # Sanft scrollen:
                self.canvas.yview_scroll(int((idx - self.canvas.canvasy(0) / label.winfo_height())), "units")
            else:
                label.config(bg=self.root.cget('bg'), fg="#4a4a4a")


    def smooth_scroll_to(self, target_idx):
        current = self.canvas.yview()[0]
        target = target_idx / len(self.labels)
        step = (target - current) / 5  # smooth speed

        def scroll():
            nonlocal current
            if abs(current - target) > 0.001:
                current += step
                self.canvas.yview_moveto(current)
                self.root.after(10, scroll)
            else:
                self.canvas.yview_moveto(target)

        scroll()

    def move_up(self):
        self.current_index = (self.current_index - 1) % len(self.labels)
        self.update_selection()

    def move_down(self):
        self.current_index = (self.current_index + 1) % len(self.labels)
        self.update_selection()

    def move_left(self):
        if len(commands[self.current_index][1]) > 1:
            self.option_indices[self.current_index] = (self.option_indices[self.current_index] - 1) % len(commands[self.current_index][1])
            self.update_selection()

    def move_right(self):
        if len(commands[self.current_index][1]) > 1:
            self.option_indices[self.current_index] = (self.option_indices[self.current_index] + 1) % len(commands[self.current_index][1])
            self.update_selection()

    def select_command(self):
        cmd = commands[self.current_index][1][self.option_indices[self.current_index]]
        keyboard.press_and_release(key)
        time.sleep(0.1)
        keyboard.write(cmd)
        keyboard.press_and_release('enter')

    def toggle_menu(self):
        if self.root.state() == "normal":
            self.root.withdraw()
        else:
            self.root.deiconify()

root = tk.Tk()
menu = ModMenu(root)
root.mainloop()
