
Carbon Note:

  Since SafeSync clients uses https connections, we added additional configuration file for nginx to handle https traffic and redirect it to flask.

  Additional requirement:
     Nginx

Ian Note:
    * Simple Upload
        Upload test.txt to filesroot.(Would be /tmp/storage provisionally)
            $ curl -X POST -F "file=@test.txt" http://127.0.0.1:8111/api/v1/upload_file
    * Show file's content
        $ curl -X GET http://127.0.0.1:8111/api/v1/filesroot/test.txt
