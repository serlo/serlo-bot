from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='serlo-bot',
    version='0.1.0',
    description='Bot for serlo.org',
    long_description=readme,
    author='Stephan Kulla',
    author_email='git.mail@kulla.me',
    url='https://github.com/kulla/serlo-bot',
    license=license,
    packages=find_packages(exclude=('tests', 'notebooks')),
    install_requires=['requests', 'beautifulsoup4'],
    extras_require={
        'dev': ['pytest'],
        'notebooks': ['jupyter', 'pandas', 'mysql-connector-python']
    }
)
