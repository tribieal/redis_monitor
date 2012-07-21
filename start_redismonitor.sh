#!/bin/bash
nohup python redismonitor.py >redis_monitor.log 2>&1 &
#enter 'exit' to quit the session, or it will caught the sighup signal.
