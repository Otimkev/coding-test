# Coding Test — Mini Expense Tracker

**Estimated time:** ~1 hour  
**Choose your language:** JavaScript (Node.js) or Python 3

---

## The Task

Build a small **Expense Tracker** class that manages financial transactions. A transaction is either an **expense** (money going out) or **income** (money coming in).

You will find starter code with skeleton methods in your chosen language's folder. Your job is to implement all the methods, add validation, handle errors, and write tests.

---

## Requirements

### 1. Implement the `ExpenseTracker` class

#### `add_expense(amount, category, description)` / `addExpense(amount, category, description)`
- Records a new expense transaction.
- `amount`: a positive number (e.g. `25.50`)
- `category`: one of `['food', 'transport', 'entertainment', 'utilities', 'health', 'other']`
- `description`: a non-empty string

#### `add_income(amount, source, description)` / `addIncome(amount, source, description)`
- Records a new income transaction.
- `amount`: a positive number
- `source`: a non-empty string (e.g. `"salary"`, `"freelance"`)
- `description`: a non-empty string

#### `get_balance()` / `getBalance()`
- Returns the current balance as a number: **total income minus total expenses**.
- Returns `0` when there are no transactions.

#### `get_transactions(type=None)` / `getTransactions(type = null)`
- Returns a list/array of all transactions.
- If `type` is `"expense"` or `"income"`, filter by that type only.
- Each transaction should have these fields:
  ```
  { id, type, amount, category_or_source, description, created_at }
  ```

#### `get_summary()` / `getSummary()`
- Returns an object/dict with:
  ```
  {
    total_income:        number,
    total_expenses:      number,
    balance:             number,
    expenses_by_category: { food: number, transport: number, ... }
  }
  ```
- `expenses_by_category` should only include categories that have at least one expense.

---

### 2. Validation & Error Handling

Throw/raise a descriptive error for each of these:
- `amount` is not a number, is zero, or is negative
- `category` is not in the allowed list
- `source` or `description` is not a string, or is empty/whitespace-only
- An unrecognised `type` is passed to `get_transactions` / `getTransactions`

---

### 3. Tests

A few tests are already written for you. You must also **write at least 5 additional tests** of your own that cover cases you think are important.

---

## Setup

### JavaScript
```bash
cd javascript
npm install
npm test
```
Requires Node.js 18+.

### Python
```bash
cd python
pip install -r requirements.txt
pytest
```
Requires Python 3.8+.

---

### 4. Git & GitHub

Your code must be submitted via a GitHub Pull Request. Follow these steps:

1. **Create a public GitHub repository** named `expense-tracker-test`.

2. **Make an initial commit on `main`** containing only the unmodified starter code from this repo. This gives us a clean baseline to diff your PR against.

3. **Create a feature branch** named exactly:
   ```
   feature/expense-tracker
   ```

4. **Work on your feature branch.** As you implement, make **at least 3 separate commits** — split them logically, for example:
   - one for the core implementation
   - one for validation and error handling
   - one for your added tests

   Do **not** squash everything into a single commit.

5. **Add a `.gitignore`** file inside your language folder that excludes build artifacts. For example:
   - JavaScript: `node_modules/`, `coverage/`
   - Python: `__pycache__/`, `.pytest_cache/`, `*.pyc`

6. **Open a Pull Request** from `feature/expense-tracker` → `main` with:
   - A clear, descriptive title (not "my submission" or "done")
   - A short description covering: what you built, any assumptions you made, and anything you would improve with more time

7. **Share the PR link** when you submit.

---

## What We Are Looking For

| Area | What good looks like |
|------|----------------------|
| **Correctness** | All provided tests pass; edge cases are handled |
| **Code organisation** | Logic is clear and methods do one thing each |
| **Validation** | Errors are thrown early with helpful messages |
| **Tests** | Your added tests cover meaningful edge cases, not just happy paths |
| **Git hygiene** | Logical commits, meaningful messages, correct branching, `.gitignore` present |
| **PR quality** | Title and description show clear thinking and self-awareness |

---

## Submitting

Share the link to your Pull Request. No zip files needed.  
Include a brief `NOTES.md` in your branch if there is anything you did not have time to finish.
# coding-test
