
from hypothesis import given, strategies as st
from password_policy import (
    first_character_type,
    split_credentials,
    digit_ratio
)


@given(st.text() | st.none())
def test_first_character_type_no_crash(s):
    first_character_type(s)


@given(st.text() | st.none())
def test_split_credentials_no_crash(s):
    split_credentials(s)


@given(st.text() | st.none())
def test_digit_ratio_no_crash(s):
    digit_ratio(s)
