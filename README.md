# خدمة المنتجات باستخدام Microservices

## فكرة المشروع  
إنشاء خدمة مصغرة (Microservice) لإدارة المنتجات باستخدام Docker وKubernetes.  
تم الاعتماد على Kind لإنشاء Kubernetes Cluster محلي لتشغيل الخدمة.

---

## الأدوات المستخدمة  
- **Python + Flask**: لبناء API بسيط لإدارة المنتجات.  
- **Docker**: لإنشاء صورة الحاوية وتشغيل الخدمة.  
- **Kubernetes (Kind)**: لنشر الخدمة داخل Cluster محلي.  
- **kubectl**: لإدارة الـ Cluster والتعامل مع الموارد.

---

## هيكل المشروع  

project-cloud/
│
├── product_service.py         # الكود الخاص بخدمة المنتجات
├── Dockerfile                 # لبناء صورة Docker
├── product_deployment.yaml   # تعريف الـ Deployment في Kubernetes
├── product_service.yaml       # (جديد) تعريف Service للتعامل مع الخدمة
└── README.md                  # هذا الملف

---

## خطوات التشغيل والاختبار

### 1. بناء صورة Docker:
```bash
docker build -t product-service:1.0 .

2. إنشاء Kubernetes Cluster باستخدام Kind:

kind create cluster

3. نشر التطبيق داخل Kubernetes:

kubectl apply -f product_deployment.yaml
kubectl apply -f product_service.yaml

4. عمل Port Forward للاختبار:

kubectl port-forward service/product-service 5001:5001

5. اختبار الخدمة باستخدام curl:

curl -X POST http://localhost:5001/add_product \
     -H "Content-Type: application/json" \
     -d '{"name": "Laptop", "price": 999}'

curl http://localhost:5001/products



⸻

ملاحظات إضافية
	•	تم تشغيل واختبار الخدمة بنجاح محليًا.
	•	يمكن التوسع لاحقًا بإضافة خدمات أخرى مثل: إدارة الطلبات، إدارة المستخدمين، بوابة API Gateway، إلخ.

⸻

لقطات شاشة (Screenshots)

أدرجي هنا صور من Postman أو الـ Terminal مثل:
	•	Docker build
	•	kubectl get pods
	•	اختبار الإضافة والعرض عبر curl أو Postman

---

## **ثانيًا: ملف `product_service.yaml` لتعريف Service في Kubernetes**

ضيفي هذا الملف داخل المستودع باسم `product_service.yaml`:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: product-service
spec:
  selector:
    app: product-service
  ports:
    - protocol: TCP
      port: 5001
      targetPort: 5001
  type: ClusterIP