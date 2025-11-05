# Simple Password Manager

A lightweight command-line password manager that reads login credentials from a CSV file and copies the selected password to the clipboard for 10 seconds before automatically clearing it.

## Modules Used

- csv: Reads and parses account data from the CSV file
- os: Handles file paths and directory operations
- time: Controls clipboard timeout (10 seconds)
- pyperclip: Copies and clears passwords from the clipboard

## How It Works

The script loads account data from example.csv in the same directory. User type an account type (e.g. email, bank, social). It lists all matching accounts for that type. User select the desired account number, and the password is copied to the clipboard. After 10 seconds, the clipboard is automatically cleared and the program exits.

## CSV Format

Each row must contain exactly three columns:
account_type,username_or_email,password

Example:
Spotify,username123,spotify123
Discord,email1@gmail.com,discord1
Gmail,user5@gmail.com,gmail5
Lloyds,username,password

## Requirements

Install dependencies with:
pip install pyperclip