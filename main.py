import tkinter as tk

def main():
    print("hello")
    root = tk.Tk()
    root.title("Collect Crystals")
    root.configure(background="red")
    root.minsize(720, 480)
    root.maxsize(720, 480)
    root.geometry("720x480+0+0")
    
    label1 = tk.Label(root, text="Collect crystals!")
    label2 = tk.Label(root, text="Avoid enemies!")
    label1.pack()
    label2.pack()
    
    root.mainloop()
    

if __name__ == "__main__":
    main()