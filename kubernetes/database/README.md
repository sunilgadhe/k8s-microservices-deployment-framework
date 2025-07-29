##Database infrastructure consist of the following Kubernetes resources
1. StatefulSet
2. Service

#### 1. StatefulSet
- StatefulSet is used to deploy statefull applications
- Used to deploy Redis with ebs as persistent volume
- In this, public redis image is used.

#### 2. Service
- Expose the Redis via a Kubernetes Service called ClusterIP
- Backend flask app access this Redis uisng DNS 
- DNS Syntax: service.namespace.svc.cluster.local
