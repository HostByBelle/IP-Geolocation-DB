
# IP Geolocation DB

This repository automatically builds IP geolocation databases in the `.mmdb` database format for both IPv4 and IPv6.
Building is handled via the [mmdbmeld](https://github.com/safing/mmdbmeld) golang package and the database sources originate from [ip-location-db](https://github.com/sapics/ip-location-db).

## Automation

These databases are automatically updated daily at 12:00 AM UTC. That may or may not match the schedule for the upstream sources and as such it is possible these databases may be slightly out of date.

Effort has gone into making these workflows efficient for all parties involved. If you see an inefficiency or issue in the automation process, feel free to report it.

### Release Retention

This repository is configured to automatically delete releases older than 30 days. For this reason, you should always use the appropriate link which points to the latest release. In the event that releases stop running for whatever reason, the latest release will always be preserved regardless.

## Variants

These URLs will always point to the latest version of the database.


| License | Database Type | IPv4 | IPv6 | File Name |
|---------|---------------|------|------|-----------|
| [CC0 License](https://creativecommons.org/publicdomain/zero/1.0/) | Country | [Download](https://github.com/HostByBelle/IP-Geolocation-DB/releases/latest/download/cc0-v4.mmdb) | [Download](https://github.com/HostByBelle/IP-Geolocation-DB/releases/latest/download/cc0-v6.mmdb) | `cc0-v4.mmdb`, `cc0-v6.mmdb` |
| [PDDL License](https://opendatacommons.org/licenses/pddl/1-0/) | ASN | [Download](https://github.com/HostByBelle/IP-Geolocation-DB/releases/latest/download/pddl-asn-v4.mmdb) | [Download](https://github.com/HostByBelle/IP-Geolocation-DB/releases/latest/download/pddl-asn-v6.mmdb) | `pddl-asn-v4.mmdb`, `pddl-asn-v6.mmdb` |
| [PDDL License](https://opendatacommons.org/licenses/pddl/1-0/) | Country | [Download](https://github.com/HostByBelle/IP-Geolocation-DB/releases/latest/download/pddl-country-v4.mmdb) | [Download](https://github.com/HostByBelle/IP-Geolocation-DB/releases/latest/download/pddl-country-v6.mmdb) | `pddl-country-v4.mmdb`, `pddl-country-v6.mmdb` |
| [PDDL License](https://opendatacommons.org/licenses/pddl/1-0/) | Country + ASN | [Download](https://github.com/HostByBelle/IP-Geolocation-DB/releases/latest/download/pddl-country-asn-v4.mmdb) | [Download](https://github.com/HostByBelle/IP-Geolocation-DB/releases/latest/download/pddl-country-asn-v6.mmdb) | `pddl-country-asn-v4.mmdb`, `pddl-country-asn-v6.mmdb` |
| [CC0 License](https://creativecommons.org/publicdomain/zero/1.0/) + [PDDL License](https://opendatacommons.org/licenses/pddl/1-0/) | Country (CC0) + ASN (PDDL) | [Download](https://github.com/HostByBelle/IP-Geolocation-DB/releases/latest/download/cc0-pddl-country-asn-v4-variant-1.mmdb) | [Download](https://github.com/HostByBelle/IP-Geolocation-DB/releases/latest/download/cc0-pddl-country-asn-v6-variant-1.mmdb) | `cc0-pddl-country-asn-v4-variant-1.mmdb`, `cc0-pddl-country-asn-v6-variant-1.mmdb` |

### Notes

- `County` database types only include what country an IP address is associated with.
- `ASN` databases includes [ASN](https://www.arin.net/resources/guide/asn/) information for a given address such as what organization the IP address is associated with.

## Licensing

All code in this repository is licensed under the CC0 license. The [mmdbmeld](https://github.com/safing/mmdbmeld) and [ip-location-db](https://github.com/sapics/ip-location-db) projects each have their own licenses as do the original databases. Presently, we only build databases utilizing data that's under the [CC0](https://creativecommons.org/publicdomain/zero/1.0/) and [PDDL](https://opendatacommons.org/licenses/pddl/1-0/) licenses which should be noted both in their file name as well as the variants section of this document.
