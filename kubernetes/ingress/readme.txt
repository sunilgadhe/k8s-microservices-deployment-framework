
************************************************
Ingress Resource & Nginx Ingress controller
************************************************
- will use Frontend Ingress for frontend services & Backend Ingress for Flask api (backend.sunilcloud.online)
- A single NGINX Ingress Controller to handle traffic for both services.
- By using an Ingress for external access to the backend service, you can keep the backend service as a ClusterIP (internal only) while exposing it via Ingress to the outside world through HTTPS. This avoids the need for exposing the backend with an external Load Balancer or changing its type to NodePort.

Step 1: Create Ingress for Frontend
Step 2: Create Ingress for Backend
Step 3: Ensure Your Ingress Controller is Configured
Step 4: - Configure Route 53
        Go to Route 53 Console:
	Open Route 53 in AWS.
	Navigate to the Hosted Zone for sunilcloud.online.

	- Create a CNAME Record:
	Name: backend.sunilcloud.online
	Type: CNAME
	Value: The DNS name of your Ingress Controller’s Load Balancer (e.g., aafc132bdecc1483880f0adad670bce7-1612644691.us-east-1.elb.amazonaws.com).
Step 5: Test the Setup
	nslookup backend.sunilcloud.online
	
	- Check HTTPS Access:
	curl -v https://backend.sunilcloud.online

************************************************
Check aws-load-balancer-controller logs for ssl certificate related errors
************************************************
1. To get all pods
kubectl get pods --all-namespaces

2. Check logs
kubectl logs aws-load-balancer-controller-5c648b46b5-frpxd -n kube-system


