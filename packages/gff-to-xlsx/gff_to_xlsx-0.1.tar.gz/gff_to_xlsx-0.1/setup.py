from setuptools import setup

setup(
    name='gff_to_xlsx',
    version='0.1',
    py_modules=['gff_to_xlsx'],
    install_requires=['pandas', 'openpyxl'],
    entry_points={
        'console_scripts': [
            'gff_to_xlsx=gff_to_xlsx:main',
        ],
    },
    author="Emmanuel Agyare",
    author_email="your_email@example.com",
    description="A tool to convert GFF files to Excel (XLSX) format.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    # url="https://your_project_url.com",  # Optional, add your project URL here
)
