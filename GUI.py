import tkinter as tk
from tkinter import *



class State_Manager:

    def __init__(self):
        self.root = tk.Tk()
        self.current_state = None

    def set_state(self, new_state):

        if self.current_state:
            self.current_state.window_frame.destroy()

        self.current_state = new_state

    def run(self):
        self.root.mainloop()

class Application:

    def __init__(self):
        self.state_manager = State_Manager()

        # Set the initial state to the main menu
        self.state_manager.set_state(Main_Menu(self.state_manager.root, self.state_manager))

    def run(self):
        self.state_manager.run()
        





class Window():
    
    def __init__(self, root, state, grid_rows, grid_columns, resolution):

        self.root = root
        self.root.geometry(resolution)
        self.state = state
        self.window_frame = tk.Frame(self.root, width=1200, height=720)
        self.window_frame.pack(fill=tk.BOTH, expand=True)
        self.root.bind("<Configure>", self.on_resize)

        self.create_grid(grid_rows, grid_columns, self.window_frame)
        
    def create_grid(self, grid_rows, grid_columns,parent_frame):
        
        for i in range(grid_rows):
            parent_frame.grid_rowconfigure(i, weight=1)
            
        for j in range(grid_columns):
            parent_frame.grid_columnconfigure(j, weight=1)
            
    def on_resize(self, event):
        # Get the new size of the window
        new_width = event.width
        new_height = event.height

        # Configure the frame to fill the new size of the window
        self.window_frame.config(width=new_width, height=new_height)

    
        

class Main_Menu(Window):
    
    def __init__(self, root, state):
        super().__init__(root, state, 7,3, "1200x700")
        self.create_menu_widgits()

        
    
    def create_menu_widgits(self):
        self.page_menu()
        # self.NW_imageFrame
        # self.SW_imageFrame
        # self.NE_imageFrame
        # self.SE_imageFrame
        
        
    def page_menu(self): #menu with options to select

        self.page_menu_frame = tk.Frame(self.window_frame, width= 1200/3, height=720/3 ,bg="red")
        self.page_menu_frame.grid(row=1, rowspan=4, column=1, sticky="nsew")
        
        self.create_grid(3,3,self.page_menu_frame)
        self.menu_wigits()

         
    def menu_wigits(self): #list of all the wigits
        self.play_button = tk.Button(self.page_menu_frame, text="Play", command=self.play_action)
        self.play_button.grid(row=1, column=1, pady=10)
        
        self.settings_button = tk.Button(self.page_menu_frame, text="Settings", command=self.settings_action)
        self.settings_button.grid(row=2, column=1, pady=10)
        
        self.exit_button = tk.Button(self.page_menu_frame, text="Exit", command=self.exit_action)
        self.exit_button.grid(row=3, column=1, pady=10)
        
    def play_action(self):
        print("test")
        
    def settings_action(self):
        self.state.set_state(Settings_Menu(self.root, self.state))


    def exit_action(self):
        self.root.destroy()
        
class Settings_Menu(Window):
    
    def __init__(self, root, state):
        super().__init__(root,state, 7,3, "1200x720")
        self.page_menu()
        self.selections = []

        
    def page_menu(self): #menu with options to select
        # Create the page_menu_frame
        self.page_menu_frame = tk.Frame(self.window_frame, width= 1200/3, height=720/3 ,bg="red")
        self.page_menu_frame.grid(row=1, rowspan=4, column=1, sticky="nsew")
        self.create_grid(3,3,self.page_menu_frame)
        self.create_menu_wigits()
         
    def create_menu_wigits(self):
        self.difficulty_button = tk.Button(self.page_menu_frame, text="Difficulty", command=self.play_action)
        self.difficulty_button.grid(row=1, column=1, pady=10)
        
        
        self.menu_button = tk.Button(self.page_menu_frame, text="Back to Menu", command=self.menu_action)
        self.menu_button.grid(row=3, column=1, pady=10)

    def play_action(self):
        print("test")

    def settings_action(self):
        print("test")

    def menu_action(self):
        self.state.set_state(Main_Menu(self.root, self.state))

        



if __name__ == "__main__":
    app = Application()
    app.run()


        
