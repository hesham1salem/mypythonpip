from setuptools import setup, find_packages

setup(
    name="my_project",
    version="0.1.0",
  #  entry_points={
   #     "console_scripts": [
    #        "my_command=my_project.main:main_function",
     #   ],
    #},
        scripts=["hello.sh"],  # Specify the binary to install
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

setup(
  
