# Hobrus RabbitMQ

Simple RabbitMQ wrapper using FastStream for easy message publishing and subscribing in Python.

## Installation

```bash
pip install hobrus-rabbitmq
```

## Environment Variables

The package uses the following environment variables (with default values):

```env
RABBITMQ_USERNAME=guest
RABBITMQ_PASSWORD=guest
RABBITMQ_HOST=localhost
RABBITMQ_PORT=5672
RABBITMQ_PROTOCOL=amqp
```

You can set these variables in your environment or use a `.env` file.

## Usage

### Synchronous Message Publishing

```python
from hobrus_rabbitmq import send_message_sync

# Send a message synchronously
send_message_sync("queue_name", "Hello, World!")
```

### Asynchronous Message Publishing

```python
import asyncio
from hobrus_rabbitmq import send_message

async def publish_message():
    await send_message("queue_name", "Hello, World!")

# Run the async function
asyncio.run(publish_message())
```

### Message Subscribing

```python
from hobrus_rabbitmq import subscriber, run

# Define a message handler
@subscriber("queue_name")
async def process_message(message: str):
    print(f"Received message: {message}")

# Start the subscriber
if __name__ == "__main__":
    run()
```

## Complete Examples

### Async Publisher Example

```python
import asyncio
from hobrus_rabbitmq import send_message

async def test_async():
    for i in range(5):
        message = f"Async message {i}"
        print(f"Sending: {message}")
        await send_message("test_queue", message)
        await asyncio.sleep(1)  # Small delay between messages

if __name__ == "__main__":
    asyncio.run(test_async())
```

### Sync Publisher Example

```python
from hobrus_rabbitmq import send_message_sync
import time

def test_sync():
    for i in range(5):
        message = f"Sync message {i}"
        print(f"Sending: {message}")
        send_message_sync("test_queue", message)
        time.sleep(1)  # Small delay between messages

if __name__ == "__main__":
    test_sync()
```

### Subscriber Example

```python
from hobrus_rabbitmq import subscriber, run

@subscriber("test_queue")
async def process_message(message: str):
    print(f"Received message: {message}")

if __name__ == "__main__":
    print("Starting subscriber...")
    run()
```

## Dependencies

- faststream[rabbit]

## License

This project is open-source.

## Author

- Suhobrus Boris
- Email: bhobrus@gmail.com
- GitHub: [SimpleRabbitMQFastStreamByHobrus](https://github.com/Hobrus/SimpleRabbitMQFastStreamByHobrus)
