from setuptools import setup

setup(
    name='frosty_ai',
    version='0.1',
    packages=['frosty_ai'],  # Update the package name here
    install_requires=[
        'requests',
        'openai>=0.27.0',
        'mistralai>=1.0.0',  # Ensure version 1.0.0 or higher
        'anthropic>=0.16.0',
        'urllib3<1.27,>=1.25.4',  # Ensure compatibility with botocore
        # Add other dependencies as needed
    ],
)
