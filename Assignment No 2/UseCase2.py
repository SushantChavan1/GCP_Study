#In this usecase I going to extract the Test data from Excel file 
#and I going to perform the following operations 
#1. Read the data from the Excel file
#2. Display the data in the console
#3. Extracting the average marks for test
#4. Extracting the criteria or cut off analyasis
#5. Extracting the student who scored more than 50 marks
#6. Extracting the students who scored less than 30 marks 
#7. predicting those students who scored more than 50 they will get pass the aptitude test of Smart Hiring


import pandas as pd

#Reading the data from the Excel file
def read_data():
    data = pd.read_csv('C:\\Users\\Admin\\Desktop\\Python\\GCP_Study\\Assignment No 2\\ECS.csv')
    return data

def transform_data(data):
    #extracting the average marks
    data['MARKS'].fillna(0 ,inplace = True)
    avg_marks = data['MARKS'].mean()
    #Now I am going to extract the number of students who scored more than 50 marks
    count_50 = 0
    count_30 = 0
    absent_students = 0
    for i in range(len(data)):
        if (data["MARKS"][i] > 50):
            count_50 = count_50 + 1
        elif (data["MARKS"][i] > 30):
            count_30 = count_30 + 1
        elif (data["MARKS"][i] <= 0):
            absent_students = absent_students + 1
    print("length od data" , len(data))
    present_students = len(data) - absent_students
    all_results = (avg_marks , count_50 , count_30 , present_students , absent_students)
    return all_results    

data = read_data()
print(data)
result = transform_data(data)
print("The final reports are")
print("Average marks of the students are" , result[0])
print("Number of students who scored more than 50 marks are" , result[1])
print("Number of students who scored more than 30 marks and having chances to place are" , result[2])
print("Number of students who are present for test" , result[3])
print("Number of students who are absent for test" , result[4])