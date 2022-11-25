alphabet = []
states = []
initial_state = []
final_states = []
transitions = []
banned = [" ", ")"]

f = open("automation.txt", "r")
text = f.read().split("\n")

for l in text:
	line = l.split("->")
	pair = line[0].split(",")
	# Working on adding the states/determining initial state
	if pair[0][1] != "{":
	  first = pair[0][1:]
	  if first not in states:
	    states.append(first)
	else:
	  first = pair[0][2:-1]
	  states.append(first)
	  initial_state = first
	
	  # Working on completing the alphabet 
	i = 0
	okay = 0
	for i in pair[1]:
		if okay == 0:
		   if i == "-":
		    okay = 1
		   else:
		    if i not in alphabet and i not in banned:
		     alphabet.append(i)
		    prev = i
		else:
			okay = 0
			k = chr(ord(prev) + 1)
			while k <= i:
				  if k not in alphabet and k not in banned:
				   alphabet.append(k)
				  k = chr(ord(k)+1)

    # Working on determining and adding destination state
	a = str(line[1])[1:]
	second = str(a)[1:-1]
	if second not in states:
			states.append(second)
	if str(a)[0] == "[":
		if second not in final_states:
			final_states.append(second)
	# Constructing transitions
	transitions.append((first,second))



print("the alphabet: " + str(alphabet))
print("the states: " + str(states))
print("the initial state: " + str(initial_state))
print("the final states: " + str(final_states))
print("the transitions: " + str(transitions))
			
