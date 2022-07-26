پروژه Quran_Mir به عنوان پروژه‌ی درس بازیابی پیشرفته اطلاعات در بهار ۱۴۰۱ انجام شده‌است. هدف از انجام این پروژه، ایجاد یک موتور جست‌و‌جو برای آیات قرآن بوده است. همچنین به کمک روش‌های آماری و الگوریتمی، ابزارهای دیگری مانند تشخیص آیات محوری، خوشه‌بندی آیات به صورت مفهومی به ۲ دسته (که با دقت ۹۰ درصد، معادل دسته‌بندی مکی/مدنی شد)، و … توسعه داده شده است.<br />
از آنجا که توسعه و ارزیابی مدل‌ها و ذخیره‌ی نتایج آن‌ها در مقایسه با توسعه‌ی وبسایت و نمایش خروجی‌ها محیط کاملا متفاوتی نیاز دارد، این پروژه در ۲ مخزن ذخیره شده‌است.<br />
- مخزن اول در آدرس https://github.com/Jarrahi-MM/quran_mir حاوی بخش علمی پروژه است. تمام کد‌ها و نتایج و ارزیابی مدل‌های مختلف در این مخزن قرار دارد. <br />
- مخزین دوم در آدرس https://github.com/IR1401-Spring-Final-Projects/Quran1401-1_20 حاوی بخش وبسایت پروژه است. برخی کدها به صورت مستقیم از مخزن دیگر در این مخزن قرار گرفته‌اند و برای کدهای دیگر، صرفا خروجی‌های مدل‌ها آورده شده‌اند. برای برخی کدها نیز صرفا نتایج بررسی آیات و سوره‌ها در قالب فایل‌های اکسل در این مخزن قرار گرفته است و صرفا از آن‌ها استفاده می‌شود. <br />
در هر کدام از مخزن‌ها، در فایل‌های README.md به توضیح ساختار مخزن پرداخته شده‌است. <br />

## توضیح ساختار پروژه:
رابط کاربری این پروژه با فریم‌ورک جنگو زده شده است. با استفاده از این فریم‌ورک توانستیم رابطی شبیه به گوگل با اسم Qoogle یا همان Quran Google بسازیم که این رابط اجازه‌ی سرچ عبارات مورد نظر شما را در کل قرآن می‌دهد.
این پروژه از دیتابیس sqlite استفاده می‌کند و با تکنولوژی‌ داکرکامپوز، داکرایز شده است.
## نحوه استفاده: 
 کافی است عبارت مورد نظر را در search bar نوشته، سپس موتور جستجوی پیشنهادی خود را از بین موارد زیر که در dropdown کنار search bar موجود است، انتخاب کنید:
* Boolean
* TF-IDF
* Fasttext
* Transformer
* Elastic Search
سپس با زدن دکمه‌ی سرچ، نتایج مورد نظر را ببینید. این نتایج شامل آیه‌هایی است که به ترتیب و با استفاده از الگوریتم‌ page rank به شما نشان داده می‌شوند. هم‌چنین نشانی آیه‌ها یعنی نام سوره و نام آیه و مکی یا مدنی بودن آن‌ها نیز بالای آیه نوشته شده است که می‌توانید با کلیک روی‌ آن‌ها آیه یا سوره آن را باز کنید. در نهایت، در قسمت پایینی هر نتیجه، می‌توانید classification هایی که نشان‌دهنده‌ی سوره‌ی حدس زده شده توسط سامانه و مکی یا مدنی بودن یا کلاستری ۴ دسته‌ای که کردیم را مشاهده کنید و با مقدار واقعی آن‌ها مقایسه کنید.
در نهایت برای مشاهده‌ی آیه‌ی محوری هر سوره، می‌تواند از دکمه‌ی I'm Feeling Lucky در صفحه‌ی اصلی استفاده کنید.

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
