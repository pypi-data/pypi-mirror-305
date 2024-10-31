# setup.py
from setuptools import setup, find_packages

setup(
    name="ark_metrics_collector",
    version="0.2.0",
    packages=find_packages(),
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        "Flask",
        "prometheus_client",
        "pyyaml"
    ],
    entry_points={
        'console_scripts': [
            'ark-metrics-collector=ark_metrics_collector.main:main',
        ],
    },
)

