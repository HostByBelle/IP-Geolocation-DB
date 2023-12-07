import argparse
import re
import json
import ipaddress

wk_mapping = {
    'wk1': {
        'country_code': 'US',
        'city': 'New York'
    },
    'wk2': {
        'country_code': 'US',
        'city': 'San Francisco'
    },
    'wk3': {
        'country_code': 'NL',
        'city': 'Amsterdam'
    },
    'wk4': {
        'country_code': 'GB',
        'city': 'London'
    },
    'wk5': {
        'country_code': 'DE',
        'city': 'Frankfurt'
    },
    'wk6': {
        'country_code': 'SG',
        'city': 'Singapore'
    },
    'wk7': {
        'country_code': 'US',
        'city': 'Dallas'
    },
    'wk8': {
        'country_code': 'AUS',
        'city': 'Sydney'
        },
    'wk9': {
        'country_code': 'BR',
        'city': 'Sao Paulo'
    },
    'wk10': {
        'country_code': 'JP',
        'city': 'Tokyo'
    },
    'wk11': {
        'country_code': 'IN',
        'city': 'Mumbai'
    },
    'wk12': {
        'country_code': 'PL',
        'city': 'Warsaw'
    }
}

def get_range(address):
    ip_address = ipaddress.ip_address(address)
    return str(ipaddress.ip_network(f"{ip_address}/{ip_address.max_prefixlen}", strict=False))

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
            match = re.match(r'^(\S+)\s+(\S+)', line)
            if match:
                hostname = match.group(1)
                ip_address = match.group(2)
                wk = extract_wk(hostname)

                if hostname and ip_address and wk:
                    if wk in wk_mapping:
                        data_list.append({
                            'ip_range': get_range(ip_address),
                            **wk_mapping[wk]
                        })
                    else:
                        print(f"{wk} is not yet mapped")

        # Write the updated data back to the JSON file
        with open(json_file, 'w', encoding='utf-8') as json_file:
            json.dump(data_list, json_file, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", help="path to the file")
    parser.add_argument("json_file", help="path to output JSON file")
    args = parser.parse_args()

    parse(args.file_path, args.json_file)
