import argparse
import json
import maxminddb
import pycountry
import ipaddress
import time

def get_location_data(reader, ip_address):
    try:
        location_data = reader.get(ip_address)
        return {
            'country': location_data['country']['iso_code'],
            'city': location_data.get('city', {}).get('names', {}).get('en', ''),
        }
    except Exception as e:
        return None

def convert_to_2_letter_code(three_letter_code):
    try:
        country = pycountry.countries.get(alpha_3=three_letter_code)
        if country:
            return country.alpha_2
        else:
            return "Not found"
    except Exception as e:
        print(f"Error: {e}")
        return None

def get_ip_list(cidr):
    network = ipaddress.ip_network(cidr, strict=False)
    step = max(1, network.num_addresses // 15000) # 10k max IPs per CIDR
    return range(int(network[0]), int(network[-1]), step)

def perform_test(json_file, geoip_db):
    start_time = time.time()

    with open(json_file, 'r', encoding='utf-8') as json_file:
        data_list = json.load(json_file)

    total = 0
    total_covered = 0
    total_wrong = 0

    with maxminddb.open_database(geoip_db) as reader:
        for data in data_list:
            country_code = data['country_code']
            ip_list = get_ip_list(data['ip_range'])
            
            for int_ip_address in ip_list:
                ip_address = ipaddress.ip_address(int_ip_address)
                total += 1
                location_data = get_location_data(reader, ip_address)
                
                if country_code and location_data and location_data.get('country'):
                    total_covered += 1
                    
                    if len(country_code) == 3:
                        country_code = convert_to_2_letter_code(country_code)

                    if len(location_data['country']) == 3:
                        location_data['country'] = convert_to_2_letter_code(location_data['country'])

                    if country_code.lower() != location_data['country'].lower():
                        total_wrong += 1

    end_time = time.time()
    elapsed_time = end_time - start_time

    if total and total_covered:
        accuracy = 100 - round(total_wrong / total_covered * 100, 2)
        coverage = round(total_covered / total * 100, 2)
        print(f"Covered {total_covered:,}/{total:,} ({coverage}%) IP addresses. Got {total_wrong:,} wrong for an overall accuracy of {accuracy}%. Took {elapsed_time:.2f} seconds")
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
