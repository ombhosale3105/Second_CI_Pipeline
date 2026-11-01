# Second_CI_Pipeline — Assignment 6

Fresh Git repository for Assignment 6. It contains `main` plus ten feature branches, one for each Python program (31–40). Each feature branch has its own program file and matching pytest file.

## Push the repository to GitHub

1. Create an **empty** GitHub repository named `Second_CI_Pipeline`.
2. Extract this ZIP and open a terminal inside the extracted `Second_CI_Pipeline_Fresh` folder.
3. Add your remote (replace YOUR-USERNAME):

```bash
git remote add origin https://github.com/YOUR-USERNAME/Second_CI_Pipeline.git
```

4. Push main:

```bash
git push -u origin main
```

5. **Push all ten feature branches** (this is essential; pushing `main` alone will publish only one branch):

```bash
git push origin --all
```

6. Confirm the remote has all branches:

```bash
git ls-remote --heads origin
```

You should see 11 branch refs total: `main` and the ten feature branches listed below.

## Feature branches

- `31-pangram`
- `32-count-words`
- `33-first-non-repeating`
- `34-check-sorted`
- `35-move-zeros`
- `36-most-frequent`
- `37-rotate-string`
- `38-missing-number-xor`
- `39-transpose-matrix`
- `40-gcd`

## Pull Requests

On GitHub, create one Pull Request for each feature branch, with `main` as the base branch. Wait for the **Python CI** check to pass, then merge the PR. Repeat for all ten branches.

## Run tests locally

```bash
python -m pip install -r requirements.txt
python -m pytest -v
```
