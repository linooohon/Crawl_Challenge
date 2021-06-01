<h1 align="center">Crawl Challenge</h1>

<p align="center">Crawling 200 Articles URL</p>


## Task
- DataEngineer_CodeChallenge_Input.csv (input)
- results.csv (output)

## Available Commands

In the project directory, you can run:

1. Clone the project

2. Under `CrawlChallenge/`, and run command `python3 -m venv venv` : for building environments

3. Run command `source ./venv/bin/activate`

4. Run command `pip3 install -r requirements.txt`

5. Go to `CrawlChallenge/CrawlChallenge/`

6. Run command `python go.py` 

7. Then, `results.csv` will show up


## Built With:
- Python: Scrapy


## Static Files:
- rebuild_data.csv (Grouping DataEngineer_CodeChallenge_Input.csv)
     - Run `python read_files.py` , to get `rebuild_data.csv`

- results.json (Run multiple spiders in single file)


## Problem:

### The URLs in DataEngineer_CodeChallenge_Input.csv are disabled, 
### and I already grouped all the URLs in rebuild_data.csv.

1. Here are the URLs which are disabled:

   - group 1: 1 URL
   - group 9: 5 URLs
   - group 12: 3 URLs
   - group 21: 4 URLs

2. Here are the URLs which points to the same page:
   - id: 125 and id: 126 are pointing to the same page

3. Here are the URLs which I couldn't crawl:
   - group 24: 10 URLs

## Total Input and Output (200 / 176) 
200 - (1 + 5 + 3 + 4 + 1 + 10) = 176


### Due to the problems above:
- Input: 200 URLs
- Output Result: 176 URLs, authors, socail media links
