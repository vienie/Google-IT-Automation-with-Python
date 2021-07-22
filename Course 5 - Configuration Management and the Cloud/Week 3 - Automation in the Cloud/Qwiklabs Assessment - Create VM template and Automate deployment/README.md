## Qwiklabs Assessment: Create VM template and Automate deployment

**Missing from the Qwiklab assessment:** 

During the instance template creation, under the '**Identity and API access**', you must select: **Qwiklab User Service Account** 

(as shown in course-5-qwiklab.png)

If you don't, you will not be able to get full access to the API. So when you run this command:
```
gcloud compute instances create --zone us-west1-b --source-instance-template vm1-template vm2 vm3 vm4 vm5 vm6 vm7 vm8
```
it will fail with an error:
```
ERROR: (gcloud.compute.instances.create) Could not fetch resource:
 - Request had insufficient authentication scopes.
```

Also, don't forget to start up your VM instance again after you have create an instance template.
