# OEC-2021

## Project Structure:
### requirements.txt
Contains a list of all of the project dependencies (all of the libraries the project uses)
### main.py
Runs main project
### parseData.py
Takes care of loading data from the Excel file
### probabibilities.py
Module containing functions that calculate probabilities of virus transmission
### testProbabilities.py
Simple script to inspect the probabilities generated from normal conditions
### algorithm.py
Module that runs a simulation of virus spread throughout the school

## Usage:
### Clone repository
`git clone git@github.com:ksinger12/OEC-2021.git`
### Navigate to repository
`cd OEC-2021`
### Ensure Python and Pip are installed
### Create virtual environment
`python3 -m venv venv`
### Activate virtual environemnt
`source ./venv/bin/activate`
### Install dependencies
`pip3 install -r requirements.txt`
### Run program
`python3 main.py`
