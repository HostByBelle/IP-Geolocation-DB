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

## Automated testing

Each release will automatically be run through testing an the results will be attached as the release body.
Presently only Country data is tested as we don't have a source for ASN data to test and the current databases don't provide City data.

### GeoLite2-Country Testing Result

For those who are curious how the public domain databases compare to the MaxMind GeoLite2 database, here's how their databases perform in the tests:

**Last updated:** 12/06/2023

- IPv4: `Covered 115/116 (99.14%) IP addresses. Got 1 wrong for an overall accuracy of 99.13%`
- IPv6: `Covered 67/67 (100.0%) IP addresses. Got 5 wrong for an overall accuracy of 92.54%`
