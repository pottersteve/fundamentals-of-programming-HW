from csv import DictReader

def avg_grades(path):
    file = open(path, "r")
    reader = DictReader(file)
    grades = {}

    for row in reader:
        subject = row["subject"]
        grade = float(row["grade"])
        if subject not in grades:
            grades[subject] = [grade]
        else:
            grades[subject].append(grade)

    for subject in grades:
        avg = sum(grades[subject]) / len(grades[subject])
        grades[subject] = round(avg, 2)
        
    file.close()
    return grades    
    