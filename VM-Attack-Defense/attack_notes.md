# 🔺 Attack Scenario - Brute Force SSH

## 💻 Setup

- **Attacker VM**: Kali Linux
- **Target VM**: Windows 10 (with OpenSSH enabled)
- **Network**: Host-only / Bridged

## ⚙️ Tools Used

- `hydra`
- `nmap`
- `whoami`
- Windows Event Viewer

## 🧪 Steps

1. Nmap scan to discover open ports on the Windows VM
2. SSH brute-force attack using Hydra
3. Successful login detection
4. Windows logs reviewed for failed logins

## 🧠 Observations

- Windows Event ID 4625 showed multiple failed attempts
- Lockout policy triggered after 5 tries
- Defender raised alert on unauthorized access

## 📸 Screenshots

_Include screenshots of the attack, logs, and any alerts triggered._

---

📌 Next step: Add defense_notes.md for the blue team side
