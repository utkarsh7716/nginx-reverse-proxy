# Nginx Reverse Proxy for Multiple Dockerized Flask Apps

This project demonstrates how to use **Docker Compose** and **Nginx** as a reverse proxy to run multiple **Flask applications** on a single server behind different URL paths.

## 🧱 Project Structure

nginx-reverse-proxy/
├── app1/
│ ├── app.py
│ └── Dockerfile
├── app2/
│ ├── app.py
│ └── Dockerfile
├── nginx/
│ └── nginx.conf
└── docker-compose.yml 

## 🚀 How to Run

### 1. Prerequisites
- Ubuntu (or any Linux)
- Docker
- Docker Compose

### 2. Clone the Repo
```bash
git clone https://github.com/utkarsh7716/nginx-reverse-proxy.git
cd nginx-reverse-proxy
docker-compose up -d
3. Start the containers
bash
Copy
Edit
docker-compose up -d
4. Access the Apps
http://<EC2_PUBLIC_IP>/app1 → App 1

http://<EC2_PUBLIC_IP>/app2 → App 2

🛠️ Technologies Used
Python (Flask)

Docker

Docker Compose

Nginx

✅ Expected Output
For /app1:
Hello from App 1
For /app2:
Hello from App 2
You can also test with curl:
curl http://<your-ec2-public-ip>/app1
# Hello from App 1

curl http://<your-ec2-public-ip>/app2
# Hello from App 2
