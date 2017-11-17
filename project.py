from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import DecBase, Sites, Categories, Items, Sales, Keycode

app = Flask(__name__)

engine = create_engine('sqlite:///ecommanalyser.db')
DecBase.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/sites/<sitename>/')
def siteMenu(sitename):
	sites = session.query(Sites).filter_by(site_name=sitename)
	for s in sites:
		items = session.query(Items).filter_by(s_id=s.s_id)
	output = ''
	for i in items:
		output += str(i.item_name)
		output += '</br>'
		output += str(i.price)
		output += '</br>'
		output += str(i.no_viewed)
		output += '</br>'
		output += '</br>'
	return output
	
@app.route('/sites/<sitename>/new/')
def newItem(sitename):
	return "page to create a new item. Task 1 complete!"
	
@app.route('/sites/<sitename>/<itemid>/update/')
def editItem(sitename,itemid):
	return "page to update an item. Task 2 complete!"
	
@app.route('/sites/<sitename>/<itemname>/delete/')
def deleteItem(sitename,itemid):
	return "page to delete an item. Task 3 complete!"

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=5000)
