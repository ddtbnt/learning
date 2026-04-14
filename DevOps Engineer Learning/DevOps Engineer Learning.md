# 🚀 DevOps Engineer Learning Roadmap

> Mục tiêu: Trở thành DevOps Engineer + sẵn sàng thi các chứng chỉ cloud hàng đầu  
> Phương pháp: Học LOCAL → hiểu bản chất → triển khai CLOUD → thi CERT  

---

# 🧠 Tổng quan lộ trình

Local (Foundation)  
→ Cloud (AWS/Azure/GCP)  
→ Project thực tế  
→ Certification  
→ Job DevOps  

---

# 📌 1. Local DevOps Learning Path (Offline – Nền tảng)

🎯 Mục tiêu: Hiểu bản chất DevOps (Docker, Kubernetes, CI/CD)

## Nội dung chính:
- Environment setup (Git, Docker, VS Code)
- Microservices (Docker Compose)
- Kubernetes local (Minikube / Kind)
- CI/CD (GitHub Actions / Jenkins)
- Monitoring cơ bản
- Project hoàn chỉnh

## Mindmap:
<!-- Dán mindmap LOCAL vào đây -->

```
Local DevOps Learning Path (From Laptop → Certification Ready)
│
├─ 1. Chuẩn bị môi trường máy cá nhân
│   │
│   ├─ Yêu cầu cơ bản
│   │   ├─ RAM: ≥ 8GB (khuyến nghị 16GB)
│   │   ├─ CPU: ≥ 4 cores
│   │   └─ OS: Windows / Linux / macOS
│   │
│   ├─ Cài đặt công cụ
│   │   ├─ Git (version control)
│   │   ├─ Docker (container platform)
│   │   ├─ Visual Studio Code (code editor)
│   │   └─ Node.js hoặc Python (backend runtime)
│   │
│   └─ Mục tiêu
│       └─ Sẵn sàng build & run project local
│
├─ 2. Nền tảng DevOps cơ bản
│   │
│   ├─ Version Control
│   │   ├─ git init / add / commit / push
│   │   └─ Làm việc với GitHub (repo, branch)
│   │
│   ├─ Linux cơ bản
│   │   ├─ File system (ls, cd, mkdir)
│   │   ├─ Process (ps, top)
│   │   └─ Networking (curl, ping)
│   │
│   └─ Mục tiêu
│       └─ Hiểu workflow dev thực tế
│
├─ 3. Docker (Cốt lõi DevOps)
│   │
│   ├─ Kiến thức
│   │   ├─ Image vs Container
│   │   ├─ Dockerfile
│   │   └─ Docker networking
│   │
│   ├─ Thực hành
│   │   ├─ docker build
│   │   ├─ docker run
│   │   └─ docker-compose
│   │
│   └─ Mục tiêu
│       └─ Containerize ứng dụng
│
├─ 4. Microservices local
│   │
│   ├─ Kiến trúc
│   │   ├─ auth-service
│   │   ├─ user-service
│   │   ├─ order-service
│   │   └─ API gateway (nginx)
│   │
│   ├─ Chạy bằng Docker Compose
│   │   └─ Nhiều service trên 1 máy
│   │
│   └─ Mục tiêu
│       └─ Hiểu giao tiếp giữa services
│
├─ 5. Kubernetes local
│   │
│   ├─ Công cụ
│   │   ├─ Minikube (Kubernetes local)
│   │   └─ Kind (Kubernetes bằng Docker)
│   │
│   ├─ Kiến thức
│   │   ├─ Pod
│   │   ├─ Deployment
│   │   ├─ Service
│   │   └─ ConfigMap / Secret
│   │
│   ├─ Thực hành
│   │   ├─ kubectl apply
│   │   ├─ scale deployment
│   │   └─ expose service
│   │
│   └─ Mục tiêu
│       └─ Hiểu orchestration (quản lý container)
│
├─ 6. CI/CD (Automation)
│   │
│   ├─ Công cụ
│   │   ├─ GitHub Actions
│   │   └─ Jenkins
│   │
│   ├─ Pipeline
│   │   ├─ Code → Build
│   │   ├─ Test
│   │   └─ Deploy (local)
│   │
│   └─ Mục tiêu
│       └─ Tự động hóa workflow
│
├─ 7. Monitoring cơ bản
│   │
│   ├─ Tools
│   │   ├─ docker logs
│   │   └─ Basic metrics (CPU, RAM)
│   │
│   └─ Mục tiêu
│       └─ Debug & quan sát hệ thống
│
├─ 8. Project thực tế (QUAN TRỌNG)
│   │
│   ├─ Build system hoàn chỉnh
│   │   ├─ Microservices app
│   │   ├─ Dockerized
│   │   ├─ CI/CD pipeline
│   │   └─ Kubernetes deploy
│   │
│   ├─ Workflow
│   │   └─ Code → Push → Auto deploy
│   │
│   └─ Kết quả
│       └─ Portfolio DevOps (đưa vào CV)
│
├─ 9. Chuyển lên Cloud (bước bắt buộc)
│   │
│   ├─ Nền tảng
│   │   ├─ Amazon Web Services (AWS)
│   │   ├─ Microsoft Azure
│   │   └─ Google Cloud
│   │
│   ├─ Học dịch vụ cơ bản
│   │   ├─ Compute (EC2 / VM)
│   │   ├─ Storage (S3 / Blob)
│   │   └─ IAM (quyền truy cập)
│   │
│   ├─ Deploy lại system
│   │   └─ Từ local → cloud
│   │
│   └─ Mục tiêu
│       └─ Hiểu production environment
│
├─ 10. Chuẩn bị thi chứng chỉ
│   │
│   ├─ Target
│   │   ├─ AWS Certified DevOps Engineer – Professional
│   │   ├─ Microsoft DevOps Engineer Expert
│   │   └─ Google Professional DevOps Engineer
│   │
│   ├─ Kiến thức cần bổ sung
│   │   ├─ Cloud services (AWS/Azure/GCP)
│   │   ├─ Security (IAM)
│   │   ├─ Monitoring nâng cao
│   │   └─ Scaling systems
│   │
│   └─ Practice
│       ├─ Scenario-based questions
│       └─ Mock exams
│
└─ 11. Insight quan trọng
    ├─ Local = hiểu bản chất DevOps
    ├─ Docker + Kubernetes = cốt lõi
    ├─ Cloud = phần thi & thực tế
    ├─ Sai lầm lớn:
    │   └─ Nhảy vào cloud quá sớm
    └─ Lộ trình đúng:
        └─ Local → Project → Cloud → Certification
```
---

