import pandas as pd

# Чтение данных из файла
df = pd.read_excel('second.xlsx')

# Анализ данных

# Поиск дня, в котором количество переключений между операторами увеличилось
increased_switching_day = df[df['first_skill'] != df['last_skill']]['date'].value_counts().idxmax()
switching_count = df[df['date'] == increased_switching_day]['first_skill'].ne(df['last_skill']).sum()
print("День, в котором количество переключений увеличилось:", increased_switching_day)
print("Общее количество переключений в этот день:", switching_count)

# Вычисление наиболее часто встречающегося скилла, на который переводит интент
most_common_skill = df['first_skill'].value_counts().idxmax()
print("Наиболее часто встречающийся скилл:", most_common_skill)

# Вывод рекомендации по смене скилла, на который переводит интент
if most_common_skill != 'deposit':
    print("Рекомендуется сменить скилл, на который переводит интент, на", most_common_skill)
else:
    print("Смена скилла, на который переводит интент, не требуется.")