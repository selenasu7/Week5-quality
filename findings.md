# Week 5 Static Analysis Findings (`legacy_fees.py`)

## 1. Ruff Findings Table

| Rule | Count | Smell (lecture name) | Refactoring |
| :--- | :---: | :--- | :--- |
| F401 | 2 | Dead code (unused imports) | Delete the imports |
| PLR2004 | 6 | Magic numbers | Replace with named constants / an enum |
| C901 | 1 | High complexity / long conditional chain | Replace the `if`/`elif` chain with a rate table |
| PLR0913 | 1 | Long parameter list (too many arguments) | Remove the unused argument `y` |
| ARG001 | 1 | Dead code (unused function argument `y`) | Delete the unused argument `y` |
| B006 | 1 | Mutable default argument (`extra=[]`) | Use an immutable default `extras=()` |
| E711 / E712 | 2 | Redundant / non-idiomatic comparisons (`!= None`, `== True`) | Use `if summer:` and a default of `0` for the discount |
| F841 | 1 | Dead code (unused variable `tmp`) | Delete the unused variable `tmp` |
| N802 | 1 | Inconsistent / invalid function naming (`ProcessAll`) | Rename to `process_all` (snake_case) |

## 2. Extra Smells Ruff Did Not Report

1. **Mysterious names:** Single-letter parameter and variable names (`d`, `t`, `y`, `s`, `c`, `e`, `x`) obscure the meaning of the code.
2. **Primitive obsession and type-code comments:** Courses are stored as raw dictionaries (`{"h": ...}`) instead of a `Course` data class, and student types are encoded as integers (`1`, `2`, `3`) explained only in a comment instead of an `Enum`.
3. **Mixed responsibilities:** The `report` function mixes tuition calculation with console output (`print(...)`) instead of returning formatted text.
4. **Duplicated code:** `ProcessAll` repeats the `calc(...)` call inside separate `if` blocks for student types `1` and `2`.

## 3. Hidden Bug in `ProcessAll`

A scholarship student (`type == 3`) should pay `0`, because their tuition rate is zero. However, `ProcessAll` only has `if` statements for `st["type"] == 1` and `st["type"] == 2`, so neither branch runs for Omar (`type == 3`) and `print(st["name"], fee)` mistakenly prints Sara's leftover `fee` value (`1050`). If Omar were the first student in the list, `fee` would never be defined before `print`, causing Python to crash with an `UnboundLocalError`.