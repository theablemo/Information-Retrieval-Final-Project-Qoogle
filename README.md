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

### Download and Start ElasticSearch
```shell
curl -fsSL https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-7.x.list
sudo apt update
sudo apt install elasticsearch
```

### Train Fasttext model
```shell
python manage.py train_fasttext
```
