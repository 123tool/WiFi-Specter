import os
import sys
import time
import subprocess
import platform
from prettytable import PrettyTable

# --- SPY-E HUD COLORS ---
R = "\033[1;31m"  # Danger / Weak
G = "\033[1;32m"  # Secure / Strong
Y = "\033[1;33m"  # Medium
C = "\033[1;36m"  # Info
W = "\033[1;37m"  # Text
X = "\033[0m"     # Reset

def header():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    print(f"""{C}
  ██████  ██████  ██    ██      ███████ 
 ██      ██    ██  ██  ██       ██      
  █████  ██    ██   ████        █████   
      ██ ██    ██    ██         ██      
 ██████   ██████     ██         ███████ 
    {W}WIFI-SPECTER v1.0 | BY: 123TOOL{X}
    """)

def get_wifi_list():
    # Logika Scan Lintas Platform
    results = []
    try:
        if platform.system() == "Windows":
            # Scan via CMD Netsh
            proc = subprocess.check_output("netsh wlan show networks mode=bssid", shell=True).decode('utf-8')
            # Parsing sederhana untuk Windows (Logic Only)
            return "Windows Support Active" 
        else:
            # Scan via Linux/Termux (nmcli atau iwlist)
            cmd = "nmcli -f SSID,SIGNAL,SECURITY,CHAN device wifi list"
            scan_data = subprocess.check_output(cmd, shell=True).decode('utf-8').split('\n')
            return scan_data
    except:
        return None

def show_dashboard():
    header()
    print(f"{Y}[*] MENGAMBIL DATA SINYAL SEKITAR...{X}\n")
    
    table = PrettyTable()
    table.field_names = [f"{C}SSID{X}", f"{C}SIGNAL{X}", f"{C}SECURITY{X}", f"{C}STATUS{X}"]
    
    raw_data = get_wifi_list()
    if not raw_data:
        print(f"{R}[!] Error: Pastikan WiFi Aktif & Izin Root diberikan.{X}")
        return

    # Skip header nmcli
    for line in raw_data[1:]:
        if line.strip():
            parts = line.split()
            if len(parts) >= 3:
                ssid = parts[0]
                signal = int(parts[1])
                security = parts[2]
                
                # Penentuan Warna Berdasarkan Kekuatan Sinyal
                if signal > 70: sig_color = G
                elif signal > 40: sig_color = Y
                else: sig_color = R
                
                # Penentuan Keamanan
                if "WPA3" in security: status = f"{G}ULTRA SECURE{X}"
                elif "WPA2" in security: status = f"{Y}STANDARD{X}"
                elif "--" in security or "OPEN" in security: status = f"{R}VULNERABLE (OPEN){X}"
                else: status = f"{W}UNKNOWN{X}"
                
                table.add_row([f"{W}{ssid}{X}", f"{sig_color}{signal}%{X}", f"{W}{security}{X}", status])

    print(table)
    print(f"\n{C}[RE-SCAN SETIAP 5 DETIK] - Tekan Ctrl+C untuk Berhenti{X}")

if __name__ == "__main__":
    try:
        while True:
            show_dashboard()
            time.sleep(5)
    except KeyboardInterrupt:
        print(f"\n{R}[!] SPY-E OFFLINE.{X}")
