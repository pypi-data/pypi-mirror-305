from setuptools import setup, find_packages

setup(
    name="joke_business_fastprog",
    version="0.1.0",
    description="Быстрый анализ дохода и расходов",
    author="Pablo-3_16",
    author_email="p.ergle@edu.centraluniversity.ru",
    packages=find_packages(),
    install_requires=["setuptools", "wheel"],
    entry_points={
        'console_scripts': [
            'business_prog = joke_business_fastprog.__main__:main',
        ],
    },
    python_requires='>=3.7',
)