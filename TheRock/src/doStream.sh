#!/bin/bash 
wwwroot="/tmp/www"

mkdir -p "/tmp/www"
cp play.html "/tmp/www/"
raspivid -n -w 1024 -h 768 --framerate 10 -vf -t 86400000 -b 32000 -ih -o - \
| ffmpeg -y -r 10 \
    -i - \
    -b:v 32000 \
    -c:v copy \
    -analyzeduration 1M \
    -map 0:0 \
    -f ssegment \
    -segment_time 2 \
    -segment_wrap 20 \
    -segment_format mpegts \
    -segment_list "$wwwroot/stream.m3u8" \
    -segment_list_size 360 \
    -segment_list_flags live \
    -segment_list_type m3u8 \
    "$wwwroot/%08d.ts" 

#raspivid -n -w 720 -h 405 -fps 20 -awb off -vf -t 86400000 -b 1800000 -o - \
#   | ffmpeg -y \
#    -analyzeduration 5M \
#    -i - \
#    -c:v copy \
#    -map 0:0 \
#    -hls_time 10 \
#    -hls_wrap 40 \
#    "${wwwroot}/stream.m3u8"

#trap "rm ${wwwroot}/{stream.m3u8,stream*.ts}" EXIT
