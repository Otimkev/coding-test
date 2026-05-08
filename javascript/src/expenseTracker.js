'use strict';

const VALID_CATEGORIES = ['food', 'transport', 'entertainment', 'utilities', 'health', 'other'];

class ExpenseTracker {
  constructor() {
    this._transactions = [];
    this._nextId = 1;
  }

  /**
   * Records a new expense.
   * @param {number} amount      - Must be a positive number
   * @param {string} category    - Must be one of VALID_CATEGORIES
   * @param {string} description - Must be a non-empty string
   */
  addExpense(amount, category, description) {
    // TODO: validate inputs, then push a transaction object to this._transactions
    // Transaction shape: { id, type: 'expense', amount, category, description, createdAt }
  }

  /**
   * Records a new income entry.
   * @param {number} amount      - Must be a positive number
   * @param {string} source      - Must be a non-empty string (e.g. 'salary')
   * @param {string} description - Must be a non-empty string
   */
  addIncome(amount, source, description) {
    // TODO: validate inputs, then push a transaction object to this._transactions
    // Transaction shape: { id, type: 'income', amount, source, description, createdAt }
  }

  /**
   * Returns the current balance (total income - total expenses).
   * @returns {number}
   */
  getBalance() {
    // TODO: calculate and return the balance
  }

  /**
   * Returns all transactions, optionally filtered by type.
   * @param {string|null} type - 'expense', 'income', or null for all
   * @returns {Array}
   */
  getTransactions(type = null) {
    // TODO: return the full list or filter by type
    // Throw an error if type is provided but not 'expense' or 'income'
  }

  /**
   * Returns a summary of all transactions.
   * @returns {{ total_income: number, total_expenses: number, balance: number, expenses_by_category: object }}
   */
  getSummary() {
    // TODO: compute and return the summary object
    // expenses_by_category should only include categories that have been used
  }
}

module.exports = { ExpenseTracker, VALID_CATEGORIES };
