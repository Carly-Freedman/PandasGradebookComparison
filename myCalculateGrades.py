
from pathlib import Path
import pandas as pd
import time
pd.set_option('display.max_columns', None, 'display.max_rows', None)
HERE = HERE = Path(__file__).parent
DATA_FOLDER = HERE / "data"

HW_WEIGHT = 30
QUIZ_WEIGHT = 30
EXAM_WEIGHT = 40

#For use in mapping total grades to final letter grades
gradeCutoffs = [[[90], ["A"]], [[80], ["B"]],[[70], ["C"]], [[60], ["D"]],[[0], ["F"]]]

#function to read in data for each type of assignment
def readCategoryData(category):
    fileName = category + '.csv'
    data = pd.read_csv(
        DATA_FOLDER / fileName,
        converters = {"SID": str.lower},
        index_col = "SID",
        )
    return data

#extracts grade information from previously initialized data frames
def getGradeData(category, curData, num):  
    names = []
       
    for n in range(1, num + 1):
        names.append(category + ' ' +  str(n) + ' Score')
        names.append(category + ' '  + str(n) + ' Max Points')

    
    grades = curData.loc[:, names]
    
    return grades

#calculates final grade percentages and letters
def calculateGrades(category, grades, num):
    tempSumScore = 0
    tempSumMax = 0
    for n in range(1, num + 1):
        grades[f"{category} {n} Grade"] = (
            grades[f"{category} {n} Score"] / grades[f"{category} {n} Max Points"]
        )
        tempSumScore += grades[f"{category} {n} Score"]
        tempSumMax +=  grades[f"{category} {n} Max Points"]

    grades[f"Total {category} Grade"] = (
        tempSumScore/tempSumMax
        )

    return grades

def mapGrade(finalGrades):
    for grade in gradeCutoffs:
        if finalGrades >= grade[0][0]:
            return grade[1][0]
roster = pd.read_csv(
    DATA_FOLDER / "Roster.csv",
    converters={"NetID": str.lower, "Email Address": str.lower},
    usecols=['Name',  'NetID', 'Email Address'],
    index_col='NetID',
)

#keep track of number of elements 
numel = 0
numel += len(roster) * len(roster.columns)
numRecords = len(roster)


hw = readCategoryData('HW')
quiz = readCategoryData('Quiz')
exam = readCategoryData('Exam')


numel += (len(hw) * len(hw.columns)) + (len(quiz) * len(quiz.columns)) + (len(exam) * len(exam.columns))
n_hw = 10
n_quiz = 5
n_exam = 4

hwGrades = getGradeData('HW', hw, n_hw)
quizGrades = getGradeData('Quiz', quiz, n_quiz)
examGrades = getGradeData('Exam', exam, n_exam)

hwGrades = calculateGrades('HW', hwGrades, n_hw)
quizGrades = calculateGrades('Quiz', quizGrades, n_quiz)
examGrades = calculateGrades('Exam', examGrades, n_exam)

#final formatting of grades
allGrades = pd.merge(
    hwGrades, quizGrades, left_index=True, right_index=True,
)
allGrades = pd.merge(
    allGrades, examGrades, left_index = True, right_index = True
)
allGrades[f"Final Grade %"] = (
    allGrades['Total HW Grade'] * HW_WEIGHT + allGrades['Total Quiz Grade'] * QUIZ_WEIGHT + allGrades['Total Exam Grade'] * EXAM_WEIGHT
    )

allGrades[f"Final Grade Letter"] = (
    allGrades[f"Final Grade %"].map(mapGrade)
    )

