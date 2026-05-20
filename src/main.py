#!/usr/bin/env python3

import re
import json


# function to read text file
def read_text_file(raw):

    try:
        with open(raw, encoding="utf-8") as f:
            contents = f.read()
        return contents
    except FileNotFoundError:
        print(f"{raw} was not found")


# extract credit card details


def extract_card_details(text):
    matches = re.findall(r"\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b", text)
    results = []
    for match in matches:
        cleaned = match.replace("-", "").replace(" ", "")
        if len(cleaned) != 16:
            continue

        obfuscated = obfuscate_card_details(cleaned)
        # show results with appended obfuscation
        results.append(obfuscated)
    return results


# obfuscate  the last 12 numnbers
def obfuscate_card_details(cleaned):
    obfuscated = re.sub(
        r"\d{12}$", " xxxx xxxx xxxx", cleaned
    )  # added space before the "x"s to keep format consistent
    return obfuscated


# extract email addressses
def extract_email(text):
    matches = re.findall(r"[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}", text)
    results = []

    for match in matches:
        tagged = tag_email(match)
        results.append(tagged)
    return results


def tag_email(email):
    if email.endswith("@alumni.alueducation.com"):
        return {"email": email, "type": "Alumni"}
    elif email.endswith("@si.alueducation.com"):
        return {"email": email, "type": "ALU SI"}
    elif email.endswith("@alueducation.com"):
        return {"email": email, "type": "ALU Official"}
    else:
        return {"email": email, "type": "Generic"}


# Extract Phone Numbers
def extract_phone_numbers(text):
    return re.findall(r"\+(?:\d[- ]?){7,15}", text)


# Extract Date and Time
def extract_datetime(text):
    return re.findall(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}", text)


# Extract Currency Amount
def extract_currency(text):
    return re.findall(r"\$\d{1,3}(?:,\d{3})*\.\d{2}", text)


# Output to JSON file
def write_json_output(cards, emails, phone, dt, currency):
    output = {
        "credit_cards": cards,
        "emails": emails,
        "phone_numbers": phone,
        "date_time": dt,
        "currency": currency,
    }
    with open("output/sample-output.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=4)


def main():
    text = read_text_file("input/raw-text.txt")
    cards = extract_card_details(text)
    emails = extract_email(text)
    phone = extract_phone_numbers(text)
    dt = extract_datetime(text)
    currency = extract_currency(text)
    write_json_output(cards, emails, phone, dt, currency)


if __name__ == "__main__":
    main()
