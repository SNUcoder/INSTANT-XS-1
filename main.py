import time
import getpass
import geocoder
import os
import webbrowser

time.sleep(1)
print(".")
time.sleep(1)
print("..")
time.sleep(1)
print("...")
time.sleep(1)
username = getpass.getuser()
g = geocoder.ip('me')
time.sleep(1.5)
print("\n============================================================ Hello", username, "from", g.city,"============================================================\n")
time.sleep(1.8)
print("What can I do for you??? :)")
print("A. Open Windows terminal")
print("B. Open Browser")
print("C. Open VScode")
print("D. Special options")
while (1):
    option = input("Your Option: ")
    if (option == 'A'):
        print("============================================================opens windows terminal============================================================")
        os.startfile(f"C:\\Users\\{username}\\AppData\\Local\\Microsoft\\WindowsApps\\wt.exe")
    elif (option == 'B'):
        print("============================================================Select which browser you want to open in============================================================")
        webbrowser.open('https://google.com')
    elif (option == 'C'):
        print("============================================================Opens VScode============================================================")
        os.startfile(f"C:\\Users\\{username}\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
    elif (option == 'D'):
        print("=========================================================Never gonna give you up=========================================================")
    else:
        print("LOL, what are you trying to say?\n")
