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

### Run with Django Server
```shell
python manage.py runserver 0:81
```