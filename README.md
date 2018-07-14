MoeStat
=======

A fetcher for [stats.moe.gov.tw](stats.moe.gov.tw)

`MoeStat` 是一個用來獲取台灣教育部統計查詢網資料的工具。


HOW TO USE
==========

## Install requirements by pipenv

```bash
$ pipenv install
$ pipenv shell
```

## Run grab_all.py to get all dataset

All of the data will be downloaded to `dataset` directory.

Since it only run with one thread, be patient.

```bash
$ python grab_all.py
[*] Get all qno in stats.moe.gov.tw
[*] Start to get all data
[*] Downloading: 各級學校校數
[*] Downloading: 平均每千方公里各級學校校數
[*] Downloading: 中等以下學校班級數
[*] Downloading: 各級學校學生數
[*] Downloading: 各級學校畢業生數
[*] Downloading: 各級學校學生結構
[*] Downloading: 平均每百戶在學之各級學校學生數
[*] Downloading: 各級學校學生人數占年底人口千分比
[*] Downloading: 各級學校女性學生比率
[*] Downloading: 各級學校專任教師數
[*] Downloading: 各級學校教師學歷
[*] Downloading: 各級學校專任職員數
[*] Downloading: 各級學校女性教師比率
[*] Downloading: 各級學校女性校長比率
[-] Found multiple data in one set: 各級學校女性主管比率
    [*] Downloading: 各級學校女性主管比率-中等以下學校女性主管比率
    [*] Downloading: 各級學校女性主管比率-大專校院女性主管比率
[-] Found multiple data in one set: 在學率
    [*] Downloading: 在學率-各級教育學齡人口淨在學率
    [*] Downloading: 在學率-各級教育學齡人口粗在學率
[*] Downloading: 國中畢業生就學機會率
[*] Downloading: 中等以下學校畢業生升學率
[-] Found multiple data in one set: 縣市別學校概況
    [*] Downloading: 縣市別學校概況-國民小學概況
...
```
