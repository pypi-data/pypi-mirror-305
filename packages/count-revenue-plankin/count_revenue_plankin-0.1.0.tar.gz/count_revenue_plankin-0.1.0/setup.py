from setuptools import setup, find_packages

setup(
    name='count_revenue_plankin',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
    ],
    entry_points={
        'console_scripts': [
            'count_revenue_costs=count_revenue_costs.__main__:main',
        ],
    },
)
