from flask import Flask, render_template, session, redirect, url_for, request
import pickle
import pandas as pd

app = Flask(__name__)
ml_model = pickle.load(open('thesis_model.pkl','rb'))

app.secret_key = 'thesis2'


@app.route('/')
def index():
      return render_template('index.html')  
 
@app.route('/prediction') 
def prediction():
      return render_template(
        'prediction.html',
        fs=[{'Financial_Status':'More than P100,000'}, {'Financial_Status':'P50,000 to P100,000'}, {'Financial_Status':'P20,000 to P50,000'}, 
               {'Financial_Status':'P10,000 to P20,000'}, {'Financial_Status':'Below P10,000'},  {'Financial_Status':'Prefer not to say'}],
        hal=[{'Has_a_laptop':'Yes'},{'Has_a_laptop':'Planning to purchase'},{'Has_a_laptop':'No'}],
        ic=[{'Internet_Connection':'Post-paid plan(Unlimited Data Subscription to PLDT, GLOBE, SMART, Sky, etc.)'},
               {'Internet_Connection':'Pre-paid plan(Limited Data Subscription)'},
               {'Internet_Connection':'No internet subscription, including no access to internet connection at all'}],
        cc100=[{'CC100':'1'},{'CC100':'1.25'},{'CC100':'1.5'},{'CC100':'1.75'},{'CC100':'2'},{'CC100':'2.25'},{'CC100':'2.5'},
               {'CC100':'2.75'},{'CC100':'3'},{'CC100':'INC'}],
        cc101=[{'CC101':'1'},{'CC101':'1.25'},{'CC101':'1.5'},{'CC101':'1.75'},{'CC101':'2'},{'CC101':'2.25'},{'CC101':'2.5'},
               {'CC101':'2.75'},{'CC101':'3'},{'CC101':'INC'},{'CC101':'5'}],
        cc102=[{'CC102':'1'},{'CC102':'1.25'},{'CC102':'1.5'},{'CC102':'1.75'},{'CC102':'2'},{'CC102':'2.25'},{'CC102':'2.5'},
               {'CC102':'2.75'},{'CC102':'3'},{'CC102':'INC'},{'CC102':'UW'}],
        csit=[{'csit':'1'},{'csit':'1.25'},{'csit':'1.5'},{'csit':'1.75'},{'csit':'2'},{'csit':'2.25'},{'csit':'2.5'},
               {'csit':'2.75'},{'csit':'3'},{'csit':'INC'},{'csit':'UW'},{'csit':'5'}],
        strand=[{'SHS_Strand':'ABM/BAM'},{'SHS_Strand':'GAS'},{'SHS_Strand':'HUMMS'},{'SHS_Strand':'STEM'},
               {'SHS_Strand':'Sports Track'},{'SHS_Strand':'TVL-HE'},{'SHS_Strand':'TVL-ICT'}],
        gender=[{'Gender':'Female'},{'Gender':'Male'},{'Gender':'Prefer not to say'}],
        year=[{'Year_Started':'2018'},{'Year_Started':'2019'},{'Year_Started':'2020'},{'Year_Started':'2021'}]
        )
    
