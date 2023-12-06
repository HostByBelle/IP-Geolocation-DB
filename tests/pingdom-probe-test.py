import xml.etree.ElementTree as ET
import maxminddb
import sys

def parse_xml(xml_file, geoip_db, ip_type):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    for item in root.findall('.//item'):
        ip_address = item.find(f'pingdom:{ip_type}', {'pingdom': 'http://www.pingdom.com/ns/PingdomRSSNamespace'}).text

        # Perform IP geolocation with MaxMind
        location_data = get_location_data(geoip_db, ip_address)
        print(f"Country: {location_data['country']}")
        print(f"City: {location_data['city']}")
        print(f"State: {location_data['state']}")

def get_location_data(geoip_db, ip_address):
    with maxminddb.open_database(geoip_db) as reader:
        try:
            location_data = reader.get(ip_address)
            return {
                'country': location_data['country']['iso_code'],
                'city': location_data.get('city', {}).get('names', {}).get('en', ''),
                'state': location_data.get('subdivisions', [{}])[0].get('names', {}).get('en', ''),
            }
        except Exception as e:
            print(f"Error retrieving location data for IP {ip_address}: {e}")
            return None

def main():
    if len(sys.argv) != 4:
        print("Usage: python script.py <path_to_xml_file> <path_to_geoip_db> <ip_type>")
        sys.exit(1)

    xml_file = sys.argv[1]
    geoip_db = sys.argv[2]
    ip_type = sys.argv[3]

    parse_xml(xml_file, geoip_db, ip_type)

if __name__ == "__main__":
    main()
