from calest import calest_app, mongo
from flask import request, jsonify, Response
from ..models.search import Search

output = Search


@calest_app.route('/api/v1/text', methods=['POST'])
def post_text_file():
    global output
    output = request.form['']
    get_search = Search(output).split_sentences()
    save_search = mongo.db.searches
    return jsonify(get_search), 201

@calest_app.route("/")
def hello():
    return '''
        <html><body>
        Hello. <a href="/getPlotCSV">Click me.</a>
        </body></html>
        '''

@calest_app.route("/getPlotCSV")
def getPlotCSV():
    # with open("outputs/Adjacency.csv") as fp:
    #     csv = fp.read()
    csv = '1,2,3\n4,5,6\n'
    return Response(
        csv,
        mimetype="text/csv",
        headers={"Content-disposition":
                 "attachment; filename=medals.csv"})


app.run(debug=True)
