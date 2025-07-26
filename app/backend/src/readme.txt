Cross-Namespace Communication

- Use fully qualified domain names (FQDN) to communicate across namespaces.
- Example:
  cache = redis.Redis(host='redis.cache.svc.cluster.local', port=6379)

  redis = Service name of Redis
  cache = Namespace where Redis is deployed
  svc.cluster.local = Default cluster domain suffix

Similarly, if your Nginx needs to communicate with your backend service:
  proxy_pass http://app.backend.svc.cluster.local:5000;

