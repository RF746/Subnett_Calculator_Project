import ipaddress

def subnet_calculator(ip, subnet_mask):
    """Calculate subnet details from IP address and subnet mask."""
    try:
        # Create an IPv4Network object
        network = ipaddress.IPv4Network(f"{ip}/{subnet_mask}", strict=False)

        # Extract details
        network_address = network.network_address
        broadcast_address = network.broadcast_address
        num_hosts = network.num_addresses - 2  # Excluding network and broadcast
        host_range = list(network.hosts())

        return {
            "Network Address": str(network_address),
            "Broadcast Address": str(broadcast_address),
            "Number of Hosts": num_hosts,
            "Host Range": f"{host_range[0]} - {host_range[-1]}"
        }
    except ValueError as e:
        return {"Error": str(e)}

if __name__ == "__main__":
    print("Welcome to the Subnet Calculator!")
    
    # Get user input
    ip = input("Enter an IP address (e.g., 192.168.1.1): ")
    subnet_mask = input("Enter the subnet mask (e.g., 24): ")
    
    # Calculate and display results
    result = subnet_calculator(ip, subnet_mask)
    for key, value in result.items():
        print(f"{key}: {value}")
