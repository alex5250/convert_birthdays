# contacts-to-birthdays

A simple way to convert contact lists to birthdays. All docs are created with chatGPT and is amazing...

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You will need to have [Poetry](https://python-poetry.org/) installed on your machine in order to install the dependencies and run the project.

### Installing

To install the project, you can use the following command:

```
poetry install
```
This command will install all the dependencies listed in the `pyproject.toml` file.

### Running the project

To run the project, use the following command:

```
poetry run convert
```
This command will execute the `convert` script defined in the `pyproject.toml` file.

## Building the project

To build the project, use the following command:
```
./build.sh
```

This command will execute the `build.sh` file that will build the project and create the executable file in the `build` folder.

## Built With

* [Poetry](https://python-poetry.org/) - Dependency Management
* [beautifulsoup4](https://pypi.org/project/beautifulsoup4/) - Used to parse html and xml documents
* [ics](https://pypi.org/project/ics/) - Used to create ics files
* [xlrd](https://pypi.org/project/xlrd/) - Used to read excel files
* [xlwt](https://pypi.org/project/xlwt/) - Used to write excel files
* [openpyxl](https://pypi.org/project/openpyxl/) - Used to read and write excel files
* [pandas](https://pypi.org/project/pandas/) - Used to read and write excel files

## Authors

* **Alex Zasalvskis** - [alex5250](https://github.com/alex5250)
* **ChatGPT**

## License

This project is licensed under the MIT License - see the [LICENSE](https://chat.openai.com/LICENSE) file for details.

## Additional scripts

In addition to the `convert` script, the project also includes `version` and `build_docs` scripts that can be run using Poetry as well.

```
poetry run version
```

This command will execute the `version` script defined in the `pyproject.toml` file.

```
poetry run build_docs
```

This command will execute the `build_docs` script defined in the `pyproject.toml` file.
