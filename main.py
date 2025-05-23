from flask import Flask, send_file, send_from_directory
import os

app = Flask(__name__)

# Đường dẫn đến thư mục chứa file HLS
HLS_DIR = "hls_output"

# @app.route('/')
# def index():
#     # Trả về một trang HTML đơn giản với video player
#     return '''
#     <!DOCTYPE html>
#     <html>
#     <head>
#         <title>HLS Streaming with Flask</title>
#         <script src="https://cdn.jsdelivr.net/npm/hls.js@latest"></script>
#     </head>
#     <body>
#         <h1>HLS Video Streaming</h1>
#         <video id="video" controls width="720" height="400"></video>
#         <script>
#             const video = document.getElementById('video');
#             const videoSrc = '/hls/output.m3u8';
#             if (Hls.isSupported()) {
#                 const hls = new Hls();
#                 hls.loadSource(videoSrc);
#                 hls.attachMedia(video);
#                 hls.on(Hls.Events.MANIFEST_PARSED, function() {
#                     video.play();
#                 });
#             } else if (video.canPlayType('application/vnd.apple.mpegurl')) {
#                 video.src = videoSrc;
#                 video.addEventListener('canplay', function() {
#                     video.play();
#                 });
#             }
#         </script>
#     </body>
#     </html>
#     '''
@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>HLS Streaming with Video.js</title>
        <link href="https://vjs.zencdn.net/8.0.4/video-js.css" rel="stylesheet" />
        <script src="https://vjs.zencdn.net/8.0.4/video.min.js"></script>
        <style>
            .video-js .vjs-control-bar {
                display: flex !important;
                opacity: 1 !important;
                visibility: visible !important;
            }

            .video-js .vjs-current-time {
                display: block !important;
            }

            .video-js .vjs-remaining-time {
                display: block !important;
            }

            .video-js .vjs-time-control {
                display: flex !important;
            }
        </style>
    </head>
    <body>
        <h1>HLS Streaming</h1>
        <video id="video" class="video-js vjs-default-skin" controls autoplay width="720" height="400"
            data-setup='{
                "controlBar": {
                    "children": [
                        "playToggle",
                        "currentTimeDisplay",
                        "timeDivider",
                        "durationDisplay",
                        "remainingTimeDisplay",
                        "progressControl",
                        "volumePanel",
                        "fullscreenToggle"
                    ]
                }
            }'>
            <source src="/hls/output.m3u8" type="application/x-mpegURL">
        </video>
    </body>
    </html>
    '''


@app.route('/hls/<path:filename>')
def serve_hls(filename):
    # Phục vụ các file .m3u8 và .ts
    return send_from_directory(HLS_DIR, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)