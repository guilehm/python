# https://www.hackerrank.com/challenges/nested-list/problem?h_r=next-challenge&h_v=zen

if __name__ == '__main__':
    students_grades = dict()
    grades = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        grades.append(score)
        students_grades[name] = score
    second_lowest_grade = sorted(set(grades))[1]
    for student in sorted(students_grades.items(), key=lambda x: x[0]):
        if student[1] == second_lowest_grade:
            print(student[0])
