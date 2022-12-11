# DeGrasse
A Discord bot written in python for sharing interesting information about Space, Science and Technology.

The bot, in it's current state, uses [NASA's APOD API](https://github.com/nasa/apod-api) to send NASA's Astronomy Picture of the Day. 

## Installation and Setup:

-1. Go to the [Discord Developers Portal](https://discord.com/developers/) and create a new bot with intents-enabled.
0. Sign-up on <https://api.nasa.gov/#signUp> and get the API key. 
1. Clone the repository:
```console
$ git clone https://github.com/exitflynn/DeGrasse.git
```
2. Add your Discord bot key in `config.py`.
4. Install the dependencies.
```console
$ pip install discord
```
5. Run the `main.py` and pass the NASA API with the `-k` and the `--key` flag.
```console
$ python main.py -k <API_KEY>
```
