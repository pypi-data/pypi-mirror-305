from setuptools import setup, find_packages

setup(
    name="JoelAntony_LibraryManager_BPS_Doha",
    version='2.0.0',
    packages=find_packages(),
    description = ("A tool for managing library operations such as book registration, issuance, and return with a Tkinter-based GUI for an enhanced user experience."),
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Joel Varghese Antony',
    author_email='joelantony30101@gmail.com',  
    url='',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
