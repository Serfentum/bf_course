# IO, modules, graphs
Модуль об инпуте-оутпуте, импорте модулей и графах


# Источники информации
* [официальная документация по IO](https://docs.python.org/3/library/io.html)
* [работа с файлами](https://www.guru99.com/reading-and-writing-files-in-python.html)
* [кратко о контекстных мэнеджерах](https://www.geeksforgeeks.org/context-manager-in-python/)
* [более подробно о контекстных мэнеджерах](https://jeffknupp.com/blog/2016/03/07/python-with-context-managers/)
* [ещё о контекстных мэнеджерах](https://stackabuse.com/python-context-managers/)
* [туториал по импортам](https://pythonworld.ru/osnovy/rabota-s-modulyami-sozdanie-podklyuchenie-instrukciyami-import-i-from.html)
* [ещё об импортах](https://realpython.com/absolute-vs-relative-python-imports/)
* [представления графов и их особенности](https://www.geeksforgeeks.org/graph-and-its-representations/)
* [видео о формах представления графов](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=2&cad=rja&uact=8&ved=2ahUKEwjUiaCYlpfkAhUN3aQKHQqND5MQFjABegQICxAK&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DHDUzBEG1GlA&usg=AOvVaw32gSsnwMNZCH3ldyHSU6Z3)
* [разбор разных графовых задачек](https://www.python-course.eu/graphs_python.php)
* Либы для рисования графов
    * [graph-tool](https://graph-tool.skewed.de/)
    * [NetworkX](https://networkx.github.io/)
    * [graphviz](https://graphviz.readthedocs.io/en/stable/manual.html)


# Задания
* Создайте пару файлов (наполненных каким-то кодом), один из которых
импортируется в другом, удостоверьтесь, что при импорте выполняется
импортируемый файл
* Создайте функцию, которая получает на вход путь к файлу, который нужно считать,
путь к файлу, куда будет идти сохранение, и номера строк с которой и до какой
нужно переписать содержимое из одного файла в другой (то есть она выдирает
часть текста из одного файла в другой), если номера строк не были переданы -
копирует содержимое файла целиком
* Посмотрите на либы для рисования графов, выберите понравившуюся и
визуализируйте какой-нибудь граф
* Напишите функцию, вычисляющую число компонент связности в графе,
переданном в формате списка связности (для этого можно использовать dfs)
* Установите модуль [biopython](https://biopython.org/wiki/Download)
