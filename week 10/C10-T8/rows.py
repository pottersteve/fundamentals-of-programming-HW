from csv import DictReader

def count_complete_rows(path):
    file = open(path, "r")
    reader = DictReader(file)
    completed = 0
    for row in reader:
        check = True

        for value in row.values():
            if value.strip() == "":
                check = False
                break   

        if check:
            completed += 1
                
    file.close()
    return completed