# ☁️ 2. AWS DevOps Learning Path (Online)

🎯 Target: AWS Certified DevOps Engineer – Professional

## Nội dung chính:
- AWS Account + Billing
- EC2 + Networking
- CI/CD (CodePipeline)
- Monitoring (CloudWatch)
- Infrastructure as Code
- Security (IAM)
- Deploy system lên AWS

## Mindmap:
<!-- Dán mindmap AWS vào đây -->

```
AWS DevOps Learning Path (From Account → Certification Ready)
│
├─ 1. Tạo AWS Account (5–10 phút)
│   ├─ Bước 1: Truy cập website
│   │   └─ aws.amazon.com → Create an AWS Account
│   │
│   ├─ Bước 2: Nhập thông tin
│   │   ├─ Email
│   │   ├─ Password
│   │   └─ Tên account
│   │
│   ├─ Bước 3: Thêm thẻ thanh toán
│   │   ├─ Visa / Mastercard
│   │   └─ Dùng để xác minh (không mất tiền nếu dùng đúng)
│   │
│   ├─ Bước 4: Xác minh
│   │   └─ Số điện thoại (OTP)
│   │
│   └─ Bước 5: Chọn plan
│       └─ Basic (Free Tier 12 tháng)
│
├─ 2. Quản lý chi phí (CỰC QUAN TRỌNG)
│   │
│   ├─ Setup Billing Alert
│   │   ├─ Vào Billing Dashboard
│   │   ├─ Chọn Budgets
│   │   └─ Tạo budget:
│   │       ├─ Limit: 5 USD
│   │       └─ Alert: 80% → gửi email
│   │
│   ├─ Mục tiêu
│   │   ├─ Tránh phát sinh phí
│   │   └─ Kiểm soát usage
│   │
│   └─ Nguyên tắc
│       ├─ Luôn kiểm tra billing
│       └─ Không dùng dịch vụ ngoài Free Tier
│
├─ 3. Tạo server miễn phí (EC2)
│   │
│   ├─ Launch Instance
│   │   ├─ AMI: Amazon Linux 2
│   │   ├─ Instance: t2.micro (Free Tier)
│   │   └─ Storage: 8GB
│   │
│   ├─ Security Group
│   │   ├─ Port 22 → SSH
│   │   ├─ Port 80 → HTTP
│   │   └─ (Optional) 443 → HTTPS
│   │
│   ├─ Public Access
│   │   ├─ Có Public IP
│   │   └─ Truy cập: http://<ip>
│   │
│   └─ Connect server
│       └─ ssh -i key.pem ec2-user@ip
│
├─ 4. Setup môi trường DevOps (Docker)
│   │
│   ├─ Cài đặt Docker
│   │   ├─ yum update
│   │   ├─ yum install docker
│   │   ├─ start service
│   │   └─ add user vào docker group
│   │
│   ├─ Test Docker
│   │   └─ docker run hello-world
│   │
│   └─ Mục tiêu
│       ├─ Chạy container
│       └─ Chuẩn bị deploy app
│
├─ 5. Lab DevOps cơ bản (FREE)
│   │
│   ├─ Deploy web đơn giản
│   │   ├─ docker run -p 80:80 nginx
│   │   └─ Truy cập qua browser
│   │
│   ├─ Build app
│   │   ├─ Clone project
│   │   ├─ Docker build
│   │   └─ Docker run
│   │
│   ├─ CI/CD cơ bản
│   │   ├─ Git push
│   │   ├─ Build image
│   │   └─ Deploy container
│   │
│   └─ Kết quả
│       └─ Website chạy online toàn cầu
│
├─ 6. Dọn tài nguyên (TRÁNH MẤT TIỀN)
│   ├─ Stop instance
│   ├─ Terminate instance
│   └─ Xóa resource không dùng
│
├─ 7. Mở rộng kỹ năng DevOps
│   │
│   ├─ CI/CD nâng cao
│   │   ├─ CodePipeline
│   │   ├─ GitHub Actions
│   │   └─ Jenkins
│   │
│   ├─ Container orchestration
│   │   ├─ Kubernetes
│   │   └─ ECS / EKS
│   │
│   ├─ Monitoring
│   │   ├─ CloudWatch
│   │   └─ Logging system
│   │
│   └─ Infrastructure as Code
│       └─ CloudFormation / Terraform
│
├─ 8. Chuẩn bị thi chứng chỉ
│   │
│   ├─ Target:
│   │   └─ AWS Certified DevOps Engineer – Professional
│   │
│   ├─ Kiến thức cần có
│   │   ├─ CI/CD pipelines
│   │   ├─ High availability
│   │   ├─ Security & IAM
│   │   ├─ Monitoring & logging
│   │   └─ Automation
│   │
│   ├─ Practice
│   │   ├─ Lab nhiều lần
│   │   ├─ Practice exam
│   │   └─ Scenario-based questions
│   │
│   └─ Điều kiện thực tế
│       ├─ 1–2 năm kinh nghiệm (hoặc lab tương đương)
│       └─ Hiểu hệ thống end-to-end
│
└─ 9. Insight quan trọng
    ├─ DevOps = học bằng thực hành
    ├─ AWS = môi trường thật (production-like)
    ├─ Free Tier đủ để bắt đầu
    ├─ Sai lầm lớn:
    │   └─ Chỉ học lý thuyết, không lab
    └─ Lộ trình đúng:
        └─ Setup → Lab → Project → Certification
```
---

