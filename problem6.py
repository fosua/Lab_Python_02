primarySchoolAge= 6
theVotingAge = 18
thePresidentAge = 40
theRetirementAge = 60
personAge = input ("Enter an age: ")
personAge = int(personAge)
if personAge < primarySchoolAge:
    print 'Too young'
elif personAge >= theVotingAge:
    print 'Remember to vote'
elif personAge >= thePresidentAge:
    print 'Vote for me'
elif personAge < thePresidentAge:
    print 'You cant be president'
elif personAge >= theRetirementAge:
    print 'too old'
else:
    print 'well i have nothing to say about your age'
 #question 7  
i = 40
while i >=0:
	x = i*3
	if x<40:
		print x,
	i = i-1
	#question 8
for i in range (6, 30):
    if i % 2 != 0:
        if i&3 != 0:
            if i % 5 !=0:
                print i,
	


	# question 9
	
n=0
while ((79*n) % 97) != 1:
	n = n+1
print n

