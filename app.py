from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler


def delete(client, message):

    
        if 'начала' in message.text:

            message.delete()


def main():
    app = Client('bot', 9486126, '4c9a424419e82df39660998e18417397')

    
    app.add_handler(MessageHandler(delete), filters.bot)
    app.run()
    

if __name__ == '__main__':
    main()