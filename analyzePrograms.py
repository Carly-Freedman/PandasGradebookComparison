import time

#Code Analysis and Comparison for Carly Freedman\'s take on Dan Bader\'s Python Pandas gradebook

tic = time.time()
import calculatingGrades
toc = time.time()
print('Code Analysis and Comparison for Carly Freedman\'s take on Dan Bader\'s Python Pandas gradebook')
print('Time in seconds it takes to load data and calculate grades for Dan Bader\'s RealPython source code:')
sourceCodeRuntime = toc - tic
print(sourceCodeRuntime)


tic = time.time()
import myCalculateGrades
toc = time.time()
print('Time in seconds it takes to load data and calculate grades for my code:')
myRuntime = toc - tic
print(myRuntime)



print('Number of data elements read from file in my code:')
print(myCalculateGrades.numel)
print('Number of students used loaded in for my code:')
print(myCalculateGrades.numRecords)

print('Number of data elements read from file in Dan Bader\'s Real Python Source Code:')
print(calculatingGrades.numDataEl)
print('Number of students used loaded in for Dan Bader\'s Real Python Source Code:')
print(calculatingGrades.numRecords)

print('Percent difference between my time and the source code\'s time:')
print(str(100*((myRuntime-sourceCodeRuntime)/myRuntime)) + '%')
print('Percent difference between number of data elements loaded in and analyzed by my program and the source code\'s number of elements loaded and analyzed:')
print(str(100 * ((myCalculateGrades.numel - calculatingGrades.numDataEl)/(myCalculateGrades.numel))) + '%')
print('Percent difference between total number of students\' / records  analyzed by my program and the source code\'s total number of student\'s records analyzed:')
print(str(100 * ((myCalculateGrades.numRecords - calculatingGrades.numRecords)/(myCalculateGrades.numRecords))) + '%')

