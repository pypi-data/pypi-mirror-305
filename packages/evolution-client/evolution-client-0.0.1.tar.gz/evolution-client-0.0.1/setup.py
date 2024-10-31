from setuptools import setup, find_packages

setup(
    name='evolution-client',
    version='0.0.1',
    description='Client Python para a API Evolution',
    author='Davidson Gomes',
    author_email='contato@agenciadgcode.com',
    packages=find_packages(),
    install_requires=[
        'requests>=2.25.1',
    ],
    python_requires='>=3.6',
)
