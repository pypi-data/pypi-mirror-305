from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.0.3'
DESCRIPTION = 'Extract token-level probabilities from LLMs for classification-type outputs.'
LONG_DESCRIPTION = 'A package that allows one to extract token-level probabilities. This method can be used for example to extract sentiment class probabilities or other probability-based queries instead of parsing text-generation outputs.'

# Common dependencies
COMMON_REQUIREMENTS = [
    'transformers>=4.0.0',
    'bitsandbytes',
    'datasets',
    'accelerate',
    'loralib',
    'peft',
    'trl',
    'torch',
    'tqdm',
    'pandas'
]

# Setting up
setup(
    name="TokenProbs",
    version=VERSION,
    author="Francesco A. Fabozzi",
    author_email="francescoafabozzi@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    python_requires=">=3.8,<3.13",
    #python_requires=">=3.8",
    install_requires=COMMON_REQUIREMENTS,
    keywords=['python', 'LLMs', 'finance', 'forecasting', 'language models', 'huggingface'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12"
    ]
)