

def main():
    
    mainDict = {
            "Rohan": {
                "Math": 93,
                "English": 88,}}
    mainRun = True
    while mainRun:
        print("""
Commands:
    'view report card'
    'add student'
    'add subject & grade'
    'remove student'
    'remove subject & grade' 
    'quit' """)
        cmdInput = input(":")
        
        if cmdInput == "add student":           
            newNameInput = input("New student name: ")
            if newNameInput in mainDict:
                print("Student already exists")
            else:
                mainDict[newNameInput] = {}
            continue
        elif cmdInput == "view report card":
            if mainDict == {}:
                print("Report card is empty")
            else:
                for i in mainDict:
                    print(i)
                    for j in mainDict[i]:
                        print(j, mainDict[i][j])
            continue
        elif cmdInput == "add subject & grade":
            studentNameInput = input("Name of the student: ")
            newSubjectInput = input("New subject: ")
            newGradeInput = input("New grade for the subject: ")
            if int(newGradeInput) > 100 or int(newGradeInput) < 0:
                print("Grade must be between 0 and 100")
                continue
            try:
                mainDict[studentNameInput][newSubjectInput] = newGradeInput
                continue
            except:
                print("Invalid name.")
                continue
        elif cmdInput == "remove student":
            removeStudentName = input("Name of student: ")
            try:
                del mainDict[removeStudentName]
                print("Succesfully removed.")
                continue
            except:
                print("Invalid name.")
                continue
        elif cmdInput == "remove subject & grade":
            removeStudentName2 = input("Student name: ")
            removeSubjectName = input("Subject to remove: ")
            try:
                del mainDict[removeStudentName2][removeSubjectName]
                print("Successfully removed")
                continue
            except:
                print("Invalid name or subject")
                continue


        elif cmdInput == "quit":
            break
        else:
            print("Invalid command")
            continue
        break


if __name__ == "__main__":
    main()