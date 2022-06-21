from logging import root
import tkinter as tk
import tkinter.messagebox as tkm
def btn_click(event):
    botan = event.widget
    txt = botan["text"]
    #tkm.showinfo("確認", f"[{txt}]ボタンが押されました")
    entry.insert(tk.END,txt)
if __name__ == "__main__":
    root = tk.Tk()
    root.title("電卓")
    root.geometry("300x600")

    entry = tk.Entry(root, justify="right",
                     width = 10,
                      font = ("Times New Roman", 40))
    entry.grid(columnspan = 3)
    c = 0
    r = 1
    for i in range(9, -1, -1):

        btn = tk.Button(root, text = f"{i}",
                        width = 4, height = 2,
                        font = ("Times New Roman", 30)
                        )
        
        btn.grid(row = r, column = c)
        btn.bind("<1>", btn_click)
        c += 1
        if (i-1)%3 == 0:
            r += 1
            c = 0
    root.mainloop()
