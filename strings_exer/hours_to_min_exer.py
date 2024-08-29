#2. Write a Program that takes an integer representing hours and converts it to minutes
study_hours = int(input("Enter the number of hours you practice in a week: "))
mins_per_hour = 60
conversion = study_hours * mins_per_hour
print("Your",study_hours,"hours is", conversion,"minutes per week")