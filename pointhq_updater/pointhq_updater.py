# PointHQ dDNS Updater
# Checks current IP address then updates the record
# Kyle Cheung <kyle@kylezoa.com> <kyle@sekren.se>
# Dependencies: pointhq (pip install pointhq), requests (pip install requests)

"""
Usage notes:

* Edit your crontab to automatically run the script at a given time.
* Edit the variables that contain your personal data below.

"""

from pointhq import Point 
import requests

# grab current IP address
IP_req = requests.get('http://rhinoequipment.com/ip.php')
IP = IP_req.content

# enter your personal data in between < > 
username = '<your pointhq email address login>'
apitoken = '<your API token found at https://pointhq.com/settings>'
zone = <zone to update> 
record = <record to update>

point = Point(username=username, apitoken=apitoken)

# check the existing IP address

records = point.zones(zone).records(record).retrieve()
A_record = records['zone_record']['data']

print A_record, IP

if IP == A_record:
    print 'Current IP address matches PointHQ record. Quitting!'
    exit(1)
else:
    print 'updating ', zone
    point.zones(zone).records(record).update(data=IP)
