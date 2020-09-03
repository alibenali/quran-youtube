ffmpeg -stream_loop -1 -f concat -i input.txt -i input.mp3 -map 0:v -map 1:a -c:v libx264 -crf 29 -preset slower -shortest -movflags +faststart output.mp4
