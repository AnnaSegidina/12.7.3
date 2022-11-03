per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = 100000
deposit = [int(per_cent.get("ТКБ")*money/100),
           int(per_cent.get("СКБ")*money/100),
           int(per_cent.get("ВТБ")*money/100),
           int(per_cent.get("СБЕР")*money/100)]
print(deposit)
max_element = max(deposit)
print("Max deposit: ", max_element)
