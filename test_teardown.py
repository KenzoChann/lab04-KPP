import pytest
from bank import BankAccount


@pytest.fixture
def account_with_logging():
    print("[setup]")
    acct = BankAccount(100)
    yield acct
    print("[teardown]")


def test_deposit_with_teardown(account_with_logging):
    account_with_logging.deposit(50)
    assert account_with_logging.balance == 150


def test_withdraw_with_teardown(account_with_logging):
    account_with_logging.withdraw(30)
    assert account_with_logging.balance == 70