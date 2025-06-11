# 🛡️ Defense Response - SSH Brute Force Attempt

## 🎯 Goal

Identify and respond to the brute-force SSH attack simulated in the red team scenario.

## 🧰 Tools Used

- Windows Event Viewer
- Task Manager
- Windows Defender
- PowerShell

## 🧪 Detection Steps

1. Opened **Event Viewer**
   - Navigated to **Windows Logs > Security**
   - Filtered for **Event ID 4625** (failed login attempts)

2. Used PowerShell:
```powershell
Get-EventLog -LogName Security | Where-Object { $_.EventID -eq 4625 }
