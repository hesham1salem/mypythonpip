from setuptools import setup, find_packages

setup(
    name="my_project",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "some_dependency>=1.0",
        "another_dependency==2.1"
    ],
    entry_points={
        "console_scripts": [
            "my_command=my_project.main:main_function",
        ],
    },
    description="A brief description of your project",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/your_username/my_project",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
