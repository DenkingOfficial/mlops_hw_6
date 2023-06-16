# MLOps Final task

Team #2

Цель проекта: разработать конвеер машинного обучения data-продукта (Web или API приложение).

Разработана модель для определения эмоциональной окраски текста (позитивный/негативный). Также разработаны:
1. Простой веб-интерфейс

![WebUI](https://raw.github.com/DenkingOfficial/mlops_hw_6/main/static/webui-screenshot.jpg)

2. Тесты на качество данных, на качество работы модели на тестовых данных и на работоспособность модели в веб-приложении.
3. Пайплайн в Jenkins (Jenkinsfile)

![pipeline](https://raw.github.com/DenkingOfficial/mlops_hw_6/main/static/pipeline-screenshot.jpg)

4. Версионирование данных с помощью DVC
5. Сборка Docker образа в пайплайне
6. Загрузка Docker образа на Dockerhub в пайплайне

![pipeline](https://raw.github.com/DenkingOfficial/mlops_hw_6/main/static/Dockerhub-screenshot.jpg)

Использованы наборы данных:
* [Russian-language reviews](https://www.kaggle.com/datasets/laytsw/reviews)
* [Тональность отзывов об обслуживании](https://www.kaggle.com/competitions/tonality-reviews/data)

Студенты:
* Шершнев Андрей (РИМ-120907)
* Кожин Артём (РИМ-120906)
* Иванов Сергей (РИМ-120906)
* Чупахин Юрий (РИМ-120908)
