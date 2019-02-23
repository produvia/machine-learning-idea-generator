# ML Idea Generator

## About

In a world of infinite machine learning opportunities or use cases, how do we pursue any one model? In other words, how do we decide on which machine learning model to develop? With `ml-idea-generator`, we will answer this question. For this project, I propose we use Google Trends to find the most commonly searched prediction-related phrases on Google. This information will give us an indication on which model we can dedicate our time and resources to.

## Installation

Clone the repo and change directory to it

```
$ git clone https://github.com/produvia/ml-idea-generator.git
$ cd ml-idea-generator
```

Install requirements

```
$ pipenv install
$ pipenv shell
```

## Usage
Retrieve Google Trends Interest Over Time for up to five keywords:

```
$ python3 retrieve_google_trends.py
```

This command generates `output.csv` file

## Dataset

The `data` folder contains `search_phrases_on_google.txt`, a dataset which contains ML-related keywords. This dataset can be for analysis with Google Trends script `retrieve_google_trends.py`

## To Do

- Implement a script to iterate through `data/search_phrases_on_google.txt` while adhering to Google Trend's five term search limitation. Learn more [here](https://github.com/GeneralMills/pytrends#common-api-parameters).
