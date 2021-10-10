import nmap
import ipaddress
import re

def main():
    # Regular Expression Pattern to extract the number of ports you want to scan.
    # You have to specify <lowest_port_number>-<highest_port_number> (ex 10-100)
    port_range_pattern = re.compile("([0-9]+)-([0-9]+)")

    # Initialising the variables, will be using these later on
    one_port = 0
    port_min = 0
    port_max = 65535
    common_ports = [21, 22, 40, 443]
    scan_type = [1, 2, 3]
    nm = nmap.PortScanner()

    while True:
        ip_add_entered = input("\nPlease enter the ip address that you want to scan: ")
        try:
            ip_address_obj = ipaddress.ip_address(ip_add_entered)
            break
        except:
            print("You entered an invalid ip address")

    def hot_ports():
        for port in common_ports:
            try:
                result = nm.scan(ip_add_entered, str(port))
                port_status = (result['scan'][ip_add_entered]['tcp'][port]['state'])
                print(f"Port {port} is {port_status}")
            except:
                print(f"Cannot scan port {port}.")

    def scan_range():
        print("Please enter the range of ports you want to scan in format: <int>-<int> (ex would be 60-120)")
        port_range = input("Enter port range: ")
        port_range_valid = port_range_pattern.search(port_range.replace(" ",""))
        if port_range_valid:
            port_min = int(port_range_valid.group(1))
            port_max = int(port_range_valid.group(2))
        for port in range(port_min, port_max + 1):
            try:
                result = nm.scan(ip_add_entered, str(port))
                port_status = (result['scan'][ip_add_entered]['tcp'][port]['state'])
                print(f"Port {port} is {port_status}")
            except:
                print(f"Cannot scan port {port}.")

    def indi_scan():
        one_port = input("\nWhat port do you wish to scan for? ")
        res = nm.scan(ip_add_entered, one_port)
        print(res)

    while True:
        scan_input = input("\nWhat type of scan do you wish to run: 1: Commonly Hacked Ports, 2: Scan Range, 3: Specific Port ")
        if scan_input == "1":
            hot_ports()
        elif scan_input == "2":
            scan_range()
        elif scan_input == "3":
            indi_scan()
            break
        else:
            print("invalid")


if __name__ == "__main__":
    main()