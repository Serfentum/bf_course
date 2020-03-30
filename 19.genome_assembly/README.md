# Genome Assembly
Модуль о сборке генома


# Источники информации
* [введение в сборку от Певзнера](http://users.dimi.uniud.it/~alberto.policriti/home/sites/default/files/bioinformatica-specialistica/PS_chapter-3.pdf)
* [видюшка об overlap layout consensus](https://www.youtube.com/watch?v=hB2i_Uwm-HQ)
* [годная лекция об OLC и DBG сборках от MIT (у них вообще много годного)](https://www.youtube.com/watch?v=ZYW2AeDE6wU)
* [канал этого чувака на ютубе (там много о чём)](https://www.youtube.com/user/RobEdwardsSDSU/videos)
* [вероятно это возникновение OLC подхода](https://www.ncbi.nlm.nih.gov/pubmed/?term=Myers+EW.+Toward+simplifying+and+accurately+formulating+fragment)
* [алгоритм OLC](http://www.cs.jhu.edu/~langmea/resources/lecture_notes/assembly_olc.pdf)
* [сравнение OLC и DBG](https://watermark.silverchair.com/elr035.pdf?token=AQECAHi208BE49Ooan9kkhW_Ercy7Dm3ZL_9Cf3qfKAc485ysgAAAlEwggJNBgkqhkiG9w0BBwagggI-MIICOgIBADCCAjMGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMvCaVMAaS5PVm5EtqAgEQgIICBFeNBwmIWD-eq8Pw3Er-2K7oJCRM_-H6EbSQg0urU4dPR2y91ulnLR2mRxKSRSKAAYhiDqd91WWAc2dhp0_LKJq4LZilOkmGtGSN7PQMaFVyfDYhOzyvbWl67xpIpsSh4Zi33v28O4nCQ-einSfhACWFUy9CIDO-HgG44ESGQF0H3aFRloR0vr6f1kybUvvEfs6k0ZZBtcxJDQZCyBK3GyeADHfUSWUAmXpGX3jFpx1WUqBVhGYG048Ny5mqdOmCEbQ3kouBn09nA7sw4GT78mu9IRH-eJmPd40qy4kC4pkNPUX1XDeXV7I0jBMp3cX4JVlYOjDLGkxkR6SEt1R2ujV_DVVxyTz4V8534rhPo2JupqK0gl6yNqpbWIhLQEJa1Dyn0Lrs7ksrHlB6fIT0-4_ioApt7z3Jwa_fYITLLEx_CcritJcfPa9JQp86eX4L4aGyzIaDTuHeIyCkYKvZDzNtFoL-SVP83dWVSv7bsqfyhf8U6fM2sZZ_tW4O5eMZe5tK9vj1UwhUgGHYD64lEiiXoqXY1m-fwBMIpY7orI6xLaeBFqK4GVxktwqd4GFdj6RyuaU5w4NfWXCRQ09X1Wr_4mPQoq_AV-G-E5i0lTCrGEJsR4VObKvO0OoeWtc9vpqwIGml5V1a0Onnu-KAk4X0S4CNcOVwiCa4IunvhgsOZ7TW8g)
* [статья о сборке с графами де Брюйна](https://www.ncbi.nlm.nih.gov/pubmed/22068540)
* [о том, почему используют нечётные k](https://bioinformatics.stackexchange.com/questions/156/why-do-some-assemblers-require-an-odd-length-kmer-for-the-construction-of-de-bru)
* [сборка с помощью суперридов](https://watermark.silverchair.com/btt476.pdf?token=AQECAHi208BE49Ooan9kkhW_Ercy7Dm3ZL_9Cf3qfKAc485ysgAAAnYwggJyBgkqhkiG9w0BBwagggJjMIICXwIBADCCAlgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMkAIKyqgV6_m1XfNxAgEQgIICKdSIp-gVaKFz3DEsCT24g8BZN0HMhBk5ryOkc16e28f3lBgQ6Dn_D08_dNwSmJFHmAxll1rN2HTjYUt35N1UpDAkZL6BK_pUKHibb_yVxkF7dAuyWbCEemwfpTnab1mw7l2wc6iSWu806BD4uB4Cwo0kRAdQFUoPm9FsSbli01Pqxo8OSArtdgE1XsNjiStCyRburnJWO6gTjUmUZI5HY_a2XbDYye-Gw4K7GZmax85oKK4dMDbe7mkuRR2I7dW450_r7Xx7UZEQHeLam121nq83bl2ZxsEfNBs5TLKUFEVqW7sKHWG9zoBcXwiEbKZqFDk4P_sBUFBWdu99HLg40NYeCo0__sIlHRNopzwEOPlAxUSOV4OzMZDiIml60XcZj_zdjCIxLw841hKEHKxUCIWxDHPSGkeSLC-b1zAsgYXEa8LZzD2KzXhIvWBD17rzA55OnDqM3wma7bjper8iPcD8oN714FM7IPLfw03tKwO7vjlw8zaOtx4wsO_z2X-8Lx_jbHAZ8E3MBKRm6F2beVzr4FcEc1SUUxq_7WONfQjQ_vDQuVJZgM1twY0sI4FlqoToeyePuLnlInAoQEcd6WOY66h8-LeET5NusGlty2s49XkJ7wwnhtiNNoy_7roGXgPIkCehRw-nMzkLX3nXx-aav3eZmo9v30SjQ5Y72zYz0RTKJYOVbM1g3pK400brhYhrYKTa0-OyQCWoLJK7x2w-51b7X3KpMeM)
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
* *Напишите сборщик на суперридах (25 баллов)
