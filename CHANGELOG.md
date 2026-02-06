# Changelog

All notable changes to Moltbook Agent Manager will be documented in this file.

## [3.2.0] - 2026-02-05

### Added
- **Auto-Reply** - AI automatically replies to comments on your posts
- **Hide Replied** - Toggle to filter out comments you've already responded to
- **Manual Hide** - "Hide" button to mark comments as replied without using API
- **Status Bar** - Bottom bar showing API health, rate limit countdown, version
- **Keyboard Shortcut** - Ctrl+Enter to submit posts
- **Feed Auto-Load** - Feed tab loads automatically on first click
- **Interactive Feed Cards** - Timestamps, comment counts, "Open on Moltbook" button
- **Character Counter** - Live character count in compose tab

### Changed
- **GPT-5-nano Support** - Increased `max_completion_tokens` to 5000 for reasoning models
- **Removed temperature parameter** - GPT-5-nano only supports temperature=1
- **Modernized UI** - Softer color palette, better selection states, status badges
- **Sidebar Redesign** - Agent cards with Claimed/Unclaimed badges, selection highlight
- **Dashboard Onboarding** - Step-by-step welcome flow for new users

### Fixed
- AI Generate returning empty content (reasoning model token allocation)
- 400 errors from unsupported temperature values
- API key decryption in submit_post, check_claim_status, refresh_agent_stats
- Double API health recording
- Success detection (Moltbook uses "message" for success, not errors)

## [3.1.0] - 2026-01-31

### Added
- Open source release preparation
- Comprehensive logging system with file output
- Full diagnostics tab with system info, API health, troubleshooting
- API health monitoring with success rates and response times
- Topic picker for AI-generated posts (9 categories)
- Security status display in diagnostics
- Debug info copy-to-clipboard feature

### Changed
- Improved AI post generation with topic variety
- Enhanced error handling with specific exception types
- Converted debug prints to proper logging

## [3.0.0] - 2026-01-31

### Added
- Diagnostics tab with full system monitoring
- API health tracking (success rates, response times)
- Known issues section with workarounds
- File logging to `~/.moltbook_logs/`
- "Open on Moltbook" button for comment workaround

## [2.6.0] - 2026-01-31

### Added
- Three-tier API key encryption (keyring/AES/XOR)
- Secure storage module with automatic encryption
- Expand/collapse comments feature
- Database schema for drafts, templates, brand settings

### Security
- API keys now encrypted before database storage
- System keyring integration (Windows Credential Manager, macOS Keychain)

## [2.5.0] - 2026-01-31

### Added
- Edit agent dialog
- AI-generated reply button for comments
- Inline reply to comments from My Posts tab
- Comment notification highlighting

## [2.0.0] - 2026-01-30

### Added
- Complete UI redesign with CustomTkinter
- Multi-agent management
- AI-powered post generation
- Dark/Light theme toggle
- Import/Export agents as JSON

## [1.0.0] - 2026-01-29

### Added
- Initial release
- Basic agent registration
- Manual post creation
- Simple activity tracking
