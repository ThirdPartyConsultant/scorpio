
An api server for small business boss to handle the business track 
and the communication between Pad (boss) and phone (customer)

(1) phase-1: the waitting system (MenDan)
    Pad: 
        (a) simple view for customer to "take barcode/qrcode"
        (b) administration console 
    Phone:
        (a) take bar code, understand the waitting time
    Server: handle log and most of the logic.

(2) quick deployment method.
    (2.1) install following packages:
        #apt-get install uwsgi
        #apt-get install uwsgi-plugin-python
        #apt-get install python
        #apt-get install nginx
        #apt-get install python-flask

    (2.2) check-out file from github, here assume that the folder is:
        /root/github/scorpio/TheBoss/

    (2.3) copy conf files
         cp scorpio/TheBoss/conf/nginx_theboss.conf /etc/nginx/sites-available/theboss
         ln -s /etc/nginx/sites-available/theboss /etc/nginx/sites-enabled/theboss
         cp scorpio/TheBoss/conf/uwsgi_theboss.conf /etc/uwsgi/apps-available
         ln -s /etc/uwsgi/apps-available/uwsgi_theboss.conf /etc/uwsgi/apps-enabled/uwsgi_theboss.ini

    (1.4) restart nginx and uwsgi
        !! the two service must run in root permission to control GPIO


