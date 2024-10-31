import subprocess
import regex as re
import string
import random

network_interface_reg_path = r"HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Class\\{4d36e972-e325-11ce-bfc1-08002be10318}"
transport_name_regex = re.compile("{.+}")
mac_address_regex = re.compile(r"([A-Z0-9]{2}[:-]){5}([A-Z0-9]{2})")

def get_random_mac_address():
    """Generate and return a MAC address in WINDOWS format"""
    uppercased_hexdigits = ''.join(set(string.hexdigits.upper()))

    return random.choice(uppercased_hexdigits) + random.choice("24AE") + "".join(random.sample(uppercased_hexdigits, k=10))

def clean_mac(mac):
    """Clean non hexadecimal characters from a MAC address"""
    return "".join(c for c in mac if c in string.hexdigits).upper()