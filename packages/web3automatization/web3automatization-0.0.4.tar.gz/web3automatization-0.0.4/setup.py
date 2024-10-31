from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

version = '0.0.4'
setup(
    name='web3automatization',
    version=version,
    description=(
        u'A library for simplified interaction with web3.'
        u'From sybils for sybils.'),
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='G7[azazlo]',
    author_email='MaloyMeee@yandex.ru',
    url='https://github.com/g7AzaZLO/web3automatization',
    download_url='https://github.com/g7AzaZLO/web3automatization/archive/v{}.zip'.format(version),
    license='Apache Licence, Version 2.0',
    package='web3automatization',
    install_requires=['web3', 'hexbytes', "requests"],
    include_package_data=True,
    packages=find_packages(),
    package_data={
        'web3automatization': ['**/*']
    },
)
