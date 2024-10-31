# Thinklabs Powerflow CLI

## Overview
`thinklabs-powerflow` is a command-line interface (CLI) tool designed to process energy data efficiently and is intended for ML based power flow analysis.

## Features
- **Interactive CLI:** Prompts the user for input through a user-friendly command-line interface.
- **Data Processing:** Reads, filters, and transforms CSV files containing P and Q data based on specific timestamp criteria. P is acvtive power, Q is  reactive power
- **API Integration:** Sends the processed data to an external API endpoint for inference requests.

## Installation

### Prerequisites
- Python 3.12 or higher
- Internet access for installing dependencies and making API requests

### Installing via pip
To install the latest version from [PyPI](https://pypi.org/):

```bash
pip install thinklabs-powerflow
