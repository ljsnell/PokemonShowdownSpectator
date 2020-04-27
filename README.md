# PokemonShowdownSpectator
An Automatic Spectator for Pokemon Showdown Matches

## Overview
`PokemonShowdownSpectator` is a bot that automatically spectates random Pokemon Showdown matches for streaming and coordinating bets on the winners on the Twitch Channel `#showdownspectator`. (Basically bare bones SaltyTeemo but for Pokemon.)

Pokemon Showdown is an open source game which enables people all around the world to play competitive matches. Check it out here! This stream selects random matches and broadcasts them for your enjoyment.

Please do not attempt to contact any players in the featured matches and be respectful in the chat.

## Installation
1. Clone the repository to your local system
2. Install dependencies with `pip install -r requirements.txt`. (It's possible some additional dependencies have still be left out from the file.)
3. You should also install [a recent version of Firefox](https://www.mozilla.org/en-US/firefox/new/) for the bot to control.
3. Modify the relevant variables in the class definition of `twitch_chat_bot` within `twitch_connect.py` to specify your account credentials and channel. You can generate the token to authenticate your chatbot with Twitch's servers [here](https://twitchapps.com/tmi/) while logged into your chatbot account.

## Usage
Executing `python-showdown.py` will initiate the spectation loop. Desktop streaming to your Twitch channel must be configured separately. Twitch account and channel may require additional configuration to support betting and other features.

## Contributing
Pull requests are welcome. For feature requests, you can message a contributor or open an issue to discuss what you would like to change.