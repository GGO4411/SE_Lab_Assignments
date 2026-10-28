# Reflection — Static Code Analysis

> The assigned repository's README refers to four reflection questions in the lab handout, but the handout itself was not available in the repository. These draft answers cover the usual reflection topics; align the headings to the exact question wording on your handout before submission.

## 1. What is static code analysis, and why is it useful?

Static code analysis checks source code without requiring the program to be executed. It helps detect common errors, unsafe coding patterns, and style problems early. It is useful because code can appear to work in a short demonstration and still contain security risks or bugs that occur only in particular circumstances.

## 2. Which issues were most important, and why?

The shell command constructed from a variable was the most serious issue because using `shell=True` with dynamically constructed command text can lead to command injection. The hard-coded password was also undesirable because secrets should not be stored directly in source code. The mutable default list could cause state to be shared between calls, while the broad exception handler could hide unexpected errors. These issues affect security, correctness, and maintainability rather than just appearance.

## 3. How do Pylint, Bandit, and Flake8 differ?

Pylint provides broad feedback about likely programming mistakes, naming, documentation, and maintainability. Bandit concentrates on security-sensitive code patterns, such as shell invocation and weak cryptographic hashes. Flake8 checks common Python style violations and selected programming errors. The tools overlap in places, but using them together provides a wider review than relying on just one tool. Their reports still need human interpretation: a finding is a prompt to investigate, not always proof of a vulnerability.

## 4. What did you learn, and what would you do differently in a future project?

I learned to treat static analysis as a regular part of development rather than something done only before submission. I would run the tools early, fix high-risk issues first, rerun the checks after changes, and keep the results with the project where required. I would also add tests for normal cases and edge cases, such as unknown service types, missing vehicles, and repeated calls to `add_service`. Static analysis complements tests and code review; it does not replace them.
