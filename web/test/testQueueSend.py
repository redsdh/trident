# !/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename:testQueueSend.py

__author__ = 'yuyichuan'


# 循环发送消息到stomp
import time
import stomp
import configCur


if __name__ == "__main__":
    conn = stomp.Connection(host_and_ports=[(configCur.STOMP_HOST, configCur.STOMP_PORT)])
    callback_listener = stomp.WaitingListener("123")
    conn.set_listener('test_send', callback_listener)
    conn.start()
    conn.connect()

    time.sleep(5)

    _ntimes = 0
    while _ntimes < 10 :
        #conn.send(body='{"attachments":[],"children":[{"attachments":[],"elapse":301,"status":"S","url":"info.kozz.web.Netiquette.netiquette"}],"elapse":328,"status":"S","url":"/home/netiquette.do"}', destination=configCur.DESTINATION, receipt="123")
        conn.send(body='{"attachments":[],"children":[{"children":[{"elapse":0,"status":"S","url":"com.tc.session.servlet.RemotableRequestWrapper(javax.servlet.http.HttpServletRequest,com.tc.session.SessionManager)"},{"elapse":0,"status":"S","url":"com.tc.session.servlet.RemotableRequestWrapper.setResponse(javax.servlet.http.HttpServletResponse)"},{"children":[{"children":[{"children":[{"children":[{"elapse":0,"status":"S","url":"com.tc.session.helper.CookieHelper.findCookie(java.lang.String,javax.servlet.http.HttpServletRequest)"}],"elapse":0,"status":"S","url":"com.tc.session.helper.CookieHelper.findCookieValue(java.lang.String,javax.servlet.http.HttpServletRequest)"}],"elapse":0,"status":"S","url":"com.tc.session.helper.CookieHelper.findSessionId(javax.servlet.http.HttpServletRequest)"}],"elapse":0,"status":"S","url":"com.tc.session.AbstractSessionManager.getRequestSessionId(javax.servlet.http.HttpServletRequest)"},{"children":[{"elapse":0,"status":"S","url":"com.tc.session.AbstractSessionManager.getHttpSession(java.lang.String,javax.servlet.http.HttpServletRequest)"},{"children":[{"children":[{"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolableObjectFactory.activateObject(java.lang.Object)"},{"children":[{"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolableObjectFactory.validateObject(org.apache.zookeeper.ZooKeeper)"}],"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolableObjectFactory.validateObject(java.lang.Object)"}],"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolManager.borrowObject()"},{"children":[{"children":[{"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolableObjectFactory.validateObject(org.apache.zookeeper.ZooKeeper)"}],"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolableObjectFactory.validateObject(java.lang.Object)"},{"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolableObjectFactory.passivateObject(java.lang.Object)"}],"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolManager.returnObject(org.apache.zookeeper.ZooKeeper)"}],"elapse":2,"status":"S","url":"com.tc.session.zookeeper.ZookeeperSessionClient.getSession(java.lang.String)"},{"children":[{"elapse":0,"status":"S","url":"com.tc.session.SessionMetaData.getLastAccessTime()"},{"elapse":0,"status":"S","url":"com.tc.session.SessionMetaData.getMaxIdle()"}],"elapse":0,"status":"S","url":"com.tc.session.SessionMetaData.isValid()"},{"children":[{"children":[{"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolableObjectFactory.activateObject(java.lang.Object)"},{"children":[{"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolableObjectFactory.validateObject(org.apache.zookeeper.ZooKeeper)"}],"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolableObjectFactory.validateObject(java.lang.Object)"}],"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolManager.borrowObject()"},{"elapse":0,"status":"S","url":"com.tc.session.SessionMetaData.getId()"},{"elapse":0,"status":"S","url":"com.tc.session.SessionMetaData.setLastAccessTime(java.lang.Long)"},{"children":[{"children":[{"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolableObjectFactory.validateObject(org.apache.zookeeper.ZooKeeper)"}],"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolableObjectFactory.validateObject(java.lang.Object)"},{"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolableObjectFactory.passivateObject(java.lang.Object)"}],"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolManager.returnObject(org.apache.zookeeper.ZooKeeper)"}],"elapse":2,"status":"S","url":"com.tc.session.zookeeper.ZookeeperSessionClient.updateSession(com.tc.session.SessionMetaData)"},{"elapse":0,"status":"S","url":"com.tc.session.TCSession.setRequest(javax.servlet.http.HttpServletRequest)"}],"elapse":4,"status":"S","url":"com.tc.session.TCSessionManager.getHttpSession(java.lang.String,javax.servlet.http.HttpServletRequest)"}],"elapse":4,"status":"S","url":"com.tc.session.servlet.RemotableRequestWrapper.getSession(boolean)"},{"children":[{"elapse":0,"status":"S","url":"com.tc.session.TCSession.access()"},{"elapse":0,"status":"S","url":"com.tc.session.TCSession.getId()"},{"elapse":0,"status":"S","url":"com.tc.session.TCSessionManager.getSessionClient()"},{"children":[{"children":[{"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolableObjectFactory.activateObject(java.lang.Object)"},{"children":[{"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolableObjectFactory.validateObject(org.apache.zookeeper.ZooKeeper)"}],"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolableObjectFactory.validateObject(java.lang.Object)"}],"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolManager.borrowObject()"},{"children":[{"children":[{"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolableObjectFactory.validateObject(org.apache.zookeeper.ZooKeeper)"}],"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolableObjectFactory.validateObject(java.lang.Object)"},{"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolableObjectFactory.passivateObject(java.lang.Object)"}],"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolManager.returnObject(org.apache.zookeeper.ZooKeeper)"}],"elapse":3,"status":"S","url":"com.tc.session.zookeeper.ZookeeperSessionClient.getAttribute(java.lang.String,java.lang.String)"}],"elapse":3,"status":"S","url":"com.tc.session.TCSession.getAttribute(java.lang.String)"},{"elapse":0,"status":"S","url":"com.tc.session.servlet.RemotableRequestWrapper.getSession(boolean)"},{"children":[{"elapse":0,"status":"S","url":"com.tc.session.TCSession.access()"},{"elapse":0,"status":"S","url":"com.tc.session.TCSession.getId()"},{"elapse":0,"status":"S","url":"com.tc.session.TCSessionManager.getSessionClient()"},{"children":[{"children":[{"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolableObjectFactory.activateObject(java.lang.Object)"},{"children":[{"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolableObjectFactory.validateObject(org.apache.zookeeper.ZooKeeper)"}],"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolableObjectFactory.validateObject(java.lang.Object)"}],"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolManager.borrowObject()"},{"children":[{"children":[{"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolableObjectFactory.validateObject(org.apache.zookeeper.ZooKeeper)"}],"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolableObjectFactory.validateObject(java.lang.Object)"},{"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolableObjectFactory.passivateObject(java.lang.Object)"}],"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolManager.returnObject(org.apache.zookeeper.ZooKeeper)"}],"elapse":1,"status":"S","url":"com.tc.session.zookeeper.ZookeeperSessionClient.getAttribute(java.lang.String,java.lang.String)"}],"elapse":1,"status":"S","url":"com.tc.session.TCSession.getAttribute(java.lang.String)"},{"elapse":0,"status":"S","url":"com.tc.session.servlet.RemotableRequestWrapper.getSession(boolean)"},{"children":[{"elapse":0,"status":"S","url":"com.tc.session.TCSession.access()"}],"elapse":0,"status":"S","url":"com.tc.session.TCSession.getAttribute(java.lang.String)"},{"elapse":0,"status":"S","url":"com.tc.session.servlet.RemotableRequestWrapper.getSession(boolean)"},{"children":[{"elapse":0,"status":"S","url":"com.tc.session.TCSession.access()"},{"elapse":0,"status":"S","url":"com.tc.session.TCSession.getId()"},{"elapse":0,"status":"S","url":"com.tc.session.TCSessionManager.getSessionClient()"},{"children":[{"children":[{"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolableObjectFactory.activateObject(java.lang.Object)"},{"children":[{"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolableObjectFactory.validateObject(org.apache.zookeeper.ZooKeeper)"}],"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolableObjectFactory.validateObject(java.lang.Object)"}],"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolManager.borrowObject()"},{"children":[{"children":[{"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolableObjectFactory.validateObject(org.apache.zookeeper.ZooKeeper)"}],"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolableObjectFactory.validateObject(java.lang.Object)"},{"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolableObjectFactory.passivateObject(java.lang.Object)"}],"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolManager.returnObject(org.apache.zookeeper.ZooKeeper)"}],"elapse":1,"status":"S","url":"com.tc.session.zookeeper.ZookeeperSessionClient.getAttribute(java.lang.String,java.lang.String)"}],"elapse":1,"status":"S","url":"com.tc.session.TCSession.getAttribute(java.lang.String)"},{"children":[{"children":[{"elapse":0,"status":"S","url":"info.kozz.spring.PlainComponentBean.getOrder()"}],"elapse":101,"status":"S","url":"info.kozz.spring.SimpleBean.getFoo()"}],"elapse":301,"status":"S","url":"info.kozz.web.Netiquette.netiquette(org.springframework.ui.ModelMap)"},{"elapse":0,"status":"S","url":"com.tc.session.servlet.RemotableRequestWrapper.getSession(boolean)"},{"children":[{"elapse":0,"status":"S","url":"com.tc.session.TCSession.access()"},{"elapse":0,"status":"S","url":"com.tc.session.TCSession.getId()"},{"elapse":0,"status":"S","url":"com.tc.session.TCSessionManager.getSessionClient()"},{"children":[{"children":[{"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolableObjectFactory.activateObject(java.lang.Object)"},{"children":[{"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolableObjectFactory.validateObject(org.apache.zookeeper.ZooKeeper)"}],"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolableObjectFactory.validateObject(java.lang.Object)"}],"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolManager.borrowObject()"},{"children":[{"children":[{"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolableObjectFactory.validateObject(org.apache.zookeeper.ZooKeeper)"}],"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolableObjectFactory.validateObject(java.lang.Object)"},{"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolableObjectFactory.passivateObject(java.lang.Object)"}],"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolManager.returnObject(org.apache.zookeeper.ZooKeeper)"}],"elapse":1,"status":"S","url":"com.tc.session.zookeeper.ZookeeperSessionClient.getAttribute(java.lang.String,java.lang.String)"}],"elapse":1,"status":"S","url":"com.tc.session.TCSession.getAttribute(java.lang.String)"},{"children":[{"children":[{"children":[{"children":[{"children":[{"elapse":0,"status":"S","url":"com.tc.session.helper.CookieHelper.findCookie(java.lang.String,javax.servlet.http.HttpServletRequest)"}],"elapse":0,"status":"S","url":"com.tc.session.helper.CookieHelper.findCookieValue(java.lang.String,javax.servlet.http.HttpServletRequest)"}],"elapse":0,"status":"S","url":"com.tc.session.helper.CookieHelper.findSessionId(javax.servlet.http.HttpServletRequest)"}],"elapse":0,"status":"S","url":"com.tc.session.AbstractSessionManager.getRequestSessionId(javax.servlet.http.HttpServletRequest)"},{"children":[{"elapse":0,"status":"S","url":"com.tc.session.AbstractSessionManager.getHttpSession(java.lang.String,javax.servlet.http.HttpServletRequest)"},{"children":[{"children":[{"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolableObjectFactory.activateObject(java.lang.Object)"},{"children":[{"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolableObjectFactory.validateObject(org.apache.zookeeper.ZooKeeper)"}],"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolableObjectFactory.validateObject(java.lang.Object)"}],"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolManager.borrowObject()"},{"children":[{"children":[{"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolableObjectFactory.validateObject(org.apache.zookeeper.ZooKeeper)"}],"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolableObjectFactory.validateObject(java.lang.Object)"},{"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolableObjectFactory.passivateObject(java.lang.Object)"}],"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolManager.returnObject(org.apache.zookeeper.ZooKeeper)"}],"elapse":1,"status":"S","url":"com.tc.session.zookeeper.ZookeeperSessionClient.getSession(java.lang.String)"},{"children":[{"elapse":0,"status":"S","url":"com.tc.session.SessionMetaData.getLastAccessTime()"},{"elapse":0,"status":"S","url":"com.tc.session.SessionMetaData.getMaxIdle()"}],"elapse":0,"status":"S","url":"com.tc.session.SessionMetaData.isValid()"},{"children":[{"children":[{"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolableObjectFactory.activateObject(java.lang.Object)"},{"children":[{"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolableObjectFactory.validateObject(org.apache.zookeeper.ZooKeeper)"}],"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolableObjectFactory.validateObject(java.lang.Object)"}],"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolManager.borrowObject()"},{"elapse":0,"status":"S","url":"com.tc.session.SessionMetaData.getId()"},{"elapse":0,"status":"S","url":"com.tc.session.SessionMetaData.setLastAccessTime(java.lang.Long)"},{"children":[{"children":[{"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolableObjectFactory.validateObject(org.apache.zookeeper.ZooKeeper)"}],"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolableObjectFactory.validateObject(java.lang.Object)"},{"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolableObjectFactory.passivateObject(java.lang.Object)"}],"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolManager.returnObject(org.apache.zookeeper.ZooKeeper)"}],"elapse":3,"status":"S","url":"com.tc.session.zookeeper.ZookeeperSessionClient.updateSession(com.tc.session.SessionMetaData)"},{"elapse":0,"status":"S","url":"com.tc.session.TCSession.setRequest(javax.servlet.http.HttpServletRequest)"}],"elapse":4,"status":"S","url":"com.tc.session.TCSessionManager.getHttpSession(java.lang.String,javax.servlet.http.HttpServletRequest)"}],"elapse":4,"status":"S","url":"com.tc.session.servlet.RemotableRequestWrapper.getSession(boolean)"}],"elapse":4,"status":"S","url":"com.tc.session.servlet.RemotableRequestWrapper.getSession()"},{"elapse":0,"status":"S","url":"com.tc.session.servlet.RemotableRequestWrapper.getSession(boolean)"},{"children":[{"elapse":0,"status":"S","url":"com.tc.session.TCSession.access()"}],"elapse":0,"status":"S","url":"com.tc.session.TCSession.getAttribute(java.lang.String)"},{"children":[{"elapse":0,"status":"S","url":"com.tc.session.TCSession.access()"},{"elapse":0,"status":"S","url":"com.tc.session.TCSession.getId()"},{"elapse":0,"status":"S","url":"com.tc.session.TCSessionManager.getSessionClient()"},{"children":[{"children":[{"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolableObjectFactory.activateObject(java.lang.Object)"},{"children":[{"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolableObjectFactory.validateObject(org.apache.zookeeper.ZooKeeper)"}],"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolableObjectFactory.validateObject(java.lang.Object)"}],"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolManager.borrowObject()"},{"children":[{"children":[{"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolableObjectFactory.validateObject(org.apache.zookeeper.ZooKeeper)"}],"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolableObjectFactory.validateObject(java.lang.Object)"},{"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolableObjectFactory.passivateObject(java.lang.Object)"}],"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolManager.returnObject(org.apache.zookeeper.ZooKeeper)"}],"elapse":1,"status":"S","url":"com.tc.session.zookeeper.ZookeeperSessionClient.getAttribute(java.lang.String,java.lang.String)"}],"elapse":1,"status":"S","url":"com.tc.session.TCSession.getAttribute(java.lang.String)"},{"children":[{"elapse":0,"status":"S","url":"com.tc.session.TCSession.access()"},{"elapse":0,"status":"S","url":"com.tc.session.TCSession.getId()"},{"elapse":0,"status":"S","url":"com.tc.session.TCSessionManager.getSessionClient()"},{"children":[{"children":[{"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolableObjectFactory.activateObject(java.lang.Object)"},{"children":[{"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolableObjectFactory.validateObject(org.apache.zookeeper.ZooKeeper)"}],"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolableObjectFactory.validateObject(java.lang.Object)"}],"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolManager.borrowObject()"},{"children":[{"children":[{"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolableObjectFactory.validateObject(org.apache.zookeeper.ZooKeeper)"}],"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolableObjectFactory.validateObject(java.lang.Object)"},{"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolableObjectFactory.passivateObject(java.lang.Object)"}],"elapse":0,"status":"S","url":"com.tc.session.ZookeeperPoolManager.returnObject(org.apache.zookeeper.ZooKeeper)"}],"elapse":1,"status":"S","url":"com.tc.session.zookeeper.ZookeeperSessionClient.getAttribute(java.lang.String,java.lang.String)"}],"elapse":1,"status":"S","url":"com.tc.session.TCSession.getAttribute(java.lang.String)"},{"elapse":0,"status":"S","url":"com.tc.session.servlet.RemotableRequestWrapper.getSession(boolean)"},{"children":[{"elapse":0,"status":"S","url":"com.tc.session.TCSession.access()"}],"elapse":0,"status":"S","url":"com.tc.session.TCSession.getAttribute(java.lang.String)"},{"elapse":0,"status":"S","url":"com.tc.session.servlet.RemotableRequestWrapper.getSession(boolean)"},{"elapse":0,"status":"S","url":"com.tc.session.servlet.RemotableRequestWrapper.getSession(boolean)"},{"elapse":0,"status":"S","url":"com.tc.session.TCSession.getId()"}],"elapse":329,"status":"S","url":"com.tc.session.filter.TCSessionFilter.doFilter(javax.servlet.ServletRequest,javax.servlet.ServletResponse,javax.servlet.FilterChain)"}],"elapse":329,"status":"S","url":"/home/netiquette.do"}', destination=configCur.DESTINATION, receipt="123")
        callback_listener.wait_on_receipt()
        _ntimes += 1
        print "send %s messages." % _ntimes
        #time.sleep(1)



    conn.send(body='empty', destination=configCur.DESTINATION, headers={"receipt-id": "DISCONNECT1"}, receipt="123")
    callback_listener.wait_on_receipt()
    print "send disconnect messages:DISCONNECT1"

    conn.disconnect()
