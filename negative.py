from udmabuf import Udmabuf
from uio     import Uio
import numpy as np
import time

if __name__ == '__main__':
    uio1       = Uio('negative-uio')
    regs       = uio1.regs()
    udmabuf4   = Udmabuf('negative-udmabuf4')
    udmabuf5   = Udmabuf('negative-udmabuf5')

    test_dtype = np.uint32
    test_size  = min(int(udmabuf4.buf_size/(np.dtype(test_dtype).itemsize)),
                     int(udmabuf5.buf_size/(np.dtype(test_dtype).itemsize)))
    
    udmabuf4_array    = udmabuf4.memmap(dtype=test_dtype, shape=(10))
    udmabuf4_array[:] = [64591051, 3172697395, 0, 0, 76157580, 46281898, 1342177280, 48498273, 3373798755, 4290117632]
    udmabuf4.set_sync_to_device(0, 10*(np.dtype(test_dtype).itemsize))

    udmabuf5_array    = udmabuf5.memmap(dtype=test_dtype, shape=(4))
    udmabuf5_array[:] = [0, 0, 0, 0]
    udmabuf5.set_sync_to_cpu(0, 4*(np.dtype(test_dtype).itemsize))
    
    print(udmabuf4_array)
    print(udmabuf5_array)
    total_setup_time   = 0
    total_cleanup_time = 0
    total_xfer_time    = 0
    total_xfer_size    = 0
    count              = 0

    start_time  = time.time()
    udmabuf4.sync_for_device()
    udmabuf5.sync_for_device()
    regs.write_word(0x18, udmabuf4.phys_addr & 0xFFFFFFFF)
    regs.write_word(0x20, udmabuf5.phys_addr & 0xFFFFFFFF)
    regs.write_word(0x04, 0x000000001)
    regs.write_word(0x08, 0x000000001)
    regs.write_word(0x0C, 0x000000001)
    uio1.irq_on()
    phase0_time = time.time()
    regs.write_word(0x00, 0x000000001)
    uio1.wait_irq()
    

    phase1_time = time.time()
    regs.write_word(0x0C, 0x000000001)
    udmabuf4.sync_for_cpu()
    udmabuf5.sync_for_cpu()

    end_time     = time.time()
    setup_time   = phase0_time - start_time
    xfer_time    = phase1_time - phase0_time
    cleanup_time = end_time    - phase1_time
    total_time   = end_time    - start_time

    total_setup_time   = total_setup_time   + setup_time
    total_cleanup_time = total_cleanup_time + cleanup_time
    total_xfer_time    = total_xfer_time    + xfer_time
    total_xfer_size    = total_xfer_size    + test_size
    count              = count              + 1
    print ("total:{0:.3f}[msec] setup:{1:.3f}[msec] xfer:{2:.3f}[msec] cleanup:{3:.3f}[msec]".format(round(total_time*1000.0,3), round(setup_time*1000.0,3), round(xfer_time*1000.0,3), round(cleanup_time*1000.0,3)))
    print ("throughput          :{0:.3f}".format(round(((total_xfer_size/total_xfer_time)/(1000*1000)),3)) + "[MByte/sec]")

    print(udmabuf4_array)
    print(udmabuf5_array)
    
