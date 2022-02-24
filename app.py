#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask


# In[2]:


app = Flask(__name__)


# In[3]:


from flask import request, render_template
import joblib

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        AnnualIncome = request.form.get("Annual Income")
        Age = request.form.get("Age")
        LoanAmount = request.form.get("Loan Amount")
        print(AnnualIncome, Age, LoanAmount)
        model=joblib.load("Default Probability")
        pred=model.predict([[float(AnnualIncome), float(Age), float(LoanAmount)]])
        s = "The predicted bankruptcy score is : " + str(pred)
        return(render_template("index.html", result=s))
    else:
        return(render_template("index.html", result="2"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:




