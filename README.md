# ALU Regex Data Extraction

We were tasked in using Regex to extract information of various data types using Python or JavaScript. I opted to use Python because I'm more familiar with it (not a pro, but not completely useless).

## What It Does

The Python script reads through a .txt file of ALU student records (AI Generated to mimick real world scenario). After reading, credit cards details, email addresses, phone numbers, date & time stamps and currency amounts are extracted and output to a .json file.

I'm using re and json libraries for the regex functions and the json output.

## How To Run

1. Clone repo to your pc/mac.
2. Ensure you have Python installed (version 3.6 or higher).
3. Navigate to the project directory in your terminal.
4. Run the script using the command: `python src/main.py` (python3 src/main.py for Mac users).
5. The extracted data will be saved in `output/sample-output.json`.

## File Structure

```
alu-regex-data-extraction_ngicheru-netizen/
├── input/
│   └── raw-text.txt
├── src/
│   └── main.py
├── output/
│   └── sample-output.json
└── README.md
```

## Regex Patterns

### Credit Cards

`\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b`

This means:
"[4 digits][one or more hyphen or space as a separator]" repeated 3 times
on the fourth:
"[4 digits]" with no separator at the end.
I used the \b to ensure that only card details with 16 numbers were extracted, nothing more nothing less.

### Emails

`[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}`
This means:
"One or more word characters, dots or hyphens (for the username)" then;
@ symbol then;
"One or more word characters, dots or hyphens (for the domain)" again (for the domain name) then;
"a literal dot(\.)" followed by 2 or more letters (for the domain extension).

### Phone Numbers

`\+(?:\d[- ]?){7,15}`
This means:
"A literal plus sign" followed by;
"One digit followed by an optional space or hyphen"
minimum of 7 and maximum of 15 digits

### DateTime

`\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}`
This means:
4 digits for year, dash, 2 digits for month, dash, 2 digits for day, space, 2 digits for hour, colon, 2 digits for minutes, colon, 2 digits for seconds

### Currency

`\$\d{1,3}(,\d{3})*\.\d{2}`
"One or more digits, with an optional comma"

## Security Considerations

- No input is trusted automatically. The regex patterns act as the first screening - anything that doesn't match is ignored.
- At output, credit card numbers are obfuscated, only showing the first four digits.
- wrongly written emails, invalid cards/numbers or suspicious input such as `<script>alert('xss')</script>` is ignored.
- Validation happens BEFORE obfuscation.

## Sample Output

Sample output can be found in `output/sample-output.json`
