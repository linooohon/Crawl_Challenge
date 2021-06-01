
# @Author  : Phil
# @File    : go.py
# @job     : run all spiders, export csv file: "results.csv"

from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
import pandas as pd
import json


def main():
    setting = get_project_settings()
    process = CrawlerProcess(setting)

    for spider_name in process.spiders.list():
        print("Running spider %s" % (spider_name))
        process.crawl(spider_name)
    process.start()

    with open("results.json", "r") as file:
        data = json.loads(file.read().replace("][", "").replace("}", "},").replace("},,", "},").replace("},\n]", "}]"))
        results_df = pd.DataFrame(data).sort_values(
            ["url"], ascending=True).reset_index(drop=True)
        results_df.to_csv("results.csv")


main()
