# ---- Safely tests Azure authentication methods for Log Analytics access without executing queries. ---- #

import sys
from azure.identity import DefaultAzureCredential, ManagedIdentityCredential, AzureCliCredential, VisualStudioCodeCredential
from azure.monitor.query import LogsQueryClient

def test_authentication_methods():
    """Test different authentication methods"""
    methods = [
        ("Managed Identity", ManagedIdentityCredential),
        ("Azure CLI", AzureCliCredential),
        ("VS Code", VisualStudioCodeCredential),
        ("Default", DefaultAzureCredential)
    ]
    
    for method_name, cred_class in methods:
        try:
            print(f"Testing {method_name}...", end=" ")
            credential = cred_class()
            # Test with a simple operation
            client = LogsQueryClient(credential)
            # Try a simple query or just test token acquisition
            token = credential.get_token("https://api.loganalytics.io/.default")
            print("✅ SUCCESS")
            return credential
        except Exception as e:
            print(f"❌ FAILED: {e}")
    
    return None

# Replace your credential initialization with:
print("🔐 Testing authentication methods...")
credential = test_authentication_methods()
if credential is None:
    print("❌ No authentication method worked!")
    sys.exit(1)

client = LogsQueryClient(credential)
