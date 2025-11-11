# 🔐 Azure Authentication Tester for Log Analytics

A simple, **safe** Python tool to test multiple **Azure authentication methods** for access to **Azure Log Analytics** — without running any actual queries.

This helps you quickly verify whether your environment (local, VM, Azure Function, etc.) can successfully authenticate to Azure using different credentials.

---

## 🚀 Features

✅ Tests these authentication methods:
- Managed Identity (`ManagedIdentityCredential`)
- Azure CLI (`AzureCliCredential`)
- Visual Studio Code (`VisualStudioCodeCredential`)
- Default Azure Credential (`DefaultAzureCredential`)

✅ Acquires a **token only** — no queries or writes are made  
✅ Works in **any environment** (local, cloud, or container)  
✅ Prints a clear success/failure message for each method  

---

## 🧰 Requirements

- Python **3.8+**
- Azure SDK packages:
  - `azure-identity`
  - `azure-monitor-query`

Install dependencies:

```bash
pip install -r requirements.txt
````

---

## 🧑‍💻 Usage

1. **Clone this repository**

   ```bash
   git clone https://github.com/<your-username>/azure-auth-tester.git
   cd azure-auth-tester
   ```

2. **Run the authentication tester**

   ```bash
   python test_azure_auth_loganalytics.py
   ```

3. **Example output**

   ```
   🔐 Testing authentication methods...
   Testing Managed Identity... ❌ FAILED: ManagedIdentityCredential authentication unavailable, no managed identity endpoint found.
   Testing Azure CLI... ✅ SUCCESS
   ```

4. If at least one method succeeds, you can reuse that `credential` object in your own Azure SDK scripts.

---

## 🧩 Example Integration

```python
from azure.monitor.query import LogsQueryClient

# Use the credential that succeeded in the test
client = LogsQueryClient(credential)
```

---

## ⚠️ Notes

* This script **only tests token acquisition** and **does not execute any queries**.
* You can safely run it in any environment.
* Ideal for verifying authentication setup in:

  * Developer machines
  * Azure VMs
  * Azure App Services
  * Function Apps
  * Containers

---

## 🧾 License

MIT License © 2025
Feel free to use and modify this for your own Azure projects.
