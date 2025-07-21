*********************************************************
Create EKS cluster Manually
*********************************************************
1. Creaet a config file (cluster-config.yaml)

2: Create the cluster
   eksctl create cluster -f cluster-config.yaml

3. Conenct to eks cluster
   aws eks update-kubeconfig --name my-eks-cluster --region us-east-1
 
