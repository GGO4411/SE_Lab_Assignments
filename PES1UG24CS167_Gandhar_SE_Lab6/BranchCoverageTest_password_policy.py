from password_policy import check_password, strength, suggest_fix


def test_length_boundaries_and_common_password():
    assert "too short" in check_password("")
    assert "too short" in check_password("Ab1!")
    assert "too long" in check_password("A" * 65 + "a1!")
    assert "common" in check_password("password")
    assert check_password("Abcdef1!") == []


def test_character_class_branches():
    # Exercise uppercase, lowercase, digit and special branches, including
    # the paths where each category is absent.
    assert check_password("ABCDEFG1!") == ["no lowercase"]
    assert check_password("abcdefg1!") == ["no uppercase"]
    assert check_password("Abcdefgh!") == ["no digit"]
    assert check_password("Abcdefg1") == ["no special"]
    assert check_password("12345678") == [
        "no uppercase", "no lowercase", "no special"
    ]


def test_empty_loop_and_all_character_classes():
    assert check_password("") == [
        "too short", "no uppercase", "no lowercase", "no digit", "no special"
    ]
    assert check_password("A")
    assert check_password("a1!")


def test_strength_all_decisions():
    assert strength("Abcdef1!") == "good"
    assert strength("Abcdefghijk1!X") == "strong"
    assert strength("Abcdefgh") == "weak"
    assert strength("abc") == "very weak"


def test_suggest_fix_all_decisions():
    assert suggest_fix([]) == "none needed"
    assert suggest_fix(["too short"]) == "add more characters"
    assert suggest_fix(["common"]) == "avoid common passwords"
    assert suggest_fix(["no uppercase"]) == "add uppercase"
    assert suggest_fix(["too long"]) == "shorten it"
