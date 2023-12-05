
# IP Geolocation DB

This repository automatically builds IP geolocation databases in the `.mmdb` database format for both IPv4 and IPv6.
Building is handled via the [mmdbmeld](https://github.com/safing/mmdbmeld) golang package and the database sources originate from [ip-location-db](https://github.com/sapics/ip-location-db).

## Automation

These databases are automatically updated daily at 12:00 AM UTC. That may or may not match the schedule for the upstream sources and as such it is possible these databases may be slightly out of date.

Effort has gone into making these workflows efficient for all parties involved. If you see an inefficiency or issue in the automation process, feel free to report it.

### Release Retention

This repository is configured to automatically delete releases older than 30 days. For this reason, you should always use the appropriate link which points to the latest release. In the event that releases stop running for whatever reason, the latest release will always be preserved regardless.

## Variants

Presently, only database sources under the [CC0](https://creativecommons.org/publicdomain/zero/1.0/) license are utilized and as such these are the only variants available. We presently have no intention of automatically building others, however the release naming scheme may allow this in the future without breaking existing URLs.

### CC0

These URLS will always point to the latest version of the database.
- [IPv4](https://github.com/HostByBelle/IP-Geolocation-DB/releases/latest/download/geoip-cc0-v4.mmdb) (File name: `geoip-cc0-v4.mmdb ` Included data: `country`)
- [IPv6](https://github.com/HostByBelle/IP-Geolocation-DB/releases/latest/download/geoip-cc0-v6.mmdb) (File name: `geoip-cc0-v6.mmdb` Included data: `country`)

## Licensing

All code in this repository is licensed under the CC0 license. The [mmdbmeld](https://github.com/safing/mmdbmeld) and [ip-location-db](https://github.com/sapics/ip-location-db) projects each have their own licenses as do the original databases. Presently, only databases under the CC0 license are utilized.
