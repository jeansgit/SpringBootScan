#!/usr/bin/python3
# -*- coding: UTF-8 -*- 
# Author Jean
import requests
import urllib3
import threading

urllib3.disable_warnings()

file = open('url.txt','r+')
path = ['/%20/swagger-ui.html', '/actuator', '/actuator/auditevents', '/actuator/beans', '/actuator/conditions', '/actuator/configprops', '/actuator/env', '/actuator/health', '/actuator/heapdump', '/actuator/httptrace', '/actuator/hystrix.stream', '/actuator/info', '/actuator/jolokia', '/actuator/loggers', '/actuator/mappings', '/actuator/metrics', '/actuator/scheduledtasks', '/actuator/threaddump', '/api-docs', '/api.html', '/api/index.html', '/api/swagger-ui.html', '/api/v2/api-docs', '/auditevents', '/autoconfig', '/beans', '/caches', '/conditions', '/configprops', '/distv2/index.html', '/docs', '/dubbo-provider/distv2/index.html', '/dump', '/env', '/flyway', '/health', '/heapdump', '/httptrace', '/info', '/intergrationgraph', '/jolokia', '/liquibase', '/logfile', '/loggers', '/mappings', '/metrics', '/prometheus', '/refresh', '/scheduledtasks', '/sessions', '/shutdown', '/spring-security-oauth-resource/swagger-ui.html', '/spring-security-rest/api/swagger-ui.html', '/static/swagger.json', '/sw/swagger-ui.html', '/swagger', '/swagger-dubbo/api-docs', '/swagger-ui', '/swagger-ui.html', '/swagger-ui/html', '/swagger-ui/index.html', '/swagger/codes', '/swagger/index.html', '/swagger/static/index.html', '/template/swagger-ui.html', '/threaddump', '/trace', '/user/swagger-ui.html', '/v2/api-docs', '/v2/swagger.json', '/actuator/logfile', '/actuator/swagger-ui.html', '/actuator/trace', '/swagger-resources/configuration/ui', '/swagger-resources/configuration/security', '/api/swagger', '/Swagger/ui/index', '/swagger/ui', '/libs/swaggerui', '/api/swaggerui', '/api/swagger/ui', '/api/doc', '/docs/', '/doc.html', '/v1/api-docs', '/v3/api-docs', '/cloudfoundryapplication', '/druid/index.html', '/druid/login.html', '/druid/websession.html', '/entity/all', '/env/(name)', '/eureka', '/gateway/actuator', '/gateway/actuator/auditevents', '/gateway/actuator/beans', '/gateway/actuator/conditions', '/gateway/actuator/configprops', '/gateway/actuator/env', '/gateway/actuator/health', '/gateway/actuator/heapdump', '/gateway/actuator/httptrace', '/gateway/actuator/hystrix.stream', '/gateway/actuator/info', '/gateway/actuator/jolokia', '/gateway/actuator/logfile', '/gateway/actuator/loggers', '/gateway/actuator/mappings', '/gateway/actuator/metrics', '/gateway/actuator/scheduledtasks', '/gateway/actuator/swagger-ui.html', '/gateway/actuator/threaddump', '/gateway/actuator/trace', '/heapdump.json', '/hystrix', '/hystrix.stream', '/jolokia/list', '/monitor', '/swagger/swagger-ui.html', '/system/druid/index.html', '/v1.1/swagger-ui.html', '/v1.2/swagger-ui.html', '/v1.3/swagger-ui.html', '/v1.4/swagger-ui.html', '/v1.5/swagger-ui.html', '/v1.6/swagger-ui.html', '/v1.7/swagger-ui.html', '/v1.8/swagger-ui.html', '/v1.9/swagger-ui.html', '/v2.0/swagger-ui.html', '/v2.1/swagger-ui.html', '/v2.2/swagger-ui.html', '/v2.3/swagger-ui.html', '/swagger/v1/swagger.json', '/swagger/v2/swagger.json', '/webpage/system/druid/index.html']
urls = [] 
for i in file.readlines():
	#print(i.strip())
	for j in path:
		urls.append(i.strip()+j)
#print(urls)
headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chro'
                      'me/53.0.2785.104 Safari/537.36 Core/1.53.2372.400 QQBrowser/9.5.10548.400'
}

def springcheck(url):
	try:
		#print("开启检测%s......"%url)
		response = requests.get(url,headers=headers,verify=False,allow_redirects=False)
		if response.text:
			if response.status_code==200:
				print("Url:%s,Content-length:%s"%(url,str(len(response.content))))
	except:
		pass

thread = []
for url in urls:
	t = threading.Thread(target=springcheck,args=(url,))
	thread.append(t)
for t in range(len(thread)):
	thread[t].start()
for t in range(len(thread)):
	thread[t].join()
