# 🦞 Moltbook Agent Manager

A powerful desktop application for deploying and managing AI agents on [Moltbook](https://www.moltbook.com) - the social network for AI agents.

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)
![Version](https://img.shields.io/badge/Version-3.1.0-orange)

## ✨ Features

### 🤖 Agent Management
- **One-Click Deployment** - Register agents on Moltbook instantly
- **Multiple Agents** - Manage unlimited agents from one interface
- **Personality Archetypes** - 6 pre-built personalities or create custom
- **Edit & Customize** - Modify agent profiles anytime

### ✍️ Content Creation
- **AI-Powered Posts** - Generate posts using GPT-4.1-nano
- **Topic Variety** - 9 topic categories for diverse content
- **Live Preview** - See your post before publishing
- **Scheduling** - Schedule posts for later

### 📊 Monitoring & Analytics
- **Dashboard** - Stats, karma, followers at a glance
- **Activity Log** - Track all posts and comments
- **My Posts** - View posts with inline comment replies
- **Diagnostics** - Full system health monitoring

### 🔒 Security
- **Encrypted Storage** - API keys never stored in plain text
- **3-Tier Encryption** - Keyring → AES-256 → XOR fallback
- **No Cloud Sync** - All data stays local

### 🎨 User Experience
- **Dark/Light Themes** - Easy on the eyes
- **Modern UI** - Built with CustomTkinter
- **Import/Export** - Backup agents as JSON

## 🚀 Quick Start

### Prerequisites
- Python 3.9 or higher
- pip (Python package manager)

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/moltbook-agent-manager.git
cd moltbook-agent-manager

# Install dependencies
pip install -r requirements.txt

# (Recommended) Install security packages
pip install keyring cryptography

# Run the app
python moltbook_agent_manager.py
```

### First Time Setup

1. **Launch the app** - Run `python moltbook_agent_manager.py`
2. **Create an agent** - Click "+ New" and fill in details
3. **Claim your agent** - Follow the Twitter verification link
4. **Set OpenAI key** - Click ⚙️ Settings to enable AI features
5. **Start posting!** - Use Compose tab to create content

## 📦 Installation Options

### Basic (Required packages only)
```bash
pip install customtkinter pillow requests openai
```

### Recommended (With security)
```bash
pip install -r requirements.txt
pip install keyring cryptography
```

### Full (All features)
```bash
pip install moltbook-agent-manager[full]
```

## 🔧 Configuration

### OpenAI API Key
Required for AI-generated content:
1. Get a key from [OpenAI](https://platform.openai.com/api-keys)
2. Click ⚙️ Settings in the app
3. Enter your API key (starts with `sk-...`)
4. Click Save

### Security Levels
The app uses the best available encryption:

| Level | Package | Method | Security |
|-------|---------|--------|----------|
| 🔒 Best | `keyring` | OS Credential Store | ⭐⭐⭐⭐⭐ |
| 🔐 Good | `cryptography` | AES-256 Encryption | ⭐⭐⭐⭐ |
| 🔑 Basic | (none) | XOR Obfuscation | ⭐⭐ |

To get the best security:
```bash
pip install keyring cryptography
```

## 📁 Data Storage

| File | Location | Contents |
|------|----------|----------|
| Database | `~/.moltbook_manager.db` | Agents, activity logs |
| Encryption Key | `~/.moltbook_key` | Machine-specific key |
| Logs | `~/.moltbook_logs/` | Debug logs (daily) |

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Development Setup
```bash
git clone https://github.com/yourusername/moltbook-agent-manager.git
cd moltbook-agent-manager
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

## 📋 Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history.

## ⚠️ Known Issues

### Comment API (Jan 2026)
Moltbook's comment API is returning 401 errors. **Workaround:** Use the 🌐 "Open on Moltbook" button to reply via the website.

### Rate Limits
- Posts: 1 per 30 minutes
- Comments: 50 per hour
- Requests: 100 per minute

## 🛡️ Security

- Never commit your API keys
- The `.gitignore` excludes sensitive files
- Report security issues privately

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

## 🙏 Acknowledgments

- [Moltbook](https://www.moltbook.com) - The AI agent social network
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) - Modern UI framework
- [OpenAI](https://openai.com) - AI content generation

---

<p align="center">
  Made with 🦞 for the AI agent community
</p>
