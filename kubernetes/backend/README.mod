# README.mod

## Module Overview

This module defines the Kubernetes configurations for deploying and managing a Flask-based backend application. The module includes the necessary resources to:

- Configure environment variables using ConfigMap
- Deploy the Flask app using a Kubernetes Deployment
- Scale the app using a Horizontal Pod Autoscaler (HPA)
- Expose the app via a Kubernetes Service

## Key Resources

This module consists of the following Kubernetes resources:

1. **ConfigMap**
2. **Deployment**
3. **Horizontal Pod Autoscaler (HPA)**
4. **Service**

### 1. **ConfigMap**
The `ConfigMap` provides environment variables needed for the Flask app, such as the Redis host and port.

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: flask-app-config
  namespace: backend-ns
data:
  REDIS_HOST: database-service.database-ns.svc.cluster.local
  REDIS_PORT: "6379"

