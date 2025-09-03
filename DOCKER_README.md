# Docker для TellMeApp

Этот проект настроен для запуска в Docker контейнере.

## Быстрый старт

### 1. Сборка образа
```bash
docker build -t tellmeapp .
```

### 2. Запуск контейнера

#### Для Windows:
```bash
docker run -it --rm tellmeapp
```

#### Для Linux/macOS (с GUI):
```bash
# Разрешить X11 forwarding
xhost +local:docker

# Запустить контейнер
docker run -it --rm \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
  tellmeapp
```

### 3. Использование Docker Compose

#### Сборка и запуск:
```bash
docker-compose up --build
```

#### Остановка:
```bash
docker-compose down
```

## Структура файлов

- `Dockerfile` - конфигурация Docker образа
- `docker-compose.yml` - конфигурация для Docker Compose
- `requirements.txt` - Python зависимости
- `.dockerignore` - файлы, исключаемые из контекста сборки

## Особенности

- Приложение использует Kivy для GUI
- Настроены все необходимые системные зависимости
- Поддержка отображения GUI через X11 (Linux/macOS)
- Автоматическая установка Python зависимостей

## Устранение проблем

### Проблемы с GUI на Linux:
```bash
# Убедитесь, что X11 forwarding включен
xhost +local:docker
```

### Проблемы с правами доступа:
```bash
# Запустите Docker с правами администратора
sudo docker run -it --rm tellmeapp
```

## Разработка

Для разработки рекомендуется монтировать исходный код:
```bash
docker run -it --rm -v $(pwd):/app tellmeapp
```
