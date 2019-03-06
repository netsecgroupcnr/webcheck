# This program is created by NetSec group of CNR-IEIIT: http://www.netsec.ieiit.cnr.it
# Original GitHub page for the is https://github.com/netsecgroupcnr/webcheck

import cherrypy

class HelloWorld(object):
	def index(self):
		MAX = 150
		result = '''<html>
			<head>
			<meta http-equiv="refresh" content="10">
			<title>HTTP Server Status Check</title>
			<script type="text/javascript" src="https://www.google.com/jsapi"></script>
			<script type="text/javascript">
				google.load("visualization", "1", {packages:["corechart"]});
				google.setOnLoadCallback(drawChart);
				function drawChart() {
					var data = google.visualization.arrayToDataTable([
						['t', 'Seized Connections'],
			'''
		in_file = open("status.txt","r")
		lines = in_file.readlines()
		in_file.close()
		bgcolor = 'afa'
		i = 0
		for l in lines:
			try: v = int(l[:-1])
			except: continue
			if v >= MAX:
				bgcolor = 'faa'
				v = MAX
			else:
				bgcolor = 'afa'
			ii = abs(int(i)-60)
			result += "['-"+str(ii)+"', "+str(v)+"],"
			i += 1
		result += '''
					]);
					var options = {
						title: 'Server Status',
						hAxis: {title: 'time', titleTextStyle: {color: '#333'}},'''
		result += "vAxis: {title: 'connections', minValue: 0, maxValue: 100, viewWindow: {min:0,max:"+str(MAX)+"}}"
		result += '''
					};
					var chart = new google.visualization.AreaChart(document.getElementById('chart_div'));
					chart.draw(data, options);
				}
			</script>
			</head>'''
		result += '<body style="text-align:center;padding:20px;background-color:#'+bgcolor+';">'
		result += '''
				<div style="padding:30px;font-size:2em;font-weight:bold;text-transform:uppercase;">Server Status Check</div>
				<div id="chart_div" style="border:1px solid #000; width:900px;height:500px;margin:0 auto;text-align:center;"></div>
			</body>
			</html>'''
		return result
	index.exposed = True

cherrypy.server.socket_host = '0.0.0.0'
cherrypy.server.socket_port = 8000
cherrypy.quickstart(HelloWorld())

