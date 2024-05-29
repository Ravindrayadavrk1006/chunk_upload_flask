from flask import Flask,request

#__name__ for the name of the current module so that static and all other file can be found easily
print(__name__)
app = Flask(__name__)
file_to_store = 'uploaded_file'
#here our chunk size we have kept to 1mb
chunk_size = 1024*8
@app.route("/upload", methods = ['POST'])
def upload_chunk_file():
    sent_chunk = request.stream
    file_name_from_server= request.headers.get('X-file-Name')
    with open(file_to_store+file_name_from_server, 'ab') as f:
        while True:
        #reading sent chunk 
            chunk_read = sent_chunk.read(chunk_size)
            if chunk_read:
                #writing to file if chunk is present
                f.write(chunk_read)
            else:
                break
    return "chunk uploaded"

if __name__ == '__main__':
    app.run(debug=True, port = 8090, host = '127.0.0.1')
