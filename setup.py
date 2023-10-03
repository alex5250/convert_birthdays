from setuptools import setup, find_packages

setup(
    name='contacts_to_birthdays',
    version='0.1.0',
    author='Alex Zaslavskis',
    author_email='sahsariga111@gmail.com',
    description='Awesome .vcf/instagram birthday converter.',
    packages=find_packages(),
    install_requires=[
        'datetime',
        'pandas',
        'xlwt',
        'beautifulsoup4',
        'python-dateutil',
        'ics'
    ],
    entry_points={
        'console_scripts': ['contacts_to_birthdays = contacts_to_birthdays.main:main'],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12'
    ],
)
