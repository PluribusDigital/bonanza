import io
import unicodedata

import configargparse
import PyPDF2


def build_whitespace_replace():
    space = ord(' ')

    table = {
        0xa: None,
        0xd: None,
        0xa0: space,
        0x180e: space,
        0x202f: space,
        0x205f: space,
        0x3000: space,
        0xfeff: space
    }

    table.update({c: space for c in range(0x2000, 0x200b)})

    return table


def replace_characters(table, s, combine_whitespace=False):
    '''
    Using the translation tables, fix up a unicode string
    '''
    b = unicodedata.normalize('NFKD', s)
    s = b.translate(table)

    if combine_whitespace:
        return ' '.join(s.split())

    return s

# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------

def build_arg_parser():
    p = configargparse.ArgParser(prog='extract_pdf',
                                 description='extracts text from a PDF')
    g = p.add_argument_group('I/O')
    g.add('infile',
          help='the input file')
    g.add('outfile',
          help='the output file')

    return p


def main():
    # Get the arguments from the command line
    p = build_arg_parser()
    options = p.parse_args()

    read_pdf = PyPDF2.PdfFileReader(options.infile)

    table = build_whitespace_replace()

    with io.open(options.outfile, 'w', encoding='utf-8') as f:
        for i in range(read_pdf.getNumPages()):
            page = read_pdf.getPage(i)
            content = page.extractText()
            content = replace_characters(table, content, True)
            f.write(content)
            f.write('\n')

if __name__ == '__main__':
    main()