# ☁️ 3. Azure DevOps Learning Path (Online)

🎯 Target: Microsoft Certified: DevOps Engineer Expert

## Nội dung chính:
- Azure setup
- Azure DevOps (CI/CD)
- Azure Kubernetes Service (AKS)
- Monitoring (Azure Monitor)
- Infrastructure as Code
- Security & Identity
- Deploy system lên Azure

## Mindmap:
<!-- Dán mindmap AZURE vào đây -->
```
Azure DevOps Learning Path (From Account → Certification Ready)
│
├─ 1. Tạo Azure Account (5–10 phút)
│   ├─ Bước 1: Truy cập website
│   │   └─ portal.azure.com → Sign up
│   │
│   ├─ Bước 2: Nhập thông tin
│   │   ├─ Email (Microsoft account)
│   │   ├─ Password
│   │   └─ Thông tin cá nhân
│   │
│   ├─ Bước 3: Thêm thẻ thanh toán
│   │   ├─ Visa / Mastercard
│   │   └─ Dùng để xác minh (có free credit ban đầu)
│   │
│   ├─ Bước 4: Xác minh
│   │   └─ Số điện thoại (OTP)
│   │
│   └─ Bước 5: Free tier
│       ├─ Free credit (~$200 trong 30 ngày)
│       └─ Một số dịch vụ free 12 tháng
│
├─ 2. Quản lý chi phí (CỰC QUAN TRỌNG)
│   │
│   ├─ Setup Cost Alert
│   │   ├─ Vào Cost Management + Billing
│   │   ├─ Chọn Budgets
│   │   └─ Tạo budget:
│   │       ├─ Limit: 5–10 USD
│   │       └─ Alert: 80% → gửi email
│   │
│   ├─ Mục tiêu
│   │   ├─ Tránh phát sinh phí
│   │   └─ Kiểm soát usage
│   │
│   └─ Nguyên tắc
│       ├─ Luôn kiểm tra billing
│       └─ Không dùng dịch vụ ngoài free tier
│
├─ 3. Tạo server (Virtual Machine)
│   │
│   ├─ Create VM
│   │   ├─ Image: Ubuntu / Windows Server
│   │   ├─ Size: B1s (free tier eligible)
│   │   └─ Storage: Standard SSD (free limit)
│   │
│   ├─ Networking
│   │   ├─ Open port 22 → SSH
│   │   ├─ Open port 80 → HTTP
│   │   └─ (Optional) 443 → HTTPS
│   │
│   ├─ Public Access
│   │   ├─ Public IP
│   │   └─ Truy cập qua IP
│   │
│   └─ Connect server
│       └─ ssh user@ip
│
├─ 4. Setup môi trường DevOps (Docker)
│   │
│   ├─ Cài đặt Docker
│   │   ├─ apt update
│   │   ├─ apt install docker.io
│   │   ├─ systemctl start docker
│   │   └─ usermod -aG docker user
│   │
│   ├─ Test Docker
│   │   └─ docker run hello-world
│   │
│   └─ Mục tiêu
│       ├─ Chạy container
│       └─ Chuẩn bị deploy app
│
├─ 5. Lab DevOps cơ bản
│   │
│   ├─ Deploy web đơn giản
│   │   ├─ docker run -p 80:80 nginx
│   │   └─ Truy cập qua browser
│   │
│   ├─ Build app
│   │   ├─ Clone project
│   │   ├─ Docker build
│   │   └─ Docker run
│   │
│   ├─ CI/CD cơ bản
│   │   ├─ Azure DevOps Pipeline
│   │   ├─ Build image
│   │   └─ Deploy container
│   │
│   └─ Kết quả
│       └─ Website chạy online
│
├─ 6. Dọn tài nguyên (TRÁNH MẤT TIỀN)
│   ├─ Stop VM
│   ├─ Delete VM
│   └─ Xóa resource group không dùng
│
├─ 7. Mở rộng kỹ năng DevOps
│   │
│   ├─ CI/CD nâng cao
│   │   ├─ Azure DevOps Pipelines
│   │   ├─ GitHub Actions
│   │   └─ Jenkins
│   │
│   ├─ Container orchestration
│   │   ├─ Kubernetes
│   │   └─ AKS (Azure Kubernetes Service)
│   │
│   ├─ Monitoring
│   │   ├─ Azure Monitor
│   │   ├─ Log Analytics
│   │   └─ Application Insights
│   │
│   └─ Infrastructure as Code
│       └─ ARM Templates / Terraform
│
├─ 8. Chuẩn bị thi chứng chỉ
│   │
│   ├─ Target:
│   │   └─ Microsoft Certified: DevOps Engineer Expert
│   │
│   ├─ Kiến thức cần có
│   │   ├─ CI/CD pipelines (Azure DevOps)
│   │   ├─ Infrastructure automation
│   │   ├─ Security & Identity (Azure AD)
│   │   ├─ Monitoring & logging
│   │   └─ Container & Kubernetes
│   │
│   ├─ Practice
│   │   ├─ Lab nhiều lần
│   │   ├─ Practice exam
│   │   └─ Scenario-based questions
│   │
│   └─ Điều kiện thực tế
│       ├─ 1–2 năm kinh nghiệm (hoặc lab tương đương)
│       └─ Hiểu hệ thống end-to-end
│
└─ 9. Insight quan trọng
    ├─ DevOps = thực hành liên tục
    ├─ Azure DevOps = mạnh về CI/CD enterprise
    ├─ AKS = Kubernetes production
    ├─ Sai lầm lớn:
    │   └─ Không học Azure AD & pipeline
    └─ Lộ trình đúng:
        └─ Setup → Lab → Project → Certification
```
---

