# numpy & pandas
Модуль по нампаю и пандасу


# Источники информации
* [документация numpy](https://numpy.org/doc/)
* [документация pandas](https://pandas.pydata.org/docs/)
* [kaggle](https://www.kaggle.com/) - площадка датасаентистов, где проводятся
соревнования и можно многому научиться из кёрнелов участников
* [курс по мл](https://github.com/adasegroup) - курс от Бурнаева и
его коллег по машинному обучению в питоне с sklearn (половина математики сложновата имхо)
* [об индексах датафрэймов](https://towardsdatascience.com/pandas-index-explained-b131beaf6f7b)
* [визуализация reshape, ravel и stack'ов](https://towardsdatascience.com/reshaping-numpy-arrays-in-python-a-step-by-step-pictorial-tutorial-aed5f471cf0b)
* [работа с файлами больше чем оперативная память](https://stackoverflow.com/questions/25962114/how-to-read-a-6-gb-csv-file-with-pandas)
* [иерархия типов numpy](https://docs.scipy.org/doc/numpy/reference/arrays.scalars.html)
* [группировка](https://jakevdp.github.io/PythonDataScienceHandbook/03.08-aggregation-and-grouping.html) (там не сразу начинается)
* [типы join'ов](https://datacarpentry.org/python-ecology-lesson/05-merging-data/index.html)
* [pivot](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.pivot_table.html) и [melt](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.melt.html) - мы их не проходили, но при трансформации данных, они могут быть очень полезны
* [визуализация корреляций](https://seaborn.pydata.org/generated/seaborn.pairplot.html)
* [либа для EDA в пандасе](https://github.com/pandas-profiling/pandas-profiling)
* [try vs if](https://stackoverflow.com/questions/1835756/using-try-vs-if-in-python)


# Задания
* Зарегистрируйтесь на кэггле
* В файлике train.csv содержится информация о числе ридов с каждым из 4-ёх нуклеотидов
по разным позициям (колонки A, T, G, C)). Постройте гистограмму распределения этих чисел (7 баллов)
* Сохраните в файл train_part.csv следующую часть из файла train.csv:
    * строки, где matches больше чем среднее
    * колонки pos, reads_all, mismatches, deletions, insertions

(5 баллов)
* Проведите [Explorative Data Analysis](https://en.wikipedia.org/wiki/Exploratory_data_analysis) знаменитого датасэта [титаника](https://www.kaggle.com/c/titanic/overview) (или какого-нибудь другого, если вам скушно с Титаником). Нужны корреляции, графики распределений (25 баллов)
