
****************************************************************
		 Install Ingress Controller
****************************************************************

1. Configure IAM OIDC provider
   eksctl utils associate-iam-oidc-provider --cluster <cluster_name> --approve

2. Setup ALB add on
   Create IAM policy for ALB with name "AWSLoadBalancerControllerIAMPolicy":
   aws iam create-policy \
    --policy-name AWSLoadBalancerControllerIAMPolicy \
    --policy-document file://alb_iam_policy.json
   
3. Create IAM Role
  eksctl create iamserviceaccount \
    --name ebs-csi-controller-sa \
    --namespace kube-system \
    --cluster my-eks-cluster \
    --attach-policy-arn arn:aws:iam::aws:policy/service-role/AmazonEBSCSIDriverPolicy \
    --approve \
    --role-only \
    --role-name AmazonEKS_EBS_CSI_Driver_Role \
    --region us-east-1







4. Deploy ALB controller
   Add helm repo:
   helm repo add eks https://aws.github.io/eks-charts

   Update the repo:
   helm repo update eks

   helm install aws-load-balancer-controller eks/aws-load-balancer-controller \
   --namespace kube-system \
   --set clusterName=<cluster_name> \
   --set serviceAccount.create=false \
   --set serviceAccount.name=aws-load-balancer-controller \
   --set region=<region_id> \
   --set vpcId=<cluster_vpc_id>

5. Validate is "aws-load-balancer-controller" pods are running 
   kubectl get pods -n kube-system

   
****************************************************************
			Install AWS EBS Driver
****************************************************************
1. Enable OIDC provide on EKS cluster
   eksctl utils associate-iam-oidc-provider --cluster <cluster_name> --approve

2. Create IAM Role and Kubernetes Service Account (IRSA) using eksctl
   This single command:
   - Creates the IAM Role with the correct trust relationship
   - Attaches the AWS-managed AmazonEBSCSIDriverPolicy
   - Creates and annotates the Kubernetes Service Account (ebs-csi-controller-sa)
 
   eksctl create iamserviceaccount \
     --name ebs-csi-controller-sa \
     --namespace kube-system \
     --cluster <your-cluster-name> \
     --attach-policy-arn arn:aws:iam::aws:policy/AmazonEBSCSIDriverPolicy \
     --approve \
     --role-name AmazonEKS_EBS_CSI_DriverRole

3. Add the AWS EBS CSI Helm Chart Repo
   helm repo add aws-ebs-csi-driver https://kubernetes-sigs.github.io/aws-ebs-csi-driver
   helm repo update

4. Install the EBS CSI Driver via Helm

   helm upgrade --install aws-ebs-csi-driver aws-ebs-csi-driver/aws-ebs-csi-driver \
     --namespace kube-system \
     --set controller.serviceAccount.create=false \
     --set controller.serviceAccount.name=ebs-csi-controller-sa

5. Verify EBS CSI Driver Installation
   You should see the EBS CSI Controller pods running.
   
   kubectl get pods -n kube-system -l "app.kubernetes.io/name=aws-ebs-csi-driver"


6. Create a StorageClass for EBS (if not already defined) #optional
7. Deploy Your Workloads (StatefulSet, PVCs, etc.)  #optional
