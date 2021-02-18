import copy
import csv
#from loguru import logger
#from VarDBapp import models # need this?
import re
import warnings

variant_file = 'brca1_vars.csv'

class CSVParser():

    def __init__(self):
        self.variant_file = variant_file
        self.sequencers = ['Miseq', 'Hiseq']

    def csv_reader(self):
        """
        This function parses the variant data from the uploaded csv_file into a dictionary
        :return:
        """
        with open(self.variant_file, 'r') as csv_file:
            csv_lines = csv_file.readlines()
            csv_dicts = csv.DictReader(csv_lines)
        return csv_dicts

    def process_bools(self, dictionary, key):
        if key == 'Proband' or key == 'Affected Relatives':
            if dictionary[key] == 'Y':
                dictionary[key] = True
            elif dictionary[key] == 'N':
                dictionary[key] == False
        return dictionary

    def check_values(self, dictionary, key):
        """
        This function needs fixing - lower priority than getting the data in
        """
        if key == 'Sequencer':
            if dictionary[key] not in self.sequencers:
                raise warnings
                # Want to add functionality to check if it's an error with the cases
        elif key == 'SampleID':
            episode_pattern = re.compile("20[0-9]{2}_[0-9]*")
            if not re.match(episode_pattern, dictionary[key]):
                raise warnings
        # Check cDNA begins with c.
        # Check genome begins with g.
        # Check gene name only includes letters and numbers

    def split_evidence(self, dictionary, key):
        """
        Split the evidence codes into a list and checks evidence codes are valid
        """
        evidence_list = []
        if key == 'Evidence Codes':
            dictionary[key] = dictionary[key].split(',')
            for code in dictionary[key]:
                print(code)
                code_pattern = re.compile("[PB]V?[MSP][1-7]")
                if not re.match(code_pattern, code):
                    raise warnings
        return dictionary

    def add_variants(self):
        """
        This function adds the results to the ? table(s)
        """
        
        pass

    def main(self):
        csv_dicts = self.csv_reader()
        for dictionary in csv_dicts:
            for key in dictionary:
                dictionary[key] = dictionary[key].strip()
                dictionary = self.process_bools(dictionary, key)
                dictionary = self.split_evidence(dictionary, key)
            break


if __name__ == "__main__":
    csv_parser_runner = CSVParser()
    csv_parser_runner.main()