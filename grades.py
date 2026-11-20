"""Convert numeric scores (0-100) into letter grades."""

MIN_SCORE = 0
MAX_SCORE = 100
GRADE_A_MIN = 90
GRADE_B_MIN = 80
GRADE_C_MIN = 70
GRADE_D_MIN = 60

GRADE_THRESHOLDS = (
    (GRADE_A_MIN, "A"),
    (GRADE_B_MIN, "B"),
    (GRADE_C_MIN, "C"),
    (GRADE_D_MIN, "D"),
)


def letter_grade(score):
    """Return the letter grade for a score from 0 to 100."""
    if not MIN_SCORE <= score <= MAX_SCORE:
        raise ValueError("Score must be between 0 and 100")

    for min_score, grade in GRADE_THRESHOLDS:
        if score >= min_score:
            return grade
    return "F"