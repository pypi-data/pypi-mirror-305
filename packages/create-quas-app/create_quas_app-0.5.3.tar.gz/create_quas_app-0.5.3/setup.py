from setuptools import setup, find_packages

with open("QUAS-template/README.md", "r") as f:
    long_description = f.read()

setup(
    name="create-quas-app",
    version="0.5.3",
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["Click"],
    entry_points={
        "console_scripts": [
            "create-quas-app=app:create_quas_app",
        ],
    },
    author="Emmanuel Esho",
    description="A basic Quick API Setup using Flask, intended for rapid project initiation.",
    url="https://github.com/zeddyemy/QUAS",
)