# ☁️ 4. Google Cloud DevOps Learning Path (Online)

🎯 Target: Google Professional DevOps Engineer

## Nội dung chính:
- Google Cloud setup
- Cloud Build (CI/CD)
- Kubernetes (GKE)
- Monitoring (Cloud Monitoring)
- SRE principles
- Logging & Alerting
- Deploy system lên GCP

## Mindmap:
<!-- Dán mindmap GCP vào đây -->

```
Google Cloud DevOps Learning Path (From Account → Certification Ready)
│
├─ 1. Tạo Google Cloud Account (5–10 phút)
│   ├─ Bước 1: Truy cập website
│   │   └─ console.cloud.google.com → Get started
│   │
│   ├─ Bước 2: Đăng nhập
│   │   ├─ Gmail account
│   │   └─ Thông tin cá nhân
│   │
│   ├─ Bước 3: Thêm thanh toán
│   │   ├─ Visa / Mastercard
│   │   └─ Dùng để xác minh
│   │
│   ├─ Bước 4: Free tier
│   │   ├─ $300 credit (90 ngày)
│   │   └─ Một số dịch vụ always free
│   │
│   └─ Bước 5: Tạo Project
│       └─ Project = đơn vị quản lý tài nguyên
│
├─ 2. Quản lý chi phí (CỰC QUAN TRỌNG)
│   │
│   ├─ Setup Billing Alert
│   │   ├─ Vào Billing → Budgets & alerts
│   │   └─ Tạo:
│   │       ├─ Limit: 5–10 USD
│   │       └─ Alert: 50% / 80% / 100%
│   │
│   ├─ Mục tiêu
│   │   ├─ Tránh phát sinh phí
│   │   └─ Kiểm soát usage
│   │
│   └─ Nguyên tắc
│       ├─ Luôn kiểm tra billing
│       └─ Tắt resource khi không dùng
│
├─ 3. Tạo server (Compute Engine)
│   │
│   ├─ Create VM Instance
│   │   ├─ Machine type: e2-micro (free tier)
│   │   ├─ OS: Ubuntu / Debian
│   │   └─ Disk: ~10GB
│   │
│   ├─ Firewall
│   │   ├─ Allow HTTP (80)
│   │   ├─ Allow HTTPS (443)
│   │   └─ SSH (22)
│   │
│   ├─ Public Access
│   │   ├─ External IP
│   │   └─ Truy cập qua browser
│   │
│   └─ Connect server
│       ├─ SSH trên web console
│       └─ Hoặc ssh local
│
├─ 4. Setup môi trường DevOps (Docker)
│   │
│   ├─ Cài Docker
│   │   ├─ apt update
│   │   ├─ apt install docker.io
│   │   ├─ systemctl start docker
│   │   └─ usermod -aG docker user
│   │
│   ├─ Test
│   │   └─ docker run hello-world
│   │
│   └─ Mục tiêu
│       ├─ Chạy container
│       └─ Chuẩn bị deploy app
│
├─ 5. Lab DevOps cơ bản
│   │
│   ├─ Deploy web đơn giản
│   │   ├─ docker run -p 80:80 nginx
│   │   └─ Truy cập qua IP
│   │
│   ├─ Build app
│   │   ├─ Clone project
│   │   ├─ Docker build
│   │   └─ Docker run
│   │
│   ├─ CI/CD cơ bản
│   │   ├─ Cloud Build
│   │   ├─ Build image
│   │   └─ Deploy container
│   │
│   └─ Kết quả
│       └─ Website chạy online
│
├─ 6. Dọn tài nguyên (TRÁNH MẤT TIỀN)
│   ├─ Stop VM
│   ├─ Delete VM
│   └─ Xóa project hoặc resource không dùng
│
├─ 7. Mở rộng kỹ năng DevOps
│   │
│   ├─ CI/CD nâng cao
│   │   ├─ Cloud Build
│   │   ├─ Cloud Deploy
│   │   └─ GitHub Actions
│   │
│   ├─ Container orchestration
│   │   ├─ Kubernetes
│   │   └─ GKE (Google Kubernetes Engine)
│   │
│   ├─ Monitoring
│   │   ├─ Cloud Monitoring
│   │   ├─ Cloud Logging
│   │   └─ Alerting policies
│   │
│   ├─ Infrastructure as Code
│   │   └─ Terraform / Deployment Manager
│   │
│   └─ SRE (Site Reliability Engineering)
│       ├─ SLI / SLO / SLA
│       ├─ Error budget
│       └─ Reliability mindset
│
├─ 8. Chuẩn bị thi chứng chỉ
│   │
│   ├─ Target:
│   │   └─ Google Professional DevOps Engineer
│   │
│   ├─ Kiến thức cần có
│   │   ├─ CI/CD pipelines (Cloud Build)
│   │   ├─ Monitoring & alerting
│   │   ├─ Kubernetes (GKE)
│   │   ├─ Reliability (SRE)
│   │   └─ Security & IAM
│   │
│   ├─ Practice
│   │   ├─ Lab nhiều lần
│   │   ├─ Case study
│   │   └─ Scenario-based questions
│   │
│   └─ Điều kiện thực tế
│       ├─ 1–2 năm kinh nghiệm (hoặc lab)
│       └─ Hiểu hệ thống production
│
└─ 9. Insight quan trọng
    ├─ Google = DevOps theo hướng SRE
    ├─ Monitoring + reliability = trọng tâm
    ├─ GKE = Kubernetes mạnh nhất trong 3 cloud
    ├─ Sai lầm lớn:
    │   └─ Bỏ qua SRE concepts
    └─ Lộ trình đúng:
        └─ Setup → Lab → Project → Certification
```
---

