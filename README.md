# Assignment 6 — CI Flow with GitHub Branches

Repository: `Second_CI_Pipeline`

## Included
- Python programs 31–40 and a matching pytest file for each
- `requirements.txt`
- `.github/workflows/ci.yml` using the workflow supplied with the assignment

## Run all tests locally in VS Code
Open this folder in VS Code, then in its terminal run:

```bash
python -m pip install -r requirements.txt
python -m pytest -v
```

The included project was checked locally: all 30 tests passed.

## Important: keep `main` as the shared base
The assignment asks for one program and its test file on each feature branch. Therefore, **do not run `git add .` for the first commit**. First commit only the shared setup files to `main`, then commit one program/test pair per feature branch.

### 1. Create an empty GitHub repository
Create a repository named `Second_CI_Pipeline` on GitHub. Do not initialize it with a README, license, or .gitignore.

### 2. Initialize the local repository and push shared files to `main`
Run these commands from this folder, replacing `YOUR-USERNAME`:

```bash
git init
git branch -M main
git add README.md __init__.py requirements.txt .github/workflows/ci.yml
git commit -m "Add shared CI pipeline setup"
git remote add origin https://github.com/YOUR-USERNAME/Second_CI_Pipeline.git
git push -u origin main
```

### 3. Create and push each feature branch
The program and test files are included in the folder, but remain untracked until you add them. Use the relevant pair on each branch.

**Program 31**
```bash
git checkout -b 31-pangram
git add 31_pangram.py test_31_pangram.py
git commit -m "Add pangram program and tests"
git push -u origin 31-pangram
```

For each next program, switch back to `main` and create a new branch:

```bash
git checkout main
git checkout -b 32-count-words
git add 32_count_words.py test_32_count_words.py
git commit -m "Add word count program and tests"
git push -u origin 32-count-words
```

Repeat the same pattern for the remaining branch/file pairs:

| Branch | Files to add |
|---|---|
| `33-first-non-repeating` | `33_first_non_repeating.py` and `test_33_first_non_repeating.py` |
| `34-check-sorted` | `34_check_sorted.py` and `test_34_check_sorted.py` |
| `35-move-zeros` | `35_move_zeros.py` and `test_35_move_zeros.py` |
| `36-most-frequent` | `36_most_frequent.py` and `test_36_most_frequent.py` |
| `37-rotate-string` | `37_rotate_string.py` and `test_37_rotate_string.py` |
| `38-missing-number-xor` | `38_missing_number_xor.py` and `test_38_missing_number_xor.py` |
| `39-transpose-matrix` | `39_transpose_matrix.py` and `test_39_transpose_matrix.py` |
| `40-gcd` | `40_gcd.py` and `test_40_gcd.py` |

Each branch must be created from `main`, not from the previous feature branch.

### 4. Trigger GitHub Actions
The supplied `ci.yml` runs on pull requests targeting `main`. After pushing each branch, open a pull request from that branch into `main`. GitHub Actions should run the syntax check and `pytest` automatically.

Note: after a feature branch is merged into `main`, that program/test pair becomes part of the shared base for later branches. If your instructor requires the branches to remain independent, do not merge until instructed.
