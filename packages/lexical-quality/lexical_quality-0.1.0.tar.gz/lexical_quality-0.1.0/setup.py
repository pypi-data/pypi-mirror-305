from setuptools import setup, find_packages

setup(
    name='lexical_quality',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'scikit-learn',
        'cleanlab',
        'textstat', 
        'language-tool-python',
        'pytest'
    ],
    entry_points={
        'console_scripts': [
            'lexical_quality=lexical_quality.main:main',
        ],
    },
)
