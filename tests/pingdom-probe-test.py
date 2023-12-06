import argparse
import xml.etree.ElementTree as ET
import maxminddb

PINGDOM_NAMESPACE = 'http://www.pingdom.com/ns/PingdomRSSNamespace'

def parse_xml(xml_file, geoip_db, ip_type):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    total = 0
    totalCovered = 0
    totalWrong = 0

    with maxminddb.open_database(geoip_db) as reader:
        for item in root.findall('.//item'):
            ip_address_element = item.find(f'pingdom:{ip_type}', {'pingdom': PINGDOM_NAMESPACE})
            if(ip_address_element is None):
                continue
            ip_address= ip_address_element.text
            country_element = item.find('pingdom:country', {'pingdom': PINGDOM_NAMESPACE})
            country_code = country_element.attrib.get('code', '')

            total+=1

            location_data = get_location_data(reader, ip_address)

            if(country_code and location_data and location_data['country']):
                totalCovered+=1
                if(country_code != location_data['country']):
                    totalWrong+=1

    if(total and totalCovered):
        accuracy = 100 - round(totalWrong / totalCovered * 100, 2)
        coverage = round(totalCovered / total * 100, 2)
        print(f"Covered {totalCovered}/{total} of tested IP addresses ({coverage}%). It got {totalWrong} wrong for a overall accuracy of {accuracy}%")
    else:
        print(f"Does not contain the needed info to perform the Pingdom test")

def get_location_data(reader, ip_address):
    try:
        location_data = reader.get(ip_address)
        return {
            'country': location_data['country']['iso_code'],
            'city': location_data.get('city', {}).get('names', {}).get('en', ''),
        }
    except Exception as e:
        return None

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("xml_file", help="path to XML file")
    parser.add_argument("geoip_db", help="path to GeoIP database")
    parser.add_argument("ip_type", help="type of IP address")
    args = parser.parse_args()

    parse_xml(args.xml_file, args.geoip_db, args.ip_type)

if __name__ == "__main__":
    main()