# 🔁 5. Multi-Cloud Mapping (Quan trọng)

🎯 Mục tiêu:  
- Hiểu 1 lần → áp dụng 3 cloud  
- Không bị phụ thuộc vào 1 nền tảng  
- Nắm concept thay vì học thuộc service  

---

## 🧠 5.1. Core Mapping (Overview)

| Concept      | AWS         | Azure            | Google Cloud       |
|--------------|------------|------------------|--------------------|
| Compute      | EC2        | Virtual Machine  | Compute Engine     |
| Storage      | S3         | Blob Storage     | Cloud Storage      |
| CI/CD        | CodePipeline | Azure DevOps   | Cloud Build        |
| Kubernetes   | EKS        | AKS              | GKE                |
| Monitoring   | CloudWatch | Azure Monitor    | Cloud Monitoring   |

---

## ⚙️ 5.2. DevOps Mapping (Thực chiến)

### 🖥️ Compute & Scaling

| Use Case         | AWS                | Azure                  | GCP                      |
|------------------|--------------------|------------------------|--------------------------|
| VM               | EC2                | Virtual Machine        | Compute Engine           |
| Auto Scaling     | Auto Scaling Group | VM Scale Set           | Managed Instance Group   |
| Load Balancer    | ALB / NLB          | Azure LB / App Gateway | Cloud Load Balancing     |

