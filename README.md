# lab04-KPP
## Who Did What
| Member | GitHub Username | File |
|---|---|---|
| Preston Shah | preston-shah | test_teardown.py |
| Paing Oo Thant | potpot2626 | test_withdraw.py, test_shared.py |
| Kenzo | KenzoChann | conftest.py, test_deposit.py |

## Our Merge Conflict

Conflict markers we encountered:

    <<<<<<< HEAD
    | Paing Oo Thant | potpot2626 | test_withdraw.py, test_shared.py |
    =======
    | Kenzo | KenzoChann | conftest.py, test_deposit.py |
    >>>>>>> 4175db51e84ec24859704f499478db9047ad764a

Lines kept in the final version: we kept both rows (and later Preston's row too), because each row belongs to a different group member. We only deleted the marker lines.

Why Git could not resolve it automatically: two people changed the same lines of README.md in different commits, so Git could not tell which version should be kept.

Preston also got a conflict when he ran git pull, because he had already committed his own row before pulling. He resolved it the same way: he kept all the rows and deleted the marker lines.

##  Git Contribution Summary
     9  KenzoChann
     6  potpot2626
     6  preston-shah

## Reflection Questions

1. **Why was your push rejected, and how did you fix it?**
   My push was rejected because a teammate had already pushed to GitHub, so my local copy was out of date. I fixed it by running `git pull` to merge their changes and then `git push` again.

2. **Why could Git not resolve the README conflict automatically?**
   Several of us edited the same lines at the end of the table in `README.md`, so Git couldn't tell which version to keep and needed us to decide.

3. **What is the difference between committing and pushing?**
   Committing saves a snapshot in my local repository only. Pushing uploads those commits to GitHub so teammates can see them.

4. **How do fixtures reduce duplicated setup code in tests?**
   A fixture defines setup once, like creating `BankAccount(100)`, and any test can request it by name instead of repeating the same lines.
