# 🏦 CLI Banking App (Python Project)

Welcome to the CLI Bank App – a command-line banking system built with pure Python and JSON for data storage. It simulates real-world banking operations like account creation, login, withdrawals, and transfers, all handled securely through the terminal.

---

## ✅ Current Features (Fully Working)

### 🔐 Account Creation
- User inputs full name and selects account type (Savings, Current, Student)
- User sets a secure 4-digit PIN (masked using `getpass`)
- Unique 11-digit account number is automatically generated
- Account details are stored in a persistent `data.json` file

### 🔓 Secure Login
- Users log in using their account number and PIN
- Users have only 3 PIN attempts before account gets locked
- Locked accounts are denied access

### 💰 Check Account Balance
- View current account balance
- Low balance alert if below ₦1,000

### 💸 Withdraw Money
- Users enter amount and must confirm their PIN
- Checks for insufficient balance
- New balance is saved to `data.json`

### 🔁 Transfer Funds
- Validates that recipient account number is **exactly 11 digits**
- Only accepts numbers as input
- Confirms amount and user PIN before processing
- Saves updated balance to the data file

---

## 🔄 Data Storage
- All account data is stored in a local `data.json` file
- Data includes: Fullname, PIN, Account Number, Balance, Account Type, Locked status

---

## 🧠 What You’ll See Next (Coming Soon)

### 📥 Deposit Function  
Allow users to fund their account manually from CLI.

### 📲 Airtime Purchase  
Buy airtime directly from your account balance.

### 🔁 Change PIN  
Let users change their PIN securely after PIN confirmation.

### 🧨 Delete Account  
Give users the option to permanently delete their bank account.

### 🧾 Transaction History (Mini Statement)  
Save and show the last few actions (withdrawals, transfers, etc.)

### 🧼 Input & UX Polishing  
- Handle edge cases and invalid inputs gracefully  
- Improve prompts and feedback for a cleaner user experience  
- Add basic color formatting (maybe with `colorama`) for CLI aesthetics

---

## 🛠 How to Run

Make sure Python 3 is installed on your machine.

```bash
python yourfilename.py
