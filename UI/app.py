from database import Question
from sqlachemy.engine import create_engine
from sqlalchemy.orm import sessionmaker


from flask import Flask, render_template,flash,redirect,request
app = Flask(__name__)
app.secret_key='thisisasecretkey'


@app.route('/', methods=['GET','Post'])
def index():
  if request.method=='POST':
     question=request.form.get('question')
     op1=request.form.get("op1")
     op2=request.form.get("op2")
     op3=request.form.get("op3")     
     op4=request.form.get("op4")
     ans=request.form.get('ans')
     category=request.form.get("category")
     
     if not question or len(question) <5:
       flash('Question is required and should have atlest 5 characters')
       return redirect('/')
     elif not op1:
       flash('Option 1 is required')
       return redirect('/')     
     elif not op2:
       flash('Option 2 is required')
       return redirect('/')     
     elif not op3:
       flash('Option 3 is required')
       return redirect('/')     
     elif not op4:
       flash('Option 4 is required')
       return redirect('/')     
     elif not category:
       flash('Category is required')
       return redirect('/')     
     elif not ans or ans==op1 or ans==op2 or ans==op3 or ans==op4:
       flash('Answer 1 is required')
       return redirect('/')     
     else:
      flash("Successful")
      return redirect('/')

  return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 