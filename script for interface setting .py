import netmiko

# Prompt user for IP address
ip_address = input("Enter the IP address of the switch: ")

# Connect to the switch
try:
    connection = netmiko.ConnectHandler(
        device_type="cisco_ios",
        host=ip_address,
        username="yourusername",
        password="yourpassword"
    )
except netmiko.ssh_exception.NetMikoAuthenticationException:
    print("Authentication failed. Check your username and password.")
    exit()
except netmiko.ssh_exception.NetMikoTimeoutException:
    print("Timeout connecting to the device. Check the IP address and try again.")
    exit()

# Get the list of interfaces
interface_list = connection.send_command("show interfaces").splitlines()

# Iterate through the interfaces and run the command on each one
for interface in interface_list:
    interface = interface.split()[0]
    if interface.startswith("Gig"):
        command = "interface " + interface + "\nno access-session"
        connection.send_config_set(command)

# Close the connection
connection.disconnect()

print("Access-session has been removed from all interfaces")
