# Конвертер кода в PDF

Простое веб-приложение для конвертации файлов с кодом в PDF формат.

## Возможности

- Поддержка множества языков программирования (Python, JavaScript, TypeScript, Java, C/C++, C#, Go, Rust, Ruby, PHP, Bash, HTML, CSS, JSON, XML, Markdown, SQL)
- Drag-and-drop загрузка файлов
- Автоматическое определение кодировки файла
- Сохранение форматирования кода в PDF
- Работа локально без отправки данных в интернет

## Развертывание на Render.com

### Способ 1: Использование Docker (рекомендуется)

1. Запушьте этот репозиторий на GitHub
2. Зарегистрируйтесь на [Render.com](https://render.com)
3. Создайте новый сервис → "Web Service"
4. Подключите ваш GitHub репозиторий
5. Выберите опцию "Docker" в качестве среды выполнения
6. Render автоматически обнаружит Dockerfile и развернет приложение

### Способ 2: Использование Python среды

1. Запушьте этот репозиторий на GitHub
2. Зарегистрируйтесь на [Render.com](https://render.com)
3. Создайте новый сервис → "Web Service"
4. Подключите ваш GitHub репозиторий
5. Выберите среду выполнения "Python 3"
6. Build Command: `pip install -r requirements.txt`
7. Start Command: `python app.py`

## Локальный запуск

### С помощью Docker:

```bash
docker build -t code-to-pdf .
docker run -p 8080:8080 code-to-pdf
```

### Без Docker:

```bash
pip install -r requirements.txt
python app.py
```

Приложение будет доступно по адресу http://localhost:8080

## Использование

1. Перетащите файл с кодом в область загрузки или нажмите для выбора файла
2. Нажмите кнопку "Конвертировать в PDF"
3. Скачайте полученный PDF файл

## Структура проекта

- `app.py` - основной файл приложения Flask
- `templates/index.html` - HTML шаблон веб-интерфейса
- `requirements.txt` - зависимости Python
- `Dockerfile` - конфигурация Docker для развертывания
- `render.yaml` - конфигурация для Render.com (опционально)
- `.dockerignore` - файлы, исключаемые из Docker образа

## Поддерживаемые форматы

txt, py, js, ts, java, c, cpp, h, hpp, cs, go, rs, rb, php, sh, bash, html, css, json, xml, md, sql
