import pandas as pd

# Создаем DataFrame
data = {
    'Имя': ['Алексей Иванов', 'Мария Петрова', 'Иван Сидоров', 'София Орлова', 'Петр Кузнецов',
            'Дарья Смирнова', 'Андрей Фролов', 'Ольга Захарова', 'Николай Матвеев', 'Екатерина Соболева'],
    'Математика': [78, 85, 90, 92, 74, 88, 80, 85, 70, 95],
    'Русский язык': [85, 88, 92, 90, 87, 89, 91, 86, 88, 93],
    'Физика': [82, 78, 85, 90, 80, 87, 84, 88, 85, 86],
    'История': [89, 85, 90, 87, 88, 90, 85, 87, 86, 92],
    'Информатика': [91, 88, 85, 90, 89, 92, 87, 85, 88, 93]
}

df = pd.DataFrame(data)

# Выводим первые несколько строк
print("Первые несколько строк DataFrame:")
print(df.head())

# Вычисляем среднюю оценку по каждому предмету
mean_scores = df[['Математика', 'Русский язык', 'Физика', 'История', 'Информатика']].mean()
print("\nСредние оценки по каждому предмету:")
print(mean_scores)

# Вычисляем медианную оценку по каждому предмету
median_scores = df[['Математика', 'Русский язык', 'Физика', 'История', 'Информатика']].median()
print("\nМедианные оценки по каждому предмету:")
print(median_scores)

# Вычисляем Q1 и Q3 для оценок по математике
Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
IQR_math = Q3_math - Q1_math
print(f"\nQ1 (25%) по математике: {Q1_math}")
print(f"Q3 (75%) по математике: {Q3_math}")
print(f"Межквартильный размах (IQR) по математике: {IQR_math}")

# Вычисляем стандартное отклонение по каждому предмету
std_scores = df[['Математика', 'Русский язык', 'Физика', 'История', 'Информатика']].std()
print("\nСтандартное отклонение по каждому предмету:")
print(std_scores)

