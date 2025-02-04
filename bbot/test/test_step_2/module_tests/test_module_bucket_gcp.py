from .test_module_bucket_aws import *


class TestBucket_GCP(Bucket_AWS_Base):
    provider = "gcp"
    random_bucket_1 = f"{random_bucket_name_1}.storage.googleapis.com"
    random_bucket_2 = f"{random_bucket_name_2}.storage.googleapis.com"
    random_bucket_3 = f"{random_bucket_name_3}.storage.googleapis.com"
    open_bucket_body = """{
  "kind": "storage#testIamPermissionsResponse",
  "permissions": [
    "storage.objects.create",
    "storage.objects.list"
  ]
}"""

    def bucket_setup(self):
        self.url_setup()
        self.website_body = f"""
        <a href="{self.url_1}"/>
        <a href="https://{self.random_bucket_2}"/>
        """

    def url_setup(self):
        self.url_1 = f"{random_bucket_name_1}.storage.googleapis.com"
        self.url_2 = f"https://www.googleapis.com/storage/v1/b/{random_bucket_name_2}/iam/testPermissions?permissions=storage.buckets.setIamPolicy&permissions=storage.objects.list&permissions=storage.objects.get&permissions=storage.objects.create"
        self.url_3 = f"https://www.googleapis.com/storage/v1/b/{random_bucket_name_3}"
