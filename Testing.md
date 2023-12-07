# Database Testing

We are looking for more available data sources to use for testing. The data must be programmatically parse-able, easily accessible, and not reliant on external databases. (Meaning, it can't be another geolocation database.)

Best case scenario are where companies self-publish a list of their IP address and locations as this can be considered a know-good data source.

## Data sources utilized

- [Pingdom probe server data](https://www.pingdom.com/rss/probe_servers.xml)
  - IP address types: `IPv4`, `IPv6`
  - Data available: `Country code`, `Country name`, `City`, `Region`
- [Hetrix Monitoring IPs](https://docs.hetrixtools.com/uptime-monitoring-ip-addresses/)
  - IP address types: `IPv4`
  - Data available: `Country code`, `City`
- [Updown.io Monitoring IPs](https://updown.io/api/nodes)
  - IP address types: `IPv4`, `IPv6`
  - Data available: `Country code`, `City`, `Latitude`, `Longitude`
- [AWS IP Address Ranges](https://ip-ranges.amazonaws.com/ip-ranges.json)
  - IP address types: `IPv4`, `IPv6`
  - Data available: `Country code`
- [Oracle Cloud IP Address Ranges](https://docs.oracle.com/en-us/iaas/tools/public_ip_ranges.json) 
	- IP address types: `IPv4`
	- Data available: `Country code`

## Automated testing

Each release will automatically be run through testing an the results will be attached as the release body.
Presently only Country data is tested as we don't have a source for ASN data to test and the current databases don't provide City data.

### GeoLite2-Country Testing Result

For those who are curious how the public domain databases compare to the MaxMind GeoLite2 database, here's how their databases perform in the tests:

**Last updated:** 12/06/2023

- IPv4: `Covered 8,534,785/8,535,035 (100.0%) IP addresses. Got 328,462 wrong for an overall accuracy of 96.15%. Took 56.19 seconds`
- IPv6: `Covered 9,912,218/9,912,218 (100.0%) IP addresses. Got 410,088 wrong for an overall accuracy of 95.86%. Took 72.35 seconds`
