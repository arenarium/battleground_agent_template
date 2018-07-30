[![Codacy Badge](https://api.codacy.com/project/badge/Grade/a9df47f65c4a4af18b08c0aff9072109)](https://www.codacy.com/app/arenarium/battleground_agent_template?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=arenarium/battleground_agent_template&amp;utm_campaign=Badge_Grade)

# Agent Template
Develop your own agents for the [Arenarium](http://www.arenarium.com/).
This repository has several examples of agents, which, if you come from the Arenarium webpage, you can find in the `arena-game` folder. Those agent are able to play the arena game. For the basic game, look into the `basic-game` folder. For more information about
the anatomy of an agent, [read the docs](https://arenarium.readthedocs.io/).


## System Setup
You can develop agents using any of your own favorite tools.
Just fork and download this repository and adapt the `my_agent.py` and/or `my_persistent_agent.py` examples.

Debugging your agents locally requires you to run the battleground platform locally.
There are 2 ways to do this:
1. Using a virtual machine and vagrant
2. Running/Installing natively

If you are familiar with [vagrant](https://www.vagrantup.com/docs/installation/), you can use the provided vagrant file. If not, don't worry, setting up without vagrant is quick and easy as well.

### Genral Requirements:
- Python 3.4+
- Docker (optional, to be able to save games and agent memory)


#### 1. Download
Clone or [download](https://github.com/arenarium/battleground_agent_template/archive/master.zip) this git repository into a new folder on your local machine.


#### 2. Setting up

##### 2.1 Using Vagrant (recommended)
Even if you are not already familiar with Vagrant, this is probably the easiest way to go.
Make sure you follow all the [installation instructions for vagrant.](https://www.vagrantup.com/docs/installation/)
Then run
```
vagrant up
```
in the folder that contains the Vagantfile supplied in this repo, using the console. 
This automatically installs all necessary components (battleground package, docker, etc.) for the environment to run.  

You can then connect to your virtual machine using
```
vagrant ssh
```

*If you are using this method, you can skip to running your first game.*


##### 2.2 Without Vagrant

We will assume that you already have python installed and that you are familiar with using python from the terminal/command line.

We recommend that you [create a python virtual environment](https://docs.python.org/3/tutorial/venv.html). **Activate your virtual enviromnent** and then install the requirements:
```
pip install --upgrade -r requirements.txt
```

**optional:**
[Install Docker, following instructions here](https://www.docker.com/community-edition), and start a local mongoDB container:
```
docker run -d mongo
```


## Running your First Game

Ok, now we're ready to play!

You can configure a lot about the game you want to play and which agents are playing. For now, we'll use the `example_config.json` file to determine what game configuration you will play.
The basic game, which is provided as an example, is just a number guessing game. 
It instantiates four players: one from the battleground core component, two from my_agent 
in the basic_agent folder, and one from my_persistent_agent in the same folder. 
In contrast to my_agent, the persistent agent has access to a memory, which is stored 
in a local mongoDB. Accessing it, the agent continuously tries to improve the guess for the next move.

Then run the game server (if you configured mongoDB, you can omit the `--no_save` flag):

```
battleground_start --no_save --config ./config/example_config.json
```

The output should look something like this:
```
starting battleground ...
basic_game
[0, 0, 18, 104.95247559816133]
[113, 4, 26, 55.89236974948232]
[76, 72, 78, 106.24012447916485]
[17, 80, 61, 102.5762349599125]
[0, 112, 58, 54.317275558520976]
[87, 61, 51, 103.39438307304312]
[13, 25, 83, 108.00378216234243]
[112, 80, 74, 92.91713184595727]
[1, 18, 42, 105.93647499926735]
[23, 85, 41, 110.7781658404697]
Win rates:
basic_1: 0.2000
my_agent: 0.1000
my_agent_2: 0.0000
my_persistent_agent: 0.7000
```

These numbers are the final scores of each of the four players in each of the ten games that were played.

The game we've played so far is just a simple random number guessing game. It's not a very interesting game, but it's instructive to see how the arenarium works. Have a look at the agent code in `basic_game/my_agent.py`. To see how to use an agent with memory you can look at `basic_game/my_persistent_agent.py`.


### Playing an Arena Game

This is where things get interesting!
As a second example, there is an `arena_config.json` file which plays four arena games with 
a similar agent composition as above. The core agents take random moves by default. 

The whole game is designed to be very modular and allows for many mods to be included. If you want to include more or other mods, check out the 
[battleground.games.arena.mods](https://github.com/arenarium/battleground/tree/master/battleground/games/arena/mods) 
folder to see what is available, and append your choice to the list of mod_paths in the `arena_config.json`  file.
There is an interesting 'boosts' mod, which introduces the option for the agent use spirit points (aka mana) to boost 
certain stats of the gladiator it is playing.

To start the game server, we run
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

The score is 1 for each other gladiator killed, but 
set to 0 if your gladiator dies.

See if you can change the `arena_game/my_arena_agent.py` file to increase your win rate.


### Compete with other players

So far, you've only run your agent locally and played against some built-in agents. If you want to test your agent against agents written by other people, [upload](http://www.arenarium.com/upload) your agent file to the Arenarium platform.
