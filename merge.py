import csv
import json


class PalmeroFTW(object):
    """
    All the tricks we need to merge our data.
    """
    primary_csv_path = "./votos_establecimiento_caba_paso.csv"
    general_csv_path = "./votos_establecimiento_caba_octubre.csv"

    def transform(self):
        self.transform_primary()

    def transform_primary(self):
        primary_csv = csv.DictReader(open(self.primary_csv_path, 'r'))
        for row in primary_csv:
            print row


if __name__ == '__main__':
    pftw = PalmeroFTW()
    pftw.transform()
