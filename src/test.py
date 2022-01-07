from goprocam import GoProCamera, constants
import time


time_list = []
gpCam = GoProCamera.GoPro()

# time_list.append(time())
print(gpCam.shoot_video())

time.sleep(5)
gpCam.shutter(param=constants.stop)

# for idx in range(len(time_list) - 1):
# 	print(f'time {idx + 1}: {time_list[idx + 1] - time_list[idx]}')
time.sleep(3)
gpCam.downloadLastMedia(custom_filename='data/' + gpCam.getMediaInfo("file"))