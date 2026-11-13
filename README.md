# 🎲 Dice Rolling Game (PS No: 54)

**Course:** Bachelor of Computer Application (BCA)  
**School:** School of Information Technology  
**University:** Rungta International Skills University  
**Student Name:** Homendra Kumar  
**GitHub ID:** Homie3579  
**Language:** Python 3  
**Concepts:** Random Module, While/For Loops, Modular Functions, Data Structures (Dictionary/List), Descriptive Statistics  

---

## 📋 Project Overview

The **Dice Rolling Game** is a console-based simulation developed in Python 3. It simulates rolling a standard six-faced die across a user-specified frequency ($1$ to $1000$ rolls). 

The program tracks individual outcomes, tallies face frequencies using a dictionary mapping, computes aggregate statistics (total sum and average value), and accurately determines the most frequent face(s), including tie handling.

---

## 🎯 Objectives

1. Implement random generation using Python's built-in `random.randint()`.
2. Restrict and validate inputs strictly between $1$ and $1000$.
3. Handle non-numeric and out-of-range exceptions gracefully with continuous retry loops.
4. Record occurrences in key-value pairs (`{face: count}`).
5. Compute arithmetic mean and sum across all generated rolls.
6. Support multi-round gameplay through interactive replay prompts (`y/n`).

---

## ✨ Key Features & Validations

| Feature | Description |
|---|---|
| **Boundary Protection** | Rejects inputs $< 1$, $> 1000$, non-integers, and empty strings. |
| **Statistical Analysis** | Automatically calculates `Total` and `Average` formatted to 2 decimal places. |
| **Multi-modal / Tie Handling** | Accurately identifies single or multiple most frequent numbers (e.g. `2 and 5 (2 times each)`). |
| **Singular/Plural Grammar** | Differentiates single outcomes (`1 time`, `Roll:`) from multiples (`2 times`, `Roll 1:`). |
| **Clean Console Lifecycle** | Continuous loop until explicit user exit (`n`), terminating with a goodbye message. |

---

## 📂 Project Repository Structure

```text
📁 Python-projects/
└── 📁 p1/
    ├── one.py                                  # Core Python script
    ├── README.md                               # Project documentation
    ├── Test_cases_passed.pdf                   # Test case verification report
    └── PS_No_54_Dice_Rolling_Game_details.png   # Problem statement & rubric allocation
```

---

## ▶️ Execution Instructions

1. Clone or download the repository:
   ```bash
   git clone https://github.com/Homie3579/Python-projects.git
   cd Python-projects/p1
   ```
2. Run the script via terminal or command prompt:
   ```bash
   python one.py
   ```

---

## 🧪 Verified Test Cases

### Test Case 1: Normal Input
* **Input:** `5` rolls
* **Output Sample:** `Roll 1: 5`, `Roll 2: 5`, `Roll 3: 3`, `Roll 4: 4`, `Roll 5: 4`
* **Stats:** `Total: 21 | Average: 4.20 | Most frequent: 4 and 5 (2 times each)`

### Test Case 2: Boundary Minimum Input
* **Input:** `1` roll
* **Output Sample:** `Roll: 1`
* **Stats:** `Total: 1 | Average: 1.00 | Most frequent: 1 (1 time)`

### Test Case 3: Invalid Input Handling
* **Inputs:** `0`, `abc`, `-2`, then valid `3`
* **Output:** Error notification `"Invalid input. Enter a whole number from 1 to 1000."` triggered on each invalid attempt before accepting `3`.

### Test Case 4: Multiple Scenario & Game Termination
* **Inputs:** `6` rolls, then `Play again? (y/n): n`
* **Output:** Displays frequencies, totals, averages, and safely exits with `"Thanks for playing!"`.

---

## 📄 Submission Files Checklist

- [x] **`one.py`** — Source program
- [x] **`README.md`** — Comprehensive documentation
- [x] **`Test_cases_passed.pdf`** — Full verification document containing all test run screenshots
- [x] **`PS_No_54_Dice_Rolling_Game_details.png`** — Original PS No. 54 allocation snapshot
- [x] Supporting data files: Not applicable for PS No. 54 (in-memory simulation).
