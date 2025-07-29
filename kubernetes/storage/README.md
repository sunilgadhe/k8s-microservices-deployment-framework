## Infrastructure used to provision ebs volume for Redis pod
- Redis is a staefull application, need persistent volume.

### 1. StorageClass
- In Kubernetes, a StorageClass is a way to define how storage is provisioned dynamically. It acts like a blueprint for storage, describing what type of storage you want, and how it should be created.

### 2. PersistentVolumeClaim
- It is a request for storage by a user or application.
- It asks for storage of a certain size, access mode, and possibly StorageClass.
- Kubernetes binds it to a suitable PersistentVolume (PV) — either existing or dynamically provisioned.
- Once bound, a PVC is used by a pod as a volume.

## Provisioning of EBS volumes dynamically for pods
- Follow below steps 
- Step 1: Install necessary packages (AWS EBS Driver)
- Step 2: Create StorageClass
- Step 2: Create PVC
