import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="Homie4 - Nex",
    version="0.3.3",
    description="Homie 4.0.0 Implementation",
    author="Michael Cumming - Edited by RJRIII",
    author_email="rromano@pdx.edu",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NEXGARDEN/homie4",
    keywords=["HOMIE", "MQTT"],
    packages=setuptools.find_packages(exclude=("test", "ARCHIVE",)),
    classifiers=[
        "Development Status :: 4 - Final Testing",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["paho-mqtt>=1.3.0", "netifaces>=0.10.6"],
)
