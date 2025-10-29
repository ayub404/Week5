names = ["Alice", "Bob", "Charlie", "David", 'Ayub', 'Humoyun']
scores = [88, 92, 99, 95, 95, 88]

def find_best_student(student_names, student_scores):
    max_score = 0
    index = 0
    highest_index = 0
    if len(names) == 0 and len(scores) == 0:
        return None
    for i in student_scores:
        if max_score < i:
            max_score = i
            highest_index = index

        index += 1
    
    return student_names[highest_index]




def finding_tiar_stu( student_scores, student_names):
    
    
    tiar_index = []
    if  len(student_scores) == 0:
        return None
    step = 0
    while step < len(student_scores) - 1:
        for i in range(step + 1, len(student_scores)):
            if student_scores[step] == student_scores[i]:
                tiar_index.append((step, i))
        step += 1
    
    firststu = tiar_index[0][0]
    secondstu = tiar_index[1][1]
    return f"Top student in a tie is:{student_names[firststu]} and {student_names[secondstu]}"

    



def res_empty(students_scores):
    if len(students_scores) != 0:
        return None
    
    
isempty = res_empty(scores)
top_tie = finding_tiar_stu(scores, names)
best_student = find_best_student(names, scores)

print(f"The top student is: {best_student}")
print(top_tie)
print(f"Results for empty list: {isempty}")
