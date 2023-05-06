# xiaolongbao-discord
Discord bot


Some details to note:
this code works with https://github.com/lloesche/valheim-server-docker
code.py - python script user to scrape docker logs and return join code
status.js - js file using gamedig to query server status
valheim_discord.py - python script which add slash commands to discord channel and functions as our bot, this script is registered with pm2 to run at boot and is always listening for slash commands
docker_run.sh - this script is registered with pm2 to run at boot, the script will log in to docker and start the container
stop_container.sh - this script is registered with launchctl (mac equivalent of systemctl) in order to gracefully stop the container during a shutdown or reboot event
valheim.env - sets up environment variables for the container
docker-compose.yaml - dictates some general config for starting the container


If you have an existing world - the instructions from https://github.com/lloesche/valheim-server-docker will help you get set up. 

In our case we will likely have a backup of the config and data folders which we can copy and paste into the valheim-server dir which should reside at $HOME/valheim-server/
