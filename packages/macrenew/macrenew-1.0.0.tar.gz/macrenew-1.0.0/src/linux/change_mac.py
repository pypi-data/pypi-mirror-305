import argparse
import subprocess
import string
import random
import re

def get_random_mac_address():
    """Generate and return a MAC address in Linux format"""
    uppercased_hexdigits = ''.join(set(string.hexdigits.upper()))
    mac = ""
    for i in range(6):
        for j in range(2):
            if i == 0:
                mac += random.choice("02468ACE")
            else:
                mac += random.choice(uppercased_hexdigits)
        mac += ":"

    return mac.strip(":")

def get_current_mac_address(iface):
    output = subprocess.check_output(f"ip a show {iface}", shell=True).decode()

    return re.search("ether (.+) ", output).group().split()[1].strip()

def change_mac_address(iface, new_mac_address):
    subprocess.check_output(f"ip link set dev {iface} down", shell=True)
    subprocess.check_output(f"ip link set dev {iface} address {new_mac_address}", shell=True)
    subprocess.check_output(f"ip link set dev {iface} up", shell=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Python Linux Mac Changer.")
    parser.add_argument("-i", "--interface", help="Network interface name.")
    parser.add_argument("-r", "--random", action="store_true", help="Generate a random MAC address.")
    parser.add_argument("-m", "--mac", help="New MAC address.")

    args = parser.parse_args()
    iface = args.interface
    if args.random:
        new_mac_address = get_random_mac_address()
    elif args.mac:
        new_mac_address = args.mac

    old_mac_address = get_current_mac_address(iface)
    print(f"[+] Original MAC: {old_mac_address}")

    change_mac_address(iface, new_mac_address)
    new_mac_address = get_current_mac_address(iface)
    print(f"[+] New MAC: {new_mac_address}")

