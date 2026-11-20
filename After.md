Week 5: Before/After Comparison & Pairing Reflection

====================================================



Before/After Comparison

-----------------------

Measure                        | Before (legacy_fees.py)                      | After (fees.py)

-------------------------------|----------------------------------------------|------------------------------------------------------

Ruff issues (total)            | 16 (lab config) / 6 (current pyproject.toml) | 0 (fees.py)

Highest cyclomatic complexity  | 9 (calc)                                     | 4 (tuition_fee)

Arguments of the main function | 6                                            | 5

Pylint score (/10)             | 6.32 / 10                                    | 9.69 / 10

Tests passing                  | 0 (no tests)                                 | 16 passed (6 in test_fees.py, 10 in test_grades.py)



Pairing Reflection

------------------

Working together in driver and navigator roles helped us catch boundary cases and unclear naming early instead of leaving them for the end. Switching roles on a timer kept both of us engaged and ensured we both understood every refactoring step. Writing characterization tests before touching the legacy code gave us confidence that our structural changes did not alter existing behaviour while pytest verified each small step. Combining pair review with Ruff and Pylint showed us that static-analysis tools quickly flag mechanical smells, while human review is still necessary to catch logic bugs such as the skipped scholarship student.