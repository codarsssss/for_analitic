import pandas as pd
import re

# Чтение данных из файла
df = pd.read_excel('third.xlsx')

# Фильтрация данных только для продукта "Страховая"
insurance_df = df[df['product'] == 'Страховая']

# Определение нужных слов на основе частоты использования
filtered_words = insurance_df[insurance_df['frequency'] > insurance_df['frequency_ngram'] / 2]['ngram'].tolist()

# Создание регулярного выражения для поиска сообщения с нужными словами
regex = r"\b(?:{})\b".format("|".join(filtered_words))

# Применение регулярного выражения к каждому сообщению
matching_messages = insurance_df[insurance_df['ngram'].str.contains(regex, case=False)]['ngram'].tolist()

# Вывод найденных сообщений
print("Найденные сообщения:")
for message in matching_messages:
    print(message)