# coding: utf-8
import subprocess, time, sys, os, signal

p = subprocess.Popen('ping -n 100 127.0.0.1', shell=False)

time.sleep(5) # кол-во секунд типа float

#p.terminate()

#os.kill(p.pid, signal.SIGTERM)
p.send_signal(signal.SIGTERM)


sys.exit(0)