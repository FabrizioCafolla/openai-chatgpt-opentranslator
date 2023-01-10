# ChatGPT - Translate with python

### Setup local env

1. Setup env

```
git clone https://github.com/FabrizioCafolla/chatgpt-translate-app.git

cd chatgpt-translate-app

export OPENAI_API_KEY="${YOUR_OPENAI_API_KEY}" > .env

chmod +x setup.sh

./setup.sh

source .activate
```

### Usage

```
python app.py --filepath examples/it.txt --translate english

python app.py --filepath examples/en.txt --translate italian

python app.py --text "Ciao Mondo!" --translate english
```