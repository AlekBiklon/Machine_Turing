# Готова реалізація Машини Тьюринга, яка робить додавання.
# Також тут представлений зразок циклу з постумовою ОРИГІНАЛ
tape1=['|','|','|','*','|','|']
print(tape1)

while '*' in tape1:
    tape1.append('') # цей вираз задовольняє умову нескінченності стрічки
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