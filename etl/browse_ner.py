import io
from collections import Counter, OrderedDict, defaultdict

import configargparse
import spacy
from spacy import displacy

ENTITY_TYPES = OrderedDict({
    'PERSON': 'People, including fictional.',
    'NORP': 'Nationalities or religious or political groups.',
    'FAC': 'Buildings, airports, highways, bridges, etc.',
    'ORG': 'Companies, agencies, institutions, etc.',
    'GPE': 'Countries, cities, states.',
    'LOC': 'Non-GPE locations, mountain ranges, bodies of water.',
    'PRODUCT': 'Objects, vehicles, foods, etc. (Not services.)',
    'EVENT': 'Named hurricanes, battles, wars, sports events, etc.',
    'WORK_OF_ART': 'Titles of books, songs, etc.',
    'LAW': 'Named documents made into laws.',
    'LANGUAGE': 'Any named language.',
    'DATE': 'Absolute or relative dates or periods.',
    'TIME': 'Times smaller than a day.',
    'PERCENT': 'Percentage, including ”%“.',
    'MONEY': 'Monetary values, including unit.',
    'QUANTITY': 'Measurements, as of weight or distance.',
    'ORDINAL': '“first”, “second”, etc.',
    'CARDINAL': 'Numerals that do not fall under another type.'
})

# Helper Methods

# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------

def build_arg_parser():
    p = configargparse.ArgParser(prog='browse_ner',
                                 description='explore the Named Entities')
    p.add('--visualize', action='store_true',
          help='show a color coded version of the named entities')
    g = p.add_argument_group('Processing')
    g.add('--model', default='en_core_web_sm',
          help='the statistical model to use for tokenizing and tagging')
    g = p.add_argument_group('I/O')
    g.add('infile',
          help='the input file')

    return p


def main():
    # Get the arguments from the command line
    p = build_arg_parser()
    options = p.parse_args()

    # Load a previous trained-model
    nlp = spacy.load(options.model)

    # Open a text file
    with io.open(options.infile, 'r', encoding='utf-8') as f:
        raw = f.read()

    # Process the raw text into a document
    doc = nlp(raw)

    # Get the entities
    tally = {x:Counter() for x in ENTITY_TYPES.keys()}
    for x in doc.ents:
        tally[x.label_].update([x.text])

    # Visualize
    if options.visualize:
        displacy.serve(doc, style='ent')
    else:
        for k,v in ENTITY_TYPES.items():
            print(k, v)
            print('=' * 80)
            for t,n in tally[k].most_common():
                print(t, n, sep='\t')
            print(' ')


if __name__ == '__main__':
    main()
