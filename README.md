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