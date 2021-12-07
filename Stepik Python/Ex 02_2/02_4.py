a, b = int(input()), int(input())
print(f'{a} + {b} = {a+b}', f'{a} - {b} = {a-b}',
      f'{a} * {b} = {a*b}', sep='\n')

целое, ввод, вывод = int, input, print
а = целое(ввод())
вывод(а, а * 2, а * 3, а * 4, а * 5, sep='---')

(lambda x: print('---'.join(str((i+1)*x) for i in range(5))))(int(input()))