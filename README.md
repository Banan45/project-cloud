Microservices Platform with Docker & Kubernetes

# Steps to Run:
1. Install Docker, kind, Python.
2. Build Docker images:  
   docker build -t product-service:1.0 .
3. Deploy to Kubernetes:  
   kubectl apply -f product_deployment.yaml
4. Test the API (e.g., using `curl`).
