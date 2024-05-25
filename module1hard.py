grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
alphabet_students = sorted(students)
data = {}
for i in range(5):
    average = sum(grades[i]) / len(grades[i])
    data[alphabet_students[i]] = average
    print(data)