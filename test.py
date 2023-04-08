import random

b = ((random.random() + 0.01) * 100) // 1 + 12
end = int(b) + 1
for i in range(1, end):
    if i % 2 == 0:
        print("🙂" * i)
    elif (i * 3) % 4 == 3:
        print("😎" * i)
    else:
        print("🤡" * i)
