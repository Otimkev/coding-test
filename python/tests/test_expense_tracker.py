import pytest
from src.expense_tracker import ExpenseTracker, VALID_CATEGORIES

# ---------------------------------------------------------------------------
# Pre-written tests — these must all pass with your implementation
# ---------------------------------------------------------------------------

class TestProvidedTests:
    def setup_method(self):
        self.tracker = ExpenseTracker()

    def test_balance_is_zero_with_no_transactions(self):
        assert self.tracker.get_balance() == 0

    def test_adds_expense_and_reflects_in_balance(self):
        self.tracker.add_expense(50, 'food', 'Lunch')
        assert self.tracker.get_balance() == -50

    def test_adds_income_and_reflects_in_balance(self):
        self.tracker.add_income(1000, 'salary', 'Monthly salary')
        assert self.tracker.get_balance() == 1000

    def test_balance_correct_with_mixed_transactions(self):
        self.tracker.add_income(2000, 'salary', 'Monthly salary')
        self.tracker.add_expense(300, 'utilities', 'Electricity bill')
        self.tracker.add_expense(80, 'food', 'Groceries')
        assert self.tracker.get_balance() == 1620

    def test_get_transactions_returns_all(self):
        self.tracker.add_income(500, 'freelance', 'Website project')
        self.tracker.add_expense(30, 'transport', 'Bus pass')
        assert len(self.tracker.get_transactions()) == 2

    def test_get_transactions_filters_by_expense_type(self):
        self.tracker.add_income(500, 'freelance', 'Website project')
        self.tracker.add_expense(30, 'transport', 'Bus pass')
        expenses = self.tracker.get_transactions('expense')
        assert len(expenses) == 1
        assert expenses[0]['type'] == 'expense'

    def test_get_summary_returns_correct_totals(self):
        self.tracker.add_income(1000, 'salary', 'Monthly salary')
        self.tracker.add_expense(200, 'food', 'Groceries')
        self.tracker.add_expense(100, 'transport', 'Monthly pass')
        summary = self.tracker.get_summary()
        assert summary['total_income'] == 1000
        assert summary['total_expenses'] == 300
        assert summary['balance'] == 700

    def test_get_summary_groups_expenses_by_category(self):
        self.tracker.add_expense(50, 'food', 'Lunch')
        self.tracker.add_expense(30, 'food', 'Dinner')
        self.tracker.add_expense(20, 'transport', 'Taxi')
        by_cat = self.tracker.get_summary()['expenses_by_category']
        assert by_cat['food'] == 80
        assert by_cat['transport'] == 20

    def test_raises_for_negative_amount(self):
        with pytest.raises(ValueError):
            self.tracker.add_expense(-10, 'food', 'Lunch')

    def test_raises_for_zero_amount(self):
        with pytest.raises(ValueError):
            self.tracker.add_expense(0, 'food', 'Lunch')

    def test_raises_for_non_numeric_amount(self):
        with pytest.raises((ValueError, TypeError)):
            self.tracker.add_expense('free', 'food', 'Lunch')

    def test_raises_for_invalid_category(self):
        with pytest.raises(ValueError):
            self.tracker.add_expense(10, 'vacation', 'Hotel')

    def test_raises_for_empty_description(self):
        with pytest.raises(ValueError):
            self.tracker.add_expense(10, 'food', '')

    def test_raises_for_whitespace_only_description(self):
        with pytest.raises(ValueError):
            self.tracker.add_expense(10, 'food', '   ')

    def test_raises_for_unknown_type_in_get_transactions(self):
        with pytest.raises(ValueError):
            self.tracker.get_transactions('salary')

    def test_each_transaction_gets_unique_id(self):
        self.tracker.add_expense(10, 'food', 'Coffee')
        self.tracker.add_expense(20, 'food', 'Lunch')
        t1, t2 = self.tracker.get_transactions()
        assert t1['id'] != t2['id']


# ---------------------------------------------------------------------------
# Your tests — add at least 5 tests below
# ---------------------------------------------------------------------------

class TestMyTests:
    def setup_method(self):
        self.tracker = ExpenseTracker()

    # TODO: write your tests here
    # Think about cases like:
    #  - What happens with decimal amounts (e.g. 9.99)?
    #  - What does get_summary look like when there are no transactions?
    #  - What if None is passed as an argument?
    #  - Are transactions returned in the order they were added?
    #  - Does filtering by 'income' only return income transactions?
