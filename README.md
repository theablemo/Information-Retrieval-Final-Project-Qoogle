فقط پوشه‌ها، پرونده‌ها و کلاس‌ها را توضیح دهید و سند کنید. همچنین مدل‌های به‌کاررفته در هر بخش
> پروژه Quran_Mir به عنوان پروژه‌ی درس بازیابی پیشرفته اطلاعات در بهار ۱۴۰۱ انجام شده‌است. هدف از انجام این پروژه، ایجاد یک موتور جست‌و‌جو برای آیات قرآن بوده است. همچنین به کمک روش‌های آماری و الگوریتمی، ابزارهای دیگری مانند تشخیص آیات محوری، خوشه‌بندی آیات به صورت مفهومی به ۲ دسته (که با دقت ۹۰ درصد، معادل دسته‌بندی مکی/مدنی شد)، و … توسعه داده شده است.
از آنجا که توسعه و ارزیابی مدل‌ها و ذخیره‌ی نتایج آن‌ها در مقایسه با توسعه‌ی وبسایت و نمایش خروجی‌ها محیط کاملا متفاوتی نیاز دارد، این پروژه در ۲ مخزن ذخیره شده‌است.

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
