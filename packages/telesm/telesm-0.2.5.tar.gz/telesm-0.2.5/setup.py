from setuptools import setup, find_packages

setup(
    name='telesm',
    version='0.2.5',
    description='A command-line dictionary app using WordNet and OpenAI',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author='Pedram Behroozi',
    author_email='pedrambehroozi@gmail.com',
    url='https://github.com/pedrambehroozi/telesm',
    packages=find_packages(),
    install_requires=['nltk', 'requests', 'python-dotenv'],
    entry_points={
        'console_scripts': [
            'telesm=telesm.__main__:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)