from setuptools import find_packages, setup

setup(
    name='job_stats',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'job_stats',
    ],
)