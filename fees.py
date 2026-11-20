def tuition_fee(courses, student_type, summer, discount, extra=[]):
    # t: 1=student, 2=staff child, 3=scholarship
    total = 0

    for c in courses:
        if student_type == 1:
            total = total + c["h"] * 350
        elif student_type == 2:
            total = total + c["h"] * 350 * 0.5
        elif student_type == 3:
            total = total + 0

    if total > 6000:
        total = total - 200

    if summer == True:
        total = total + 150

    if discount != None:
        total = total - discount

    for e in extra:
        total = total + e

    return total





def report(courses, student_type, summer, discount):
    x = tuition_fee(courses, student_type, summer, discount)

    if student_type == 1:
        print("Student fee: " + str(x))
    elif student_type == 2:
        print("Staff child fee: " + str(x))

    if x > 6000:
        print("High fee")

    return x


def process_all(students):
    for st in students:
        if st["type"] == 1:
            fee = tuition_fee(st["courses"], 1, st["summer"], None)

        elif st["type"] == 2:
            fee = tuition_fee(st["courses"], 2, st["summer"], None)

        else:
            continue

        print(st["name"], fee)
