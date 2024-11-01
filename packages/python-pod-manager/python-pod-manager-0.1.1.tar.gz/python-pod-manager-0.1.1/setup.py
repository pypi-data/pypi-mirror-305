from setuptools import setup, find_packages

setup(
    name="python-pod-manager",
    version="0.1.1",
    author="Hakan İSMAİL",
    author_email="hakanismail53@gmail.com",
    description="A pod manager for version dependency python projects.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://gitlab.com/hakanismail53/python-pod-manager",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "pyyaml",
    ],
)
