#!/usr/bin/env python3
"""Simple script to query mac address with macaddress.io API

Script flow is
* Read arguments
* Query API
* Print Company Name as Output

Example:
./mac_addr_tool.py $(cat .api_key) 4F:3B:61:34:FD:E0
"""

import argparse
import re
import requests
import sys


def main():
    parser = argparse.ArgumentParser(description="Query macaddress.io for data.")
    parser.add_argument("-d", "--debug", action='store_true', help="Prints all output from query")
    parser.add_argument("api_key", help="API Key for macaddress.io")
    parser.add_argument("mac_address",
                        help="Mac address to query, must be in MM:MM:MM:SS:SS:SS format")
    args = parser.parse_args()

    # Validate Mac Address to format MM:MM:MM:SS:SS:SS
    # regex = "^[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}$"
    # if not re.match(regex, args.mac_address.lower()):
    #     print("Invalid Mac addr({}), expecting MM:MM:MM:SS:SS:SS format".format(args.mac_address))
    #     sys.exit(1)

    print("Querying macaddress.io for {}".format(args.mac_address))

    api_url = "https://api.macaddress.io/v1?apiKey=" + args.api_key
    api_url = api_url + "&output=json&search=" + args.mac_address

    api_data = requests.get(api_url)
    json_api_data = api_data.json()

    if args.debug:
        print("Debug Output: {}".format(json_api_data))

    if api_data.status_code != 200:
        print("Macaddress.io returned status: {}".format(api_data.status_code))
        print("Output: {}".format(api_data.text))
        sys.exit(1)

    if "vendorDetails" in json_api_data and "companyName" in json_api_data["vendorDetails"]:
        print("Company Name: " + json_api_data["vendorDetails"]["companyName"])
    else:
        print("Company Name appears to be missing in macaddress.io output.")
        print("Output: {}".format(api_data.text))

if __name__ == "__main__":
    main()
