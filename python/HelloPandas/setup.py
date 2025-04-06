from setuptools import setup, find_packages

setup(
    name='HelloPandas',
    version='0.1',
    packages=find_packages(),
    entry_points = {
        'console_scripts': [
            'hello_world=HelloPandas.HelloWorldRunner:cli',
            'hello_pandas=HelloPandas.HelloPandasRunner:cli'
        ]
    }
)
