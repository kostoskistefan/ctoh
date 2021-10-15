from re import finditer
from argparse import ArgumentParser, SUPPRESS
from os.path import splitext, basename, dirname, join


def argument_parser() -> list:
    parser = ArgumentParser(
            description='Create header file from a source file', add_help=False)

    required = parser.add_argument_group('required arguments')
    optional = parser.add_argument_group('optional arguments')

    optional.add_argument(
        '-h',
        '--help',
        action='help',
        default=SUPPRESS,
        help='show this help message and exit'
    )

    required.add_argument('-i', '--input', required=True,
                        help='Path to the source file')

    optional.add_argument('-s', '--sort', required=False, action='store_true',
                        help='Sort the functions in the header file by length')

    optional.add_argument('-o', '--output', required=False,
                        help='Specify the full output path and filename for the generated header file')

    args = parser.parse_args()

    return {
        'input': args.input,
        'output': args.output,
        'sort': args.sort
    }


def get_functions_from_file(input_file: str, sort_flag: bool) -> list:
    functions = []

    with open(input_file, 'r') as source:
        code = source.read()
        matches = finditer('(.* .*\(.*\).*)[\r\n]{0,1}\{', code)
        for match in matches:
            functions.append(match.group(1) + ';')

    if sort_flag:
        functions.sort(key=len)

    return functions


def save_header_file(input_file: str, output_file: str, functions: list) -> None:
    output = splitext(input_file)[0] + '.h'

    if output_file:
        output = output_file

    with open(output, 'w') as header:
        include_guard_name = basename(output).upper() + '_H'

        header.write('#ifndef ' + include_guard_name + '\n')
        header.write('#define ' + include_guard_name + '\n\n')

        header.writelines('\n'.join(functions))

        header.write('\n\n')

        header.write('#endif')


def main(args: list):
    functions = get_functions_from_file(args['input'], args['sort'])
    save_header_file(args['input'], args['output'], functions)


if __name__ == '__main__':
    args = argument_parser()
    main(args)
