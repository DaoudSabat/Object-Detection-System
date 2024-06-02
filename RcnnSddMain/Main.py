import tkinter as tk
from tkinter import messagebox

# Your model loading functions
def load_yolo():
    model_name = "YOLO"
    with open("C:/Users/daoud/FYP2/FYP2/RcnnSddMain/YOLO.py", "r", encoding="cp1252") as file:
        exec(file.read(), globals())

def load_faster_rcnn():
    model_name = "Faster R-CNN"
    with open("C:/Users/daoud/FYP2/FYP2/RcnnSddMain/faster_rcnn_detection.py", "r", encoding="cp1252") as file:
        exec(file.read(), globals())

def load_ssd():
    model_name = "SSD"
    with open("C:/Users/daoud/FYP2/FYP2/RcnnSddMain/SSD.py", "r", encoding="cp1252") as file:
        exec(file.read(), globals())

def create_main_window():
    # Create the main window
    window = tk.Tk()
    window.title("Object Detection System")
    window.geometry("600x600")  # Set width and height as desired

    # Function to handle model selection
    def select_model(model_loader):
        model_loader()
        messagebox.showinfo("Model Loaded", f"{model_loader.__name__} model loaded successfully!")

    # Function to handle exit button click
    def exit_application():
        window.destroy()

    # GUI elements
    tk.Label(window, text="Welcome to Object Detection System Prototype", font=("Arial", 14)).grid(row=0, columnspan=3, pady=50)
    tk.Label(window, text="Please Select an Object Detection Model:", font=("Arial", 13)).grid(row=2, column=0, padx=20, sticky=tk.W)
    tk.Label(window, text="Press 'e' To Exit Any Model", font=("Arial", 11)).grid(row=4, column=0, padx=20, sticky=tk.W)
    tk.Label(window, text="", font=("Arial", 14)).grid(row=5)  # Empty row for space

    tk.Label(window, text="1 -- You Only Look Once", font=("Arial", 11)).grid(row=6, column=0, padx=20, sticky=tk.W)
    tk.Button(window, text="YOLO", command=lambda: select_model(load_yolo), width=20, height=2, font=("Arial", 11),borderwidth=1, relief="solid").grid(row=6, column=2, padx=20, pady=20)
    
    tk.Label(window, text="2 -- Region-based Convolutional Neural Network ", font=("Arial", 11)).grid(row=7, column=0, padx=20, sticky=tk.W)
    tk.Button(window, text="Faster R-CNN", command=lambda: select_model(load_faster_rcnn), width=20, height=2, font=("Arial", 11),borderwidth=1, relief="solid").grid(row=7, column=2, padx=20, pady=20)
    
    tk.Label(window, text="3 -- Single Shot MultiBox Detector", font=("Arial", 11)).grid(row=8, column=0, padx=20, sticky=tk.W)
    tk.Button(window, text="SSD", command=lambda: select_model(load_ssd), width=20, height=2, font=("Arial", 11),borderwidth=1, relief="solid").grid(row=8, column=2, padx=20, pady=20)
    
    tk.Button(window, text="Exit", command=exit_application, width=20, height=2, font=("Arial", 11),borderwidth=1, relief="solid").grid(row=20, columnspan=3, pady=20)

    window.mainloop()

if __name__ == "__main__":
    create_main_window()
