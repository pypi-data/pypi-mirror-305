from setuptools import setup, find_packages

setup(
    name='pixegami_hello_new',
    version='0.3',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "pixegami-hello = pixegami_hello:hello",
        ]
    }
)