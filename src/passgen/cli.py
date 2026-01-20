from __future__ import annotations

import typer

from .core import DEFAULT_SYMBOLS, generate_password

app = typer.Typer(add_completion=False, help="Secure password generator (CLI).")


@app.command()
def gen(
    length: int = typer.Option(16, "--length", "-l", min=4, help="Password length."),
    upper: bool = typer.Option(True, "--upper/--no-upper", help="Include uppercase letters."),
    lower: bool = typer.Option(True, "--lower/--no-lower", help="Include lowercase letters."),
    digits: bool = typer.Option(True, "--digits/--no-digits", help="Include digits."),
    symbols: bool = typer.Option(True, "--symbols/--no-symbols", help="Include symbols."),
    symbol_set: str = typer.Option(DEFAULT_SYMBOLS, "--symbol-set", help="Custom symbol set."),
    exclude: str = typer.Option("", "--exclude", help="Characters to exclude."),
    require_each: bool = typer.Option(
        True, "--require-each/--no-require-each",
        help="Require at least one char from each selected group."
    ),
    copy: bool = typer.Option(False, "--copy", help="Copy result to clipboard (if available)."),
) -> None:
    pwd = generate_password(
        length,
        use_upper=upper,
        use_lower=lower,
        use_digits=digits,
        use_symbols=symbols,
        symbols=symbol_set,
        exclude=exclude,
        require_each_selected=require_each,
    )

    if copy:
        try:
            import pyperclip  # optional dependency
            pyperclip.copy(pwd)
            typer.echo(pwd)
            typer.echo("(copied to clipboard)")
            return
        except Exception:
            typer.echo(pwd)
            typer.echo("(clipboard copy unavailable — install pyperclip)")
            return

    typer.echo(pwd)


if __name__ == "__main__":
    app()
