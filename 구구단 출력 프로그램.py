print('''=============================
== 구구단 출력 프로그램 ==
== 20234348 최원준 ==
''')


while True:
    num = int(input('몇 단을 출력할까요? '))
    for i in range(1, 10):
            print(num, '*', i, '=', num * i)

    command = input('계속 하시려면 y를, 그만하시려면 n을 눌러주세요. ')

    if command == 'y':
        continue
       
        

    elif command == 'n':
        break
