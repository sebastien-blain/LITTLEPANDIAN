#########################
# DO NOT EDIT THIS FILE #
#########################
from time import sleep
from bot import Bot
from helper.app import Settings
from helper.game_server import GameServerService
from helper.lhapi import LHAPIService

if __name__ == '__main__':
    is_online = False

    lhapi_url = Settings().lhapi_url
    if lhapi_url != None and lhapi_url != "":
        is_online = True

    bot = Bot()
    GameServerService().set_bot(bot)

    if is_online:
        print("Running the bot in online mode...")
        LHAPIService().start()
    else:
        print("Running the bot in offline mode...")
        game_server_url = Settings().game_server_url
        if game_server_url == None or game_server_url == "":
            print("Error: GAME_SERVER_URL variable isn't defined")
            exit(1)
        GameServerService().set_team_id(Settings().team_id)
        GameServerService().start()

    while True:
        sleep(1000)
