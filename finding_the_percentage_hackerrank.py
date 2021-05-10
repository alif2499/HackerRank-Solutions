    sum = 0
    for i in student_marks:
        if i == query_name:
            value = student_marks[i]
            for j in range(len(value)):
                sum = sum + value[j]
            average = sum/len(value)
    print("{:.2f}".format(average))