# Tests. These rely on **set data in private/**.
# GPL licensing info + stuff
# run with `python3 -m pytest`

from people import *
assert(students.shape[0] == 76)

def test_append_does_not_modify():
    studs = []
    studs.append(student_at_row(0))
    assert(studs[0].name == ('Bekendam', 'Aidan'))
    assert(studs[0].ranks == [4, 1, 4, 1, 0, 5])
    studs.append(student_at_row(1))
    assert(studs[0].name == ('Bekendam', 'Aidan'))
    assert(studs[0].ranks == [4, 1, 4, 1, 0, 5])
