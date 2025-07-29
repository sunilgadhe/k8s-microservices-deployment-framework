# Backend Infrastructure
## Backend infrastructure consist of the following Kubernetes resources
1. ConfigMap
<<<<<<< HEAD
2. Deployment
3. Horizontal Pod Autoscaler (HPA)
4. Services

## 1: ConfigMap

####
- Configure environment variables using ConfigMap

=======
2. Deployment- Deploy the Flask app using a Kubernetes Deployment
3. Horizontal Pod Autoscaler (HPA)- Scale the app using a Horizontal Pod Autoscaler (HPA)
4. Services- Expose the app via a Kubernetes Service

## 1: ConfigMap
- Configure environment variables using ConfigMap
- Following env variables are used in the app
  REDIS_HOST: database-service.database-ns.svc.cluster.local
  REDIS_PORT: "6379"
#### 2. Deployment
- Deploy the Flask app using a Kubernetes Deployment
>>>>>>> 1618fb2 (updated README.md)
