import os
import socket
from gtts import gTTS
from playsound import playsound
def nm(l):
    for i in l:
        if i == "0":
            c = snetmask.index("0")
    return c

mytext = "Welcome to IP Ping Program by: Djordje Simic Promena"
mytextt= "Program Start Pinging, Please Wait"
print(mytext)
myobj = gTTS(text=mytext, lang="en", slow=False)
myobj.save("Music/welcome.mp3")
myobjj= gTTS(text=mytextt, lang="en", slow=False)
myobjj.save("Music/loading.mp3")
playsound("Music/welcome.mp3")
print ("""
████████████████████████████████████████
████████████████████████████████████████
██████▀░░░░░░░░▀████████▀▀░░░░░░░▀██████
████▀░░░░░░░░░░░░▀████▀░░░░░░░░░░░░▀████
██▀░░░░░░░░░░░░░░░░▀▀░░░░░░░░░░░░░░░░▀██
██░░░░░░░░░░░░░░░░░░░▄▄░░░░░░░░░░░░░░░██
██░░░░░░░░░░░░░░░░░░█░█░░░░░░░░░░░░░░░██
██░░░░░░░░░░░░░░░░░▄▀░█░░░░░░░░░░░░░░░██
██░░░░░░░░░░████▄▄▄▀░░▀▀▀▀▄░░░░░░░░░░░██
██▄░░░░░░░░░████░░░░░░░░░░█░░░░░░░░░░▄██
████▄░░░░░░░████░░░░░░░░░░█░░░░░░░░▄████
██████▄░░░░░████▄▄▄░░░░░░░█░░░░░░▄██████
████████▄░░░▀▀▀▀░░░▀▀▀▀▀▀▀░░░░░▄████████
██████████▄░░░░░░░░░░░░░░░░░░▄██████████
████████████▄░░░░░░░░░░░░░░▄████████████
██████████████▄░░░░░░░░░░▄██████████████
████████████████▄░░░░░░▄████████████████
██████████████████▄▄▄▄██████████████████
████████████████████████████████████████
████████████████████████████████████████

""")
hn = socket.gethostname() 
ip = socket.gethostbyname(hn) 
print("Your Computer Name is: " + hn) 
print("Your Computer IP Address is :" + ip) 
sip = ip.split(".")
netmask = input("Please enter your subnet mask: ")
snetmask = netmask.split(".")
downRangeForPing = int(input("Please enter last number of ip addres as range for pinging| from: "))
upRangeForPing = int(input("Please enter last number of ip addres as range for pinging| up to: "))
print(mytextt)
print("... ... ... ...")
playsound("Music/loading.mp3")
print("The .txt files will be created in same directory as program after finish.")
dif = upRangeForPing - downRangeForPing
kk = nm(snetmask)
lll = []
if upRangeForPing > downRangeForPing:
    if kk == 3:
        f = open("Pinged IP addresses.txt", "w")
        for i in range(downRangeForPing, upRangeForPing + 1):
            f.write(f"{sip[0]}.{sip[1]}.{sip[2]}.{i}\n")
            lll.append(f"{sip[0]}.{sip[1]}.{sip[2]}.{i}")
        f.close()
    for i in lll:
        response = os.popen(f"ping {i}").read()
        if "Destination host unreachable" in response:
            c = open("Unreachable IP addresses.txt","a")
            c.write(f"{str(i)}\n")
            c.close()
        elif "Approximate round trip times" in response:
            d = open("Packet sent IP addresses.txt","a")
            d.write(f"{str(i)}\n")
            d.close()
        

else:
    print("error in typing ip range")
playsound("Music/Music.mp3")



        
        
