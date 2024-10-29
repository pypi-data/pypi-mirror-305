from setuptools import setup, find_packages

setup(
    name='r2d2_bigquery_duckdb_analysis_engine',
    version='0.3',
    packages=find_packages(),
    install_requires=[
        'google-auth',
        'google-cloud-bigquery',
        'pandas',
        'duckdb',
        'jinja2'
    ],
    author='Tiago Navarro',
    description='Pacote para consultas e manipulação de dados no BigQuery com DuckDB, focado em analytics engineering.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
