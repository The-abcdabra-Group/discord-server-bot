# discord-server-bot
Public Repository for the python based discord API wrapper client used on The People's Republic of Abcdabra

Discord Bot for the People's Republic of Abcdabra

## Execute
### To run this code, you will first need to set a few things up
```
PS> python --version
PS> pip install -r requirements.txt
PS> New-Item -Name "config.json" -ItemType "file"
```
Information on what to put in the config.json will be provided by the Project Leader

## Working on the Project
Committing to the `main` branch is strictly forbidden. You must use the dev channel and pull requests to add contributions to the project.

#### Pull Requests
Pull requests from your working branch to `dev` must be reviewed by a different developer, other than you. Pull requests from `dev` to `main` must be approved by the project manager.

#### Merging from `dev` to `main`
After the `dev` branch is tested in the Beta Server, a collaborator should open a PR `dev` -> `main`. The PR needs an overview of what has been developed. PRs should contain only significant changes to the bot

## Token Safety
There will be a config.json file used to run the project. You will have to input your Discord API token there. The token you insert is the backbone of keeping the server running, and therefore, is vital to protect.

## Release
Releases are made on every significant update to the discord bot