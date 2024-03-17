# Використовуємо офіційний образ Python в якості базового образу
FROM python:3.12

# Встановлюємо залежності за допомогою pip
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Копіюємо файли проекту в образ Docker
COPY . /app

# Встановлюємо робочу директорію
WORKDIR /app

# Запускаємо команду для створення міграцій та запуску сервера Django
CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
