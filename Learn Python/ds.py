class StaticArray:
    def __init__(self, n):
        self.data = [None] * n
    
    def get_at(self, i):
        if not (0 <= i < len(self.data)):
            raise IndexError
        return self.data[i]

    def set_at(self, i, x):
        if not (0 <= i < len(self.data)):
            raise IndexError
        self.data[i] = x

def birthday_match(students):
    n = len(students)
    record = StaticArray(n)
    for k in range(n):
        (name1, bday1) = students[k]
        for i in range(k):  # Changed indentation to correct loop scope
            (name2, bday2) = record.get_at(i)
            if bday1 == bday2:
                return (name1, name2)
        record.set_at(k, (name1, bday1))
    return None

students_list = [
    ("Alice", "2000-05-15"),
    ("Bob", "2000-05-20"),
    ("Charlie", "2001-03-10"),
    ("David", "2000-05-15"),
    ("Eve", "2002-01-30"),
    # Add more students as needed
]

result = birthday_match(students_list)
print(result)

