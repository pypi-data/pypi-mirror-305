from setuptools import setup, find_packages

setup(
    name="productivity-timer",
    version="1.0.2",
    packages=find_packages(), 

    description="A timer library for managing multiple timers for multiple individuals.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Abhishek",
    author_email="abhishekshivtiwari@gmail.com",
    url='https://github.com/Abhi-shekes/productivity-timer', 
    python_requires=">=3.6",
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",

        "Operating System :: OS Independent",
    ],
)


