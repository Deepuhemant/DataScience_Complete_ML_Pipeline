from setuptools import setup, find_packages

setup(
    name="datascience",
    version="0.0.1",
    author="deepu",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=[
        'pandas',
        'mlflow',
        'notebook',
        'numpy',
        'scikit-learn',
        'matplotlib',
        'python-box',
        'pyYAML',
        'tqdm',
        'ensure',
        'joblib',
        'types-pyYAML',
        'Flask',
        'Flask-Cors'
    ]
)
