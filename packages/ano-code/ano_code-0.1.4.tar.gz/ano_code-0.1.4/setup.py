from setuptools import setup, find_packages



def read_requirement():
    with open("./requirements.txt") as f:
        requirements = f.readlines()
    return requirements


setup(
    name="ano-code",
    version="0.1.4",
    packages=find_packages(),
    include_package_data=True,
    # install_requires=open("requirements.txt").read().splitlines(),
    entry_points='''
    [console_scripts]
    ano-code=auto_code.cli:cli
    ''',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    
)