#result page
@app.route('/predicted', methods =['GET','POST'])
def result_predict():
   Financial_Status = 0
   Has_a_Laptop = 0
   Internet_Connection = 0
   CC100_grade = 0
   CC101_grade = 0
   CC102_grade = 0
   CSIT_grade = 0
   Strand_data = {'ABM/BAM':0,'GAS':0,'HUMMS':0,'STEM':0,'Sports Track':0,'TVL-HE':0,'TVL-ICT':0}
   Gender_data = {'Female':0,'Male':0, 'Prefer not to say':0}
   Year_data = {'2018':0,'2019':0,'2020':0,'2021':0}
   
   for key in Strand_data:
      if request.form['strand'] == key:
         Strand_data[key] = 1
      else:
         Strand_data[key] = 0

   for key in Gender_data:
      if request.form['gender'] == key:
         Gender_data[key] = 1
      else:
         Gender_data[key] = 0
         
   for key in Year_data:
      if request.form['year'] == key:
         Year_data[key] = 1
      else:
         Year_data[key] = 0
       
   if request.form['fs'] == "More than P100,000":
      Financial_Status = 5
   elif request.form['fs'] == "P50,000 to P100,000":
      Financial_Status = 4
   elif request.form['fs'] == "P20,000 to P50,000":
      Financial_Status = 3
   elif request.form['fs'] == "P10,000 to P20,000":
      Financial_Status = 2
   elif request.form['fs'] == "Below P10,000":
      Financial_Status = 1
   elif request.form['fs'] == "Prefer not to say":
      Financial_Status = 0
       
   if request.form['hal']  == "Yes":
      Has_a_Laptop = 2
   elif request.form['hal'] == "Planning to purchase":
      Has_a_Laptop = 1
   elif request.form['hal'] == "No":
      Has_a_Laptop = 0
      
   if request.form['ic'] == "Post-paid plan(Unlimited Data Subscription to PLDT, GLOBE, SMART, Sky, etc.)":
      Internet_Connection = 2
   elif request.form['ic'] == "Pre-paid plan(Limited Data Subscription)":
      Internet_Connection = 1
   elif request.form['ic'] == "No internet subscription, including no access to internet connection at all":
      Internet_Connection = 0
       
   if request.form['cc100'] == "1":
      CC100_grade = 9
   elif request.form['cc100'] == "1.25":
      CC100_grade = 8
   elif request.form['cc100'] == "1.5":
      CC100_grade = 7
   elif request.form['cc100'] == "1.75":
      CC100_grade = 6
   elif request.form['cc100'] == "2":
      CC100_grade = 5    
   elif request.form['cc100'] == "2.25":
      CC100_grade = 4
   elif request.form['cc100'] == "2.5":
      CC100_grade = 3   
   elif request.form['cc100'] == "2.75":
      CC100_grade = 2
   elif request.form['cc100'] == "3":
      CC100_grade = 1    
   elif request.form['cc100'] == "INC":
      CC100_grade = 0   
    
   if request.form['cc101'] == "1":
      CC101_grade = 10
   elif request.form['cc101'] == "1.25":
      CC101_grade = 9
   elif request.form['cc101'] == "1.5":
      CC101_grade = 8
   elif request.form['cc101'] == "1.75":
      CC101_grade = 7
   elif request.form['cc101'] == "2":
      CC101_grade = 6    
   elif request.form['cc101'] == "2.25":
      CC101_grade = 5
   elif request.form['cc101'] == "2.5":
      CC101_grade = 4   
   elif request.form['cc101'] == "2.75":
      CC101_grade = 3
   elif request.form['cc101'] == "3":
      CC101_grade = 2    
   elif request.form['cc101'] == "INC":
      CC101_grade = 1
   elif request.form['cc101'] == "5":
      CC101_grade = 0
    
   if request.form['cc102'] == "1":
      CC102_grade = 10
   elif request.form['cc102'] == "1.25":
      CC102_grade = 9
   elif request.form['cc102'] == "1.5":
      CC102_grade = 8
   elif request.form['cc102'] == "1.75":
      CC102_grade = 7
   elif request.form['cc102'] == "2":
      CC102_grade = 6    
   elif request.form['cc102'] == "2.25":
      CC102_grade = 5
   elif request.form['cc102'] == "2.5":
      CC102_grade = 4   
   elif request.form['cc102'] == "2.75":
      CC102_grade = 3
   elif request.form['cc102'] == "3":
      CC102_grade = 2    
   elif request.form['cc102'] == "INC":
      CC102_grade = 1
   elif request.form['cc102'] == "UW":
      CC102_grade = 0
    
   if request.form['csit'] == "1":
      CSIT_grade = 11
   elif request.form['csit'] == "1.25":
      CSIT_grade = 10
   elif request.form['csit'] == "1.5":
      CSIT_grade = 9
   elif request.form['csit'] == "1.75":
      CSIT_grade = 8
   elif request.form['csit'] == "2":
      CSIT_grade = 7    
   elif request.form['csit'] == "2.25":
      CSIT_grade = 6
   elif request.form['csit'] == "2.5":
      CSIT_grade = 5   
   elif request.form['csit'] == "2.75":
      CSIT_grade = 4
   elif request.form['csit'] == "3":
      CSIT_grade = 3    
   elif request.form['csit'] == "INC":
      CSIT_grade = 2
   elif request.form['csit'] == "UW":
      CSIT_grade = 1
   elif request.form['csit'] == "5":
      CSIT_grade = 0
   
   newdata=dict()
   newdata['Age']= request.form['Age']
   newdata['Financial Status']= Financial_Status
   newdata['Has a Laptop']= Has_a_Laptop
   newdata['Type of Internet Connection']= Internet_Connection
   newdata['CC100']= CC100_grade
   newdata['CC101']= CC101_grade
   newdata['CC102']= CC102_grade
   newdata['CS111/IT112']= CSIT_grade
   newdata['English Prof']= request.form['EPG']
   newdata['Reading Compre']= request.form['RCG']
   newdata['Science Process']= request.form['SPG']
   newdata['Quantitative']= request.form['QG']
   newdata['Abstract']= request.form['AG']
   newdata['CET OAPR']= request.form['CET']
   newdata['SHS/HS GPA']= request.form['SHS-GPA']
   newdata['ABM/BAM']= Strand_data['ABM/BAM']
   newdata['GAS']= Strand_data['GAS']
   newdata['HUMSS']= Strand_data['HUMMS']
   newdata['STEM']= Strand_data['STEM']
   newdata['Sports Track']= Strand_data['Sports Track']
   newdata['TVL-HE']= Strand_data['TVL-HE']
   newdata['TVL-ICT']= Strand_data['TVL-ICT']
   newdata['Female']= Gender_data['Female']
   newdata['Male']= Gender_data['Male']
   newdata['Prefer not to say']= Gender_data['Prefer not to say']
   newdata['2018']= Year_data['2018']
   newdata['2019']= Year_data['2019']
   newdata['2020']= Year_data['2020']
   newdata['2021']= Year_data['2021']
    
   df=pd.DataFrame([newdata.values()],columns=list(newdata.keys()))
        
   prediction= ml_model.predict(df)
   print('\n\nPrediction: ',prediction,'\n\n')

   return render_template(
        'prediction.html', prediction=prediction,
        fs=[{'Financial_Status':'More than P100,000'}, {'Financial_Status':'P50,000 to P100,000'}, {'Financial_Status':'P20,000 to P50,000'}, 
               {'Financial_Status':'P10,000 to P20,000'}, {'Financial_Status':'Below P10,000'},  {'Financial_Status':'Prefer not to say'}],
        hal=[{'Has_a_laptop':'Yes'},{'Has_a_laptop':'Planning to purchase'},{'Has_a_laptop':'No'}],
        ic=[{'Internet_Connection':'Post-paid plan(Unlimited Data Subscription to PLDT, GLOBE, SMART, Sky, etc.)'},
               {'Internet_Connection':'Pre-paid plan(Limited Data Subscription)'},
               {'Internet_Connection':'No internet subscription, including no access to internet connection at all'}],
        cc100=[{'CC100':'1'},{'CC100':'1.25'},{'CC100':'1.5'},{'CC100':'1.75'},{'CC100':'2'},{'CC100':'2.25'},{'CC100':'2.5'},
               {'CC100':'2.75'},{'CC100':'3'},{'CC100':'INC'}],
        cc101=[{'CC101':'1'},{'CC101':'1.25'},{'CC101':'1.5'},{'CC101':'1.75'},{'CC101':'2'},{'CC101':'2.25'},{'CC101':'2.5'},
               {'CC101':'2.75'},{'CC101':'3'},{'CC101':'INC'},{'CC101':'5'}],
        cc102=[{'CC102':'1'},{'CC102':'1.25'},{'CC102':'1.5'},{'CC102':'1.75'},{'CC102':'2'},{'CC102':'2.25'},{'CC102':'2.5'},
               {'CC102':'2.75'},{'CC102':'3'},{'CC102':'INC'},{'CC102':'UW'}],
        csit=[{'csit':'1'},{'csit':'1.25'},{'csit':'1.5'},{'csit':'1.75'},{'csit':'2'},{'csit':'2.25'},{'csit':'2.5'},
               {'csit':'2.75'},{'csit':'3'},{'csit':'INC'},{'csit':'UW'},{'csit':'5'}],
        strand=[{'SHS_Strand':'ABM/BAM'},{'SHS_Strand':'GAS'},{'SHS_Strand':'HUMMS'},{'SHS_Strand':'STEM'},
               {'SHS_Strand':'Sports Track'},{'SHS_Strand':'TVL-HE'},{'SHS_Strand':'TVL-ICT'}],
        gender=[{'Gender':'Female'},{'Gender':'Male'},{'Gender':'Prefer not to say'}],
        year=[{'Year_Started':'2018'},{'Year_Started':'2019'},{'Year_Started':'2020'},{'Year_Started':'2021'}]
        )

    
if __name__ == "__main__":
    app.run(debug=True)

