class Exam:
    def __init__(self,student,number):
        physics = number
        self.min_number = 50
        self.max_number = 100
    def grade(self,number):
        if number > 50 and number <61 :
            print('A-')
        elif number >60 and number <71:
            print('A')
        elif(number<50):
            print('F')
        else:
            print('A+')
    
moinul = Exam('Moinu',100)
print(moinul.grade(20))

