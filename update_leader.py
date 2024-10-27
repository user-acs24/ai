from kubernetes import client, config
import requests

# Load the Kubernetes configuration
config.load_kube_config()

# Define the API client
v1 = client.CoordinationV1Api()

# Function to update the lease based on AI decision
def update_leader_lease():
    response = requests.get('http://ai-leader-service/leader')
    leader = response.json().get('leader', 'node1')

    lease = {
        "metadata": {"name": "leader-lease"},
        "spec": {
            "holderIdentity": leader,
            "leaseDurationSeconds": 30
        }
    }
    v1.replace_namespaced_lease(name="leader-lease", namespace="default", body=lease)

if __name__ == '__main__':
    update_leader_lease()
