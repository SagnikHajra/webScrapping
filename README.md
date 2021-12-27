# Introduction

Scrapping "https://www.worldometers.info/coronavirus/#countries" website for countrwise covid stats and creating a csv file out of it.

# Python version

Python 3.10.0

# Libraries

Scrapy 2.5.1
```bash
pip install scrapy
```
# Scrapy project name

CovidStats

# Execution
Basically we need to execute the spider named "covid" mentioned in spiders/DataParser.py
```bash
cd WorldCovidStat/CovidStat

scrapy crawl covid
```
# Description
Spider named "covid" will scrap the webste "https://www.worldometers.info/coronavirus/#countries" in order to find out the table data displayed. After running the Execution steps, this will generate some logs generated by the scrapy library and a csv file will be dumped named WorldCovidStat\CovidStats\worldometer_corona_stat.csv
The file has the below headers:-
last_update_time, country_name, total_case, new_case, total_deaths, new_deaths, total_recovered, active_cases, critical_cases, total_case_per_million, total_death_per_million, total_tests, total_tests_per_million

# Hon'ble mentions:
1. https://www.youtube.com/watch?v=ALizgnSFTwQ&t=329s&ab_channel=TraversyMedia
2. https://docs.scrapy.org/en/latest/intro/overview.html
3. https://www.w3.org/TR/xpath20/
4. https://chrome.google.com/webstore/detail/xpath-finder/ihnknokegkbpmofmafnkoadfjkhlogph?hl=en  [This is a very useful extension for finding XPath]
