
# coding: utf-8

# In[25]:


import numpy as np
import pandas as pd
import joblib


# In[26]:







# In[28]:

def predict(centre,gender,labour_category,labour_type,state,district,month,year):


	# In[27]:
	
	file=open("ML/mappings.txt","r")
	data_maps=eval(file.read())
	file.close()


	model=joblib.load("ML/reg_xgb.joblib")


	df=pd.DataFrame({'Centre':[centre],'Gender':[gender],'LabourCategory':[labour_category],'LabourType':[labour_type],'State':[state],'District':[district],'Month':[month],'Year':[int(year)]})
	print(df)


	# In[29]:


	for i in list(data_maps.keys()):
		df[i].replace(data_maps[i],inplace=True)


	# In[22]:


	#df.drop(['Wage(INR)'],axis=1,inplace=True)


	# In[30]:


	pred=model.predict(df)[0]
	print("\n\n\nResult:",pred,"\n\n\n")
	return pred
	
#result=predict()
#print(result)
	

