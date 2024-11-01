from setuptools import setup, find_packages

setup(
    name="MCC_Linux_driver", 
    version="0.1.6",  
    author='S Ghodke',
    author_email="sghodke@ncsu.edu",
    description='Linux Drivers for MCC',
    url='https://github.com/nuttysunday/Linux_Drivers', 
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[
        "libusb1",
        "usb1",
        "pyusb",
        "hidapi", 
        "pybluez",  
    ],
)