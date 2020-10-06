students = [('Smruthi', ['Electronics', 'Communication']),
            ('Gopi', ['Maths']),
            ('Parthi', ['Science', 'Geography']),
            ('Kanwar', ['Philosophy', 'Maths']),
            ('Jay', ['Python', 'Quantum Physics', 'Matlab', 'Kafka'])]

count = 0


for (name, subjects) in students:
    # print (name, 'is studying ', len(subjects), 'subjects')
    for subject in subjects:
        if subject == 'Maths':
            print(name, 'is studying maths')
            count += 1

print('total number of students studing Maths is ', count)

