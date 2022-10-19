import random
def igra(a):
    kam=0
    if a==0:
        kam = int(input("Введите сколько камней взять (1, 2 или 3): "))
        return kam
    if a==1:
        kam = random.randint(1,3)
        print(f"Камней, взятых компьютером: {kam}")
        return kam

n = random.randint(4,30)
print(f"Игра начинается с кучки в {n} камней")
kto = random.randint(0,1)
if kto==0:
    print("Первым ходит игрок")
if kto==1:
    print("Первым ходит компьютер")
while 1:
    n=n-igra(kto)
    print(f"Оставшихся камней в кучке: {n}")
    if n<=0:
        print(f"Победил {kto}")
        exit()
    if kto==0:
        kto=1
    else:
        kto=0