from password_policy import check_password, strength, suggest_fix


def test_check_password_accepts_valid_password():
    assert check_password("Abcdef1!") == []


def test_check_password_flags_short_password():
    assert "too short" in check_password("Ab1!")


def test_check_password_flags_long_password():
    assert "too long" in check_password("A" * 65 + "a1!")


def test_check_password_flags_common_password():
    assert "common" in check_password("PASSWORD")


def test_check_password_detects_missing_character_categories():
    issues = check_password("abcdefgh")
    assert "no uppercase" in issues
    assert "no digit" in issues
    assert "no special" in issues


def test_strength_good_password():
    assert strength("Abcdef1!") == "good"


def test_strength_strong_password():
    assert strength("Abcdefghijk1!X") == "strong"


def test_strength_weak_password():
    assert strength("Abcdefgh") == "weak"


def test_strength_very_weak_password():
    assert strength("abc") == "very weak"


def test_suggest_fix_no_issues():
    assert suggest_fix([]) == "none needed"


def test_suggest_fix_short_password():
    assert suggest_fix(["too short", "no digit"]) == "add more characters"


def test_suggest_fix_common_password():
    assert suggest_fix(["common"]) == "avoid common passwords"


def test_suggest_fix_missing_category():
    assert suggest_fix(["no digit"]) == "add digit"


def test_suggest_fix_other_issue():
    assert suggest_fix(["too long"]) == "shorten it"
