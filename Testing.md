# Database Testing

Test data comes from the [ip-db-test-data](https://github.com/HostByBelle/ip-db-test-data) GitHub repository.

## Automated testing

Each release will automatically be run through testing an the results will be attached as the release body.

### GeoLite2-Country Testing Result

For those who are curious how the public domain databases compare to the MaxMind GeoLite2 database, here's how their databases perform in the tests:

**Last updated:** 12/09/2023

- IPv4: `Covered 15,893,628/15,894,076 (100.0%) IP addresses. Got 652,374 wrong for an overall accuracy of 95.9%. Took 264.71 seconds`
- IPv6: `Covered 24,046,603/24,046,603 (100.0%) IP addresses. Got 660,044 wrong for an overall accuracy of 97.26%. Took 374.80 seconds`
