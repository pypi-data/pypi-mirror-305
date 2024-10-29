from setuptools import setup, find_packages
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='roborregos-metrics-client',
    version='2.2.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'pydantic',
        'psutil',
    ],
    entry_points={
        'console_scripts': [
            'robometrics-worker = robometrics.worker.worker:main',
            'robometrics-sync   = robometrics.worker.worker:sync'
        ]
    },
    long_description=long_description,
    long_description_content_type='text/markdown'
)
