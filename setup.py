from setuptools import setup, find_packages

setup(
    name="typed-dataclass",
    version="0.1.0",
    author="Manuel Zierl",
    author_email="manuel.zierl@web.de",
    description="A decorator for Python dataclasses to enable runtime type checking.",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ManuelZierl/typed-dataclass",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=["typeguard", ],
)
