# Opentranslator - OpenAI | ChatGPT | Translate with python

Opentranslator is a simple command that can be used from the terminal to translate text (text plain or from a file). It uses OpenAI API to perform all operations, you can choose which ai engine to use by passing it as a parameter.

The following project was born to study OpenAI and how it works.
If you would contribute open a pull request or issue on GitHub.

### Mantained by

- **[Fabrizio Cafolla](https://github.com/FabrizioCafolla)** <a href="https://www.buymeacoffee.com/fabriziocafolla" target="_blank"><img align="right" src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 30px !important; width: 150px !important" ></a>

### Usage

#### Required

- Python >= 3.7
- OpenAI Account


#### Input text
```
# You can save your OPENAI_API_KEY permanently in the user's environment
export OPENAI_API_KEY="${YOUR_OPENAI_API_KEY}"

pip install opentranslator

opentranslator --translate english --text "Ciao Mondo!"
```

#### Text from file

```
opentranslator --translate english --filepath examples/it.txt
```

#### Other

```
Arg -vvv: output all info with cost of request (in progress)
```

### Dev mode

1. Setup env

```
git clone https://github.com/FabrizioCafolla/chatgpt-translate-app.git

cd chatgpt-translate-app

echo 'export OPENAI_API_KEY="${YOUR_OPENAI_API_KEY}"' > .env

chmod +x scritps/*.sh

./scripts/setup.sh

source .activate
```

2. Usage

```
python opentranslator/app.py --filepath examples/it.txt --translate english

python opentranslator/app.py --filepath examples/en.txt --translate italian

python opentranslator/app.py --text "Ciao Mondo!" --translate english
```

### Contributors

<a href="https://github.com/fabriziocafolla/opentranslator/graphs/contributors"> <img src="https://contrib.rocks/image?repo=fabriziocafolla/opentranslator" /> </a>

### License

The project is made available under the GPL-3.0 license. See the `LICENSE` file for more information.