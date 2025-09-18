from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
 <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Introduction to TCP/IP</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
            background-color: #f9f9f9;
            color: #333;
        }
        header {
            text-align: center;
            margin-bottom: 40px;
        }
        h1 {
            color: #2c3e50;
        }
        section {
            background: white;
            padding: 20px;
            margin-bottom: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.1);
        }
        h2 {
            color: #34495e;
        }
        ul {
            line-height: 1.6;
        }
        code {
            background: #ecf0f1;
            padding: 2px 5px;
            border-radius: 3px;
            font-family: monospace;
        }
    </style>
</head>
<body>
    <header>
        <h1>Understanding TCP/IP</h1>
        <p>A brief overview of the TCP/IP protocol suite</p>
    </header>

    <section>
        <h2>What is TCP/IP?</h2>
        <p><strong>TCP/IP</strong> stands for <em>Transmission Control Protocol/Internet Protocol</em>. It is the fundamental suite of communication protocols used for the internet and other similar networks.</p>
        <p>TCP/IP allows computers to communicate over long distances and through interconnected networks.</p>
    </section>

    <section>
        <h2>Main Protocols in TCP/IP Suite</h2>
        <ul>
            <li><strong>IP (Internet Protocol)</strong>: Responsible for addressing and routing packets of data so they can travel across networks and arrive at the correct destination.</li>
            <li><strong>TCP (Transmission Control Protocol)</strong>: Ensures reliable, ordered, and error-checked delivery of data between applications.</li>
            <li><strong>UDP (User Datagram Protocol)</strong>: Provides a faster, but less reliable, way to send data, often used for streaming or gaming.</li>
            <li><strong>HTTP/HTTPS</strong>: Protocols used to transfer web pages on the internet.</li>
            <li><strong>FTP</strong>: Protocol for transferring files between computers.</li>
        </ul>
    </section>

    <section>
        <h2>How TCP/IP Works</h2>
        <p>When you send data over the internet using TCP/IP, the data is broken down into small pieces called <em>packets</em>. These packets travel independently through the network and are reassembled at the destination.</p>
        <p>TCP manages the connection and ensures that all packets arrive and are put in the right order. IP handles the addressing and routing.</p>
    </section>

    <section>
        <h2>Example: TCP/IP Packet Structure</h2>
        <pre><code>
+-----------------------------+
|       IP Header             |
+-----------------------------+
|       TCP Header            |
+-----------------------------+
|       Data Payload          |
+-----------------------------+
        </code></pre>
        <p>The IP header contains source and destination addresses, while the TCP header includes port numbers and sequencing information.</p>
    </section>
</body>
</html>

"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()