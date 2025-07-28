# VS Code Setup Script for New Machine

This folder contains your VS Code configuration backup to ensure identical setup on your new machine.

## 🚀 Quick Setup on New Machine

### Method 1: Enable Settings Sync (Easiest)
1. Open VS Code on new machine
2. Press `Ctrl+Shift+P` → "Settings Sync: Turn On"
3. Sign in with your Microsoft/GitHub account (same as this machine)
4. Everything will sync automatically!

### Method 2: Manual Setup (If Settings Sync doesn't work)

#### 1. Install Extensions
```bash
# Run this in PowerShell on the new machine
Get-Content .\.vscode\extensions.txt | ForEach-Object { code --install-extension $_ }
```

#### 2. Copy Settings
```bash
# Copy settings to your user profile
Copy-Item ".\.vscode\settings.json" "$env:APPDATA\Code\User\settings.json"
Copy-Item ".\.vscode\keybindings.json" "$env:APPDATA\Code\User\keybindings.json" -ErrorAction SilentlyContinue
```

#### 3. Restart VS Code
Close and reopen VS Code to apply all settings.

## 📋 What's Included

- **settings.json**: All your VS Code preferences, formatting rules, etc.
- **keybindings.json**: Custom keyboard shortcuts (if any)
- **extensions.txt**: Complete list of installed extensions
- **Pine Script highlighting**: Your `ex-codes.pine-script-syntax-highlighter` extension

## 🎯 Key Settings for Pine Script Development

Your settings include:
- Pine Script syntax highlighting configuration
- Material Icon Theme for file icons
- GitHub Copilot settings
- Terminal preferences (PowerShell)
- Python/formatting preferences

## ⚠️ Troubleshooting

If syntax highlighting looks different:
1. Ensure Pine Script extension is installed
2. Check bottom-right corner of VS Code shows "Pine Script" for .pine files
3. If not: Right-click → "Change Language Mode" → "Pine Script"

---
**All your customizations preserved for seamless machine switching!** 🎯
