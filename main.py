print('WoW: 3.3.5')
login = input("Введите логин:" )
input('Введите пароль:' )
print("Приветсвуем Вас, ",login,end="!")
print('\nПерсонажей на сервере', 1+1, sep="|", )
print('1|Таурен : Таупалик', end="\n" '2|Розбийник :Питух')
Tauren = 1
Roz = 2

if b == 1 or b == 2:
    print("Вход")
else:
    print('Персонаж не найден')
if b == 1:
    print('\nТаупалик ', '\nЗдоровье|5000', '\nМана|3000')
if b == 2:
    print('\nРозбийник', '\nЗдоровьe| 228', '\nЯрость|100')


print('Открой рюкзак нажав b')
backpack = input()
c = backpack
if  c == backpack:
    print('В рюкзаке есть золотая монета')
else:
    print('Не та кнопка')