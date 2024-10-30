from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name='hobrus-rabbitmq',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'faststream[rabbit]'
    ],
    description='Simple RabbitMQ wrapper using FastStream for easy message publishing and subscribing in Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Suhobrus Boris',
    author_email='bhobrus@gmail.com',
    url='https://github.com/Hobrus/SimpleRabbitMQFastStreamByHobrus',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    python_requires='>=3.7',
    keywords='rabbitmq, faststream, messaging, queue',
    project_urls={
        'Bug Reports': 'https://github.com/Hobrus/SimpleRabbitMQFastStreamByHobrus/issues',
        'Source': 'https://github.com/Hobrus/SimpleRabbitMQFastStreamByHobrus',
    },
)