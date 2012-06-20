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
    print 'well i have nothing to say about your age
