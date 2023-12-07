import argparse
import json
from progressbar import progressbar
from pprint import pprint

def parse(updown_data, json_file, ipver):
    data_list = []

    try:
        # Load existing data from the JSON file
        with open(json_file, 'r') as existing_file:
            data_list = json.load(existing_file)
    except FileNotFoundError:
        pass  # File doesn't exist yet, ignore and proceed with an empty list

    with open(updown_data, 'r') as file:
        aws_ips = json.load(file)
        for prefix in progressbar(aws_ips['prefixes']):
            prefix_key = ipver + '_prefix'
            if(prefix[prefix_key]):
                data_list.append({
                    'ip_range': prefix[prefix_key],
                    'country_code': 'US',
                    'city': 'Test'
                })
        #print(f"Completed prefix: {prefix[prefix_key]}")

        # Write the updated data back to the JSON file
        #with open(json_file, 'w', encoding='utf-8') as json_file:
            #json.dump(data_list, json_file, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("updown_data", help="path to the aws ranges JSON file")
    parser.add_argument("json_file", help="path to output JSON file")
    parser.add_argument("ipver", help="IP version (ip or ipv6)")
    args = parser.parse_args()

    parse(args.updown_data, args.json_file, args.ipver)
