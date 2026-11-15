# Software Engineering Lab Assignments

This repository contains my Software Engineering laboratory assignments for PES University.

**Student:** Gandhar  
**USN:** PES1UG24CS167

## Repository Structure

| Folder | Description |
|---|---|
| `PES1UG24CS167_Gandhar_SE_Lab6/` | Lab 6 assignment files, implementation, tests, and screenshots |
| `PES1UG24CS167_Gandhar_SE_Lab7/` | Lab 7 fuzz-testing assignment, implementation, tests, and screenshots |

Each lab is maintained in its own folder. Refer to the README inside an individual lab folder, where available, for lab-specific instructions.

## Lab 7 – Fuzz Testing

Lab 7 uses **Python**, **pytest**, and **Hypothesis** to test input validation in a password-policy application.

The application contains three functions:

- `first_character_type(pw)`
- `split_credentials(text)`
- `digit_ratio(pw)`

Hypothesis generates a range of inputs, including edge cases, to identify failures. The application is then updated to handle invalid and empty inputs safely.

### Run Lab 7

From the Lab 7 folder, install the dependencies:

```bash
py -m pip install pytest hypothesis
```

Run the application:

```bash
py password_policy.py
```

Run the tests:

```bash
py -m pytest test_password_policy.py -v
```

The final test run completed with **3 tests passed**.

## Tools Used

- Python
- pytest
- Hypothesis
- Git and GitHub

## Notes

- Generated Python cache and test-tool folders are excluded using `.gitignore`.
- Screenshots for the lab execution and test results are stored in the corresponding lab's `screenshots/` folder.
