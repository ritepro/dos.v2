from flask import Flask, request

app = Flask(__name__)

@app.route('/collect_ip', methods=['GET'])
def collect_ip():
    ip = request.args.get('ip')
    if ip:
        print(f"Collected IP: {ip}")
        with open("ips.txt", "a") as file:
            file.write(ip + "\n")
        return "IP Collected", 200
    return "No IP Provided", 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
