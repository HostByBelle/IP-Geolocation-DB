import argparse
import re
import json

def extract_wk(hostname):
    match = re.match(r'^([a-zA-Z]+[0-9]+).*$', hostname)
    if match:
        return match.group(1)
    else:
        return None

def parse(file_path, json_file):
    data_list = []
    
    try:
        # Load existing data from the JSON file
        with open(json_file, 'r') as existing_file:
            data_list = json.load(existing_file)
    except FileNotFoundError:
        pass  # File doesn't exist yet, ignore and proceed with an empty list

    with open(file_path, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) >= 2:
                # Extract the hostname and IP address
                hostname = parts[0]
                ip_address = parts[1]
                wk = extract_wk(hostname)

                if hostname and ip_address and wk:
                    match wk:
                        case 'wk1':
                            data_list.append({
                                'ip_address': ip_address,
                                'country_code': 'US',
                                'city': 'New York'
                            })
                        case 'wk2':
                            data_list.append({
                                'ip_address': ip_address,
                                'country_code': 'US',
                                'city': 'San Francisco'
                            })
                        case 'wk3':
                            data_list.append({
                                'ip_address': ip_address,
                                'country_code': 'NL',
                                'city': 'Amsterdam'
                            })
                        case 'wk4':
                            data_list.append({
                                'ip_address': ip_address,
                                'country_code': 'GB',
                                'city': 'London'
                            })
                        case 'wk5':
                            data_list.append({
                                'ip_address': ip_address,
                                'country_code': 'DE',
                                'city': 'Frankfurt'
                            })
                        case 'wk6':
                            data_list.append({
                                'ip_address': ip_address,
                                'country_code': 'SG',
                                'city': 'Singapore'
                            })
                        case 'wk7':
                            data_list.append({
                                'ip_address': ip_address,
                                'country_code': 'US',
                                'city': 'Dallas'
                            })
                        case 'wk8':
                            data_list.append({
                                'ip_address': ip_address,
                                'country_code': 'AUS',
                                'city': 'Sydney'
                            })
                        case 'wk9':
                            data_list.append({
                                'ip_address': ip_address,
                                'country_code': 'BR',
                                'city': 'Sao Paulo'
                            })
                        case 'wk10':
                            data_list.append({
                                'ip_address': ip_address,
                                'country_code': 'JP',
                                'city': 'Tokyo'
                            })
                        case 'wk11':
                            data_list.append({
                                'ip_address': ip_address,
                                'country_code': 'IN',
                                'city': 'Mumbai'
                            })
                        case 'wk12':
                            data_list.append({
                                'ip_address': ip_address,
                                'country_code': 'PL',
                                'city': 'Warsaw'
                            })

        # Write the updated data back to the JSON file
        with open(json_file, 'w', encoding='utf-8') as json_file:
            json.dump(data_list, json_file, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", help="path to the file")
    parser.add_argument("json_file", help="path to output JSON file")
    args = parser.parse_args()

    parse(args.file_path, args.json_file)
