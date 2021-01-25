# OEC-2021

## About
The competition consisted of showing how a virus infecting Ontario would traverse through a high school in 1 day. The goal was to show the correlations between students, teachers, and TAs. Our program creates a simulation through each stage of the day as to how the virus is spreading through the school and the probability of someone contracting it.
For more information on the challenge, see the OEC 2021 Programming Competition Package.pdf file.

## Simulation
Each network represents the different classes, lunch groups (grade), and extra-curriculars the students are in and teachers are supervising. 

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
Module that runs the algorithm and creates different stages of the day to be visualized (contains code to output probability data to .txt)
### graph_experiments.py
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
`pip3 install -r requirement.txt`
### Run program
`python3 graph_experiments.py`
