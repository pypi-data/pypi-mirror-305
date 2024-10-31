from setuptools import setup, find_packages

setup(
    name='cliborg',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'cliborg=cliborg.cliborg:cli',
        ],
    },
    install_requires=[
        'requests',
        'click',
        'ollama'
    ],
    description="A command-line tool for querying Ollama models",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/cliborg",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
