chunk_size = 2048*8 #2 MB in one chunk
#just edit the below code
file_to_upload = 'redis_basic.tar.gz'  #file name to upload #edit it for testing
import requests
with open(file_to_upload,'rb') as f:
    while True:
        #reading the file 2mb at a time
        chunk = f.read(chunk_size)
        if chunk:
            pass
            #calling and sending the chunk to the server
            headers = {
                #content type is most important thing 
                "Content-Type":"application/octet-stream",
                "X-file-Name":file_to_upload
            }
            response = requests.post("http://127.0.0.1:8090/upload", headers = headers, data = chunk)
        else:
            break
    print("File uploaded successfully")
