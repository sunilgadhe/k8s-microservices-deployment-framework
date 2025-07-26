************************************************
Check aws-load-balancer-controller logs for ssl certificate related errors
************************************************
1. To get all pods
kubectl get pods --all-namespaces 

2. Check logs
kubectl logs aws-load-balancer-controller-5c648b46b5-frpxd -n kube-system
