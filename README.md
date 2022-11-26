# FiniteAutomaton
Statement: Write a program that reads the elements of a finite automaton from a file and:

Display set of states, alphabet, transitions, set of final states

Documentation should also include in BNF or EBNF format the form in which the FA.in file should be written

textfile := transition{transition}

transition := "(" ["{"] state ["}"] "," subalpha ")" "->" ( "(" state ")" ) | ( "[" state "]" )

state := symbol | symbol state

symbol := "a" | ... | "z" | "A" | ... | "Z" | "0" | ... | "9" 

subalpha := symbol | symbol "-" symbol | symbol subalpha | symbol "-" symbol subalpha

(with the condition that in the case of symbol "-" symbol, the initial symbol is smaller lexicographically than the second symbol )
