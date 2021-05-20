# Tests. These rely on **set data in private/**.
# GPL licensing info + stuff
# run with `python3 -m pytest`

from people import Student

def test_append_does_not_modify():
    studs = []
    studs.append(Student.at_row(0))
    assert(studs[0].name == ('Bekendam', 'Aidan'))
    assert(studs[0].ranks == [4, 1, 4, 1, 0, 5])

    studs.append(Student.at_row(1))
    assert(studs[1].name == ('Tian', 'Emma'))
    assert(studs[1].ranks == [4, 1, 5, 1, 1, 4])

    assert(studs[0].name == ('Bekendam', 'Aidan'))
    assert(studs[0].ranks == [4, 1, 4, 1, 0, 5])
