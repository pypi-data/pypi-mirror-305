from setuptools import setup, find_packages

setup(
    name='roi_count_plankin',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
    ],
    entry_points={
        'console_scripts': [
            'roi_net_profit=roi_net_profit.__main__:main',
        ],
    },
)
