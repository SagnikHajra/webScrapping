import scrapy

class DataParser(scrapy.Spider):
    # name is the unique string to identify the spider, in this case it's covid
    name = "covid"
    start_urls = ["https://www.worldometers.info/coronavirus/#countries'"]

    def parse(self, response):
        # Specify the csv headers
        file_data = "last_update_time,country_name,total_case,new_case,total_deaths,new_deaths,total_recovered,active_cases,critical_cases,total_case_per_million,total_death_per_million,total_tests,total_tests_per_million\n"
        # Last updated time picked from html
        updateTime = response.xpath("//div[@class='container']//div[@class='row']/div[@class='col-md-8']/div[@class='content-inner']/div[2]/text()").get()
        updateTime = updateTime.strip()[14:]
        # Each row of the html
        rows = response.xpath("//table[@id='main_table_countries_today']/tbody[1]/tr")
        for element in rows:
            # Reset the variables
            country=total_case=new_case=total_deaths=new_deaths=total_recovered=active_cases=critical_cases=total_case_per_million=total_death_per_million=total_tests=total_tests_per_million=''

            country = element.xpath(".//a[@class='mt_a']/text()").get()
            # Some tr tags aren't ment for a country, skip them
            if country is None:
                continue
            total_case = self.nullCheck(element.xpath(".//td[3]/text()").get())
            new_case = self.nullCheck(element.xpath(".//td[4]/text()").get())
            total_deaths = self.nullCheck(element.xpath(".//td[5]/text()").get())
            new_deaths = self.nullCheck(element.xpath(".//td[6]/text()").get())
            total_recovered = self.nullCheck(element.xpath(".//td[7]/text()").get())
            active_cases = self.nullCheck(element.xpath(".//td[9]/text()").get())
            critical_cases = self.nullCheck(element.xpath(".//td[10]/text()").get())
            total_case_per_million = self.nullCheck(element.xpath(".//td[11]/text()").get())
            total_death_per_million = self.nullCheck(element.xpath(".//td[12]/text()").get())
            total_tests = self.nullCheck(element.xpath(".//td[13]/text()").get())
            total_tests_per_million = self.nullCheck(element.xpath(".//td[14]/text()").get())

            file_data+=f'{updateTime},{country},{total_case},{new_case},{total_deaths},{new_deaths},{total_recovered},{active_cases},{critical_cases},{total_case_per_million},{total_death_per_million},{total_tests},{total_tests_per_million}\n'
        print("\n\n\nThe File Data:\n"+file_data+"\n\n")

        with open("worldometer_corona_stat.csv",'w') as f:
            f.write(file_data)
    
    def nullCheck(self, value):
        if not value or value == "N/A":
            value = ""
        else:
            value = value.strip()
        return value.replace("+","").replace(",","")