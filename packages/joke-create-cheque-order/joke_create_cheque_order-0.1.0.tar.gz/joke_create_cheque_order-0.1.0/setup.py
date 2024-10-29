from setuptools import setup, find_packages

setup(
    name="joke_create_cheque_order",
    version="0.1.0",
    description="Быстрый генератор чека",
    author="Pablo-3_16",
    author_email="p.ergle@edu.centraluniversity.ru",
    packages=find_packages(),
    install_requires=["setuptools", "wheel", "json"],
    entry_points={
        'console_scripts': [
            'joke_create_cheque_order = joke_create_cheque_order.__main__:main',
        ],
    },
    python_requires='>=3.7',
)