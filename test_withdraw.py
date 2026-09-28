import pytest
from bank import BankAccount


@pytest.fixture
def account():
    return BankAccount(100)


def test_withdraw_reduces_balance(account):
    account.withdraw(40)
    assert account.balance == 60


def test_overdraft_raises_error(account):
    with pytest.raises(ValueError):
        account.withdraw(150)
