# PMonitor
packet monitor，当在一段时间内检测不到发往特定主机特定服务的流量的时候，重启进程。

# 配置项说明
TIMEOUT         超时时间<br/>
INTERVAL        检测周期<br/>
LOGFILE         日志文件<br/>
ETHNAME         网卡名<br/>
FILTEREXP       tcpdump过滤规则<br/>
CMD_RESTART     重启命令

# 部署说明：
1) 配置PMonitor.py里的配置项ETHNAME、FILTEREXP和CMD_RESTART。<br/>
2) 运行脚本：<br/>
nohup python PMonitor.py >/dev/null &
