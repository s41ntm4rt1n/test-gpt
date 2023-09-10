# TestGPT

TestGPT is a Django Chat GPT clone using OpenAI's gpt-3.5 model.

## Installation
Clone this repository using ``` git clone https://www.github.com/s41ntm4rt1n/test-gpt.git``` or download the repo code to your local computer and extract it.
> [!IMPORTANT]
> 1. **I encourage the use of virtual environments to separate project dependencies from local packages. Read  more about virtual environments [here](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/).**
>  - First ensure you have [python](https://www.python.org/) installed in your local machine since you will be using [Python Package Installer (PIP)](https://pypi.org/project/pip/) to install project dependencies.
   - Install your virtual environment using
    
    <code><img width="10" src="https://user-images.githubusercontent.com/25181517/186884150-05e9ff6d-340e-4802-9533-2c3f02363ee3.png" alt="Windows" title="Windows"/></code> **Windows**
    
     ```
        python -m venv env  
     ```
     <code><img width="10" src="https://user-images.githubusercontent.com/25181517/186884153-99edc188-e4aa-4c84-91b0-e2df260ebc33.png" alt="Ubuntu" title="Ubuntu"/></code> **Linux**
     ```
     python3 -m venv env
     ```
- Activate the virtual environment using:
       
     <code><img width="10" src="https://user-images.githubusercontent.com/25181517/186884150-05e9ff6d-340e-4802-9533-2c3f02363ee3.png" alt="Windows" title="Windows"/></code> **Windows**
     ```
        env\Scripts\activate
     ```
     <code><img width="10" src="https://user-images.githubusercontent.com/25181517/186884153-99edc188-e4aa-4c84-91b0-e2df260ebc33.png" alt="Ubuntu" title="Ubuntu"/></code> **Linux**
     ```
     source env/bin/activate
    ```
2.  Install the requirements by running on the command line:
```bash
pip install -r requirements.txt
```

3.  Make migrations by running:
```bash
python manage.py makemigrations

```
then:
```bash
python manage.py migrate
```

4. Run the local server using:
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
