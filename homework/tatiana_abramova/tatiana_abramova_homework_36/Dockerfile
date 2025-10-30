FROM jenkins/jenkins:lts-jdk17

USER root

# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y \
    wget \
    build-essential \
    zlib1g-dev \
    libncurses5-dev \
    libgdbm-dev \
    libnss3-dev \
    libssl-dev \
    libreadline-dev \
    libffi-dev \
    libsqlite3-dev \
    libbz2-dev \
    curl \
    xvfb \
    fonts-liberation \
    libxss1 \
    libasound2 \
    libatk1.0-0 \
    libcups2 \
    libx11-xcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libgbm1 \
    libgtk-3-0 \
    gnupg2 \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем Python 3.11
WORKDIR /tmp
RUN wget https://www.python.org/ftp/python/3.11.9/Python-3.11.9.tgz && \
    tar -xf Python-3.11.9.tgz && \
    cd Python-3.11.9 && \
    ./configure --enable-optimizations && \
    make -j$(nproc) && \
    make install && \
    rm -rf /tmp/Python-3.11.9* && \
    ln -sf /usr/local/bin/python3.11 /usr/local/bin/python3 && \
    ln -sf /usr/local/bin/pip3.11 /usr/local/bin/pip3

# Устанавливаем Google Chrome
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /usr/share/keyrings/google.gpg && \
    echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google.gpg] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && apt-get install -y google-chrome-stable && \
    rm -rf /var/lib/apt/lists/*

# Устанавливаем ChromeDriver
RUN CHROME_VERSION=$(google-chrome --version | grep -oE '[0-9]+' | head -1) && \
    DRIVER_VERSION=$(wget -q -O - "https://googlechromelabs.github.io/chrome-for-testing/LATEST_RELEASE_${CHROME_VERSION}") && \
    wget -q -O /tmp/chromedriver.zip "https://storage.googleapis.com/chrome-for-testing-public/${DRIVER_VERSION}/linux64/chromedriver-linux64.zip" && \
    unzip /tmp/chromedriver.zip -d /tmp/ && \
    mv /tmp/chromedriver-linux64/chromedriver /usr/local/bin/chromedriver && \
    chmod +x /usr/local/bin/chromedriver && \
    rm -rf /tmp/chromedriver*

# Проверяем версии Chrome и ChromeDriver
RUN echo "Chrome version:" && google-chrome --version && \
    echo "ChromeDriver version:" && chromedriver --version

# Обновляем pip
RUN pip3 install --upgrade pip

# Устанавливаем Playwright и браузеры (ключевой шаг)
RUN pip3 install playwright pytest-playwright && \
    playwright install --with-deps

# Возвращаем пользователя Jenkins
USER jenkins
