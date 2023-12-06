import xml.etree.ElementTree as ET
import maxminddb
import sys

def parse_xml(xml_file, geoip_db, ip_type):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    total = 0
    totalWrong = 0

    for item in root.findall('.//item'):
        # First we need to extract the needed data from Pingdom's feed
        ip_address = item.find(f'pingdom:{ip_type}', {'pingdom': 'http://www.pingdom.com/ns/PingdomRSSNamespace'}).text
        country_element = item.find('pingdom:country', {'pingdom': 'http://www.pingdom.com/ns/PingdomRSSNamespace'})
        country_code = country_element.attrib.get('code', '')
        #city = item.find('pingdom:country', {'pingdom': 'http://www.pingdom.com/ns/PingdomRSSNamespace'}).text


        # Then pull the associated data from the database
        location_data = get_location_data(geoip_db, ip_address)

        # And finally, valdiate that they are correct
        if(country_code and location_data and location_data['country']):
            total+=1
            if(country_code != location_data['country']):
                # TODO: Do I want to record the addresses that were wrong?
                #print(f"{ip_address} Should be in {country_code}, but was instead responded as {location_data['country']}")
                totalWrong+=1

    if(total):
        accuracy = 100 - round(totalWrong / total * 100, 2)
        print(f"- Out of {total} Pingdom IP addreses tested, this database failed {totalWrong} for a total accuracy of {accuracy}%")
    else:
        print(f"- This database does not contain the neded info to perform the Pingdom test")

def get_location_data(geoip_db, ip_address):
    with maxminddb.open_database(geoip_db) as reader:
        try:
            location_data = reader.get(ip_address)
            return {
                'country': location_data['country']['iso_code'],
                'city': location_data.get('city', {}).get('names', {}).get('en', ''),
            }
        except Exception as e:
            #TODO: Cleanly handle cases where the DB does not contain the info we are looking for
            #print(f"- Error retrieving location data for IP {ip_address}: {e}")
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
