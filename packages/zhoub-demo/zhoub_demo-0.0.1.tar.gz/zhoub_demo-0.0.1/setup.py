from setuptools import find_packages, setup

with open("README.md") as f:
    long_description = f.read()

setup(
    name="zhoub-demo",
    version="0.0.1",
    author="zhoubing",
    author_email="zhoubing19820720@163.com",
    description="test",
    long_description=long_description,
    url="",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3",
    install_requires=[],
    packages=find_packages(exclude=("tests",)),
    entry_points={
        'console_scripts': [
            'fib-number = test:test_hello',
        ],
    },
)
