# Enter your code here. Read input from STDIN. Print output to STDOUT
actually = str(raw_input()).split(" ")
Da = int(actually[0])
Ma = int(actually[1])
Ya = int(actually[2])

expected = str(raw_input()).split(" ")
De = int(expected[0])
Me = int(expected[1])
Ye = int(expected[2])

fine = 0
if Ya == Ye:
    if Da > De and Ma == Me:
        fine = 15 * (Da - De)
    
    elif Ma > Me:
        fine = 500 * (Ma - Me)
    
elif Ya > Ye:
    fine = 10000

print fine