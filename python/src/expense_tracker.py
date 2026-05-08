from datetime import datetime, timezone

VALID_CATEGORIES = ['food', 'transport', 'entertainment', 'utilities', 'health', 'other']


class ExpenseTracker:
    def __init__(self):
        self._transactions = []
        self._next_id = 1

    def add_expense(self, amount, category, description):
        """
        Records a new expense.

        Args:
            amount      (float): Must be a positive number.
            category    (str):   Must be one of VALID_CATEGORIES.
            description (str):   Must be a non-empty string.

        Raises:
            ValueError: If any argument fails validation.
        """
        # TODO: validate inputs, then append a transaction dict to self._transactions
        # Transaction shape:
        # {
        #   'id': int,
        #   'type': 'expense',
        #   'amount': float,
        #   'category': str,
        #   'description': str,
        #   'created_at': datetime,
        # }
        pass

    def add_income(self, amount, source, description):
        """
        Records a new income entry.

        Args:
            amount      (float): Must be a positive number.
            source      (str):   Must be a non-empty string (e.g. 'salary').
            description (str):   Must be a non-empty string.

        Raises:
            ValueError: If any argument fails validation.
        """
        # TODO: validate inputs, then append a transaction dict to self._transactions
        # Transaction shape:
        # {
        #   'id': int,
        #   'type': 'income',
        #   'amount': float,
        #   'source': str,
        #   'description': str,
        #   'created_at': datetime,
        # }
        pass

    def get_balance(self):
        """
        Returns the current balance (total income - total expenses).

        Returns:
            float: The balance, or 0 if there are no transactions.
        """
        # TODO: calculate and return the balance
        pass

    def get_transactions(self, type=None):
        """
        Returns all transactions, optionally filtered by type.

        Args:
            type (str | None): 'expense', 'income', or None for all.

        Returns:
            list[dict]: The matching transactions.

        Raises:
            ValueError: If type is provided but not 'expense' or 'income'.
        """
        # TODO: return the full list or filter by type
        pass

    def get_summary(self):
        """
        Returns a summary of all transactions.

        Returns:
            dict: {
                'total_income': float,
                'total_expenses': float,
                'balance': float,
                'expenses_by_category': dict[str, float],  # only used categories
            }
        """
        # TODO: compute and return the summary dict
        pass
