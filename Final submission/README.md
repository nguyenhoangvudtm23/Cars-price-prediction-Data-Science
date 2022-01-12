# Car Price Prediction Project
Approximately 40 million used vehicles are sold each year. Effective pricing strategies can help any company or individual to efficiently sell its products in a competitive market and make a profit, that is why we have chosen this topic for the data science project.
 
In this repository, we will illustrate our process of doing the research, beginning from crawling car data to predicting car prices using some Machine Learning algorithm.

# Table Contents:
1. Algorithms: contains all file related to training and testing result of all algorithms.
2. Cleaning: consists of code for cleaning data and convert categorical to numerical data.
3. Crawl: includes code using Web Scraper and Scrapy library for crawling data. 
4. Data: contains all data file in form .csv 
5. EDA: contains image file after explore data and code file for coding EDA
6. Report: consists of all report file and slide in .docx, and .pdf

# Requirements
1. python3
2. numpy
3. matplotlib
4. seaborn
5. sklearn
5. scrapy
6. jupyter notebook

# How to run
* Clone the project with git: _!git clone [repos_link]_
1. Crawl: To put our spider to work, go to the crawl directory and run:
__scrapy crawl cars -O cars.csv__ -> This will generate a cars.csv file containing all scraped items

---- crawl/
    ---- scrapy.cfg            # deploy configuration file
    
    ---- car_links.csv         # car link data crawl from web scraper
 
    ---- tutorial/             # project's Python module, you'll import your code from here
        ---- __init__.py

        ---- items.py          # project items definition file

        ---- middlewares.py    # project middlewares file

        ---- pipelines.py      # project pipelines file

        ---- settings.py       # project settings file

        ---- spiders/          # a directory where you'll later put your spiders
            ---- __init__.py
            
2. Data_Cleaning
    * After crawling data, run file __cleaning_data.ipynb__
    * Then run file __covert_number.ipynb__
    * Run file __fill_missing_value.ipynb__
3. EDA
    * Run file __EDA_Final.ipynb__ for viewing all image data and some comments about features
    * Run file __EDA_categorical.ipynb__ for shown distribution and image of categorical data
    * Run file __EDA_details_features.ipynb__ for viwing details anlyssing of each features
4. Algorithms
    * Run file __DropNa_Regression_Alg.ipynb__ for viewing the result with DropNa method
    * Run file __KNN_Fill_Regression_Alg.ipynb__ for viewing the result with Filling with KNN method


[repos_link]:  https://github.com/nguyenhoangvudtm23/Cars-price-prediction-Data-Science.git

# References

# License