---

### 📦 Container & Kubernetes

| Use Case           | AWS     | Azure                | GCP               |
|--------------------|---------|----------------------|-------------------|
| Container runtime  | ECS     | Container Instances  | Cloud Run         |
| Kubernetes         | EKS     | AKS                  | GKE               |
| Container Registry | ECR     | ACR                  | Artifact Registry |

---

### 🔄 CI/CD & Automation

| Use Case        | AWS            | Azure            | GCP           |
|----------------|----------------|------------------|---------------|
| CI/CD          | CodePipeline   | Azure DevOps     | Cloud Build   |
| Deploy         | CodeDeploy     | Release Pipeline | Cloud Deploy  |
| Alternative    | GitHub Actions | GitHub Actions   | GitHub Actions|

---

### 🔐 Identity & Security

| Use Case        | AWS              | Azure        | GCP             |
|----------------|------------------|--------------|-----------------|
| IAM            | IAM              | Azure AD     | IAM             |
| Secrets        | Secrets Manager  | Key Vault    | Secret Manager  |
| Access Control | IAM Roles        | RBAC         | IAM Roles       |

---

### 📊 Monitoring & Logging

| Use Case   | AWS               | Azure           | GCP               |
|------------|------------------|-----------------|-------------------|
| Metrics    | CloudWatch       | Azure Monitor   | Cloud Monitoring  |
| Logging    | CloudWatch Logs  | Log Analytics   | Cloud Logging     |
| Alerting   | CloudWatch Alarm | Alerts          | Alerting Policies |

---

### 🏗️ Infrastructure as Code

| Use Case      | AWS             | Azure           | GCP                  |
|---------------|-----------------|-----------------|----------------------|
| Native IaC    | CloudFormation  | ARM Templates   | Deployment Manager   |
| Multi-cloud   | Terraform       | Terraform       | Terraform            |

---

## 🔄 5.3. Mapping Local → Cloud

| Local Tool        | AWS        | Azure            | GCP            |
|------------------|-----------|------------------|----------------|
| Docker           | ECS / ECR | ACI / ACR        | Cloud Run      |
| Kubernetes       | EKS       | AKS              | GKE            |
| Docker Compose   | ECS Task  | Container Apps   | Cloud Run      |
| Nginx            | ALB       | App Gateway      | Load Balancer  |
| GitHub Actions   | CodePipeline | Azure DevOps | Cloud Build    |

---

## 🔥 5.4. Insight quan trọng

- DevOps = học **concept**, không phải tool  
- 90% cloud chỉ khác:
  - Tên service  
  - UI  
  - Cách config  

---

### 💡 Rule vàng

```text
Hiểu Docker → dùng được ECS / ACI / Cloud Run  
Hiểu Kubernetes → dùng được EKS / AKS / GKE  
Hiểu CI/CD → dùng được mọi pipeline  
```

---

### ⚠️ Sai lầm phổ biến

- ❌ Học từng cloud riêng lẻ  
- ❌ Không map kiến thức  
- ❌ Nghĩ mỗi cloud là một thế giới khác  

👉 Cách đúng:

```text
1 kiến thức → 3 cloud
```

---

## ✅ 5.5. Checkpoint

