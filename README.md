# OOP Income Tracker Example

This folder contains a class-based version of the income tracker.

Files:
- `entry.py` — data model classes for transactions and totals.
- `app.py` — the Tkinter application class and UI logic.
- `data.json` - entries are stored here for persistance between application logins.
- `test_entry_logic.py` - test cases on more complex defs and functionality (currently 3 testcases)
Note: I added the `__init__` file but it is not required for my code to run. (Its just for if I ever want to import the project from outside the current folder)

Run it from the project root :

```bash
python py app.py 
```

The code separates UI behavior from business data and uses `Entry` & `EntryLogic` to keep totals and entries logic.
 