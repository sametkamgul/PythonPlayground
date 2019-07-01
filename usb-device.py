import time
import usb.core
import usb.util
import usb.backend
import usb.backend.libusb1

VID = 0x05C8
PID = 0x0379

backend = usb.backend.libusb1.get_backend(find_library=lambda x: r'C:\Users\Mate-HP\PycharmProjects\PythonPlayground\libs\libusb-1.0.dll')
device = usb.core.find(backend=backend, idVendor=VID, idProduct=PID)
if not device:
	print('[INFO] device not found')
else:
	print('[INFO] device found')

# this is a simple example. We will examine this later!






