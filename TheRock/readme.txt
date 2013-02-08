
Project TheRock, a sub project of scorpio.

Purpose: provide a easy utility for mobile to control Raspberry PI.
        (1) app inside Raspberry PI
        (2) its GPIO!

(1) quick deployment method.
    (1.1) install following packages:
        #apt-get install uwsgi
        #apt-get install python
        #apt-get install nginx

    (1.2) check-out file from github, here assume that the folder is:
        /root/github/scorpio/TheRock/

    (1.3) copy conf files
        * cp /root/github/scorpio/TheRock/config/nginx_therock.conf /etc/nginx/sites-available/therock
        * ln -s /etc/nginx/sites-available/therock /etc/nginx/sites-enabled/therock
     
    (1.4) restart nginx and uwsgi

(2) api

    (2.1) /hello 
        return {'msg':'hello'}

    (2.2) 
