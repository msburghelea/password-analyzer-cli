import json
import math
import hibp
from collections import Counter

def load_common_passwords():
    with open("passwords.txt", "r", encoding="utf-8") as f:
        return set(line.strip() for line in f)

common_passwords = load_common_passwords()

def is_common_password(password):
    return password in common_passwords

def analyze(password, check=False):
    has_upper, has_lower, has_digit, has_special = evaluate_complexity(password)
    result = {
        "length": evaluate_length(password),
        "complexity": {
            "has_uppercase": has_upper,
            "has_lowercase": has_lower,
            "has_digits": has_digit,
            "has_special_chars": has_special
        },
        "shannon_entropy": shannon_entropy(password),
        "bits_entropy": bits_entropy(password),
        "is_common": is_common_password(password) if check else "Not checked",
        "hibp": hibp.check_hibp(password) if check else "Not checked"
    }
    return result

def print_results(result):
    print(json.dumps(result, indent=4, ensure_ascii=False))

def evaluate_length(password):
    if len(password) < 8:
        return "Weak"
    elif len(password) < 12:
        return "Medium"
    else:
        return "Strong"

def evaluate_complexity(password):
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)
    return has_upper, has_lower, has_digit, has_special

def shannon_entropy(password):
    counts = Counter(password)
    entropy = 0
    for char, count in counts.items():
        probability = count / len(password)
        entropy += -probability * math.log2(probability)
    return entropy

def bits_entropy(password):
    has_upper, has_lower, has_digit, has_special = evaluate_complexity(password)
    pool = 0
    if has_upper:
        pool += 26
    if has_lower:
        pool += 26
    if has_digit:
        pool += 10
    if has_special:
        pool += 32
    if pool == 0:
        return 0
    return len(password) * math.log2(pool)