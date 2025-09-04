# Dockerfile для Kivy приложения с полными зависимостями
FROM python:3.10-slim-bullseye

# Установка системных зависимостей для Kivy
RUN apt-get update && \
    apt-get install -y \
    build-essential \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libxext6 \
    libxrender-dev \
    libgomp1 \
    libglib2.0-0 \
    libx11-6 \
    libx11-xcb1 \
    libxcb1 \
    libxcb-glx0 \
    libxcb-keysyms1 \
    libxcb-image0 \
    libxcb-shm0 \
    libxcb-icccm4 \
    libxcb-sync1 \
    libxcb-xfixes0 \
    libxcb-shape0 \
    libxcb-randr0 \
    libxcb-render-util0 \
    libxcb-render0 \
    libxcb-xinerama0 \
    libxcb-xkb1 \
    libxkbcommon-x11-0 \
    libxss1 \
    libgconf-2-4 \
    libxtst6 \
    libxrandr2 \
    libasound2 \
    libpangocairo-1.0-0 \
    libatk1.0-0 \
    libcairo-gobject2 \
    libgtk-3-0 \
    libgdk-pixbuf2.0-0 \
    libxcomposite1 \
    libxcursor1 \
    libxdamage1 \
    libxi6 \
    libxtst6 \
    libnss3 \
    libcups2 \
    libxss1 \
    libgconf-2-4 \
    libxrandr2 \
    libasound2 \
    libpangocairo-1.0-0 \
    libatk1.0-0 \
    libcairo-gobject2 \
    libgtk-3-0 \
    libgdk-pixbuf2.0-0 \
    libxcomposite1 \
    libxcursor1 \
    libxdamage1 \
    libxi6 \
    libxtst6 \
    libnss3 \
    libcups2 \
    xvfb \
    pv \
    sudo \
    git \
    libmtdev1 \
    libmtdev-dev \
    libx11-dev \
    libxext-dev \
    libxrender-dev \
    libxrandr-dev \
    libxinerama-dev \
    libxcursor-dev \
    libxi-dev \
    libxtst-dev \
    libxss-dev \
    libgl1-mesa-dev \
    libglu1-mesa-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Обновление pip
RUN pip install --upgrade pip

# Копирование файлов приложения
COPY . .

# Установка Python зависимостей
RUN pip install --no-cache-dir -r requirements.txt

# Сделать скрипт запуска исполняемым
RUN chmod +x start.sh

# Настройка виртуального дисплея для headless режима
ENV DISPLAY=:99
ENV SDL_VIDEODRIVER=x11
ENV MESA_GL_VERSION_OVERRIDE=3.3

# Команда для запуска приложения с виртуальным дисплеем
CMD ["./start.sh"]
