# Database Testing

Test data comes from the [ip-db-test-data](https://github.com/HostByBelle/ip-db-test-data) GitHub repository.

## Automated testing

Each release will automatically be run through testing an the results will be attached as the release body.

### GeoLite2-Country Testing Result

For those who are curious how the public domain databases compare to the MaxMind GeoLite2 database, here's how their databases perform in the tests:

**Last updated:** 12/06/2023

- IPv4: `Covered 8,534,785/8,535,035 (100.0%) IP addresses. Got 328,462 wrong for an overall accuracy of 96.15%. Took 56.19 seconds`
- IPv6: `Covered 9,912,218/9,912,218 (100.0%) IP addresses. Got 410,088 wrong for an overall accuracy of 95.86%. Took 72.35 seconds`
