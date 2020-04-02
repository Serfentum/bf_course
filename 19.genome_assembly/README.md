# Genome Assembly
Модуль о сборке генома


# Источники информации
* [введение в сборку от Певзнера](http://users.dimi.uniud.it/~alberto.policriti/home/sites/default/files/bioinformatica-specialistica/PS_chapter-3.pdf)
* [видюшка об overlap layout consensus](https://www.youtube.com/watch?v=hB2i_Uwm-HQ)
* [годная лекция об OLC и DBG сборках от MIT (у них вообще много годного)](https://www.youtube.com/watch?v=ZYW2AeDE6wU)
* [канал этого чувака на ютубе (там много о чём)](https://www.youtube.com/user/RobEdwardsSDSU/videos)
* [вероятно это возникновение OLC подхода](https://www.ncbi.nlm.nih.gov/pubmed/?term=Myers+EW.+Toward+simplifying+and+accurately+formulating+fragment)
* [алгоритм OLC](http://www.cs.jhu.edu/~langmea/resources/lecture_notes/assembly_olc.pdf)
* [статья о сборке с графами де Брюйна](https://www.ncbi.nlm.nih.gov/pubmed/22068540)
* [о том, почему используют нечётные k](https://bioinformatics.stackexchange.com/questions/156/why-do-some-assemblers-require-an-odd-length-kmer-for-the-construction-of-de-bru)
* [сборка с помощью суперридов](https://academic.oup.com/bioinformatics/article/29/21/2669/195975)
* [сборка с помощью TF-IDF](https://genome.cshlp.org/content/27/5/722.full.pdf+html)
* [исправление ошибок в ридах](https://www.ncbi.nlm.nih.gov/pubmed/?term=Comparative+assessment+of+long-read+error+correction+software+applied+to+Nanopore+RNA-sequencing+data)
* [полировка генома на примере pilon](https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0112963&type=printable)
* [де Брюйновская классика))](http://cab.spbu.ru/software/spades/)
* [тул для оценки качества сборки от тех же ребят](http://cab.spbu.ru/software/quast/)


# Задания
Для каждого из пунктов к коду нужны результаты работы программы - контиги в виде фасты или графики
* Напишите наивный сборщик (25 баллов)
* Напишите сборщик, использующий граф де Брюйна (35 баллов)
* Сравните сборки своими разными сборщиками (15 баллов)
* Сделайте визуализацию сборки - например, через graphviz (10 баллов)
* *Напишите сборщик на суперридах (25 баллов)
