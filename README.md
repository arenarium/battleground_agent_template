# Agent Template
Develop your own agents for the [Arenarium](http://www.arenarium.com/).
This repo has several examples of agents for Arenarium. For more information about
the anatomy of an agent, [read the docs](https://arenarium.readthedocs.io/)

## System setup
You can develop agents using any of your own favorite tools,
just adapt the `my_agent.py` and/or `my_persistent_agent.py` examples.

If you are familiar with [vagrant](https://www.vagrantup.com/docs/installation/), you can use the provided vagrant file. If not, don't worry, setting up without vagrant is quick and easy.

### Requirements:
- Python 3.4+
- Docker (optional, to be able to save games and agent memory)

#### 1. Download
Clone or [download](https://github.com/arenarium/battleground_agent_template/archive/master.zip) this git repository into a new folder on your local machine.

#### 2. Setting up
*If you are using Vagrant to can skip to the next section.*

We will assume that you already have python installed. And that you are familiar with using python from the terminal/command line.

We recommend that you [create a python virtual environment](https://docs.python.org/3/tutorial/venv.html)

**activate your python virtual enviromnent** and then install the requirements:
```
pip install --upgrade -r requirements.txt
```

**optional:**

[Install Docker following instructions here](https://www.docker.com/community-edition), and start a local mongoDB container:
```
docker run -d mongo
```

## Running your first game

Ok, now we're ready to play!

You can configure a lot about the game you want to play and which agents are playing. For now, we'll use the `example_config.json` file to determine what game configuration you want to play.
Then run the game server (if you configured mongoDB, you can omit the `--no_save` flag):

```
battleground_start --no_save --config ./config/example_config.json
```

The output should look something like:
```
starting battleground ...
basic_game
[6, 63.79083986857607, 105, 0]
[26, 101.94530518101656, 53, 1]
[0, 103.03455728229633, 68, 2]
```

These numbers are the final scores of each of the 4 players in each of the 3 games that were played.

The game we've played so far is just a simple random number guessing game. It's not a very interesting game, but it's instructive to see how the arenarium works. Have a look at the agent code in `basic_game/my_agent.py`. To see how to use an agent with memory you can look at `basic_game/my_persistent_agent.py`.

## Running the Arena game
This is where things get interesting!

```
battleground_start --no_save --config ./config/arena_config.json
```

if you want to see any errors that occur (useful when debugging), set `DEBUG=True` as an environment variable. For example:

```
DEBUG=True battleground_start --no_save --config ./config/arena_config.json
```

The output will look something like this:
```
starting battleground ...
arena_game_pos
[2, 0, 0]
[0, 0, 2]
[1, 0, 0]
[2, 0, 0]
[1, 0, 0]
[0, 0, 2]
[1, 0, 0]
[0, 0, 2]
[2, 0, 0]
[2, 0, 0]
Win rates:
my_gladiator: 0.7000
Random Walker: 0.0000
Attacker: 0.3000
```

See if you can change the `arena_game/my_arena_agent.py` file to increase your winrate.

### Compete with other players

So far, you've only run your agent locally and played against some built-in agents. If you want to test your agent against agents made by other people, upload your agent file to the Arenarium platform.
