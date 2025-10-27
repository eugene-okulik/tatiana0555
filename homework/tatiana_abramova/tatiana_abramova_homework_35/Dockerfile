FROM jenkins/jenkins:lts-jdk21
USER root

RUN apt-get update && apt-get install -y python3 python3-pip wget gnupg2

# Добавление ключа GPG и репозитория Google Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /usr/share/keyrings/google.gpg 

RUN echo "deb [signed-by=/usr/share/keyrings/google.gpg] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list

RUN apt-get update && apt-get install -y google-chrome-stable

USER jenkins
