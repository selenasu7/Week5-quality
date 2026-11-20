(.venv) PS C:\Users\Acer\Documents\#L4 T1\Agile Software Engineering\Project\week5> ruff check
I001 [*] Import block is un-sorted or un-formatted
 --> legacy_fees.py:2:1
  |
2 | / import os
3 | | import math
  | |___________^
4 |
5 |   def calc(d, t, y, s, disc, extra=[]):
  |
help: Organize imports
  |
1 |
2 + import math
3 | import os
  - import math
4 |
5 +
6 | def calc(d, t, y, s, disc, extra=[]):
  |

F401 [*] `os` imported but unused
 --> legacy_fees.py:2:8
  |
2 | import os
  |        ^^
3 | import math
  |
help: Remove unused import: `os`
  |
1 |
  - import os
2 | import math
  |

F401 [*] `math` imported but unused
 --> legacy_fees.py:3:8
  |
2 | import os
3 | import math
  |        ^^^^
4 |
5 | def calc(d, t, y, s, disc, extra=[]):
  |
help: Remove unused import: `math`
  |
2 | import os
  - import math
3 |
  |

E712 Avoid equality comparisons to `True`; use `s:` for truth checks
  --> legacy_fees.py:20:8
   |
18 |         total = total - 200
19 |
20 |     if s == True:
   |        ^^^^^^^^^
21 |         total = total + 150
   |
help: Replace with `s`
   |
19 |
   -     if s == True:
20 +     if s:
21 |         total = total + 150
   |
note: This is an unsafe fix and may change runtime behavior

E711 Comparison to `None` should be `cond is not None`
  --> legacy_fees.py:23:16
   |
21 |         total = total + 150
22 |
23 |     if disc != None:
   |                ^^^^
24 |         total = total - disc
   |
help: Replace with `cond is not None`
   |
22 |
   -     if disc != None:
23 +     if disc is not None:
24 |         total = total - disc
   |
note: This is an unsafe fix and may change runtime behavior

F841 Local variable `tmp` is assigned to but never used
  --> legacy_fees.py:29:5
   |
27 |         total = total + e
28 |
29 |     tmp = total * 1.0
   |     ^^^
30 |     return total
   |
help: Remove assignment to unused variable `tmp`
   |
28 |
   -     tmp = total * 1.0
29 +     total * 1.0
30 |     return total
   |
note: This is an unsafe fix and may change runtime behavior

I001 [*] Import block is un-sorted or un-formatted
 --> test_grades.py:1:1
  |
1 | / import pytest
2 | | from grades import letter_grade
  | |_______________________________^
help: Organize imports
  |
1 | import pytest
2 +
3 | from grades import letter_grade
  |

F811 Redefinition of unused `test_zero_is_an_f` from line 23
  --> test_grades.py:49:5
   |
48 | # Round 2: Boundary tests
49 | def test_zero_is_an_f():
   |     ^^^^^^^^^^^^^^^^^ `test_zero_is_an_f` redefined here
50 |     assert letter_grade(0) == "F"
   |
  ::: test_grades.py:23:5
   |
22 | # Round 2 boundary tests: 0, 100, 60, 69, 70, and -1
23 | def test_zero_is_an_f():
   |     ----------------- previous definition of `test_zero_is_an_f` here
24 |     assert letter_grade(0) == "F"
   |
help: Remove definition: `test_zero_is_an_f`

F811 Redefinition of unused `test_hundred_is_an_a` from line 27
  --> test_grades.py:53:5
   |
53 | def test_hundred_is_an_a():
   |     ^^^^^^^^^^^^^^^^^^^^ `test_hundred_is_an_a` redefined here
54 |     assert letter_grade(100) == "A"
   |
  ::: test_grades.py:27:5
   |
27 | def test_hundred_is_an_a():
   |     -------------------- previous definition of `test_hundred_is_an_a` here
28 |     assert letter_grade(100) == "A"
   |
help: Remove definition: `test_hundred_is_an_a`

F811 Redefinition of unused `test_sixty_is_a_d` from line 31
  --> test_grades.py:57:5
   |
57 | def test_sixty_is_a_d():
   |     ^^^^^^^^^^^^^^^^^ `test_sixty_is_a_d` redefined here
58 |     assert letter_grade(60) == "D"
   |
  ::: test_grades.py:31:5
   |
