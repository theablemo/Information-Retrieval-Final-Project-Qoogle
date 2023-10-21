# Introduction

Project `Quran MIR` was carried out as the advanced information retrieval project in the spring of 2023. The aim of this project was to create a search engine for Quranic verses. Additionally, with the help of statistical and algorithmic methods, other tools such as identifying central verses, clustering verses conceptually into two categories (which were classified as Meccan/Medinan with 90% accuracy), and more, have been developed.

Since the development and evaluation of models and storing their results require a completely different environment compared to the development of the website and displaying outputs, this project has been stored in 2 repositories.

- The first repository at https://github.com/Jarrahi-MM/quran_mir contains the scientific section of the project. All codes, results, and evaluations of different models are included in this repository.
- The second repository at https://github.com/IR1401-Spring-Final-Projects/Quran1401-1_20 contains the website section of the project. Some codes have been directly placed from the other repository in this repository, and for other codes, only the outputs of the models have been provided. For some codes, the results of the analysis of verses and chapters have been placed in the form of Excel files in this repository and are only used from there.

In each repository, the repository's structure is explained in the README.md files.

# Collaborators

- [Mohammad Abolnejadian](https://github.com/theablemo)
- [Amin Ghasemzade](https://github.com/maghasemzadeh)
- [Aryan Ahadinia](https://github.com/AryanAhadinia)
- [Mohammadmahdi Jarrahi](https://github.com/Jarrahi-MM)

# Project Structure Description

The user interface of this project has been built using the Django framework. With this framework, we were able to create a search interface similar to Google, named `Qoogle` or Quran Google, which allows you to search for your desired phrases throughout the Quran.

This project uses an SQLite database and has been dockerized with Docker Compose technology.

# Usage

Simply type the desired phrase in the search bar, then select your preferred search engine from the following options available in the dropdown next to the search bar:

- Boolean
- TF-IDF
- Fasttext
- Transformer
- Elastic Search

Then, by clicking the search button, you can see the desired results. These results include verses that are displayed to you in order using the page rank algorithm. Additionally, the address of the verses, namely the name of the chapter and verse, and whether they are Meccan or Medinan, are written above the verse, which you can click to open the verse or chapter. Finally, at the bottom of each result, you can view the classifications indicating the guessed chapters by the system, whether they are Meccan or Medinan, or the 4-category cluster we have created, and compare them with their actual values.

Finally, to view the central verse of each chapter, you can use the "I'm Feeling Lucky" button on the main page.

# Setup

### Start docker container
```shell
screen -S mir_site / -r mir_site
sudo docker-compose up --build
ctrl-A-D
```

### Go to docker container
```shell
sudo docker exec -it tmwm /bin/bash
```

### Manual Start
```shell
python3 -m venv ./venv
source ./venv/bin/activate
python -m pip install --upgrade pip
sudo apt-get install python3-dev
pip install -r requirements.txt

screen -S mir_site / -r mir_site
source ./venv/bin/activate
sudo env "PATH=$PATH" python manage.py runserver 0:81
ctrl-A-D

screen -S mir_commands / -r mir_commands
python manage.py shell

from information_retrieval.lib.quran_mir.quran_ir import ArabertQuranIR
ArabertQuranIR()
ctrl-A-D
```

### Download Fasttext lib
```shell
/information_retrieval/lib/quran_mir# git clone https://github.com/facebookresearch/fastText.git
/information_retrieval/lib/quran_mir/fastText# make
/information_retrieval/lib/quran_mir/fastText# pip install .
/information_retrieval/lib/quran_mir# mkdir fasttext_model
```

### Train Fasttext model
```shell
python manage.py train_fasttext
```

## Elasticsearch

### Download ElasticSearch
```shell
curl -fsSL https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-7.x.list
sudo apt update
sudo apt install elasticsearch
```
### Configuring security options
```shell
sudo nano /etc/elasticsearch/elasticsearch.yml
```
unconmment `network.host` and `network.port` in the **`elasticsearch.yml`** file and change it like below.

```shell
network.host: localhost
network.port: 9200
```
Save and exit. Then run the follwing in the terminal.

```shell
sudo systemctl start elasticsearch
sudo systemctl enable elasticsearch
```
### Test elasticsearch
```shell
curl -X GET 'http://localhost:9200'
```
You should get something like the following.

```shell
Output
{
  "name" : "elasticsearch-ubuntu20-04",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "qqhFHPigQ9e2lk-a7AvLNQ",
  "version" : {
    "number" : "7.6.2",
    "build_flavor" : "default",
    "build_type" : "deb",
    "build_hash" : "ef48eb35cf30adf4db14086e8aabd07ef6fb113f",
    "build_date" : "2020-03-26T06:34:37.794943Z",
    "build_snapshot" : false,
    "lucene_version" : "8.4.0",
    "minimum_wire_compatibility_version" : "6.8.0",
    "minimum_index_compatibility_version" : "6.0.0-beta1"
  },
  "tagline" : "You Know, for Search"
}

```
