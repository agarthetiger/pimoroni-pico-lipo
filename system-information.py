import sys
import gc
import micropython
import os

print(sys.version)

# See https://docs.micropython.org/en/latest/library/os.html#os.statvfs
#Get the status of a filesystem.
#Returns a tuple with the filesystem information in the following order:
#       0 f_bsize – file system block size
#       1 f_frsize – fragment size
#       2 f_blocks – size of fs in f_frsize units
#       3 f_bfree – number of free blocks
#       4 f_bavail – number of free blocks for unprivileged users
#       5 f_files – number of inodes
#       6 f_ffree – number of free inodes
#       7 f_favail – number of free inodes for unprivileged users
#       8 f_flag – mount flags
#       9 f_namemax – maximum filename length


print(os.statvfs('/'))
fs_stats = os.statvfs('/')
fs_size = fs_stats[1] * fs_stats[2]
fs_free = fs_stats[3] * fs_stats[0]

print(f"Filesystem size: {fs_size}")
print(f"Free space: {fs_free}")
print(f"Free percent: {(fs_free / fs_size) * 100}%")

print(os.uname())