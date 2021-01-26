birth_year=int(input("What year were your born? "))
month=int(input("What month were your born in terms of sequence? "))
age=int(input("How old are you? "))

if month==1:
    current_year= birth_year+ age #this has to be indented
    print("it is:", current_year) #this has to be indented 
else: 
    current_year2=(birth_year+age)+1
    print("it is:", current_year2)
