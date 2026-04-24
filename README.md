## 📡 WiFi Specter

![Platform](https://img.shields.io/badge/Platform-Termux%20%7C%20Linux%20%7C%20Windows-red?style=for-the-badge)
![Unit](https://img.shields.io/badge/Unit-123Tool%20Intelligence-7000ff?style=for-the-badge)

**WiFi Specter** adalah alat audit sinyal WiFi pasif untuk memetakan kekuatan jaringan dan tingkat keamanan di sekitar lokasi operasional.

## 🚀 Fitur
- **Live Dashboard:** Tampilan tabel ala terminal hacker.
- **Signal Tracking:** Menampilkan persentase kekuatan sinyal secara real-time.
- **Security Audit:** Otomatis menandai jaringan yang **VULNERABLE** (Terbuka).
- **Auto-Refresh:** Memantau pergerakan perangkat WiFi setiap 5 detik.

## (Install Dependency)
​Untuk Termux dan Linux, kamu butuh akses root karena memindai WiFi adalah aktivitas low-level networking.
```
pkg install python python-pip wireless-tools tsu -y
pip install scapy prettytable
```
## Run
```
git clone https://github.com/123tool/WiFi-Specter.git
cd WiFi-Specter
tsu python wifi_specter.py
