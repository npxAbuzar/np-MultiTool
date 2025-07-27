# np-cybertool.py
from pyfiglet import figlet_format
from termcolor import colored
import os
import re
import whois
import requests
from urllib.parse import urlparse
from time import sleep
print("Scanning", end="")
for _ in range(3):
    sleep(0.5)
    print(".", end="")

#---------
#
print(colored("\nThanks for using NP CyberTool 🐾 Stay Safe!", "green", attrs=["bold"]))
 

#-----------Banner Code------------------------
# Clear the terminal
os.system('cls' if os.name == 'nt' else 'clear')

# Main Banner
banner = figlet_format("NPMT", font="slant")
print(colored(banner, color="cyan"))

# Subtitle - Meaning of NPMT
print(colored("Night Panthers Multi Tool", "magenta", attrs=["bold"]))

# Version and Credits
print(colored("Version: v1.0", "yellow"))
print(colored("Created by: npxarmy", "green"))
print(colored("Contact: jassonmiler363@gmail.com", "blue"))

# Small separator
print(colored("="*50, "white"))

# ---------- Password Strength Checker ----------
def check_password_strength(password):
    length = len(password) >= 8
    upper = any(c.isupper() for c in password)
    lower = any(c.islower() for c in password)
    digit = any(c.isdigit() for c in password)
    special = any(c in "!@#$%^&*()-_=+[{]};:'\",<.>/?\\|" for c in password)

    if all([length, upper, lower, digit, special]):
        return "🟢 Strong Password"
    elif length and (upper or lower) and digit:
        return "🟡 Medium Password"
    else:
        return "🔴 Weak Password"


# ---------- Phishing URL Detector ----------
def is_suspicious_url(url):
    suspicious_keywords = ['login', 'verify', 'update', 'secure', 'account', 'banking', 'paypal', 'signin', 'confirm']
    parsed_url = urlparse(url)
    domain = parsed_url.netloc.lower()

    for keyword in suspicious_keywords:
        if keyword in domain:
            return "🔴 Suspicious URL"
    if domain.count('.') >= 3:
        return "🟡 Suspicious (Too many subdomains)"
    return "🟢 URL Looks Safe"


# ---------- Domain Info Checker ----------
def get_domain_info(domain):
    try:
        domain_info = whois.whois(domain)
        info = {
            "Domain Name": domain_info.domain_name,
            "Registrar": domain_info.registrar,
            "Creation Date": domain_info.creation_date,
            "Expiration Date": domain_info.expiration_date,
            "Name Servers": domain_info.name_servers
        }
        return info
    except Exception as e:
        return {"error": str(e)}


# ---------- Menu System ----------
def main():
    while True:
        print("\n=== 🛡️ NP CyberTool - All in One ===")
        print("1. 🔐 Check Password Strength")
        print("2. 🔗 Scan Suspicious URL")
        print("3. 🌐 Get Domain Info")
        print("4. ❌ Exit")

        choice = input("\nSelect Option (1-4): ").strip()

        if choice == '1':
            password = input("Enter your password: ")
            print("Result:", check_password_strength(password))

        elif choice == '2':
            url = input("Enter the URL to scan: ")
            print("Result:", is_suspicious_url(url))

        elif choice == '3':
            domain = input("Enter domain (e.g., example.com): ")
            info = get_domain_info(domain)
            for key, value in info.items():
                print(f"{key}: {value}")

        elif choice == '4':
            print("Exiting... Stay safe 💻🛡️")
            break
        else:
            print("Invalid input! Please choose 1-4.")


if __name__ == "__main__":
    main()
