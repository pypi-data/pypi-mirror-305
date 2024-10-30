import asyncio
from .broker import broker


async def send_message(queue_name, message):
    try:
        await broker.connect()
        await broker.publish(message, queue=queue_name)
    except Exception as e:
        print(f"Ошибка при отправке сообщения: {e}")
    finally:
        await broker.close()


def send_message_sync(queue_name, message):
    asyncio.run(send_message(queue_name, message))
