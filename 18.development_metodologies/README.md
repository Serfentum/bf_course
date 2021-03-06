# Development Methodology
Модуль о методологиях разработки


# Источники информации
* [о методологиях на хабре](https://habr.com/ru/company/edison/blog/269789/)
* [плюсы и минусы agile'а](https://geekbrains.ru/posts/methodologies_agile)
* [книжка по scrum'у](https://www.amazon.com/Scrum-Doing-Twice-Work-Half/dp/038534645X)
* [сайт для создания интерактивных досок - многим нравится)](https://trello.com)


# Задания
* Создайте репозиторий с программой для кластеризации музыки
    * инпут - программа принимает папку с песнями
    * оутпут - график кластеризации песен

[Ссылка на датасэт](https://drive.google.com/open?id=14dll-G-gh1HdM_rSIqods-fm8KuZ0ksG)

Вдобавок к этому у нас появилась [таблица с жанрами песен](https://docs.google.com/spreadsheets/d/1VUweSEue3Rp-HOQrK_9uaLyYJpvXQlQnBoaerMaNiF0/edit#gid=0) -
нужно её заполнить для своих трэков
* coarse genre - грубый жанр - классика, метал, попса, рэп, другое (если это не музыка)
* fine genre - уточнённый жанр - дэт метал, глэм рок, аудиокнига, подкаст
* genre\d - в последующих колонках указывается перечень жанров, под которые попадает данный трэк (смешение жанров)
Если не знаете, что писать в fine genre и genre1 - скопируйте туда инфу из coarse genre

Жанры позволят нам сравнить разные кластеризации - скооперируйтесь и решите, какой метрикой будете сравнивать свои методы

В презентации должны быть описаны использованные методы и ссылки на материалы в конце.
Также нужно обсудить вместе по какой метрике будем оценивать алгоритмы
Если сделаете больше, это только в плюс)

Направления для улучшения
* разные алгоритмы экстракции фичей, кластеризации и снижения размерности
* различное число выделенных кластеров

Каждый участник должен разбираться во всех аспектах программы. В этом случае
будет получен максимум баллов, иначе - пропорциональная знаниям часть (40 баллов)