import os
import time
import random
import sys

# Color Codes
R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'
W = '\033[1;37m'
P = '\033[95m'

def banner():
    os.system('clear')
    print(f"""{G}
██████╗ ██╗   ██╗██╗██╗     ███████╗
██╔══██╗╚██╗ ██╔╝██║██║     ██╔════╝
██████╔╝ ╚████╔╝ ██║██║     █████╗  
██╔═══╝   ╚██╔╝  ██║██║     ██╔══╝  
██║        ██║   ██║███████╗███████╗
╚═╝        ╚═╝   ╚═╝╚══════╝╚══════╝
{P}HACKING WORLD™ - VIP EMAIL HACK TOOL
{Y}-------------------------------------------
""")

def loading_animation(text, duration=5):
    spinner = ['|', '/', '-', '\\']
    sys.stdout.write(Y + text + " ")
    for i in range(duration*4):
        sys.stdout.write(spinner[i % len(spinner)])
        sys.stdout.flush()
        time.sleep(0.25)
        sys.stdout.write('\b')
    print(W + "✓")

def fake_hacking_output():
    outputs = [
        "[*] Injecting Payload to Gmail Server...",
        "[*] Fetching User Credentials...",
        "[*] Decrypting Password Hash...",
        "[*] Bypassing Google Firewall...",
        "[*] Extracting Backup Codes...",
        "[*] Finalizing Exploit..."
    ]
    for line in outputs:
        print(C + line)
        time.sleep(random.uniform(1.0, 2.0))

def show_credentials(email):
    names = ["Alex Morgan", "John Doe", "Samiul Islam", "Rafi Ahmed", "Mehedi Hasan"]
    passwords = ["pass@" + str(random.randint(1000,9999)), "qwerty" + str(random.randint(10,99)) + "@123", "mysecure" + str(random.randint(1,100))]
    backup_code = random.randint(100000, 999999)
    print(f"\n{G}[✓] EMAIL FOUND: {email}")
    print(f"{Y}[✓] Account Holder: {random.choice(names)}")
    print(f"{C}[✓] Password: {random.choice(passwords)}")
    print(f"{P}[✓] Backup Code: {backup_code}")
    print(f"\n{R}[!] Note: Use this info responsibly! (💓)")

def main():
    banner()
    email = input(f"{C}[+] Enter Target Email Address: {W}")
    print()
    loading_animation("[✓] Connecting to Google Secure Server", 5)
    fake_hacking_output()
    loading_animation("[✓] Extracting Credentials", 4)
    show_credentials(email)
    input(f"\n{Y}Press Enter To Exit...")

main()