from setuptools import setup, find_packages

setup(
    name='TempMail-Tg',
    version='0.1.0',
    author='Bisnu Ray',
    heroku deployed modified= 'Adnan69x',
    author_email='example@gmail.com',
    description='A simple Telegram bot for handling tasks.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Adnan69x/TampMail-Bot',
    packages=find_packages(),
    install_requires=[
        'aiogram==2.21',
        'requests==2.28.1',
        'beautifulsoup4==4.11.1'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'mytelegrambot=TempMail-Bot:main',  # Replace 'my_bot_module:main' with the path to your bot's main function
        ],
    }
)
