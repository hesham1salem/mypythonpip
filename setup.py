import os
import sys
from setuptools import setup
from setuptools.command.install import install

# Custom command to ensure hello.sh is executable
class PostInstallCommand(install):
    def run(self):
        # Run the standard install command
        install.run(self)

        # Set the executable permission for hello.sh after installation
        script_path = os.path.join(self.install_scripts, 'hello.sh')
        
        if os.path.exists(script_path):
            print(f"Setting executable permission for {script_path}")
            os.chmod(script_path, 0o755)  # chmod +x
        else:
            print(f"Script {script_path} not found.")

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
     cmdclass={
        'install': PostInstallCommand,  # Use the custom install command
    },
)

  
