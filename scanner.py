print("Scanner started")

from port_scan import scan_ports
from header_check import check_headers
from urllib.parse import urlparse

target = input("Enter target URL (example: http://example.com): ")
print(f"Scanning {target}...")

host = urlparse(target).hostname

ports = scan_ports(host)
headers = check_headers(target)

print("\nOpen Ports:", ports)
print("Missing Security Headers:", headers)
