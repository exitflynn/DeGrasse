# DeGrasse
A Discord bot written in python for sharing interesting information about Space, Science and Technology.

The bot, in it's current state, uses [NASA's APOD API](https://github.com/nasa/apod-api) to send NASA's Astronomy Picture of the Day. 

## Installation and Setup:

(0. Sign-up on <https://api.nasa.gov/#signUp> and get the API key. 
Then go to the [Discord Developers Portal](https://discord.com/developers/) and create a new bot.
Check all the three intents given under 'Privileged Gateway Intents'
Under the OAuth2 section check bot scope and check administrator in the permissions section)

1. Clone the repository:
```console
$ git clone https://github.com/exitflynn/DeGrasse.git
```
2. Add your Discord bot key in `config.py`.
3. Install the dependencies.
```console
$ pip install -r /path/to/requirements.txt
```
4. Run the `main.py` and pass the NASA API with the `-k` and the `--key` flag.
```console
$ python main.py -k <API_KEY>
```

In case of any issues feel free to raise an issue on Github. You're also more than welcome to join the Discord server at: <https://discord.gg/HkrJxE5J>
