# Тестовое задание

##  Долевое строительство

### Решение в файле shared_construction_task.py

#### Алгоритм 
1. запись списка долей shares и дополнительной переменной amount
2. проход по списку и выдача части доли от суммы amount (share / amount)

Сложность линейная O(n), память необходима для списка + интовой переменной т.е. O(n) + 1, где n - количество долей.

T = C1*n+C2, где T - время, C1 - стоимость линейной части на 1 элемент, C2 - стоимость константной части на 1 элемент.
n = (T-C2)/C1, подставив константы можно вычислить кол-во элементов для условной 5ти секунд.

Сложность задачи 2-3/10, потраченно времени 10-15 минут.

##  Мегатрейдер

### Решение в файле trader_task.py

#### Алгоритм 
1. Запись переменных количества дней N, лотов в течении дня M, доступные средства S.
2. Сохраняем лоты в список, при этом максимальное количество возможных лотов N*M. 
Лоты сохраняем в структуре данных dict с ключами: 
data - вводные данные по лоту, нужны для возвращения результата 
lot_cost - общая стоимость лота, количество облигаций * цену облигации
income_summary - общая прибыль лота, купонный доход(количество дней * доход за день) - переплата за покупку((фактическая цена облигации - номинальная)*количество облигаций)
number - порядок записи лота, нужен для возвращения результата в верном порядке
3. Получаем почти классическую "задачу о рюкзаке". Есть несколько способов решения такого типа задач, я выбрал динамическое программирование.
4. Задаем возможные действия алгоритма, не берем облигацию или берем, берем максимальное из этих значений.
5. Формируем вывод.

Сложность O(n*m), где n - количество лотов, m - ограничение по цене(максимум лотов можем купить одновременно). Изза того что я использую таблицу мемоизации, для хранения результатов, 
алгоритм требует много памяти O(n*m). 

T=C1*n*m + C2 * n + C3, отсюда можно вычислить n.

Сложность задачи 8/10, потраченно времени 1час 30минут +- 15 минут.

Не нашел способа досрочно завершить ввод элементов, поэтому отправка ввод "" завершает ввод данных и запускает алгоритм.