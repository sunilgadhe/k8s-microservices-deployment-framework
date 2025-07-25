This project showcases a scalable microservices architecture deployed on Kubernetes, with a comprehensive deployment framework featuring end-to-end monitoring, SSL encryption, and Helm charts for efficient deployment management.

Key features include:

Microservices Architecture: A 3-tier application with separate frontend, backend, and database services, each deployed as individual microservices for modularity and scalability.

End-to-End Monitoring: Integrated monitoring using Prometheus and Grafana, enabling real-time observability, metrics collection, and alerting for infrastructure and application performance.

SSL Encryption: Ensures secure, encrypted communication between microservices and external users, maintaining data privacy and integrity.

Helm Charts: Simplified Kubernetes deployment using Helm charts, allowing for easy application management, upgrades, and rollback across environments.

This framework provides an end-to-end solution for deploying, securing, and monitoring microservices on Kubernetes, emphasizing automation, observability, and security.

Technologies Used: Kubernetes

Helm

Prometheus & Grafana (for monitoring)

SSL/TLS (for encryption)

CI/CD pipeline for continuous testing and deployment

The goal of this project is to offer a reusable and robust framework that can be easily adapted for deploying production-grade microservices applications in Kubernetes environments, with built-in security and monitoring features.





*********** Folder Structure *************
eks-prod-cluster/
│
├── k8s/
│   ├── base/
│   │   ├── backend/
│   │   │   ├── statefulset.yaml
│   │   │   ├── service.yaml
│   │   │   ├── pvc.yaml #Optional
│   │   │   ├── hpa.yaml
│   │   │   └── configmap.yaml   # optional
│   │   ├── frontend/
│   │   │   ├── deployment.yaml
│   │   │   ├── service.yaml
│   │   │   ├── hpa.yaml
│   │   │   └── configmap.yaml   # optional
│   │   ├── ingress/
│   │   │   ├── ingress.yaml
│   │   │   └── tls-secret.yaml
│   │   ├── storage/
│   │   │   └── storageclass.yaml
│   │   ├── secrets/
│   │   │   ├── dockerhub-secret.yaml
│   │   │   └── tls-secret.yaml
│   │   └── namespaces/
│   │       └── app-namespace.yaml
│
├── charts/                   # Optional: Helm charts if you prefer templating
│   ├── frontend-chart/
│   └── backend-chart/
│
├── scripts/                  # Utility scripts
│   ├── deploy.sh
│   └── cleanup.sh
│
├── infra/                    # Infra as code (optional)
│   ├── eksctl/
│   │   └── eks-cluster.yaml
│   ├── terraform/            # Or use Terraform instead
│   │   ├── main.tf
│   │   └── route53.tf
│
└── README.md


*****************************
# two_tier_app_k8
****************************



*********************************************************
*********************************************************
1. Create cluster config file
2. Create eks cluster
1. Install add-on packages (Ingress Controller, EBS CSI Driver #Optional: Only if your app uses PersistentVolumeClaims with storageClassName: gp2, gp3)
1. Create k8 secrets to pull image & ssl/tls secret for ssl termination
3. Create manufest as per requirement
4. Deploy resources using manifest
   kubectl apply -f manifests/namespaces -R	# First create namepaces
   kubectl apply -f manifests -R	# Deploy other resources 


*********************************************************
Deploy Web-clicker flask app from end-to end

  - create yaml files
  - Configure EKS cluster
  - create cluster with two nodegroups
                    eksctl create cluster \
                  --name my-eks-cluster \
                  --region us-east-1 \
                  --nodegroup-name standard-workers \
                  --node-type t3.small \
                  --nodegroup-name frontend \
                  --nodegroup-name backend \
                  --nodes 1 \
                  --nodes-min 1 \
                  --nodes-max 3 \
                  --managed
  - Create k8 secrets to pull private images & configure ssl/tls certificate

    
  - Create ssl/tls secrets

  - Enable OIDC provide on EKS cluster
    eksctl utils associate-iam-oidc-provider --cluster $cluster_name --approve

  - Install the AWS EBS CSI Driver #CSI driver responsible for privisioning ebs for pods
    # But this process is less secure, use seperate IAM role for CSI driver
 
                  eksctl create addon \
                    --name aws-ebs-csi-driver \
                    --cluster my-eks-cluster \
                    --service-account-role-arn arn:aws:iam::910322382104:role/eksctl-my-eks-cluster-nodegroup-ba-NodeInstanceRole-cqHw0GQDP5Pa \
                    --force

  - Start deploying one by one all k8 resources using yaml
    kubectl apply -f namespace/
    kubectl apply -f backend/
    kubectl apply -f frontend/
    kubectl apply -f ingress/


  - Deploy Ingress Controller 

  - update Security groups to allow traffic
