import argparse
import json

# Manually gathered from https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RegionsAndAvailabilityZones.html
# It's somewhat incomplete, though so some info was gathered via google and educated guesses.
region_info = {
    'us-east-1': {
        'country_code': 'US',
    },
    'us-east-2': {
        'country_code': 'US',
    },
    'us-west-1': {
        'country_code': 'US',
    },
    'us-west-2': {
        'country_code': 'US',
    },
    'af-south-1': {
        'country_code': 'ZA',
    },
    'ap-east-1': {
        'country_code': 'HK',
    },
    'ap-south-2': {
        'country_code': 'IN',
    },
    'ap-southeast-3': {
        'country_code': 'ID',
    },
    'ap-southeast-4': {
        'country_code': 'AU',
    },
    'ap-south-1': {
        'country_code': 'IN',
    },
    'ap-northeast-3': {
        'country_code': 'JP',
    },
    'ap-northeast-2': {
        'country_code': 'KR',
    },
    'ap-southeast-1': {
        'country_code': 'SG',
    },
    'ap-southeast-2': {
        'country_code': 'AU',
    },
    'ap-northeast-1': {
        'country_code': 'JP',
    },
    'ca-central-1': {
        'country_code': 'CA',
    },
    'eu-central-1': {
        'country_code': 'DE',
    },
    'eu-west-1': {
        'country_code': 'IE',
    },
    'eu-west-2': {
        'country_code': 'GB',
    },
    'eu-south-1': {
        'country_code': 'IT',
    },
    'eu-west-3': {
        'country_code': 'FR',
    },
    'eu-south-2': {
        'country_code': 'ES',
    },
    'eu-north-1': {
        'country_code': 'SE',
    },
    'eu-central-2': {
        'country_code': 'CH',
    },
    'il-central-1': {
        'country_code': 'IL',
    },
    'me-south-1': {
        'country_code': 'BH',
    },
    'me-central-1': {
        'country_code': 'AE',
    },
    'sa-east-1': {
        'country_code': 'BR',
    },
    'us-gov-east-1': {
        'country_code': 'US',
    },
    'us-gov-west-1': {
        'country_code': 'US',
    },
    'ca-west-1': {
        'country_code': 'CA',
    },
    'cn-northwest-1': {
        'country_code': 'CN',
    },
    'cn-north-1': {
        'country_code': 'CN',
    },
    'ap-southeast-5': { #https://www.netify.ai/resources/networks/amazon-aws/pop/ap-southeast-5
        'country_code': 'ZN',
    },
}

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
        if ipver == 'ipv6':
            prefixes = aws_ips['ipv6_prefixes']
        else:
            prefixes = aws_ips['prefixes']

        for prefix in prefixes:
            prefix_key = ipver + '_prefix'
            if prefix_key in prefix and prefix[prefix_key]:
                if prefix['region'] in region_info:
                    data_list.append({
                        'ip_range': prefix[prefix_key],
                        **region_info[prefix['region']]
                    })
                else:
                    if prefix['region'] != 'GLOBAL':
                        print(f"{prefix['region']} is not yet mapped")

        # Write the updated data back to the JSON file
        with open(json_file, 'w', encoding='utf-8') as json_file:
            json.dump(data_list, json_file, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("updown_data", help="path to the AWS ranges JSON file")
    parser.add_argument("json_file", help="path to output JSON file")
    parser.add_argument("ipver", help="IP version (ip or ipv6)")
    args = parser.parse_args()

    parse(args.updown_data, args.json_file, args.ipver)
