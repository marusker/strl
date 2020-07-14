import setuptools

setuptools.setup(
    name="strl",
    version="1.2",
    author="marusker",
    license='MIT',
    author_email="marusker@pst.sakura.ne.jp",
    description="strl keeps list like data at disk storage file insted of memory",
    long_description='strl is list like data storage. Compared to list, strl reduce memory usage and keeps the data after exit. Compared to sql strl is more easy and simple to use.',
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