# two_tier_app_k8

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
    docker ser: dckr_pat_FVUePS6BYyhTIgBkjpNspHOljtw (use docker token instead password)
    
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
