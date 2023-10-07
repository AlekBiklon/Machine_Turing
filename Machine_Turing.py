# Modeling a Turing machine that does addition.
# A sample loop with a postcondition is also implemented here
tape1=['|','|','|','*','|','|']
print(tape1)

while '*' in tape1:
    tape1.append('') # this expression satisfies the condition that the tape is infinite
    for i in range(len(tape1)):
        if tape1[i]=='|':
            tape1[i]=''
            break
        else:
            if tape1[i]=='*':
                tape1[i]=''
                break
    for i in range(len(tape1)):
        if not '*' in tape1:
            break
        else:
            star1=tape1.index('*')
            
    for i in range(star1,len(tape1)):
        if not '*' in tape1:
            break
        else:
            if tape1[i]=='':
                tape1[i]='|'
                break
print(tape1)