## @brief User grafical inteface implementation
#  
#  @author Vinicius Casimiro
#  @version 0.1

import tkinter as tk
from tkinter import ttk

import os 
    
    
class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Emissor de certificados")

        self.configure_window()

    def configure_window(self):
        window_width = self.winfo_screenwidth() * 0.8
        window_height = self.winfo_screenheight() * 0.8
        
        


# class MainWindow(tk.Tk):
#     """Initialize the main window with a root Tk instance."""
#     def __init__(self, root):
#         super().__init__(root)
#         self.root = root
        
#         self.window_bg = "#f0f0f0"
        
        
#         self.configure_window()
#         self.create_navbar()
#         self.create_widgets()

#     """Configure the main window settings."""
#     def configure_window(self):    
#         self.root.title("Emissor de certificados")
#         self.root.resizable(True, True)
#         self.root.configure(bg=self.window_bg)
        
#         screen_width = root.winfo_screenwidth()
#         screen_height = root.winfo_screenheight()
        
#         window_width = int(screen_width * 0.8)
#         window_height = int(screen_height * 0.8)
#         x = (screen_width - window_width) // 2
#         y = (screen_height - window_height) // 2
        
#         self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        
#         # TODO: create an icon for the application
#         # self.root.iconbitmap(os.path.join(os.path.dirname(__file__), "icon.ico"))
        
#         self.root.protocol("WM_DELETE_WINDOW", self.root.quit)
#         self.root.bind("<Control-q>", lambda e: self.root.quit())
        
#     def create_navbar(self):
#         self.navbar = ttk.Frame(self.root, padding="5")
#         self.navbar.pack(side=tk.TOP, fill=tk.X)
        

#     def create_widgets(self):
#         self.label = ttk.Label(self.root, text="Hello, Tkinter!")
#         self.label.pack(pady=20)

#         self.button = ttk.Button(self.root, text="Click Me", command=self.on_button_click)
#         self.button.pack(pady=10)

#     def on_button_click(self):
#         print("Button clicked!")
        


if __name__ == "__main__":
    # root = tk.Tk()
    app = MainWindow()
    # app.mainloop()
    
