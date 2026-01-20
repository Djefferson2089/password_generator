# Password Generator (passgen)

Secure, customizable password generator CLI built with Python and Typer.

## Install (dev)
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -e . pytest
```

## Usage
passgen
passgen --length 24
passgen --no-symbols
passgen --exclude "O0Il1"
passgen --symbol-set "!@#"
passgen --no-upper --digits
passgen --copy

## Examples

### Generate a 24-character password without symbols:

passgen --length 24 --no-symbols

### Exclude ambiguous characters:

passgen --exclude "O0Il1"

### Generate a digits-only password:

passgen --no-upper --no-lower --symbols --digits

### Copy password to clipboard (requires pyperclip):

passgen --copy

### View all options:

passgen --help

