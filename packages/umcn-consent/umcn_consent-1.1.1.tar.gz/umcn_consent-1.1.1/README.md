[![CI](https://github.com/ResearchBureau/umcn-consent/actions/workflows/build.yml/badge.svg)](https://github.com/ResearchBureau/umcn-consent/actions/workflows/build.yml)
[![PyPI](https://img.shields.io/pypi/v/umcn-consent)](https://pypi.org/project/umcn-consent/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/umcn-consent)](https://pypi.org/project/umcn-consent/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# UMCN-Consent
A Python layer for UMCN research usage consent systems.

## Installation

Install the module with PIP

```bash
  pip install umcn-consent
```
    
Before using this package, you need to set up a `.env` file in your project's root directory.
This file will store essential environment variables required for the package to function correctly.

### Setting up `.env` file
1. Create the `.env` file in the root directory
2. Add the following variables to the `.env` file
```dotenv
USER=your_username
PASSWORD=your_password
URL=your_service_url
CLIENT_ID=your_client_id
AUTH_TOKEN=your_auth_token 
```
3. Replace the placeholder values with actual credentials and information.
4. Secure your `.env` file. <b>DO NOT</b> commit the file to version control. Add it to you `.gitignore` file.

## Usage
After setting up the .env file, you can use the package as follows:

```python
import umcn_consent
```
For a more detailed example, see ```examples/example.py```
