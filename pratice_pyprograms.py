import random
import string
import os
import shutil
import requests
from bs4 import BeautifulSoup
from threading import Thread
from tkinter import *

# ---------------- 1. Chatbot ----------------
def chatbot():
    responses = {
        "hello": ["Hi!", "Hello!", "Hey!"],
        "how are you": ["I'm fine!", "Good!", "Awesome!"]
    }
    while True:
        user = input("You: ").lower()
        if user == "bye":
            break
        print("Bot:", random.choice(responses.get(user, ["I don't understand"])))

# ---------------- 2. Password Generator ----------------
def generate_password():
    length = int(input("Enter password length: "))
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choice(chars) for _ in range(length))
    print("Password:", password)

# ---------------- 3. File Organizer ----------------
def file_organizer():
    path = input("Enter folder path: ")
    for file in os.listdir(path):
        if "." in file:
            ext = file.split('.')[-1]
            folder = os.path.join(path, ext)
            os.makedirs(folder, exist_ok=True)
            shutil.move(os.path.join(path, file), os.path.join(folder, file))
    print("Files organized!")

# ---------------- 4. Web Scraper ----------------
def web_scraper():
    url = input("Enter URL: ")
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    for link in soup.find_all("a"):
        print(link.get("href"))

# ---------------- 5. Multithreading Downloader ----------------
def download_file(url, filename):
    r = requests.get(url)
    with open(filename, "wb") as f:
        f.write(r.content)

def multi_download():
    url1 = input("Enter first URL: ")
    url2 = input("Enter second URL: ")
    t1 = Thread(target=download_file, args=(url1, "file1"))
    t2 = Thread(target=download_file, args=(url2, "file2"))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Download complete!")

# ---------------- 6. Image to ASCII ----------------
def image_to_ascii():
    from PIL import Image
    img = Image.open(input("Enter image path: ")).convert("L")
    img = img.resize((100, 50))
    chars = "@%#*+=-:. "
    for y in range(img.height):
        for x in range(img.width):
            print(chars[img.getpixel((x, y)) * len(chars) // 256], end="")
        print()

# ---------------- 7. Keylogger ----------------
def keylogger():
    from pynput.keyboard import Listener
    def log_key(key):
        print(key)
    with Listener(on_press=log_key) as listener:
        listener.join()

# ---------------- 8. Sudoku Solver ----------------
def sudoku_solver():
    board = [[0]*9 for _ in range(9)]
    
    def solve():
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    for num in range(1, 10):
                        if valid(i, j, num):
                            board[i][j] = num
                            if solve():
                                return True
                            board[i][j] = 0
                    return False
        return True

    def valid(row, col, num):
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False
        
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if board[start_row + i][start_col + j] == num:
                    return False
        return True

    if solve():
        for row in board:
            print(row)
    else:
        print("No solution exists")

# ---------------- 9. Bitcoin Price ----------------
def bitcoin_price():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    data = requests.get(url).json()
    print("Bitcoin Price (USD):", data['bpi']['USD']['rate'])

# ---------------- 10. GUI Calculator ----------------
def calculator():
    def click(event):
        text = event.widget.cget("text")
        if text == "=":
            try:
                ans = str(eval(screen.get()))
                screen.delete(0, END)
                screen.insert(END, ans)
            except:
                screen.delete(0, END)
                screen.insert(END, "Error")
        else:
            screen.insert(END, text)

    root = Tk()
    root.title("Calculator")

    screen = Entry(root)
    screen.pack()

    for char in "789/456*123-0+=":
        btn = Button(root, text=char, width=5)
        btn.pack(side=LEFT)
        btn.bind("<Button-1>", click)

    root.mainloop()

# ---------------- MENU ----------------
def main():
    while True:
        print("\n--- Advanced Python Menu ---")
        print("1. Chatbot")
        print("2. Password Generator")
        print("3. File Organizer")
        print("4. Web Scraper")
        print("5. Multi Downloader")
        print("6. Image to ASCII")
        print("7. Keylogger")
        print("8. Sudoku Solver")
        print("9. Bitcoin Price")
        print("10. Calculator GUI")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            chatbot()
        elif choice == "2":
            generate_password()
        elif choice == "3":
            file_organizer()
        elif choice == "4":
            web_scraper()
        elif choice == "5":
            multi_download()
        elif choice == "6":
            image_to_ascii()
        elif choice == "7":
            keylogger()
        elif choice == "8":
            sudoku_solver()
        elif choice == "9":
            bitcoin_price()
        elif choice == "10":
            calculator()
        elif choice == "0":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()