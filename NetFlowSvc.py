import servicemanager
import socket
import sys
import win32event
import win32service
import win32serviceutil
import Collector
from threading import Thread

class CollectorThread(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        Collector.CollectNetflow()


class NetFlowService(win32serviceutil.ServiceFramework):
    _svc_name_ = "NetFlowService"
    _svc_display_name_ = "NetFlow Service"
    udpHandle = None

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(60)
        self.isAlive = True


    def SvcStop(self):
        self.isAlive = False
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        sys.exit()

    def SvcDoRun(self):
        self.isAlive = True
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_, ''))
        rc = None
        while rc != win32event.WAIT_OBJECT_0:
            collectorThread = CollectorThread()
            collectorThread.setName('NetFlowCollector')
            collectorThread.start()
            rc = win32event.WaitForSingleObject(self.hWaitStop, win32event.INFINITE)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(NetFlowService)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(NetFlowService)