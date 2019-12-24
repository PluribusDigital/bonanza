# Installation instructions

## System Dependencies

1. Python 3
1. Virtual Environments

    ```
    pip install virtualenv virtualenv-clone virtualenvwrapper
    ```

## Installing the application

This should only need to be performed once

```bash
# Clone the project from github
git clone <TBD>
cd bonanza
source ./activate-virtualenv.sh
workon bonanza
pip install -r requirements.txt
```

#### Create a place for the documents

By default, Bonanza will not include documents in the `/confidential` folder.

```
mkdir confidential
```

## Load the text models

I think this is only needed once?

`python -m spacy download en_core_web_sm`
