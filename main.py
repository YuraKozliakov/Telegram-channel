from telethon import TelegramClient, events

# Ваши данные
api_id = 23800781
api_hash = 'f59b49091732c6d4da0654a6a86d441f'
phone_number = '+905528734616'
source_channel = '@science1177'
destination_channel = '@allaboutworldsuper'

client = TelegramClient('session_name', api_id, api_hash)


async def main():
    await client.start(phone_number)
    print("Client is running...")

    @client.on(events.NewMessage(chats=source_channel))
    async def handler(event):
        if 'Science | Наука 🤓' in event.raw_text:
            # Заменяем текст
            new_text = event.raw_text.replace('Science | Наука 🤓', '')

            # Отправляем измененное сообщение в destination_channel
            await client.send_message(destination_channel, new_text,
                                      file=event.message.media,
                                      reply_to=event.message.reply_to_msg_id)
        else:
            # Не отправляем сообщение, если текст не содержит нужные слова
            print("Message does not contain the target text.")

    # Запускаем клиента
    await client.run_until_disconnected()


# Запускаем основной асинхронный метод
with client:
    client.loop.run_until_complete(main())
