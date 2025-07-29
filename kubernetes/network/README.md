## Kubernetes Networking
- By default kubernetes resourced uses default network policy for communication.
- Communication method changes with the use of namespaces.

### Same Namespace

Redis hostname redis assumes you're running Redis in the same Kubernetes namespace using a Service named redis.
---
- Example: ConfigMap template  
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: flask-app-config
data:
  REDIS_HOST: redis    #redis is a service name
  REDIS_PORT: "6379"

- Update deployment file, container block.
   envFrom:
        - configMapRef:
            name: flask-app-config
---
###  Different Namespace

- If your Flask app and Redis are in different Kubernetes namespaces, then the hostname redis (used in your app) won’t resolve automatically. You need to explicitly reference Redis’s fully qualified domain name (FQDN)
 <service-name>.<namespace>.svc.cluster.local
 eg:  redis.redis-namespace.svc.cluster.local

---
apiVersion: v1
kind: ConfigMap
metadata:
  name: flask-app-config
  namespace: app-namespace
data:
  REDIS_HOST: redis.redis-namespace.svc.cluster.local
  REDIS_PORT: "6379"
---

##  Network Policies

- If you're using NetworkPolicies, make sure the app-namespace is allowed to access services in the redis-namespace. Otherwise, even if DNS resolves, the connection will be blocked.
