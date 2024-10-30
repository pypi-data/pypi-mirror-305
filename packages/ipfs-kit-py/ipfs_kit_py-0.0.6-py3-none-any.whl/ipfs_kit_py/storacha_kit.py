import os
import sys
import subprocess
import requests
import tempfile
import json

class storacha_kit:
    def __init__(self, resources=None, metadata=None):
        self.resources = resources
        self.metadata = metadata
        self.w3_version = "7.8.2"
        self.ipfs_car_version = "1.2.0"
        self.w3_name_version = "1.0.8"
        self.spaces = {}
        self.email_did = None
        self.tokens = {}
        self.https_endpoint = "https://up.storacha.network/bridge"
        self.ipfs_gateway = "https://w3s.link/ipfs/"
        self.space = None
        return None
    
    def space_ls(self):
        space_ls_cmd = "w3 space ls"
        try:
            results = subprocess.check_output(space_ls_cmd, shell=True)
            results = results.decode("utf-8").strip()
            results = results.split("\n")
            results = [i.replace("\n", "").replace("* ", "") for i in results]
            spaces = [i.split(" ") for i in results]
            spaces = {i[1]: i[0] for i in spaces}
            self.spaces = spaces
        except subprocess.CalledProcessError:
            print("space_ls failed")
        return spaces
    
    def space_create(self, space):
        space_create_cmd = "w3 space create " + space
        try:
            results = subprocess.run(space_create_cmd, shell=True, check=True)
        except subprocess.CalledProcessError:
            print("space_create failed")
        return results
    
    def login(self, login):
        login_cmd = "w3 login " + login
        try:
            results = subprocess.run(login_cmd, shell=True, check=True, capture_output=True, text=True)
            ## wait for the user to enter the password
            while True:
                if results.returncode == 0:
                    break
            login_results = results.stdout.strip().replace("\n", "")
            login_results = login_results.replace("⁂ Agent was authorized by ", "")
            self.email_did = login_results
        except subprocess.CalledProcessError:
            print("login failed")
        return login_results
    
    def logout(self):
        logout_cmd = "w3 logout"
        try:
            results = subprocess.run(logout_cmd, shell=True, check=True)
        except subprocess.CalledProcessError:
            print("logout failed")
        return results
    
    def bridge_generate_tokens(self, space, permissions, expiration=None):
        bridge_generate_tokens_cmd = "w3 bridge generate-tokens " + space
        permissions = ["--can '" + i + "'" for i in permissions]
        bridge_generate_tokens_cmd = bridge_generate_tokens_cmd + " " + " ".join(permissions)
        if expiration is None:
            expiration = "date -v +24H +'%Y-%m-%dT%H:%M:%S'"
        else:
            expiration = "date -v +" + expiration + " +'%Y-%m-%dT%H:%M:%S'"
        # expiration = subprocess.check_output(expiration, shell=True)
        # expiration = expiration.decode("utf-8").strip()        
        # expiration = None
        # bridge_generate_tokens_cmd = bridge_generate_tokens_cmd + " --expiration " + expiration
        try:
            results = subprocess.check_output(bridge_generate_tokens_cmd, shell=True)
            results = results.decode("utf-8").strip()
            results = results.split("\n")
            results = [i.replace("\n", "") for i in results if i != ""]
            tokens = [i.split(":") for i in results]
            tokens = {i[0].strip() : i[1].strip() for i in tokens}
            self.tokens[space] = tokens
        except subprocess.CalledProcessError:
            print("bridge_generate_tokens failed")
        return tokens
    
    def storacha_http_request(self, auth_secret, authorization,  method, data):
        url = self.https_endpoint
        headers = {
            "X-Auth-Secret": auth_secret,
            "Authorization": authorization,
        }
        try:
            results = requests.post(url, headers=headers, json=data)
        except requests.exceptions.RequestException as e:
            print(e)
        return results
    
    def install(self):
        detect_w3_cmd = "w3 --version"
        w3_version = self.w3_version
        install_cmd = "sudo npm install -g @web3-storage/w3cli"
        update_cmd = "sudo npm update -g @web3-storage/w3cli"        
        try:
            detect_results = subprocess.check_output(detect_w3_cmd, shell=True)
            version = detect_results.decode("utf-8")
            version = version.split(", ")[1]
            version_list = version.split(".")
            version_list = [int(i.replace("\n", "")) for i in version_list]
            w3_version_list = w3_version.split(".")
            w3_version_list = [int(i.replace("\n", "")) for i in w3_version_list]
            if version_list[0] >= w3_version_list[0] and version_list[1] >= w3_version_list[1] and version_list[2] >= w3_version_list[2]:
                pass
            else:
                update_results = subprocess.run(update_cmd, shell=True, check=True)
                print("storacha_kit updated")                
        except subprocess.CalledProcessError:
            print("storacha_kit not installed")
            detect_npm_cmd = "npm --version"
            try:
                subprocess.run(detect_npm_cmd, shell=True, check=True)
                print("npm installed")
                print("installing storacha_kit")
                try:
                    subprocess.run(install_cmd, shell=True, check=True)
                    print("storacha_kit installed")
                except subprocess.CalledProcessError:
                    print("storacha_kit installation failed")
            except subprocess.CalledProcessError:
                print("npm not installed")
                print("storacha_kit installation failed")
                
        detect_ipfs_car_cmd = "ipfs-car --version"
        install_ipfs_car_cmd = "sudo npm install -g ipfs-car"
        update_ipfs_car_cmd = "sudo npm update -g ipfs-car"
        try:
            detect_results = subprocess.check_output(detect_ipfs_car_cmd, shell=True)
            version = detect_results.decode("utf-8")
            version = version.split(", ")[1]
            version_list = version.split(".")
            version_list = [int(i.replace("\n", "")) for i in version_list]
            ipfs_car_version_list = self.ipfs_car_version.split(".")
            ipfs_car_version_list = [int(i.replace("\n", "")) for i in ipfs_car_version_list]
            if version_list[0] >= ipfs_car_version_list[0] and version_list[1] >= ipfs_car_version_list[1] and version_list[2] >= ipfs_car_version_list[2]:
                pass
            else:
                update_results = subprocess.run(update_ipfs_car_cmd, shell=True, check=True)
                print("ipfs-car updated")
        except subprocess.CalledProcessError:
            print("ipfs-car not installed")
            print("installing ipfs-car")
            try:
                subprocess.run(install_ipfs_car_cmd, shell=True, check=True)
                print("ipfs-car installed")
            except subprocess.CalledProcessError:
                print("ipfs-car installation failed")
                
        detect_w3_name_cmd = "npm list --depth=0 | grep w3name"
        install_w3_name_cmd = "sudo npm install w3-name"
        update_w3_name_cmd = "sudo npm update w3name"
        try:
            detect_results = subprocess.check_output(detect_w3_name_cmd, shell=True)
            version = detect_results.decode("utf-8")
            version = version.split("@")[1]
            version_list = version.split(".")
            version_list = [int(i.replace("\n", "")) for i in version_list]
            w3_name_version_list = self.w3_name_version.split(".")
            w3_name_version_list = [int(i.replace("\n", "")) for i in w3_name_version_list]
            if version_list[0] >= w3_name_version_list[0] and version_list[1] >= w3_name_version_list[1] and version_list[2] >= w3_name_version_list[2]:
                pass
            else:
                update_results = subprocess.run(update_w3_name_cmd, shell=True, check=True)
                print("w3-name updated")
        except subprocess.CalledProcessError:
            print("w3-name not installed")
            print("installing w3-name")
            try:
                subprocess.run(install_w3_name_cmd, shell=True, check=True)
                print("w3-name installed")
            except subprocess.CalledProcessError:
                print("w3-name installation failed")
        return
    
    def store_add(self, space, file):
        if space != self.space:
            space_use_cmd = "w3 space use " + space
            try:
                results = subprocess.run(space_use_cmd, shell=True, check=True)
                self.space = space
            except subprocess.CalledProcessError:
                print("space use failed")
                return False
        
        with tempfile.NamedTemporaryFile(suffix=".car") as temp:
            filename = temp.name
            ipfs_car_cmd = "ipfs-car pack " + file + " > " + filename
            try:
                results = subprocess.run(ipfs_car_cmd, shell=True, check=True, stderr=subprocess.PIPE)
                results = results.stderr.decode("utf-8").strip()
                results = results.split("\n")
                results = [i.replace("\n", "") for i in results if i != ""]
                results = results[0]
                cid = results
            except subprocess.CalledProcessError:
                print("ipfs-car failed")
                return False
            
            store_add_cmd = "w3 can store add " + filename
            try:
                results = subprocess.check_output(store_add_cmd, shell=True)
                results = results.decode("utf-8").strip()
                results = results.split("\n")
                results = [i.replace("\n", "") for i in results if i != ""]
            except subprocess.CalledProcessError:
                print("store_add failed")
                return False
            return results
        
    
    def store_get(self, space, cid):
        if space != self.space:
            space_use_cmd = "w3 space use " + space
            try:
                results = subprocess.run(space_use_cmd, shell=True, check=True)
                self.space = space
            except subprocess.CalledProcessError:
                print("space use failed")
                return False
        
        store_get_cmd = "w3 can store ls " 
        try:
            results = subprocess.check_output(store_get_cmd, shell=True)
            results = results.decode("utf-8").strip()
            results = results.split("\n")
            results = [i.replace("\n", "") for i in results if i != ""]
        except subprocess.CalledProcessError:
            print("store_get failed")
        if cid not in results:
            return False
        else:
            return [cid]
         
    def store_remove(self, space, cid):
        if space != self.space:
            space_use_cmd = "w3 space use " + space
            try:
                results = subprocess.run(space_use_cmd, shell=True, check=True)
                self.space = space
            except subprocess.CalledProcessError:
                print("space use failed")
                return False
        
        store_remove_cmd = "w3 can store rm " + cid
        try:
            results = subprocess.check_output(store_remove_cmd, shell=True)
            results = results.decode("utf-8").strip()
        except subprocess.CalledProcessError:
            print("store_remove failed")
            return False
        return [cid]
    
    def store_list(self, space):
        store_list_cmd = "w3 store list " + space
        try:
            results = subprocess.check_output(store_list_cmd, shell=True)
            results = results.decode("utf-8").strip()
            results = results.split("\n")
            results = [i.replace("\n", "") for i in results if i != ""]
        except subprocess.CalledProcessError:
            print("store_list failed")
            return False
        return results
    
    def upload_add(self, space, file):
        if space != self.space:
            space_use = "w3 space use " + space
            try:
                results = subprocess.run(space_use, shell=True, check=True)
                self.space = space
            except subprocess.CalledProcessError:
                print("space use failed")
                return False
    
        upload_add_cmd = "w3 upload " + file
        try:
            results = subprocess.check_output(upload_add_cmd, shell=True)
            results = results.decode("utf-8").strip()
            results = results.split("\n")
            results = [i.replace("\n", "") for i in results if i != ""]
            results = [i.strip() for i in results]
            results = [i.replace('⁂ https://w3s.link/ipfs/', "") for i in results]
        except subprocess.CalledProcessError:
            print("upload_add failed")
            return False
        return results
    
    def upload_list(self, space):
        if space != self.space:
            space_use = "w3 space use " + space
            try:
                results = subprocess.run(space_use, shell=True, check=True)
                self.space = space
            except subprocess.CalledProcessError:
                print("space use failed")
                return False
        
        upload_list_cmd = "w3 ls"
        try:
            results = subprocess.check_output(upload_list_cmd, shell=True)
            results = results.decode("utf-8").strip()
            results = results.split("\n")
            results = [i.replace("\n", "") for i in results if i != ""]
        except subprocess.CalledProcessError as e:
            results = e
            print("upload_list failed")
        return results
    
    def upload_list_https(self, space):
        auth_secret = self.tokens[space]["X-Auth-Secret header"]
        authorization = self.tokens[space]["Authorization header"]
        method = "upload/list"
        data = {
            "tasks": [
                [
                    "upload/list",
                    space,
                    {}
                ]
            ]
        }
        results = self.storacha_http_request(auth_secret, authorization, method, data)
        return results
    
    def upload_remove(self, space, cid):
        if type(cid) == list:
            cid = cid[0]
        if space != self.space:
            space_use = "w3 space use " + space
            try:
                results = subprocess.run(space_use, shell=True, check=True)
                self.space = space
            except subprocess.CalledProcessError:
                print("space use failed")
                return False
        
        upload_remove_cmd = "w3 rm " + cid
        try:
            results = subprocess.check_output(upload_remove_cmd, shell=True)
            results = results.decode("utf-8").strip()
        except subprocess.CalledProcessError:
            print("upload_remove failed")
            return False
        return [cid]
    
    def upload_remove_https(self, space, cid):
        auth_secret = self.tokens[space]["X-Auth-Secret header"]
        authorization = self.tokens[space]["Authorization header"]
        method = "upload/remove"
        data = {
            "tasks": [
                [
                    "upload/remove",
                    space,
                    {
                        "cid": cid
                    }
                ]
            ]
        }
        results = self.storacha_http_request(auth_secret, authorization, method, data)
        return results
    
    
    def w3usage_report(self, space):
        usage_report_cmd = "w3 usage report " + space
        try:
            results = subprocess.check_output(usage_report_cmd, shell=True)
            results = results.decode("utf-8").strip()
            results = results.split("\n")
            results = [i.replace("\n", "") for i in results if i != ""]
        except subprocess.CalledProcessError:
            print("usage_report failed")
        return results
    
    def access_delegate(self, space, email_did, permissions, expiration=None):
        access_delegate_cmd = "w3 access delegate " + space + " " + email_did
        permissions = ["--can '" + i + "'" for i in permissions]
        access_delegate_cmd = access_delegate_cmd + " " + " ".join(permissions)
        if expiration is None:
            expiration = "date -v +24H +'%Y-%m-%dT%H:%M:%S'"
        else:
            expiration = "date -v +" + expiration + " +'%Y-%m-%dT%H:%M:%S'"
        # expiration = subprocess.check_output(expiration, shell=True)
        # expiration = expiration.decode("utf-8").strip()
        # expiration = None
        # access_delegate_cmd = access_delegate_cmd + " --expiration " + expiration
        try:
            results = subprocess.run(access_delegate_cmd, shell=True, check=True)
        except subprocess.CalledProcessError:
            print("access_delegate failed")
        return
    
    def access_revoke(self, space, email_did):
        access_revoke_cmd = "w3 access revoke " + space + " " + email_did
        try:
            results = subprocess.run(access_revoke_cmd, shell=True, check=True)
        except subprocess.CalledProcessError:
            print("access_revoke failed")
        return results
    
    def space_info(self, space):
        space_info_cmd = "w3 space info " + space
        try:
            results = subprocess.check_output(space_info_cmd, shell=True)
            results = results.decode("utf-8").strip()
            results = results.split("\n")
            results = [i.replace("\n", "") for i in results if i != ""]
            results = [i.strip() for i in results]
            results = [i.split(":", 1) for i in results]
            results = {i[0]: i[1] for i in results}
        except subprocess.CalledProcessError:
            print("space_info failed")
        return results
    
    def space_info_https(self, space):
        auth_secret = self.tokens[space]["X-Auth-Secret header"]
        authorization = self.tokens[space]["Authorization header"]
        method = "space/info"
        data = {
            "tasks": [
                [
                    "space/info",
                    space,
                    {}
                ]
            ]
        }
        results = self.storacha_http_request(auth_secret, authorization, method, data)
        return results
    
    def usage_report(self, space):
        if space != self.space:
            space_use = "w3 space use " + space
            try:
                results = subprocess.run(space_use, shell=True, check=True)
                self.space = space
            except subprocess.CalledProcessError:
                print("space use failed")
                return False
  
        usage_report_cmd = "w3 usage report "
        try:
            results = subprocess.check_output(usage_report_cmd, shell=True)
            results = results.decode("utf-8").strip()
            results = results.split("\n")
            results = [i.replace("\n", "") for i in results if i != ""]
            results = [i.strip() for i in results]
            results = [i.split(":", 1) for i in results]
            results = {i[0]: i[1] for i in results}
        except subprocess.CalledProcessError:
            print("usage_report failed")
        return results
    
    def usage_report_https(self, space):
        auth_secret = self.tokens[space]["X-Auth-Secret header"]
        authorization = self.tokens[space]["Authorization header"]
        method = "usage/report"
        data = {
            "tasks": [
                [
                    "usage/report",
                    space,
                    {}
                ]
            ]
        }
        results = self.storacha_http_request(auth_secret, authorization, method, data)
        return results
             
    def space_allocate(self, space, size):
        space_allocate_cmd = "w3 space allocate " + space + " " + size
        try:
            results = subprocess.run(space_allocate_cmd, shell=True, check=True)
        except subprocess.CalledProcessError:
            print("space_allocate failed")
        return results
    
    def space_deallocate(self, space):
        space_deallocate_cmd = "w3 space deallocate " + space
        try:
            results = subprocess.run(space_deallocate_cmd, shell=True, check=True)
        except subprocess.CalledProcessError:
            print("space_deallocate failed")
        return results
    
    def store_add_batch(self, space, files):
        for file in files:
            self.store_add(space, file)
        return
    
    def store_get_batch(self, space, cids, output):
        for cid in cids:
            self.store_get(space, cid, output)
        return
    
    def store_remove_batch(self, space, cids):
        for cid in cids:
            self.store_remove(space, cid)
        return
    
    def upload_add_batch(self, space, files):
        for file in files:
            self.upload_add(space, file)
        return
    
    def upload_remove_batch(self, space, cids):
        for cid in cids:
            self.upload_remove(space, cid)
        return
    
    def store_add_https(self, space, file):
        auth_secret = self.tokens[space]["X-Auth-Secret header"]
        authorization = self.tokens[space]["Authorization header"]
        method = "store/add"
        file_path = os.path.abspath(file)
        car_length = None
        with tempfile.NamedTemporaryFile(suffix=".car") as temp:
            temp_filename = temp.name
            ipfs_car_cmd = "ipfs-car pack " + file + " > " + temp_filename
            try:
                results = subprocess.run(ipfs_car_cmd, shell=True, stderr=subprocess.PIPE)
                results = results.stderr.decode("utf-8").strip()
                results = results.split("\n")
                results = [i.replace("\n", "") for i in results if i != ""]
                results = results[0]
                cid = results
            except subprocess.CalledProcessError:
                print("ipfs-car failed")
                return False
            car_length_cmd = "wc -c " + temp_filename
            car_length = subprocess.check_output(car_length_cmd, shell=True)
            car_length = car_length.decode("utf-8").strip()
            car_length = car_length.split(" ")[0]
            car_length = int(car_length)            
            data = {
                "tasks": [
                    [
                        "store/add",
                        space,
                        {
                            "link": { file_path: cid  },
                            "size": car_length
                        }
                    ]
                ]
            }            
        results = self.storacha_http_request(auth_secret, authorization, method, data)
        return results
    
    def store_get_https(self, space, cid):
        auth_secret = self.tokens[space]["X-Auth-Secret header"]
        authorization = self.tokens[space]["Authorization header"]
        method = "store/get"
        data = {
            "tasks": [
                [
                    "store/get",
                    space,
                    {
                        "cid": cid
                    }
                ]
            ]
        }
        results = self.storacha_http_request(auth_secret, authorization, method, data)
        return results
    
    def store_remove_https(self, space, cid):
        auth_secret = self.tokens[space]["X-Auth-Secret header"]
        authorization = self.tokens[space]["Authorization header"]
        method = "store/remove"
        data = {
            "tasks": [
                [
                    "store/remove",
                    space,
                    {
                        "cid": cid
                    }
                ]
            ]
        }
        results = self.storacha_http_request(auth_secret, authorization, method, data)
        return results
    
    def store_list_https(self, space):
        auth_secret = self.tokens[space]["X-Auth-Secret header"]
        authorization = self.tokens[space]["Authorization header"]
        method = "store/list"
        data = {
            "space": space,
        }
        results = self.storacha_http_request(auth_secret, authorization, method, data)
        return results
    
    def upload_add_https(self, space, file):
        auth_secret = self.tokens[space]["X-Auth-Secret header"]
        authorization = self.tokens[space]["Authorization header"]
        method = "upload/add"
        with tempfile.NamedTemporaryFile(suffix=".car") as temp:
            filename = temp.name
            ipfs_car_cmd = "ipfs-car pack " + file + " > " + filename
            try:
                results = subprocess.run(ipfs_car_cmd, shell=True, check=True, stderr=subprocess.PIPE)
                results = results.stderr.decode("utf-8").strip()
                results = results.split("\n")
                results = [i.replace("\n", "") for i in results if i != ""]
                results = results[0]
                cid = results
            except subprocess.CalledProcessError:
                print("ipfs-car failed")
                return False
            data = {
                "tasks": [
                    [
                        "upload/add",
                        space,
                        {
                            "cid": cid,
                            "file": file
                        }
                    ]
                ]
            }
        results = self.storacha_http_request(auth_secret, authorization, method, data)
        return results
    
    def upload_remove_https(self, space, cid):
        auth_secret = self.tokens[space]["X-Auth-Secret header"]
        authorization = self.tokens[space]["Authorization header"]
        method = "upload/remove"
        data = {
            "tasks": [
                [
                    "upload/remove",
                    space,
                    {
                        "cid": cid
                    }
                ]
            ]
        }
        results = self.storacha_http_request(auth_secret, authorization, method, data)
        return results

    def test(self):
        print("storacha_kit test")
        self.install()
        email_did = self.login(self.metadata["login"])
        spaces = self.space_ls()
        this_space = spaces[list(spaces.keys())[0]]
        space_info = self.space_info(this_space)
        permissions = [
            "access/delegate",
            "space/info",
            "space/allocate",
            "store/add",
            "store/get",
            "store/remove",
            "store/list",
            "upload/add",
            "upload/list",
            "upload/remove",
            "usage/report"
        ]
        bridge_tokens = self.bridge_generate_tokens(this_space, permissions)
        usage_report = self.usage_report(this_space)
        upload_list = self.upload_list(this_space)
        upload_list_https = self.upload_list_https(this_space)
        upload_add = self.upload_add(this_space, "./ipfs_kit_py/service.json")
        upload_add_https = self.upload_add_https(this_space, "./ipfs_kit_py/service.json")
        upload_rm = self.upload_remove(this_space, upload_add)
        upload_rm_https = self.upload_remove_https(this_space, upload_add)
        store_add = self.store_add(this_space, "./ipfs_kit_py/service.json")
        store_add_https = self.store_add_https(this_space, "./ipfs_kit_py/service.json")
        store_get = self.store_get(this_space, store_add[0])
        store_get_https = self.store_get_https(this_space, store_add[0])
        store_remove = self.store_remove(this_space, store_add[0])
        store_remove_https = self.store_remove_https(this_space, store_add[0])

        results = {
            "email_did": email_did,
            "spaces": spaces,
            "space_info": space_info,
            "bridge_tokens": bridge_tokens,
            "usage_report": usage_report,
            "upload_list": upload_list,
            "upload_list_https": upload_list_https,
            "upload_add": upload_add,
            "upload_add_https": upload_add_https,
            "upload_rm": upload_rm,
            "upload_rm_https": upload_rm_https,
            "store_add": store_add,
            "store_add_https": store_add_https,
            "store_get": store_get,
            "store_get_https": store_get_https,
            "store_remove": store_remove,
            "store_remove_https": store_remove_https,
        }
        return results

if __name__ == "__main__":
    resources = {
    }
    metadata = {
        "login": "starworks5@gmail.com",
    }
    storacha_kit = storacha_kit(resources, metadata)
    test = storacha_kit.test()
    print(test)