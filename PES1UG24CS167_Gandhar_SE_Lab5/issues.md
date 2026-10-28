# Static Code Analysis — Issue Log

The line numbers below refer to the **original** `vehicle_service.py` in the assigned repository. The severity column is a practical risk assessment. Rule IDs are likely mappings for common tool versions; run the three tools locally and confirm the exact rule IDs and line numbers printed by your versions before final submission.

| Priority | Issue | Tool / category | Original line(s) | Why it matters | Fix applied |
|---|---|---|---:|---|---|
| High | Shell command constructed from a variable and run with `shell=True` | Bandit security check (commonly B602) | 57–59 | A crafted backup-folder value could alter the shell command and execute unintended commands. | Replaced shell execution with `pathlib.Path` and `shutil.copy2`; path values are no longer interpreted as shell syntax. |
| High | Hard-coded password-like value | Bandit security check (commonly B105) | 8 | Anyone who can read the repository can read the embedded password, even though it is unused in the demo. | Removed the unused password constant. A future authentication feature should obtain secrets from protected configuration or a secret manager. |
| Medium | Weak MD5 hash used to create a job-card identifier | Bandit security check (commonly B324) | 40 | MD5 is not appropriate for security-sensitive hashing. The current identifier is not an authentication token, but using a weak hash can imply unsafe practice. | Changed to SHA-256. The shortened value is still only a display identifier, not a security token. |
| Medium | Mutable default argument `history=[]` | Pylint (commonly W0102) | 11 | The same list is reused across calls that omit the argument, so records can leak from one call to another. | Changed the default to `None` and creates a fresh list inside the function. |
| Medium | Broad `except Exception` | Pylint (commonly W0718) | 22–27 | It hides unrelated errors and makes defects difficult to diagnose. | Replaced exception handling with an explicit `service_records.get(vehicle_no)` missing-record check. |
| Medium | Unknown service type silently receives a cost of zero | Manual correctness review | 12 | A typo in a service type could create a plausible-looking but incorrect service record. | Added service-type validation and raises `ValueError` for unknown names. |
| Low | Non-PEP 8 function names, inconsistent whitespace, and missing docstrings | Pylint / Flake8 (style and documentation checks) | 6–7, 11, 21, 32, 39, 43, 50–59 | Inconsistent names and formatting make code less readable and can trigger style warnings. | Changed function names to `snake_case`, cleaned up spacing, and added module/function docstrings. |
| Low | Demo runs whenever the module is imported | Design / testability review | 70 | Importing functions from this file unexpectedly runs the demonstration and writes a JSON file. | Wrapped the demo call in `if __name__ == "__main__":`. |
| Low | Text file is written without an explicit encoding | Portability review | 51 | Default text encoding can vary between systems. | Explicitly uses UTF-8 when reading and writing JSON files. |

## Commands to collect tool evidence

Run these from this folder after installing the tools. Keep the three output files and check whether the issues above appear in your exact reports.

```bash
python -m pip install pylint bandit flake8
python -m pylint vehicle_service.py > pylint_report.txt
python -m bandit -r vehicle_service.py > bandit_report.txt
python -m flake8 vehicle_service.py > flake8_report.txt
```

The issue descriptions above are based on inspection of the original source; they are not a claim that those commands were executed in this environment. Tool rule IDs and line numbers can differ across releases.
