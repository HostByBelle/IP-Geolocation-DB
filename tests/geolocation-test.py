import argparse
import json
import maxminddb

def get_location_data(reader, ip_address):
    try:
        location_data = reader.get(ip_address)
        return {
            'country': location_data['country']['iso_code'],
            'city': location_data.get('city', {}).get('names', {}).get('en', ''),
        }
    except Exception as e:
        return None

def perform_test(json_file, geoip_db):
    with open(json_file, 'r', encoding='utf-8') as json_file:
        data_list = json.load(json_file)

    total = 0
    total_covered = 0
    total_wrong = 0

    with maxminddb.open_database(geoip_db) as reader:
        for data in data_list:
            total += 1

            country_code = data['country_code']
            ip_address = data['ip_address']

            location_data = get_location_data(reader, ip_address)

            if country_code and location_data and location_data.get('country'):
                total_covered += 1
                if country_code != location_data['country']:
                    total_wrong += 1

    if total and total_covered:
        accuracy = 100 - round(total_wrong / total_covered * 100, 2)
        coverage = round(total_covered / total * 100, 2)
        print(f"Covered {total_covered}/{total} ({coverage}%) IP addresses. Got {total_wrong} wrong for an overall accuracy of {accuracy}%")
    else:
        print("Does not contain the needed info to perform this test")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("json_file", help="path to input JSON file")
    parser.add_argument("geoip_db", help="path to GeoIP database")
    args = parser.parse_args()

    perform_test(args.json_file, args.geoip_db)

if __name__ == "__main__":
    main()
