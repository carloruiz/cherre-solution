from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine

app = Flask(__name__)
api = Api(app)
db_engine = create_engine('sqlite:////testdb.db')

query = '''CREATE TABLE IF NOT EXISTS FrequentBrowsers AS SELECT COUNT(p.id) as counts, p.first_name, p.last_name FROM people as p INNER JOIN visits as v ON p.id = v.personId GROUP BY p.id ORDER BY counts DESC LIMIT 10;'''

db_engine.execute(query)

class Frequent_Visitors(Resource):
    def get(self):
        try:
            res = db_engine.execute('SELECT * FROM FrequentBrowsers;')
            out = [{'visits':r[0], 'first':r[1], 'last':r[2]} for r in res]
        except:
            return {}, 400 
        return out


api.add_resource(Frequent_Visitors, '/frequent')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

