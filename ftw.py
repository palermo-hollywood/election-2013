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
    location_json_path = "./locales_caba_paso2013.geojson"
    outheaders = [
        'fake_id', '187_total', '501_total', '502_total',
        '503_total', '505_total', '506_total',
        'leader', 'leader_total', 'margin_of_victory',
    ]
    outcsv_path = "merged_totals.csv"
    outjson_path = "merged_totals.geojson"

    def merge(self):
        """
        Merge the transformed csv file with the geojson with all
        the voting locations.
        """
        # Open raw geojson
        json_data = open(self.location_json_path, "rb").read()
        # Get it in Python
        json_data = json.loads(json_data)
        # Create list for stuff after we merge
        merged_features = []
        # Open the csv with results
        csv_data = csv.DictReader(open(self.outcsv_path, 'r'))
        # Key it by ID
        csv_data = dict((
            i['fake_id'], i
        ) for i in csv_data)
        # Loop through the features
        for row in json_data['features']:
            # Figure out each fake id
            fake_id = "%s-%s" % (
                row['properties']['mesa_desde'],
                row['properties']['mesa_hasta']
            )
            # Filter it down to the data we want to keep
            merged_dict = {
                'geometry': row['geometry'],
                'id': row['id'],
                'properties': {
                    'direccion': row['properties']['direccion'],
                    'establecim': row['properties']['establecim'],
                }
            }
            # Add in the results data
            merged_dict['properties'].update(csv_data[fake_id])
            # Toss it in the global list
            merged_features.append(merged_dict)
        # Structure out new merged JSON
        new_json = {
            'type': json_data['type'],
            'features': merged_features
        }
        # Write it out to a file
        outjson = open(self.outjson_path, "wb")
        outjson.write(json.dumps(new_json))

    def transform(self):
        """
        Transform the results file so that there is only one row
        for each precinct, with some summary stats calculated.
        """
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
{u'geometry': {u'coordinates': [-58.496182, -34.590793], u'type': u'Point'},
 u'id': 5443,
 u'properties': {u'cant_mesas': u'9',
                 u'cartodb_id': 807,
                 u'circuito': u'167',
                 u'codigo_dis': u'1',
                 u'codigo_pos': u'',
                 u'created_at': u'2013-08-12T00:10:49Z',
                 u'direccion': u'TERRADA 3983',
                 u'distrito': u'CAPITAL FEDERAL',
                 u'dne_distri': 1,
                 u'dne_seccio': 15,
                 u'establecim': u'ESC N\xba4 CNEL ALVAREZ THOMAS',
                 u'id': 5443,
                 u'localidad': u'CAP FED',
                 u'mesa_desde': 7326,
                 u'mesa_hasta': 7334,
                 u'seccion': u'15',
                 u'updated_at': u'2013-08-12T00:11:40Z'},
"""
