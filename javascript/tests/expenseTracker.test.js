'use strict';

const { ExpenseTracker, VALID_CATEGORIES } = require('../src/expenseTracker');

// ---------------------------------------------------------------------------
// Pre-written tests — these must all pass with your implementation
// ---------------------------------------------------------------------------

describe('ExpenseTracker — provided tests', () => {
  let tracker;

  beforeEach(() => {
    tracker = new ExpenseTracker();
  });

  test('balance is 0 with no transactions', () => {
    expect(tracker.getBalance()).toBe(0);
  });

  test('adds an expense and reflects it in balance', () => {
    tracker.addExpense(50, 'food', 'Lunch');
    expect(tracker.getBalance()).toBe(-50);
  });

  test('adds income and reflects it in balance', () => {
    tracker.addIncome(1000, 'salary', 'Monthly salary');
    expect(tracker.getBalance()).toBe(1000);
  });

  test('balance is correct with mixed transactions', () => {
    tracker.addIncome(2000, 'salary', 'Monthly salary');
    tracker.addExpense(300, 'utilities', 'Electricity bill');
    tracker.addExpense(80, 'food', 'Groceries');
    expect(tracker.getBalance()).toBe(1620);
  });

  test('getTransactions returns all transactions', () => {
    tracker.addIncome(500, 'freelance', 'Website project');
    tracker.addExpense(30, 'transport', 'Bus pass');
    const all = tracker.getTransactions();
    expect(all).toHaveLength(2);
  });

  test('getTransactions filters by expense type', () => {
    tracker.addIncome(500, 'freelance', 'Website project');
    tracker.addExpense(30, 'transport', 'Bus pass');
    const expenses = tracker.getTransactions('expense');
    expect(expenses).toHaveLength(1);
    expect(expenses[0].type).toBe('expense');
  });

  test('getSummary returns correct totals', () => {
    tracker.addIncome(1000, 'salary', 'Monthly salary');
    tracker.addExpense(200, 'food', 'Groceries');
    tracker.addExpense(100, 'transport', 'Monthly pass');
    const summary = tracker.getSummary();
    expect(summary.total_income).toBe(1000);
    expect(summary.total_expenses).toBe(300);
    expect(summary.balance).toBe(700);
  });

  test('getSummary groups expenses_by_category', () => {
    tracker.addExpense(50, 'food', 'Lunch');
    tracker.addExpense(30, 'food', 'Dinner');
    tracker.addExpense(20, 'transport', 'Taxi');
    const { expenses_by_category } = tracker.getSummary();
    expect(expenses_by_category.food).toBe(80);
    expect(expenses_by_category.transport).toBe(20);
  });

  test('throws when amount is not a positive number', () => {
    expect(() => tracker.addExpense(-10, 'food', 'Lunch')).toThrow();
    expect(() => tracker.addExpense(0, 'food', 'Lunch')).toThrow();
    expect(() => tracker.addExpense('free', 'food', 'Lunch')).toThrow();
  });

  test('throws when category is invalid', () => {
    expect(() => tracker.addExpense(10, 'vacation', 'Hotel')).toThrow();
  });

  test('throws when description is empty or whitespace', () => {
    expect(() => tracker.addExpense(10, 'food', '')).toThrow();
    expect(() => tracker.addExpense(10, 'food', '   ')).toThrow();
  });

  test('throws when getTransactions receives an unrecognised type', () => {
    expect(() => tracker.getTransactions('salary')).toThrow();
  });

  test('each transaction gets a unique id', () => {
    tracker.addExpense(10, 'food', 'Coffee');
    tracker.addExpense(20, 'food', 'Lunch');
    const [t1, t2] = tracker.getTransactions();
    expect(t1.id).not.toBe(t2.id);
  });
});

// ---------------------------------------------------------------------------
// Your tests — add at least 5 tests below
// ---------------------------------------------------------------------------

describe('ExpenseTracker — my tests', () => {
  let tracker;

  beforeEach(() => {
    tracker = new ExpenseTracker();
  });

  // TODO: write your tests here
  // Think about cases like:
  //  - What happens with decimal amounts?
  //  - What does getSummary look like when there are no transactions?
  //  - What if someone passes null or undefined as an argument?
  //  - Are transactions returned in the order they were added?
  //  - Does filtering by 'income' only return income transactions?
});
