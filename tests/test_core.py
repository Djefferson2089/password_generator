import re
import pytest

from passgen.core import generate_password

def test_generates_correct_length():
    pwd = generate_password(20)
    assert len(pwd) == 20

def test_requires_at_least_one_group():
    with pytest.raises(ValueError):
        generate_password(12, use_upper=False, use_lower=False, use_digits=False, use_symbols=False)

def test_exclude_removes_entire_group_raises():
    with pytest.raises(ValueError):
        generate_password(12, use_digits=True, exclude="0123456789", use_upper=False, use_lower=False, use_symbols=False)

def test_require_each_selected_enforced():
    pwd = generate_password(
        12, use_upper=True, use_lower=True, use_digits=True, use_symbols=False, require_each_selected=True
    )
    assert re.search(r"[A-Z]", pwd)
    assert re.search(r"[a-z]", pwd)
    assert re.search(r"\d", pwd)

def test_length_too_short_for_require_each():
    with pytest.raises(ValueError):
        generate_password(
            2, use_upper=True, use_lower=True, use_digits=False, use_symbols=False, require_each_selected=True
        )
