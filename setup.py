import setuptools

setuptools.setup(
    name="strl",
    version="1.0",
    author="marusker",
    author_email="marusker@pst.sakura.ne.jp",
    description="storage list holds list like data at disk storage file insted of memory",
    long_description='compared to list, strl reduce memory usage and store the data after exit',
    long_description_content_type="text/markdown",
    url="https://github.com/marusker/strl",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
)