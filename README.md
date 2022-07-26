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