- ✔️ Biết mapping service giữa 3 cloud  
- ✔️ Deploy cùng 1 project lên ≥ 2 cloud  
- ✔️ Hiểu sự khác nhau (pricing / config / UI)  
- ✔️ Không bị bỡ ngỡ khi chuyển cloud  

---

# 🎯 6. Chiến lược học (Rất quan trọng)

## 🧱 Giai đoạn 1 – Foundation (Local)

**🎯 Mục tiêu:**
- Hiểu bản chất DevOps (không phụ thuộc cloud)
- Nắm vững Docker, Kubernetes, CI/CD
- Xây dựng được hệ thống chạy hoàn toàn trên máy cá nhân

### Nội dung cần học

- **Nền tảng cơ bản**
  - Git workflow: clone → branch → commit → push
  - Linux cơ bản: file system, process, networking
  - HTTP / REST API

- **Docker (Cốt lõi)**
  - Dockerfile, Image vs Container
  - docker build / docker run
  - Volume, Network

- **Microservices**
  - Xây nhiều service (auth, user, order)
  - API Gateway (nginx)
  - Giao tiếp qua HTTP

- **Kubernetes (Local)**
  - Công cụ: Minikube hoặc Kind
  - Pod, Deployment, Service
  - ConfigMap, Secret
  - Scale hệ thống

- **CI/CD (Automation)**
  - GitHub Actions hoặc Jenkins
  - Pipeline: Code → Build → Test → Deploy

- **Monitoring cơ bản**
  - docker logs
  - Debug lỗi container
  - Quan sát CPU / RAM

### ✅ Checkpoint (Bắt buộc đạt)

- ✔️ Containerize được ứng dụng
- ✔️ Chạy nhiều service bằng Docker Compose
- ✔️ Deploy được lên Kubernetes local
- ✔️ Có CI/CD pipeline tự động deploy
- ✔️ Có 1 project DevOps hoàn chỉnh trên GitHub

---

## ☁️ Giai đoạn 2 – Cloud

**🎯 Mục tiêu:**
- Áp dụng kiến thức local lên môi trường cloud
- Hiểu hệ thống production thực tế

### Nội dung cần học

- **Chọn cloud chính**
  - AWS (khuyến nghị) / Azure / Google Cloud

- **Mapping Local → Cloud**
  - Docker → ECS / AKS / GKE
  - Kubernetes → EKS / AKS / GKE
  - Server → EC2 / VM
  - CI/CD → CodePipeline / Azure DevOps / Cloud Build

- **Deploy project**
  - Build Docker image
  - Push lên container registry
  - Deploy lên cloud

- **Cloud services cơ bản**
  - Compute (EC2 / VM)
  - Storage (S3 / Blob / Cloud Storage)
  - IAM (phân quyền)
  - Monitoring

### ✅ Checkpoint

- ✔️ Deploy thành công project lên cloud
- ✔️ Có public URL truy cập
- ✔️ Hiểu cách hệ thống hoạt động trên production

---

## 🏆 Giai đoạn 3 – Certification

**🎯 Mục tiêu:**
- Pass chứng chỉ DevOps cloud
- Hiểu các bài toán thực tế (scenario-based)

### Nội dung cần học

- **Ôn theo exam guide**
  - Domain kiến thức
  - Trọng số từng phần

- **Practice**
  - Làm lab nhiều lần
  - Làm practice test
  - Đọc case study

- **Tư duy làm bài**
  - High availability
  - Scalability
  - Security
  - Cost optimization

### ✅ Checkpoint

- ✔️ Làm được mock exam ≥ 70–80%
- ✔️ Hiểu rõ các scenario thực tế
- ✔️ Sẵn sàng đăng ký thi

---

## 🔥 Tổng kết chiến lược

```text
Local → Hiểu bản chất
→ Project → Thực chiến
→ Cloud → Áp dụng thực tế
→ Certification → Xác nhận năng lực
```text

# ⚠️ 7. Sai lầm cần tránh

## ❌ 7.1. Học cloud ngay từ đầu

**Vấn đề:**
- Nhảy vào AWS/Azure/GCP khi chưa hiểu Docker/Kubernetes
- Chỉ biết “bấm console” mà không hiểu hệ thống

**Hậu quả:**
- Không hiểu lỗi khi xảy ra
- Không pass được câu hỏi scenario trong chứng chỉ
- Tốn tiền cloud vô ích

**Cách tránh:**
- Học LOCAL trước (Docker → Kubernetes → CI/CD)
- Chỉ lên cloud khi đã có project chạy local

---

## ❌ 7.2. Không làm project

**Vấn đề:**
- Học nhiều khóa nhưng không build gì
- Không có sản phẩm thực tế

**Hậu quả:**
- Không có portfolio
- Không trả lời được phỏng vấn
- Không hiểu hệ thống end-to-end

