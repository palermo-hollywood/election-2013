import csv
import json
import calculate
from pprint import pprint


class PalmeroFTW(object):
    """
    All the tricks we need to merge our data.
    """
    primary_csv_path = "./votos_establecimiento_caba_paso.csv"
    general_csv_path = "./votos_establecimiento_caba_octubre.csv"
    outheaders = [
        'fake_id', '187_total', '501_total', '502_total',
        '503_total', '505_total', '506_total',
        'leader', 'leader_total', 'margin_of_victory',
    ]
    outcsv_path = "merged_totals.csv"

    def transform(self):
        general_csv = csv.DictReader(open(self.general_csv_path, 'r'))
        grouped_by_precinct = {}
        for row in general_csv:
            fake_id = "%s-%s" % (row['mesa_desde'], row['mesa_hasta'])
            try:
                grouped_by_precinct[fake_id][row['vot_parcodigo']] = row['total']
            except KeyError:
                grouped_by_precinct[fake_id] = {
                    row['vot_parcodigo']: row['total']
                }
        grouped_by_precinct_with_totals = []
        outrows = []
        for fake_id, totals in grouped_by_precinct.items():
            overall_total = sum(map(int, totals.values()))
            ranking = sorted(
                totals.items(),
                key=lambda x:int(x[1]),
                reverse=True
            )
            leader, leader_total = ranking[0]
            margin_of_victory = calculate.margin_of_victory([int(i[1]) for i in ranking])
            outrow = [fake_id,]
            for list_, total in sorted(totals.items(), key=lambda x:x[0]):
                outrow.append(total)
            outrow.append(leader)
            outrow.append(leader_total)
            outrow.append(margin_of_victory)
            outrows.append(outrow)
        outcsv = csv.writer(open(self.outcsv_path, 'w'))
        outcsv.writerow(self.outheaders)
        outcsv.writerows(outrows)


if __name__ == '__main__':
    pftw = PalmeroFTW()
    pftw.transform()

"""
{'cartodb_id': '4842',
 'created_at': '2013-10-29 01:48:28.187051',
 'dne_distri': '1',
 'dne_seccio': '15',
 'id': '4842',
 'mesa_desde': '7326',
 'mesa_hasta': '7334',
 'the_geom': '',
 'total': '62',
 'updated_at': '2013-10-29 01:48:29.01991',
 'vot_parcodigo': '506',
 'votacion': 'VotosCandidaturaMesasDNacionales'}
"""
