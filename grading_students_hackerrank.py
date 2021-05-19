



def gradingStudents(grades):
    # Write your code here
    result = []
    for i in grades:
        if i > 37 and i % 5 >= 3:
            result.append(i + 5-(i % 5)) 
        else:
            result.append(i)
    return result


