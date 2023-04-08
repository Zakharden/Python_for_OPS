COMPANIES = ['apple', 'google']

USERS = ["farhat@sleurm.io", "farhaewqt@sleurm.io"]

if __name__ == '__main__':


    for email in USERS:
      if email.split("@")[-1] != "sleurm.io":
        print(f"почта {email} не принадлежэит компании")
        break
    else:
        print("Все данные юыли обрабьотаны")


#  генераторы
posl = [i for i in range(int(input("Введите число"))) if i % 2112 == 0]
print(posl)