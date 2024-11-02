from setuptools import setup, find_packages

setup(
    name="mysqlonsocket",
    version='0.0.1',
    author="VedantBarhate",
    author_email="vedant.barhate27@gmail.com",
    description="A module which helps you use your MySQL database over local network by connecting another devices.",
    packages=find_packages(),
    install_requires=['mysql.connector', 'cryptography'],
    keywords=['python', 'socket', 'sockets', 'mysql', 'sql', 'database', 'server-client', 'sql remote user'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ]
)
