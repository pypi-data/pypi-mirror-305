from setuptools import setup, find_packages


# Function to read the requirements.txt file
def read_requirements():
    with open("requirements.txt") as f:
        return f.read().splitlines()


setup(
    name="tree-ring-analyzer",
    version="0.1.0",
    description="A package for tree ring detection in images",
    author="Tony Meissner",
    author_email="tonymeissner70@@gmail.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=read_requirements(),
    entry_points={
        "console_scripts": [
            "tree-ring-analyzer=main:main",
        ],
    },
    python_requires=">=3.7",
)
