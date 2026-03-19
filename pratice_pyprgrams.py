import smtplib
import qrcode
import pyshorteners
import pyperclip
import socket
import platform
import re
from PyPDF2 import PdfMerger
from http.server import SimpleHTTPRequestHandler, HTTPServer

# ---------------- 1. Email Sender ----------------
def send_email():
    sender = input("Enter your email: ")
    password = input("Enter your password: ")
    receiver = input("Enter receiver email: ")

    message = "Subject: Python Mail\n\nHello from Python!"

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receiver, message)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print("Error:", e)

# ---------------- 2. QR Code Generator ----------------
def generate_qr():
    data = input("Enter data: ")
    img = qrcode.make(data)
    img.save("qr.png")
    print("QR Code saved as qr.png")

# ---------------- 3. URL Shortener ----------------
def shorten_url():
    url = input("Enter URL: ")
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(url)
    print("Short URL:", short_url)

# ---------------- 4. Clipboard Manager ----------------
def clipboard():
    text = input("Enter text: ")
    pyperclip.copy(text)
    print("Copied to clipboard!")

# ---------------- 5. To-Do List ----------------
def todo():
    while True:
        task = input("Enter task (or exit): ")
        if task.lower() == "exit":
            break
        with open("tasks.txt", "a") as f:
            f.write(task + "\n")
    print("Tasks saved in tasks.txt")

# ---------------- 6. IP Address Finder ----------------
def get_ip():
    host = input("Enter website (e.g., google.com): ")
    try:
        ip = socket.gethostbyname(host)
        print("IP Address:", ip)
    except:
        print("Invalid website!")

# ---------------- 7. PDF Merger ----------------
def merge_pdfs():
    merger = PdfMerger()
    files = input("Enter PDF names separated by space: ").split()

    try:
        for pdf in files:
            merger.append(pdf)
        merger.write("merged.pdf")
        merger.close()
        print("PDF merged as merged.pdf")
    except:
        print("Error merging PDFs!")

# ---------------- 8. System Info ----------------
def system_info():
    print("System:", platform.system())
    print("Node:", platform.node())
    print("Release:", platform.release())
    print("Processor:", platform.processor())

# ---------------- 9. Password Strength Checker ----------------
def check_password():
    pwd = input("Enter password: ")

    if len(pwd) < 8:
        print("Weak Password")
    elif not re.search("[a-z]", pwd):
        print("Weak Password")
    elif not re.search("[A-Z]", pwd):
        print("Weak Password")
    elif not re.search("[0-9]", pwd):
        print("Weak Password")
    else:
        print("Strong Password")

# ---------------- 10. Mini HTTP Server ----------------
def run_server():
    port = 8000
    server = HTTPServer(("", port), SimpleHTTPRequestHandler)
    print(f"Server running at http://localhost:{port}")
    server.serve_forever()

# ---------------- MENU ----------------
def main():
    while True:
        print("\n--- Python Utility Toolkit (Part 2) ---")
        print("1. Send Email")
        print("2. Generate QR Code")
        print("3. URL Shortener")
        print("4. Clipboard Manager")
        print("5. To-Do List")
        print("6. IP Address Finder")
        print("7. PDF Merger")
        print("8. System Info")
        print("9. Password Checker")
        print("10. Run HTTP Server")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            send_email()
        elif choice == "2":
            generate_qr()
        elif choice == "3":
            shorten_url()
        elif choice == "4":
            clipboard()
        elif choice == "5":
            todo()
        elif choice == "6":
            get_ip()
        elif choice == "7":
            merge_pdfs()
        elif choice == "8":
            system_info()
        elif choice == "9":
            check_password()
        elif choice == "10":
            run_server()
        elif choice == "0":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()