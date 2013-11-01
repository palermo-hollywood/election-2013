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
        # Open the CSV
        general_csv = csv.DictReader(open(self.general_csv_path, 'r'))
        # Loop through the rows
        grouped_by_precinct = {}
        for row in general_csv:
            # And regroup them so each fake id is keyed to
            # all of the list totals for that precinct
            fake_id = "%s-%s" % (row['mesa_desde'], row['mesa_hasta'])
            try:
                grouped_by_precinct[fake_id][row['vot_parcodigo']] = row['total']
            except KeyError:
                grouped_by_precinct[fake_id] = {
                    row['vot_parcodigo']: row['total']
                }
        # Now loop through that
        outrows = []
        for fake_id, totals in grouped_by_precinct.items():
            # Figure out the overall total of votes
            overall_total = sum(map(int, totals.values()))
            # Rank the lists from highest to lowest votes
            ranking = sorted(
                totals.items(),
                key=lambda x:int(x[1]),
                reverse=True
            )
            # Pull out the leader and their vote total
            leader, leader_total = ranking[0]
            # Calculate their margin of victory over the second place list
            margin_of_victory = calculate.margin_of_victory([int(i[1]) for i in ranking])
            # Start up a row to print out
            outrow = [fake_id,]
            # Load in the lists in the same "alphabetical" order
            for list_, total in sorted(totals.items(), key=lambda x:x[0]):
                outrow.append(total)
            # Load in the extra stuff we've calculated
            outrow.append(leader)
            outrow.append(leader_total)
            outrow.append(margin_of_victory)
            # Add this row to the global list outside the loop
            outrows.append(outrow)
        # Open up a text file and write out all the data
        outcsv = csv.writer(open(self.outcsv_path, 'w'))
        outcsv.writerow(self.outheaders)
        outcsv.writerows(outrows)


if __name__ == '__main__':
    pftw = PalmeroFTW()
    #pftw.transform()
    pftw.merge()

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
