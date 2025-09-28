import os
import platform
import time
import secrets
import string
import math

if platform.system() == "Windows":
    clear_cmd = "cls"
else:
    clear_cmd = "clear"

def clear():
    os.system(clear_cmd)

def learn():
    clear()
    print("OPSEC")
    print("- Never share your passwords with anyone.")
    print("- Always enable 2FA on every service where it's available.")
    print("- Keep your system updated and make frequent backups.")
    print("- Never reuse passwords across accounts.\n")
    print("- This program helps produce passwords that are hard to brute-force.")
    print("Tools like Hydra, Hashcat and John the Ripper are widely used and")
    print("pose a risk to privacy. Only you can protect your accounts from exposure.")
    print()
    try:
        with open("bat.txt", "r", encoding="utf-8") as f:
            for line in f:
                print(line, end="")
                time.sleep(delay_between_lines)
    except FileNotFoundError:
        print("Error: bat.txt not found, please download all program dependencies...")

def add(password: str):
    clear()
    pw = password
    length = len(pw)
    has_lower = any(c.islower() for c in pw)
    has_upper = any(c.isupper() for c in pw)
    has_digits = any(c.isdigit() for c in pw)
    punctuation_chars = set(string.punctuation)
    has_symbols = any(c in punctuation_chars for c in pw)
    has_space = any(c.isspace() for c in pw)
    charset = 0
    if has_lower:
        charset += 26
    if has_upper:
        charset += 26
    if has_digits:
        charset += 10
    if has_symbols:
        charset += len(string.punctuation)
    if has_space:
        charset += 1
    if charset == 0:
        charset = len(set(pw))
    entropy_per_char = math.log2(charset) if charset > 0 else 0.0
    entropy = entropy_per_char * length

    def fmt_scientific_from_bits(bits):
        if bits <= 0:
            return "1"
        log10 = bits * math.log10(2)
        exponent = math.floor(log10)
        mantissa = 10 ** (log10 - exponent)
        return f"{mantissa:.3g}e{exponent:+d}"

    def seconds_to_human(seconds):
        if seconds == float("inf"):
            return "∞"
        sec = int(seconds)
        if sec < 60:
            return f"{sec} seconds"
        minutes, sec = divmod(sec, 60)
        if minutes < 60:
            return f"{minutes} minutes {sec} seconds"
        hours, minutes = divmod(minutes, 60)
        if hours < 24:
            return f"{hours} hours {minutes} minutes"
        days, hours = divmod(hours, 24)
        if days < 365:
            return f"{days} days {hours} hours"
        years, days = divmod(days, 365)
        if years < 1e3:
            return f"{years} years {days} days"
        return f"{years:.3e} years"

    rates = {
        "Online (rate-limited)": 10,
        "Weak online (no rate limit)": 1000,
        "CPU bruteforce (single CPU core)": 1e4,
        "GPU (single high-end)": 1e9,
        "Massive cluster / ASIC": 1e12,
    }

    print("Password analysis\n-----------------")
    print(f"Password: {pw}")
    print(f"Length: {length}")
    print("Character classes used:", end=" ")
    classes = []
    if has_lower: classes.append("lowercase")
    if has_upper: classes.append("UPPERCASE")
    if has_digits: classes.append("digits")
    if has_symbols: classes.append("symbols/punctuation")
    if has_space: classes.append("space")
    print(", ".join(classes) if classes else "none-detectable")
    print(f"Estimated charset size (conservative): {charset}")
    print(f"Entropy per char (bits): {entropy_per_char:.4f}")
    print(f"Total entropy (bits): {entropy:.2f}")
    print(f"Number of combinations (approx): {fmt_scientific_from_bits(entropy)}")
    print()
    print("Estimated time to crack (brute-force) — purely theoretical")
    for label, r in rates.items():
        if entropy <= 0:
            secs = 0
        else:
            log10_secs = entropy * math.log10(2) - math.log10(2 * r)
            if log10_secs > 300:
                secs = float("inf")
            else:
                secs = 10 ** log10_secs
        print(f"- {label:30s}: {seconds_to_human(secs)}")
    print("\nCaveats:")
    print("- These figures assume a pure brute-force attack against the plaintext password.")
    print("- If the password was generated using human patterns, the effective entropy may be much lower.")
    print("- Targeted attacks (phishing, leaks, keyloggers, credential reuse) can compromise the password much faster.")
    print("- If an attacker only has a hash, the real cracking speed depends on the hash algorithm and salt (bcrypt/argon2 drastically reduce cracking speed).")
    input("\nPress Enter to return to the menu...")

def password():
    clear()
    try:
        raw = input("Password length [default 16]: ").strip()
        length = int(raw) if raw else 16
        if length <= 0:
            print("Length must be > 0. Using 16.")
            length = 16
    except ValueError:
        print("Error. Using 16.")
        length = 16
    alphabet = string.ascii_letters + string.digits + string.punctuation
    alphabet = alphabet.replace('"', '').replace("'", "")
    passwords = [
        ''.join(secrets.choice(alphabet) for _ in range(length))
        for _ in range(10)
    ]
    print("\nChoose one of the following passwords:")
    for i, pwd in enumerate(passwords, 1):
        print(f"{i}: {pwd}")
    while True:
        choice = input("\nChoose a number between 1 and 10: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= 10:
            selected = passwords[int(choice) - 1]
            break
        else:
            print("Error. Choose a number between 1 and 10.")
    clear()
    print(f"\nSelected Password {selected}")
    save_choice = input("Do you wish to save the password to a file? (y/n): ").strip().lower()
    if save_choice == 'y':
        clear()
        filename = input("File name: ").strip()
        if not filename:
            filename = "passwords.txt"
        with open(filename, "a", encoding="utf-8") as f:
            f.write(selected + "\n")
        print(f"Password saved in {filename}...")
    else:
        print("Password not saved.")
    opt2 = input("\nDo you wish to see optional data about your password? (y/n): ").strip().lower()
    if opt2 == "y":
        add(selected)
    else:
        input("\nPress Enter to return to the menu...")

if __name__ == "__main__":
    clear()
    delay_between_lines = 0.15
    try:
        with open("bat.txt", "r", encoding="utf-8") as f:
            for line in f:
                print(line, end="")
                time.sleep(delay_between_lines)
    except FileNotFoundError:
        print("Error: bat.txt not found, please download all program dependencies...")

    print()
    print("Welcome to the Bat Password Tool")
    print("1 - make a new password")
    print("2 - learn more about password security")

    opt1 = input("Option: ").strip()

    if opt1 == "1":
        password()
    elif opt1 == "2":
        learn()
    else:
        print("Invalid option.")
