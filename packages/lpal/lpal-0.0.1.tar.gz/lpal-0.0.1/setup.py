from setuptools import setup, find_packages

setup(
    name="lpal",
    version="0.0.1",
    author="Brendan Ruskey",
    author_email="bjr221@lehigh.edu",
    description="An open-source tools for teaching the solution of mixed-integer linear programs",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/rusk-ey/lpal",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "numpy"
    ],
)
