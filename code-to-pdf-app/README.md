# Конвертер кода в PDF для Vercel

Веб-приложение для конвертации файлов с кодом в PDF формат, оптимизированное для развертывания на платформе Vercel.

## Возможности

- 📁 Загрузка файлов с кодом через drag-and-drop или клик
- 📄 Генерация PDF с сохранением форматирования кода
- 🔍 Поддержка более 25 форматов файлов (py, js, ts, html, css, json и др.)
- 🎨 Современный веб-интерфейс
- ⚡ Работает на serverless-функциях Vercel
- 🌐 Доступно по HTTPS из любой точки мира

## Поддерживаемые форматы

Python, JavaScript, TypeScript, JSX, TSX, HTML, CSS, JSON, XML, YAML, Markdown, TXT, Shell scripts, Ruby, PHP, Go, Rust, Swift, Kotlin, Java, C, C++, C#, SQL, R, Lua, Perl и другие.

## Развертывание на Vercel

### Способ 1: Через Vercel CLI (рекомендуется)

1. Установите Vercel CLI:
```bash
npm install -g vercel
```

2. Войдите в аккаунт Vercel:
```bash
vercel login
```

3. В директории проекта выполните:
```bash
vercel
```

4. Следуйте инструкциям в терминале.

### Способ 2: Через GitHub

1. Запушьте код в репозиторий GitHub
2. Зайдите на [vercel.com](https://vercel.com)
3. Нажмите "New Project"
4. Импортируйте ваш репозиторий
5. Vercel автоматически определит настройки и развернет приложение

## Структура проекта

```
code-to-pdf-app/
├── api/
│   └── app.py          # Serverless функция Flask
├── public/
│   └── index.html      # Веб-интерфейс
├── vercel.json         # Конфигурация Vercel
└── requirements.txt    # Python зависимости
```

## Локальная разработка

Для тестирования локально используйте Vercel CLI:

```bash
vercel dev
```

Приложение будет доступно по адресу http://localhost:3000

## Как это работает

1. Пользователь загружает файл с кодом через веб-интерфейс
2. Файл отправляется на serverless функцию `/api/convert`
3. Функция читает содержимое файла и генерирует PDF с помощью библиотеки ReportLab
4. PDF возвращается пользователю для скачивания

## Ограничения Vercel

- Максимальный размер файла: 4.5 MB (для Hobby плана)
- Таймаут функции: 10 секунд (Hobby), 60 секунд (Pro)
- Для больших файлов рекомендуется использовать Pro план

## Технологии

- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Backend**: Python, Flask (адаптированный для Vercel)
- **PDF генерация**: ReportLab
- **Хостинг**: Vercel Serverless Functions

## Лицензия

MIT
