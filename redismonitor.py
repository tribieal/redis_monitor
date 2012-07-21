import json,redis,cherrypy


class pubweb():pass

root = pubweb()

def _get_info(hostip,hostport):
    hostip = str(hostip)
    hostport = int(hostport)
    r = redis.StrictRedis(host=hostip, port=hostport, db=0)
    
    return json.dumps(r.info())
    #return r.info()
_get_info.exposed = True

root._get_info = _get_info

cherrypy.config.update({'server.socket_host':'0.0.0.0','server.socket_port':8055})
cherrypy.quickstart(root)
