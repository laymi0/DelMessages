from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler


def delete(client, message):

    
        if 'начала' in message.text:

            message.delete()


def main():
    app = Client('bot', 123, '')

    
    app.add_handler(MessageHandler(delete), filters.bot)
    app.run()
    

if __name__ == '__main__':
    main()
