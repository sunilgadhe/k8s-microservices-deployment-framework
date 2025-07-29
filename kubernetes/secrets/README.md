## Use command to create k8 secrets as per your requirements

###  To  Configure Docker Registry Secrets

1. Create Secret
  kubectl create secret docker-registry regcred \
  --docker-username=<your-dockerhub-username> \
  --docker-password=<your-dockerhub-password> \
  --docker-email=<your-email> \
  --docker-server=https://index.docker.io/v1/ \
  --namespace=<namespace_name>

2. Configure secret in the deployment manifest

### To Configure SSL/TLS Secrets

1. Buy and download your SSL certificate
  	From GoDaddy, get the .crt and .key files
  	May also include a CA bundle (gd_bundle-g2-g1.crt)

2. Create a Kubernetes TLS Secret
kubectl create secret tls my-tls-secret \
  --cert=yourdomain.crt \
  --key=yourdomain.key \
  -n your-namespace

3. Reference it in your Ingress


### Prerequisite

- Create namespace before creating secrets
