import threading

def collatz(n):
    while n > 1:
        print(n, end=' ')
        if (n % 2):
            n = 3 * n + 1
        else:
            n = n // 2
    print(1, end='')

n = int(input('Enter n: '))
i=1

while i <= n :
    print('\nSequence: ', end=' ')
    t2 = threading.Thread(target=collatz(i))
    t2.start()
    i = i + 1
