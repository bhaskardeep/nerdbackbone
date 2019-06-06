----
This project is showing a how a Kubernetes cluster can read secrets and certificates from a Azure Key Vault store. It performs that using two methodologies:

1) Using stored Service Princial <br/>
2) Using MSI based pod identity

The following commands provide the basic dev flow to work with a docker conatiner through kubernates:

##Build the Docker Image
1) Create the Dockerfile in the root of your application
2) Run the below commands to build the images
```bash
docker build -t basicwebservice
docker images (to verify that your image is build)
```

##Uploading the Dokcer image to the ACR (Azure Container Registry)
1) Login to you Azure ACL account
```bash
az login
az acr login --name MyAcrRegistry
```
2) Retag the image for the registry and push it
```bash
docker tag basicwebservice acr_server_name/basicwebservice:v1
docker push acr_server_name/basicwebservice:v1
```

##Deploying the image to a K8s Cluster
1) Create the YAML file for your application. Ensure you have the ACR details in the YAML file, so that k8s can pull the image from the registry and deploy it.
2) Run the command to deploy the image
```bash
kubectl apply -f <<path to the YAML file>> -n <<namespace>>
kubectl get services -o wide -n <<namespace>>
```
