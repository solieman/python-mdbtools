"""
mdbtools
Tools to facilitate the use of Microsoft Access databases
Install from
https://formulae.brew.sh/formula/mdbtools
GutHub source:
https://github.com/brianb/mdbtools/
install command:
brew install mdbtools
"""
import sys
import argparse
import subprocess
import pandas as pd


def get_tables(path):
    """
    Return an array of tables names for the .mdb file
    """
    try:
        tables = subprocess.check_output(['mdb-tables', path])
        list_of_tables = tables.decode().split(' ')
        list_of_tables.remove('\n')
        return list_of_tables
    except:
        return ("Error: No Database found in the file %s" % path)


def get_table_data(path, table):
    """
    Return the table data
    """
    tables = subprocess.check_output(["mdb-export", path, table])
    return tables.decode().split('\n')


def convert_df(path, table):
    """
    Return the table as pandas dataframe
    """
    temp_data_holder = get_table_data(path, table)
    columns = temp_data_holder[0].split(',')
    data = [i.split(',') for i in temp_data_holder[1:]]
    data_frame = pd.DataFrame(columns=columns, data=data)
    return data_frame


def get_table_content(file_path, table_name):
    print('table_name: ', table_name)
    new_df = convert_df(file_path, table_name)
    return new_df


def export_to_csv(file_path, table_name):
    temp_df = get_table_content(file_path, table_name)
    temp_df.to_csv(table_name + '.csv', index=False)


# '/Users/mindvalley/Downloads/DataSet1_2/Vault010320201.mdb'
def main(args):
    """
        Get the file path and return list of tables in the Database file
    """
    print('args: ', args)
    print('args: ', args['file'])
    print('args: ', args['table'])
    print('args: ', args['csv'])

    file_path = args['file'][0]
    tables_names = get_tables(file_path)
    print(tables_names)
    if args['csv']:
        if args['table']:
            export_to_csv(file_path, args['table'][0])
        else:
            for table in tables_names:
                export_to_csv(file_path, table)
    if args['table']:
        for table_name in args['table']:
            temp_df = get_table_content(file_path, table_name)
            print(temp_df.head())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', '-f', nargs='*', help='path to the file')
    parser.add_argument('--table', '-t', nargs='*', help='table name to display', default=None)
    parser.add_argument('--csv', action='store_true', help='export table to csv file', default=None)
    args_namespace = parser.parse_args()
    print('args_namespace ', args_namespace)
    print('args.csv ', args_namespace.csv)
    args = vars(args_namespace)
    main(args)
