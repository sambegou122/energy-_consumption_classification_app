# genère exemple de setup.py
from setuptools import setup, find_packages

setup(
    name='energy_forecast',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={"":"src"},    
    install_requires=[
        # project dependancies
    ],
    entry_points={
        'console_scripts': [
            'predict=energy_forecast.predict:predict',
            'retrain=energy_forecast.retrain:retrain',
        ],
    },
)