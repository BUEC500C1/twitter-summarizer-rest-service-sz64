import tweets2video as t
from flask import Flask, send_from_directory
from flask_restful import Resource, Api

app = Flask(__name__);
api = Api(app);

class twittervideo_api(Resource):
	def put(self, scr_name):
		tm.tweet2vid(scr_name);
		return {scr_name: 'Added to Queue'};
	
	# def get(self, scr_name):
		# link = tm.get_link(scr_name);
		# return {scr_name: link}

	def get(self, scr_name):
		link = tm.get_link(scr_name);
		try:
			return send_from_directory('Video/', filename = link, as_attachment=True, mimetype='video/mp4', attachment_filename=link)
		except:
			return {scr_name: link}

api.add_resource(twittervideo_api, '/<string:scr_name>');

if __name__ == "__main__":
	tm = t.twittervideo();
	app.run(debug=True);