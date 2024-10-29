# wmclient - WURFL Microservice Client for Python

## Differences between version 2.2.0 and previous ones.

Version 2.2.0 makes WURFL microservice client backward compatible with Python 2.7. To do that it replaces two libraries that are available for Python 3.x only:

- pywurfl (replaced by urrllib3)
- @lru_cache (replaced by pylru)

While in older versions cache was used by default, in this version you'll have to use the `set_cache_size` function of the client to ensure it is created and used.

## Python WURFL Microservice Client

WURFL Microservice (by ScientiaMobile, Inc.) is a mobile device detection service that can quickly and accurately detect over 500 capabilities of visiting devices. It can differentiate between portable mobile devices, desktop devices, SmartTVs and any other types of devices that have a web browser.

This is the Python Client API for accessing the WURFL Microservice. The API is released under Open-Source and can be integrated with other open-source or proprietary code. In order to operate, it requires access to a running instance of the WURFL Microservice product, such as:

- WURFL Microservice for Docker: https://www.scientiamobile.com/products/wurfl-microservice-docker-detect-device/

- WURFL Microservice for AWS: https://www.scientiamobile.com/products/wurfl-device-detection-microservice-aws/

- WURFL Microservice for Azure: https://www.scientiamobile.com/products/wurfl-microservice-for-azure/

- WURFL Microservice for Google Cloud Platform: https://www.scientiamobile.com/products/wurfl-microservice-for-gcp/

Python implementation of the WM Client api.
Requires:
- Python 3.x
- pip
- pycurl module (you can install it with `pip install pycurl`)
- requests module (you can install it with `pip install requests`)
- pylru module (you can install it with `pip install pylru`)

The Example project contains an example of client api usage for a script :


```python
from wmclient import *
from requests import Request as HttpRequest

try:
    client = WmClient.create("http", "localhost", 8080, "")

    info = client.get_info()
    print("Printing WM server information")
    print("WURFL API version: " + info.wurfl_api_version)
    print("WM server version:  " + info.wm_version)
    print("Wurfl file info: " + info.wurfl_info)

    ua = "Mozilla/5.0 (Linux; Android 7.1.1; ONEPLUS A5000 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) " \
         "Chrome/56.0.2924.87 Mobile Safari/537.36 "

    req_headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "http://itvv.net/",
        "User-Agent": "Mozilla/5.0 (Linux; U; Android 7.1.1; XT1635-02 Build/NPN26.107; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.127 Mobile Safari/537.36 OPR/51.0.2254.150807",
        "X-Forwarded-For": "157.32.186.226",
        "X-Requested-With": "com.opera.mini.native"
    }
    req = HttpRequest('GET', "http://mywebsite.com", headers=req_headers)

    client.set_requested_static_capabilities(["brand_name", "model_name"])
    client.set_requested_virtual_capabilities(["is_smartphone", "form_factor"])
    print()
    print("Detecting device for user-agent: " + ua)

    # Perform a device detection calling WM server API
    device = client.lookup_request(req)

    if device.error is not None and len(device.error) > 0:
        print("An error occurred: " + device.error)
    else:
        # Let's get the device capabilities and print some of them
        capabilities = device.capabilities
        print("Detected device WURFL ID: " + capabilities["wurfl_id"])
        print("Device brand & model: " + capabilities["brand_name"] + " " + capabilities["model_name"])
        print("Detected device form factor: " + capabilities["form_factor"])
        if capabilities["is_smartphone"] == "true":
            print("This is a smartphone")
            # Iterate over all the device capabilities and print them
            print("All received capabilities");
            for k in capabilities:
                print(k + ": " + capabilities[k])

            # Get all the device manufacturers, and print the first twenty
            print()
            limit = 20
            deviceMakes = client.get_all_device_makes()
            print("Print the first {} Brand of {} retrieved from server\n".format(limit, len(deviceMakes)))

            # Sort the device manufacturer names
            list.sort(deviceMakes)
            for i in range(limit):
                print(" - {}\n".format(deviceMakes[i]))

            # Now call the WM server to get all device model and marketing names produced by Apple
            print("Print all Model for the Apple Brand")
            devNames = client.get_all_devices_for_make("Apple")

            for model_mkt_name in devNames:
                print(" - {} {}\n".format(model_mkt_name.brand_name, model_mkt_name.model_name))

            # Now call the WM server to get all operative system names
            print("Print the list of OSes")
            oses = client.get_all_OSes()
            # Sort and print all OS names
            list.sort(oses)
            for os in oses:
                print(" - {}\n".format(os))

            # Let's call the WM server to get all version of the Android OS
            print("Print all versions for the Android OS")
            osVersions = client.get_all_versions_for_OS("Android")
            # Sort all Android version numbers and print them.
            list.sort(osVersions)
            for ver in osVersions:
                print(" - {}\n".format(ver))

except WmClientError as wme:
    # problems such as network errors  or internal server problems
    print("An error has occurred: " + wme.message)
```
