****************************************************************
                        Install AWS EBS Driver
****************************************************************


1. Install Helm
   helm repo add eks https://aws.github.io/eks-charts

2. Update Helm 
   helm repo update 

3. Install EBS CSI Driver
   helm upgrade --install aws-ebs-csi-driver \
      --namespace kube-system \
      aws-ebs-csi-driver/aws-ebs-csi-driver

4. Create a StorageClass for EBS (if not already defined) #optional
5. Deploy Your Workloads (StatefulSet, PVCs, etc.)  #optional


#############Troubleshooting################
1. If pvc is not getting created properly

  To get CSI pods
  kubectl get pods -n kube-system -l app.kubernetes.io/name=aws-ebs-csi-driver

  To get CSI container logs
  kubectl logs -n kube-system <container_name>




****************************************************************
		 Install Ingress Controller
****************************************************************

1. Configure IAM OIDC provider
   eksctl utils associate-iam-oidc-provider --cluster <cluster_name> --approve

2. Setup alb add on
   Download IAM policy
   curl -O <github_polict_url> 

  Create IAM Policy
  aws iam create-policy \
    --policy-name AWSLoadBalancerControllerIAMPolicy \
    --policy-document file://iam_policy.json

  Create IAM Role
  eksctl create iamserviceaccount \
      --cluster=eks-cluster \
      --namespace=kube-system \
      --name=aws-load-balancer-controller \
      --role-name=AmazonEKSLoadBalancerControllerRole \
      --attach-policy-arn=arn:aws:iam::910322382104:policy/AWSLoadBalancerControllerIAMPolicy \
      --approve

3. Deploy ALB controller

   Add helm repo
   helm repo add eks https://aws.github.io/eks-charts

   Update the repo
   helm repo update eks

   Install
   helm install aws-load-balancer-controller eks/aws-load-balancer-controller -n kube-system \
     --set clusterName=<your-cluster-name> \
     --set serviceAccount.create=false \
     --set serviceAccount.name=aws-load-balancer-controller \
     --set region=<your-region> \
     --set vpcId=<your-vpc-id>

   Verify that the deployments are running.
   kubectl get deployment -n kube-system aws-load-balancer-controller




