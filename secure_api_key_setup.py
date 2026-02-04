#!/usr/bin/env python3
"""
Secure API Key Storage for Moltbook
Run this once to store your API key securely
"""
import keyring
import getpass

print("Secure API Key Setup for Moltbook")
print("=" * 50)

# Get the API key securely (won't show on screen)
api_key = getpass.getpass("Paste your API key (won't be visible): ")

# Store it securely in Windows Credential Manager
try:
    keyring.set_password("moltbook", "HAL-o", api_key)
    print("✅ API key stored securely in Windows Credential Manager!")
    print("✅ The app can now access it!")
    
    # Verify it was stored
    test = keyring.get_password("moltbook", "HAL-o")
    if test == api_key:
        print("✅ Verified: Key storage is working!")
    else:
        print("⚠️  Warning: Verification failed")
        
except Exception as e:
    print(f"❌ Error: {e}")
    print("Keyring might not be available on your system")

print("\nDone! Restart the Moltbook Agent Manager app.")
