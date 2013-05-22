import requests
import json

client_key = "" #your client key
api_key = ""	#your api key

CONNECTION_ERROR = "Connection Error:"
SUCCESSFUL = "Done:"



def APICall(adress):
    r = requests.get(adress)
    assert isinstance(r, requests.Response)
    return r.text

def ShowActiveDroplets():
    resp = json.loads(APICall('https://api.digitalocean.com/droplets/?client_id={}&api_key={}'.format(client_key,api_key)))
    if resp["status"] == "OK":
        droplets = resp["droplets"]
        for a in droplets:
            for d in a:
                print('{}:{}'.format(d, a[d]))
            print("----------")
    else:
        print(CONNECTION_ERROR, "Cannot get droplets")

def NewDroplet(name, size_id, image_id,region_id,virtio,ssh_key_ids):
    rawlink = 'https://api.digitalocean.com/droplets/new??client_id={}&api_key={}&name={}&size_id={}&image_id={}&region_id={}&client_id={}&virtio={}&ssh_key_ids={}'
    link = rawlink.format(client_key, api_key, name, size_id, image_id ,region_id, client_key, virtio ,ssh_key_ids)
    resp = json.loads(APICall(link))
    if resp["status"] == "OK":
        print(SUCCESSFUL, "Droplet created")
    else:
        print(CONNECTION_ERROR, "Cannot create droplet")

def DestroyDroplet(droplet_id):
    resp = json.loads(APICall('https://api.digitalocean.com/droplets/{}/destroy/?client_id={}&api_key={}'.format(droplet_id,client_key,api_key)))
    if resp["status"] == "OK":
        print(SUCCESSFUL, "Droplet destroyed")
    else:
        print(CONNECTION_ERROR, "Cannot destroy droplet")

def TakeSnapshot(droplet_id):
    resp = json.loads(APICall('https://api.digitalocean.com/droplets/{}/snapshot/?name=&client_id={}&api_key={}'.format(droplet_id, client_key, api_key)))
    if resp["status" == "OK"]:
        print(SUCCESSFUL, "Droplet snapshot created")
    else:
        print(CONNECTION_ERROR, "Cannot create snapshot")

def ShowAvailableRegions():
    resp = json.loads(APICall('https://api.digitalocean.com/regions/?client_id={}&api_key={}'.format(client_key,api_key)))
    if resp["status"] == "OK":
        regions = resp["regions"]
        for a in regions:
            for d in a:
                print('{}:{}'.format(d, a[d]))
    else:
        print(CONNECTION_ERROR, "Cannot get regions")

def ShowAvailableSizes():
    resp = json.loads(APICall('https://api.digitalocean.com/sizes/?client_id={}&api_key={}'.format(client_key,api_key)))
    if resp["status"] == "OK":
        sizes = resp["sizes"]
        for a in sizes:
            for d in a:
                print('{}:{}'.format(d, a[d]))
    else:
        print(CONNECTION_ERROR, "Cannot get sizes")
