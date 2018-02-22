from tkinter import *
import subprocess
import sys
import time

root = Tk()

root.title("Kali Setup")
root.geometry("300x300")
root.configure(bg="#2E2E2E")


'#Commands'

'#Update Function'


def setup_kali():
    subprocess.call('cd /', shell=True)
    subprocess.call('apt-get update && apt-get upgrade -y && apt-get dist-upgrade -y', shell=True)
    time.sleep(1)


'#Tor Install Function'


def tor():
    subprocess.call('cd /', shell=True)
    subprocess.call('tar -xvf KaliSetup/tor-browser-linux64-7.5_en-US.tar.xz', shell=True)
    subprocess.call('mv start-tor-browser tor-browser_en-US/Browser', shell=True)
    subprocess.call('./tor-browser_en-US/Browser/start-tor-browser', shell=True)


'#Fat Rat Install Function'


def fat_rat():
    subprocess.call('cd /', shell=True)
    subprocess.call('git clone https://github.com/Screetsec/TheFatRat.git', shell=True)
    subprocess.call('chmod +x TheFatRat/setup.sh', shell=True)
    subprocess.call('./TheFatRat/setup.sh', shell=True)


'#Support Function'


def support_():
    subprocess.call('xdg-open http://gestyy.com/wvuk2L', shell=True)


'#Exit Function'


def exit_():
    sys.exit()


'#Buttons and Labels'


welcome_label = Label(text="Welcome to Kali Setup", bg="Black", fg="#40FF00")
welcome_label.pack(side=TOP, fill=X, padx=20, pady=0)

setup_button = Button(text="Setup", bg="Black", fg="#40FF00", command=setup_kali)
setup_button.pack(side=TOP, fill=X, padx=50, pady=20)

tor_button = Button(text="TorBrowser", bg="Black", fg="#40FF00", command=tor)
tor_button.pack(side=TOP, fill=X, padx=50, pady=0)

fat_rat_button = Button(text="TheFatRat", bg="Black", fg="#40FF00", command=fat_rat)
fat_rat_button.pack(side=TOP, fill=X, padx=50, pady=20)

exit_button = Button(text="Exit", bg="Black", fg="#40FF00", command=exit_)
exit_button.pack(side=BOTTOM, fill=X, padx=50, pady=0)

exit_button = Button(text="Support", bg="Black", fg="#40FF00", command=support_)
exit_button.pack(side=BOTTOM, fill=X, padx=50, pady=10)


'#End of Program'

mainloop()
