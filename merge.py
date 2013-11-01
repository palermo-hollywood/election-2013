import csv
import json


class PalmeroFTW(object):
    """
    All the tricks we need to merge our data.
    """
    primary_csv_path = "./votos_establecimiento_caba_paso.csv"
    general_csv_path = "./votos_establecimiento_caba_octubre.csv"

    def transform(self):
        general_csv = csv.DictReader(open(self.general_csv_path, 'r'))
        for row in general_csv:
            print row


if __name__ == '__main__':
    pftw = PalmeroFTW()
    pftw.transform()
