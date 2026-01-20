from __future__ import annotations

import secrets
import string


DEFAULT_SYMBOLS = "!@#$%^&*()-_=+[]{};:,.?/"

def generate_password(
    length: int = 16,
    *,
    use_upper: bool = True,
    use_lower: bool = True,
    use_digits: bool = True,
    use_symbols: bool = True,
    symbols: str = DEFAULT_SYMBOLS,
    exclude: str = "",
    require_each_selected: bool = True,
) -> str:
    """
    Generate a password using cryptographically secure randomness (secrets).

    - exclude: characters to remove from the allowed pool
    - require_each_selected: ensures at least one character from each selected group
    """
    if length < 4:
        raise ValueError("length must be at least 4")

    groups: list[str] = []
    if use_upper:
        groups.append(string.ascii_uppercase)
    if use_lower:
        groups.append(string.ascii_lowercase)
    if use_digits:
        groups.append(string.digits)
    if use_symbols:
        groups.append(symbols)

    if not groups:
        raise ValueError("Select at least one character group.")

    # Apply excludes
    def _filter_chars(s: str) -> str:
        return "".join(ch for ch in s if ch not in exclude)

    groups = [_filter_chars(g) for g in groups]
    if any(len(g) == 0 for g in groups):
        raise ValueError("Excluding characters removed an entire selected group.")

    pool = "".join(groups)
    if not pool:
        raise ValueError("No characters available to generate password.")

    # Ensure length can satisfy requirements
    if require_each_selected and length < len(groups):
        raise ValueError("length is too short to include at least one from each selected group.")

    password_chars: list[str] = []

    # Guarantee at least one from each selected group
    if require_each_selected:
        for g in groups:
            password_chars.append(secrets.choice(g))

    # Fill remaining length from full pool
    while len(password_chars) < length:
        password_chars.append(secrets.choice(pool))

    # Shuffle to avoid predictable first chars
    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)
