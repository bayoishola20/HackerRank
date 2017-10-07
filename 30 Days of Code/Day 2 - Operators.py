# Enter your code here. Read input from STDIN. Print output to STDOUT
mealCost = float(raw_input())
tipPercent = float(raw_input())
taxPercent = float(raw_input())
totalCost = int(round(mealCost + tipPercent*(mealCost/100) + taxPercent*(mealCost/100)))
print "The total meal cost is %s dollars." %totalCost