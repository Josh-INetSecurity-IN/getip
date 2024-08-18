import socket

def get_ip_address(website_url):
    try:
        ip_address = socket.gethostbyname(website_url)
        return ip_address
    except socket.gaierror:
        return "Unable to get IP address for the website."

# Example usage:
website = input("Enter the website URL (without 'http://', 'https://', or 'www'): ")
ip_address = get_ip_address(website)

print(f"The IP address of {website} is: {ip_address}")
