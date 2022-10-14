def medium_display(plateau):
    i = 0
    p = plateau['tiles']
    temp = ''
    while i < plateau['n']:
        temp = ''
        j = 0
        print("*************************")
        while j < plateau['n']:
            if p[i * 4 + j] > 9 and p[i * 4 + j] < 100:
                temp += '* ' + str(p[i * 4 + j]) + '  '
            elif p[i * 4 + j] > 100:
                temp += '* ' + str(p[i * 4 + j]) + ' '
            else:
                temp += '*  ' + str(p[i * 4 + j]) + '  '
            j += 1
        temp += '*'
        print(temp)
        i += 1
    print("*************************")