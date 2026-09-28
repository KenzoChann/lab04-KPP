# lab04-KPP

> **192-211 Automated Software Testing** · Lab 4: Collaborating on a Shared GitHub Repository

## Group Name

**KPP**

## Contents

- [Project Overview](#project-overview)
- [Who Did What](#who-did-what)
- [Our Merge Conflict](#our-merge-conflict)
- [Git Contribution Summary](#git-contribution-summary)
- [Reflection Questions](#reflection-questions)

## Project Overview

This repository holds a small `pytest` suite for a `BankAccount` class (`bank.py`). Each member wrote their own test file and pushed it to the shared repository, and the group used the same repository to practise pulling, pushing and resolving a merge conflict.

### Repository Structure

```text
lab04-KPP/
├── .gitignore
├── README.md
├── bank.py            # BankAccount class under test
├── conftest.py        # shared funded_account fixture
├── test_deposit.py    # deposit tests
├── test_withdraw.py   # withdrawal and overdraft tests
├── test_teardown.py   # yield fixture with setup/teardown
└── test_shared.py     # tests using the shared fixture
```

## Who Did What

| Member | GitHub Username | Files | Contribution |
|---|---|---|---|
| Preston Shah | [preston-shah](https://github.com/preston-shah) | `test_teardown.py` | Yield fixture that prints `[setup]` and `[teardown]`, plus two tests using it |
| Paing Oo Thant | [potpot2626](https://github.com/potpot2626) | `test_withdraw.py`, `test_shared.py` | Withdrawal and overdraft (`ValueError`) tests; tests using the shared fixture |
| Kenzo | [KenzoChann](https://github.com/KenzoChann) | `conftest.py`, `test_deposit.py` | Shared `funded_account` fixture; deposit tests. Also the repository owner |

## Our Merge Conflict ##

### What happened

In Round 3, all of us edited the same table in `README.md` at about the same time. The first person to push succeeded. Everyone else got a merge conflict on `git pull`, because our commits changed the same lines.

### Conflict markers we encountered

```text
<<<<<<< HEAD
| Paing Oo Thant | potpot2626 | test_withdraw.py, test_shared.py |
=======
| Kenzo | KenzoChann | conftest.py, test_deposit.py |
>>>>>>> 4175db51e84ec24859704f499478db9047ad764a
```
### Preston's conflict ###

Preston also hit a conflict on `git pull`, because he had already committed his own row before pulling. He resolved it the same way: he kept all the rows, deleted the marker lines, then ran `git add`, `git commit` and `git push`.

### Lines kept in the final version

We kept **both rows**, because each row belongs to a different member, and deleted only the three marker lines. Preston's row was added afterwards in the same way.

| Member | GitHub Username | File |
|---|---|---|
| Preston Shah | preston-shah | test_teardown.py |
| Paing Oo Thant | potpot2626 | test_withdraw.py, test_shared.py |
| Kenzo | KenzoChann | conftest.py, test_deposit.py |

## Git Contribution Summary

Output of `git shortlog -sn`:

```text
     9  KenzoChann
     6  potpot2626
     6  preston-shah
```

## Reflection Questions

1. **Why was your push rejected, and how did you fix it?**
   A teammate had already pushed to GitHub, so my local copy was behind `main`. I ran `git pull` to merge their changes, then `git push` again.

2. **Why could Git not resolve the README conflict automatically?**
   Several of us edited the same lines at the end of the table in `README.md`. Git could not tell which version to keep, so it needed us to decide.

3. **What is the difference between committing and pushing?**
   Committing saves a snapshot in my local repository only. Pushing uploads those commits to GitHub so teammates can see them.

4. **How do fixtures reduce duplicated setup code in tests?**
   A fixture defines setup once, such as creating `BankAccount(100)`, and any test can request it by name instead of repeating the same lines.