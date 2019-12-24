# Bonanza!

A quick prototype to see about digging through contracts

## Installation

Please see [the installation guide](INSTALL.md)

## Running

Assuming there are files in the `confidential` folder

```
# Turn the PDF into text
#  Each line is one page of text from the PDF
python -m etl.extract_pdf confidential/<SOME_NAME>.pdf confidential/<SOME_NAME>.txt

# Extract the Proper Nouns
python -m etl.browse_ner confidential/<SOME_NAME>.txt

# View the proper nouns in a color-coded format
python -m etl.browse_ner --visualize confidential/<SOME_NAME>.txt
http://localhost:5000
```
