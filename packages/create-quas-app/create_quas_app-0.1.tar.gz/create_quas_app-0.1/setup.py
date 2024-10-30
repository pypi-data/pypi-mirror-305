from setuptools import setup, find_packages

setup(
    name="create-quas-app",
    version="0.1",
    packages=find_packages(),
    install_requires=["Click"],
    entry_points={
        "console_scripts": [
            "create-quas-app=create_quas_app:create_quas_app",
        ],
    },
    author="Emmanuel Esho",
    description="A basic Quick API Setup using Flask, intended for rapid project initiation.",
    url="https://github.com/zeddyemy/QUAS",
)
