# Swisscard PDF Convert

This is a simple utility to convert the Swisscard statement PDF to a QIF file, since they removed the ability to export statement data to machine readable data formats in the migration to the new app.

## Installation

Clone the repo and run
```bash
pip install -r requirements.txt
```
to install dependencies

## Usage
Run
```bash
python convert.py statement.pdf
```
to convert your PDF statement to QIF compatible text. To save to a file use
```bash
python convert.py statement.pdf > statement.qif
```
