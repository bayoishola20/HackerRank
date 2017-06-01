#==================== GIVEN ======================#
class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print "Name:", self.lastName + ",", self.firstName
		print "ID:", self.idNumber
#===================== END =========================#

class Student(Person):

    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, testScores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.testScores = testScores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        sum = 0
        
        for score in self.testScores:
            sum += score
        n = len(self.testScores)     
        a = sum/n
        if 90 <= a <= 100:
            return "O"
        elif 80 <= a <= 90:
            return "E"
        elif 70 <= a <= 80:
            return "A"
        elif 55 <= a <= 70:
            return "P"
        elif 40 <= a <= 55:
            return "D"
        else:
            return "T"

#==================== GIVEN ======================#
line = raw_input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(raw_input()) # not needed for Python
scores = map(int, raw_input().split())
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print "Grade:", s.calculate()
#===================== END =========================#