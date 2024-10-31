from setuptools import setup, find_packages

with open("README.md", "r") as readme:
    description = readme.read()

setup(
    name='emrrunner',
    version='v1.0.3',
    packages=find_packages(),
    install_requires=[
        'Flask',
        'boto3',
        'python-dotenv',
        'marshmallow',
    ],
    entry_points={
        'console_scripts': [
            'run-my-emr-api=app.emr_job_api:run_app',
        ],
    },
    long_description=description,
    long_description_content_type="text/markdown"
)
