import argparse
import json
import ipaddress

def get_range(address):
    ip_address = ipaddress.ip_address(address)
    return str(ipaddress.ip_network(f"{ip_address}/{ip_address.max_prefixlen}", strict=False))

def parse(updown_data, json_file, ipver):
    data_list = []

    try:
        # Load existing data from the JSON file
        with open(json_file, 'r') as existing_file:
            data_list = json.load(existing_file)
    except FileNotFoundError:
        pass  # File doesn't exist yet, ignore and proceed with an empty list

    with open(updown_data, 'r') as file:
        updown_nodes = json.load(file)
        for node in updown_nodes:
            if not updown_nodes[node][ipver]:
                continue
            data_list.append({
                'ip_range': get_range(updown_nodes[node][ipver]),
                'country_code': updown_nodes[node]['countryiso'],
            })

        # Write the updated data back to the JSON file
        with open(json_file, 'w', encoding='utf-8') as json_file:
            json.dump(data_list, json_file, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("updown_data", help="path to the statuscake JSON file")
    parser.add_argument("json_file", help="path to output JSON file")
    parser.add_argument("ipver", help="IP version (ip or ipv6)")
    args = parser.parse_args()

    parse(args.updown_data, args.json_file, args.ipver)
