import sys
from workflow import Workflow, web

def get_data(EPSG):
	url = 'http://epsg.io/?'

	params = dict(format='json', q=EPSG)

	r = web.get(url, params)
	r.raise_for_status()
	return r.json()


def main(wf):
	args = wf.args[0]

	wf.add_item(title = 'Search \'%s\' in epsg.io' % args, arg=args, valid=True)

	def wrapper():
		return get_data(args)

	res_json = wf.cached_data("epsg_%s" % args, wrapper, max_age=600)
	
	if res_json['number_result'] >= 1:
		for result in res_json['results']:
			wf.add_item(title = u'EPSG %s: %s' % (result['code'], result['name']), subtitle=u'kind: %s, unit: %s' % (result['kind'], result['unit']), arg=result['code'], valid=True)
			
	wf.send_feedback()

				
if __name__ == u'__main__':
	wf = Workflow()
	sys.exit(wf.run(main))