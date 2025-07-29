If LB not receiving web traffic
To check Load Balancer is internal or internet facing
If you get below, it means it is internal facing LB
curl -v http://k8s-frontend-frontend-1573becf73-eea17db1c18b5f61.elb.us-east-1.amazonaws.com

* processing: http://k8s-frontend-frontend-1573becf73-eea17db1c18b5f61.elb.us-east-1.amazonaws.com
*   Trying 192.168.90.28:80...
---
To resolve: add annotations in service conf
  annotations:
    service.beta.kubernetes.io/aws-load-balancer-type: "nlb"
    service.beta.kubernetes.io/aws-load-balancer-internal: "false"


************************************
To test posrt connectivity from front end pod to backend pod
***********************************
Test actual TCP connectivity to Redis
From your frontend pod shell:
nc -zv backend-service.backend-ns 6379

or, if nc isn’t available:
telnet backend-service.backend-ns 6379

************************************
Redis connectivity from inside front end pod
************************************
nslookup backend-service.backend-ns.svc.cluster.local

## Frontend infrastructure consist of the following Kubernetes resources
1. Deployment
2. HorizontalPodAutoscaler
3. Service
4. ConfigMap

### 1. Deployment
- Deploy the Nginx app using a Kubernetes Deployment
- Private Image is used in deployment which contains html/java script script 
### 2. HorizontalPodAutoscaler
- Scale the app using a Horizontal Pod Autoscaler (HPA)

### 3. Service
- Expose the app via a Kubernetes Service caleed ClusterIP

### 4. ConfigMap
- Configure environment variables using ConfigMap

