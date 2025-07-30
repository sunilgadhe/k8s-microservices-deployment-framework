#!/bin/bash

eksctl utils associate-iam-oidc-provider --cluster my-eks-cluster --approve

eksctl create iamserviceaccount \
  --name ebs-csi-controller-sa \
  --namespace kube-system \
  --cluster my-eks-cluster \
  --attach-policy-arn arn:aws:iam::aws:policy/service-role/AmazonEBSCSIDriverPolicy \
  --approve \
  --role-only \
  --role-name AmazonEKS_EBS_CSI_Driver_Role \
  --region us-east-1

eksctl create addon --name aws-ebs-csi-driver --cluster my-eks-cluster --service-account-role-arn arn:aws:iam::910322382104:role/AmazonEKS_EBS_CSI_Driver_Role --region us-east-1 --force

#Install Nginx Ingress Controller
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
helm repo update

helm install nginx-ingress ingress-nginx/ingress-nginx \
  --namespace ingress-nginx --create-namespace \
  --set controller.service.type=LoadBalancer \
  --set controller.service.annotations."service\.beta\.kubernetes\.io/aws-load-balancer-internal"="false" \
  --set controller.service.externalTrafficPolicy=Cluster




