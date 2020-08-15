from flask import Flask,render_template,url_for,request
from modules import create_graph, tag_query 
from updates import check_updates

graph = create_graph() 

app = Flask(__name__)

@app.route('/')
@app.route('/search')#, methods = ['Get', 'Post'])
def search():
    if check_updates():         #I have decided data update through API call 
        graph = create_graph()  #is not so often required (only once in a week)
    print(1)    
    return render_template('HTML_for_Textbox.html')

@app.route('/updateresult',methods = ['POST'])
def updateresult():
  if request.method == 'POST':
    try:
         SName = request.form['name'] 
    finally:
         return render_template('Result_for_Textbox.html', SName = tag_query(graph, SName))  
         
#app.run(host = 'localhost', port = 5005)     

if __name__ == "__main__":
    app.run(debug=True)

