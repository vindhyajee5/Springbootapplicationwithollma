<img width="1917" height="1015" alt="image" src="https://github.com/user-attachments/assets/55599fd9-0c5c-4009-9a1f-44d4adfc6e89" />
How to download report

Actions → workflow run → Artifacts → download trivy-report

Then:

python fix_vuln.py


📦 How To Install ArgoCD
Install in Kubernetes:
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
Access UI:
kubectl port-forward svc/argocd-server -n argocd 9292:443
Open:
https://localhost:9292


<img width="1898" height="1082" alt="image" src="https://github.com/user-attachments/assets/6aa3e81f-6ffe-46ed-894d-8ce959100b26" />


 
