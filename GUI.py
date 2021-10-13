import tkinter as tk
from tkinter import messagebox
import nmap
import ipaddress
import re

# Regular Expression Pattern to extract the number of ports you want to scan.
# You have to specify <lowest_port_number>-<highest_port_number> (ex 10-100)
port_range_pattern = re.compile("([0-9]+)-([0-9]+)")

# Initialising the variables, will be using these later on
one_port = 0
port_min = 0
port_max = 65535
common_ports = [21, 22, 23, 25, 53, 80, 443, 110, 135, 137, 138, 139, 1433, 1434]
scan_type = [1, 2, 3]
nm = nmap.PortScanner()

#########create GUI###############333
root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Port_Scanner')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='Enter Your IP Address:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry (root)
canvas1.create_window(200, 140, window=entry1)


def getScanIP():
    while True:
        ip_add_entered = entry1.get()
        try:
            ip_address_obj = ipaddress.ip_address(ip_add_entered)
            break
        except:
            messagebox.showinfo("Title", "Invalid IP Address")
            break
    label1 = tk.Label(root, text=ipaddress.ip_address(ip_add_entered))
    canvas1.create_window(200, 230, window=label1)

button1 = tk.Button(text='Enter the IP you wish to Scan', command=getScanIP)
canvas1.create_window(200, 180, window=button1)

root.mainloop()
