"""Tuition fee calculation module refactored from legacy_fees.py."""

from dataclasses import dataclass
from enum import Enum

HOUR_RATE = 350
HIGH_FEE_THRESHOLD = 6000
HIGH_FEE_REDUCTION = 200
SUMMER_FEE = 150


class StudentType(Enum):
    """Supported student fee categories."""

    REGULAR = 1
    STAFF_CHILD = 2
    SCHOLARSHIP = 3


RATE_MULTIPLIER = {
    StudentType.REGULAR: 1.0,
    StudentType.STAFF_CHILD: 0.5,
    StudentType.SCHOLARSHIP: 0.0,
}

REPORT_LABELS = {
    StudentType.REGULAR: "Student fee",
    StudentType.STAFF_CHILD: "Staff child fee",
    StudentType.SCHOLARSHIP: "Scholarship fee",
}


@dataclass(frozen=True)
class Course:
    """A course with its credit hours."""

    hours: int


def tuition_fee(courses, student_type, summer=False, discount=0, extras=()):
    """Calculate the total tuition fee for a student."""
    rate = HOUR_RATE * RATE_MULTIPLIER[student_type]
    total = sum(course.hours * rate for course in courses)
    if total > HIGH_FEE_THRESHOLD:
        total -= HIGH_FEE_REDUCTION
    if summer:
        total += SUMMER_FEE
    total -= discount
    total += sum(extras)
    return total


def report(courses, student_type, summer=False, discount=0):
    """Build a text fee report without printing directly."""
    fee = tuition_fee(courses, student_type, summer, discount)
    lines = [f"{REPORT_LABELS[student_type]}: {fee}"]
    if fee > HIGH_FEE_THRESHOLD:
        lines.append("High fee")
    return "\n".join(lines)


def process_all(students):
    """Calculate tuition fees for all students, including scholarship students."""
    return {
        student["name"]: tuition_fee(
            student["courses"],
            student["type"],
            student["summer"],
        )
        for student in students
    }