31 | def test_sixty_is_a_d():
   |     ----------------- previous definition of `test_sixty_is_a_d` here
32 |     assert letter_grade(60) == "D"
   |
help: Remove definition: `test_sixty_is_a_d`

F811 Redefinition of unused `test_sixty_nine_is_a_d` from line 35
  --> test_grades.py:61:5
   |
61 | def test_sixty_nine_is_a_d():
   |     ^^^^^^^^^^^^^^^^^^^^^^ `test_sixty_nine_is_a_d` redefined here
62 |     assert letter_grade(69) == "D"
   |
  ::: test_grades.py:35:5
   |
35 | def test_sixty_nine_is_a_d():
   |     ---------------------- previous definition of `test_sixty_nine_is_a_d` here
36 |     assert letter_grade(69) == "D"
   |
help: Remove definition: `test_sixty_nine_is_a_d`

F811 Redefinition of unused `test_seventy_is_a_c` from line 39
  --> test_grades.py:65:5
   |
65 | def test_seventy_is_a_c():
   |     ^^^^^^^^^^^^^^^^^^^ `test_seventy_is_a_c` redefined here
66 |     assert letter_grade(70) == "C"
   |
  ::: test_grades.py:39:5
   |
39 | def test_seventy_is_a_c():
   |     ------------------- previous definition of `test_seventy_is_a_c` here
40 |     assert letter_grade(70) == "C"
   |
help: Remove definition: `test_seventy_is_a_c`

F811 Redefinition of unused `test_negative_score_is_rejected` from line 43
  --> test_grades.py:69:5
   |
69 | def test_negative_score_is_rejected():
   |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ `test_negative_score_is_rejected` redefined here
70 |     with pytest.raises(ValueError):
71 |         letter_grade(-1)
   |
  ::: test_grades.py:43:5
   |
43 | def test_negative_score_is_rejected():
   |     ------------------------------- previous definition of `test_negative_score_is_rejected` here
44 |     with pytest.raises(ValueError):
45 |         letter_grade(-1)
   |
help: Remove definition: `test_negative_score_is_rejected`

Found 13 errors.
[*] 4 fixable with `--fix` (3 unsafe fixes available with `--fix --unsafe-fixes`).

(.venv) PS C:\Users\Acer\Documents\#L4 T1\Agile Software Engineering\Project\week5> ruff check --statistics
6       F811    [ ] redefined-while-unused
2       I001    [*] unsorted-imports
2       F401    [*] unused-import
1       E711    [ ] none-comparison
1       E712    [ ] true-false-comparison
1       F841    [ ] unused-variable
Found 13 errors.
[*] 4 fixable with `--fix` (3 unsafe fixes available with `--fix --unsafe-fixes`).

(.venv) PS C:\Users\Acer\Documents\#L4 T1\Agile Software Engineering\Project\week5> pylint legacy_fees.py
************* Module legacy_fees
legacy_fees.py:1:0: C0114: Missing module docstring (missing-module-docstring)
legacy_fees.py:5:0: C0116: Missing function or method docstring (missing-function-docstring)
legacy_fees.py:5:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
legacy_fees.py:5:0: R0913: Too many arguments (6/5) (too-many-arguments)
legacy_fees.py:5:0: R0917: Too many positional arguments (6/5) (too-many-positional-arguments)
legacy_fees.py:20:7: C0121: Comparison 's == True' should be 's is True' if checking for the singleton value True, or 's' if testing for truthiness (singleton-comparison)
legacy_fees.py:23:7: C0121: Comparison 'disc != None' should be 'disc is not None' (singleton-comparison)
legacy_fees.py:5:15: W0613: Unused argument 'y' (unused-argument)
legacy_fees.py:29:4: W0612: Unused variable 'tmp' (unused-variable)
legacy_fees.py:33:0: C0116: Missing function or method docstring (missing-function-docstring)
legacy_fees.py:47:0: C0116: Missing function or method docstring (missing-function-docstring)
legacy_fees.py:47:0: C0103: Function name "ProcessAll" doesn't conform to snake_case naming style (invalid-name)
legacy_fees.py:2:0: W0611: Unused import os (unused-import)
legacy_fees.py:3:0: W0611: Unused import math (unused-import)

-----------------------------------
Your code has been rated at 6.32/10