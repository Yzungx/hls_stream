ffmpeg -i /home/yzungx/ws/media/video/input-2.mp4 -codec: copy -start_number 0 -hls_time 5 -hls_list_size 0 -hls_flags split_by_time -f hls hls_output/output.m3u8

-i input.mp4: File video đầu vào.
-codec: copy: Giữ nguyên chất lượng video và audio, không mã hóa lại.
-start_number 0: Đánh số các segment bắt đầu từ 0.
-hls_time 10: Mỗi segment dài 10 giây.
-hls_list_size 0: Không giới hạn số segment trong playlist.
-f hls: Định dạng đầu ra là HLS.
hls_output/output.m3u8: Đường dẫn file playlist đầu ra.