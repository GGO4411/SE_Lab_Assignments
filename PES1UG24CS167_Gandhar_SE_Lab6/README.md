# Lab 6 – Code and Branch Coverage

**Application:** `password_policy.py`

This folder contains the assigned password policy application and the two separate test suites required for Lab 6.

## Requirements

```bash
python -m pip install pytest coverage
```

## Code coverage

```bash
python -m coverage erase
python -m coverage run --source=password_policy -m pytest -q CodeCoverageTest_password_policy.py
python -m coverage report -m
```

Verified result: **100% code coverage** (47 statements, 0 missed).

## Branch coverage

```bash
python -m coverage erase
python -m coverage run --branch --source=password_policy -m pytest -q BranchCoverageTest_password_policy.py
python -m coverage report -m
```

Verified result: **100% branch coverage** (47 statements, 36 branches, 0 missed branches).

## Evidence

- `screenshots/code_coverage.svg` – terminal-output evidence for code coverage.
- `screenshots/branch_coverage.svg` – terminal-output evidence for branch coverage.

The test suites are kept separate to match the Lab 6 deliverables and the two-commit requirement.