**Cách tránh:**
- Bắt buộc làm ít nhất:
  - 1 project microservices
  - Có Docker + Kubernetes + CI/CD
- Đưa lên GitHub (README rõ ràng)

---

## ❌ 7.3. Chỉ học lý thuyết

**Vấn đề:**
- Xem video, đọc tài liệu nhưng không thực hành
- Biết khái niệm nhưng không làm được

**Hậu quả:**
- Quên nhanh
- Không debug được lỗi
- Không deploy được hệ thống

**Cách tránh:**
- Học tới đâu → làm lab tới đó
- Mỗi concept phải có:
  - Command thực tế
  - Demo chạy được

---

## ❌ 7.4. Không hiểu bản chất Docker / Kubernetes

**Vấn đề:**
- Copy lệnh mà không hiểu
- Không biết container/network hoạt động thế nào

**Hậu quả:**
- Không debug được lỗi production
- Không scale được hệ thống
- Fail câu hỏi nâng cao trong exam

**Cách tránh:**
- Hiểu rõ:
  - Docker: image, container, volume, network
  - Kubernetes: pod, deployment, service
- Tự viết config (không copy hoàn toàn)

---

## ❌ 7.5. Học quá nhiều tool cùng lúc

**Vấn đề:**
- Jenkins + GitLab CI + GitHub Actions cùng lúc
- Terraform + CloudFormation + ARM Templates

**Hậu quả:**
- Loạn kiến thức
- Không tool nào thành thạo

**Cách tránh:**
- Chọn 1 tool mỗi loại:
  - CI/CD: GitHub Actions
  - IaC: Terraform
- Thành thạo rồi mới mở rộng

---

# 🔥 8. Insight quan trọng

## 💡 8.1. DevOps = Practice > Theory

- 80% kỹ năng đến từ thực hành
- 20% là lý thuyết

👉 Nguyên tắc:
- “Không chạy được = chưa học xong”

---

## 💡 8.2. Docker + Kubernetes = Core skill

- Docker → đóng gói ứng dụng
- Kubernetes → vận hành hệ thống

👉 Nếu yếu 2 cái này:
- Không làm được DevOps thực tế
- Không pass chứng chỉ nâng cao

---

## 💡 8.3. Cloud = Tool, không phải mục tiêu

- AWS / Azure / GCP chỉ là công cụ
- Quan trọng là:
  - Architecture
  - Automation
  - Reliability

👉 Người giỏi:
- Có thể chuyển cloud dễ dàng

---

## 💡 8.4. 1 project tốt > 10 khóa học

- Recruiter không quan tâm bạn học bao nhiêu khóa
- Họ quan tâm:
  - Bạn build được gì?

👉 Project tốt cần có:
- Microservices
- Docker
- Kubernetes
- CI/CD
- Deploy cloud

---

## 💡 8.5. Hiểu hệ thống end-to-end là lợi thế lớn

- Code → Build → Test → Deploy → Monitor

👉 Nếu bạn hiểu full flow:
- Đi phỏng vấn cực mạnh
- Làm việc thực tế nhanh

---

# 🚀 9. Mục tiêu cuối

## 🎯 9.1. Technical Goals

- ✔️ Xây dựng được hệ thống microservices hoàn chỉnh
- ✔️ Containerize bằng Docker
- ✔️ Deploy bằng Kubernetes
- ✔️ Setup CI/CD pipeline tự động
- ✔️ Monitor & debug hệ thống

---

## ☁️ 9.2. Cloud Goals

- ✔️ Deploy project lên AWS / Azure / GCP
- ✔️ Có public URL truy cập
- ✔️ Hiểu IAM, networking, scaling

---

## 🏆 9.3. Certification Goals

- ✔️ Pass ít nhất 1 chứng chỉ:
  - AWS DevOps Engineer / Azure DevOps / GCP DevOps
- ✔️ Hiểu scenario thực tế trong đề thi
- ✔️ Làm mock exam ≥ 70–80%

---

## 💼 9.4. Career Goals

- ✔️ Có GitHub portfolio chuyên nghiệp
- ✔️ Có README mô tả project rõ ràng
- ✔️ Có thể giải thích hệ thống khi phỏng vấn
- ✔️ Apply vị trí DevOps Engineer / Cloud Engineer

---

## 🔥 9.5. Checklist hoàn thành

```text
[ ] Docker vững
[ ] Kubernetes vững
[ ] CI/CD pipeline chạy được
[ ] Có project hoàn chỉnh
[ ] Deploy lên cloud thành công
[ ] Làm được mock exam
[ ] Sẵn sàng đi thi
[ ] Sẵn sàng apply job

# 🔥 Gợi ý thêm (rất đáng giá)
```


