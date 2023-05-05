import schedule
import time
import webbrowser
from discord_webhook import DiscordWebhook, DiscordEmbed

# /- Configurations -\

chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"

send_to_discord = True # /- Set it to either True or False -\
webhookurl = 'https://discord.com/api/webhooks/1038313622805434458/-SXHr_4scUkMUpKjlW5ts3XtDB0tBGjhZjR6-Y8LussdFlLIJaAYha3kN8UeNdx_IUX6' # /- discord webhook url -\
pinguser = True # /- pings user/everyone -\
discord_userid = '788201404157132830' # /- Set it to user's discord id or everyone/here (no need to include the "@") -\

# /- Template -\

def Template(): # /- Change the "Template" to something else -\
    open_link('CHANGEME') # /- Google meet link/Zoom link -\
    if send_to_discord == True: # /- Change it to True or False -\

        webhook = DiscordWebhook(url=webhookurl)
        embed=DiscordEmbed(title='Template Title', description='Template Description', color=0x00ac47)
        webhook.add_embed(embed)

        if pinguser == True: # /- Change it to True or False -\
            webhook2 = DiscordWebhook(url=webhookurl, content=f'<@{discord_userid}>') 
            webhook2.execute()
            time.sleep(0.5)
            webhook.execute()
        else:
            webhook.execute()

# /- You don't need to edit this -\
def open_link(link):
    webbrowser.get(chrome_path).open(link, autoraise=True)


# main
def demo1():
    open_link('https://meet.google.com/xdh-cumm-lmao')
    if send_to_discord == True:

        webhook = DiscordWebhook(url=webhookurl)
        embed=DiscordEmbed(title='Subject #1', description='You\'re Subject #1 is ready', color=0x00ac47)
        webhook.add_embed(embed)

        if pinguser == True:
            webhook2 = DiscordWebhook(url=webhookurl, content=f'<@{discord_userid}>')
            webhook2.execute()
            time.sleep(0.5)
            webhook.execute()
        else:
            webhook.execute()
    

def demo2():
    open_link('https://meet.google.com/red-this-msn')
    if send_to_discord == True:
        
        webhook = DiscordWebhook(url=webhookurl)
        embed=DiscordEmbed(title='Subject #2', description='You\'re Subject #2 is ready', color=0x00ac47)
        webhook.add_embed(embed)

        if pinguser == True:
            webhook2 = DiscordWebhook(url=webhookurl, content=f'<@{discord_userid}>')
            webhook2.execute()
            time.sleep(0.5)
            webhook.execute()
        else:
            webhook.execute()

    
# /- Schedules on when it will join a meeting -\
schedule.every().day.at("06:55").do(demo1)
schedule.every().monday.at("14:15").do(demo2)

# /- You don't need to edit this -\
print('Auto gmeet is now running!')
while 1:
    schedule.run_pending()
    time.sleep(1)
