COMMON = {"password", "123456", "qwerty", "letmein"}


def check_password(pw):
    issues = []
    if len(pw) < 8:
        issues.append("too short")
    elif len(pw) > 64:
        issues.append("too long")
    if pw.lower() in COMMON:
        issues.append("common")
    upper = lower = digit = special = 0
    for ch in pw:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1
        elif ch.isdigit():
            digit += 1
        else:
            special += 1
    if upper == 0:
        issues.append("no uppercase")
    if lower == 0:
        issues.append("no lowercase")
    if digit == 0:
        issues.append("no digit")
    if special == 0:
        issues.append("no special")
    return issues


def strength(pw):
    issues = check_password(pw)
    if not issues:
        if len(pw) >= 14:
            return "strong"
        return "good"
    if len(issues) <= 2:
        return "weak"
    return "very weak"


def suggest_fix(issues):
    if not issues:
        return "none needed"
    first = issues[0]
    if first == "too short":
        return "add more characters"
    if first == "common":
        return "avoid common passwords"
    if first.startswith("no "):
        return "add " + first[3:]
    return "shorten it"
