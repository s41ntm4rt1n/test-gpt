# TestGPT

TestGPT is a Django Chat GPT clone using OpenAI's gpt-3.5 model.

## Installation
Clone this repository using ``` git clone https://www.github.com/s41ntm4rt1n/test-gpt.git``` or download the repo code to your local computer and extract it.

1. First install the requirements by running:
```bash
pip install -r requirements.txt
```
**I encourage the use of virtual environments to separate project dependencies from local packages. Read  more about virtual environments [here](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/).**

2. Make migrations by running:
```bash
python manage.py makemigrations

```
then:
```bash
python manage.py migrate
```
3. Run the local server using:
```bash
python manage.py runserver
```
and head on to [http://127.0.0.1:8000](http://127.0.0.1:8000) on your browser.

## Usage
Go to OpenAI and get your [API key](https://platform.openai.com/account/api-keys) then navigate to ```test-gpt/chatbot/.env``` to edit the **```.env```** file and add the API key.

```python
API_KEY= #your OpenAI API key.
```
or

Upon successful login, go to **⚙ Settings** on the account sidebar and update your API key.
## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change. I am open to collaboration on the same issue or other Python - AI projects.

Please make sure to update tests as appropriate.

For more information regarding the API used, read [this](https://platform.openai.com/docs/api-reference).
