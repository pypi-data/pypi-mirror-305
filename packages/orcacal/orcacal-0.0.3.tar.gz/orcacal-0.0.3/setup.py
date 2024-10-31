import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="orcacal",
    version="0.0.3",
    author="hty2dby",
    author_email="hty@hty.ink",
    description="test",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HTY-DBY/pyORCA",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
