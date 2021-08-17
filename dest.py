from scipy.stats import binom
import numpy as np
import matplotlib.pyplot as plt
import statistics as st
import scipy.stats
'''colors = ['b','g','r','y','c']
labels = ['one','two','three','four','five']'''
n=10
p=0.6
size=20
mean_list  = []
var_list=[]
testsample1=[]
testsample2 = []
population = np.random.binomial(n,p,size) 
print(population)
populationMean=st.mean(population)
print('Population Mean {}'.format(populationMean)) #mean= n*p
#for i in range(5):
#p=p+0.05
sizesample= list(range(size))  
#print(i for i in sizesample)
#mean, var = binom.stats(n,p)
    
dist1= np.random.binomial(n,p,sizesample[4])
print('Sample 1: {}--- Mean: {}-----Variance: {}'.format(dist1,st.mean(dist1), st.variance(dist1)) )
dist2= np.random.binomial(n,p,sizesample[7])
print('Sample 2: {}--- Mean: {}-----Variance: {}'.format(dist2,st.mean(dist2), st.variance(dist2)))
dist3= np.random.binomial(n,p,sizesample[7])
print('Sample 3: {}--- Mean: {}-----Variance: {}'.format(dist3,st.mean(dist3),st.variance(dist3)))
dist4= np.random.binomial(n,p,sizesample[6])
print('Sample 4: {}--- Mean: {}-----Variance: {}'.format(dist4,st.mean(dist4), st.variance(dist4)))
dist5= np.random.binomial(n,p,sizesample[9])
print('Sample 5: {}--- Mean: {}-----Variance: {}'.format(dist5,st.mean(dist5) , st.variance(dist5)))

mean1=st.mean(dist1)
mean2=st.mean(dist2)
mean3=st.mean(dist3)
mean4=st.mean(dist4)
mean5=st.mean(dist5)
var1=st.variance(dist1)
var2=st.variance(dist2)
var3=st.variance(dist3)
var4=st.variance(dist4)
var5=st.variance(dist5)

mean_list.append(mean1)
mean_list.append(mean2)
mean_list.append(mean3)
mean_list.append(mean4)
mean_list.append(mean5)
var_list.append(var1)
var_list.append(var2)
var_list.append(var3)
var_list.append(var4)
var_list.append(var5)
#sample mean
sampleMean=st.mean(mean_list)
print('Sample Mean {}'.format(sampleMean))
print('Sample Varience {}'.format(st.variance(var_list)))

#biased / unbiased estimator
print("\n********Checking for Biased/ Unbiased estimator*******")
if (populationMean==sampleMean):
    print("Unbiased Estimator ")
else:
    print("Biased Estimator")

#Taild test (samples are from same population)
print("\n\n**************Tailed  t-Test**************")
alpha=0.05 #level of significance
testsample1= np.random.binomial(n,p,sizesample[5])
testsample2= np.random.binomial(n,p,sizesample[7])
testmean1=st.mean(testsample1)
testmean2=st.mean(testsample2)
#Null Hypothesis H0: means are equal
#Alternate Hypothesis H1: means are not equal
print('test sample 1 mean {}'.format(testmean1))
print('test sample 2 mean {}'.format(testmean2))
t_value =scipy.stats.ttest_ind(testsample2,testsample1) #t test
#Interpret via p_value
if(t_value.pvalue>alpha):
    print("Accept the null hypothesis that the means are equal")
else:
    print("Reject the  null hypothesis that the means are equal")

#cal pmf
r_values=list(range(n+1))
pmfbio=[binom.pmf(r,n,p) for r in r_values]
plt.bar(r_values, pmfbio, label='pmf', color='red')
plt.show()
#cal cdf
r_values=list(range(n+1))
cdfbio=[binom.cdf(r,n,p )for r in r_values]
plt.bar(r_values, cdfbio, label="cdf", color="yellow")
#plt.legend()
plt.show()
#plotting mean and varience in graph
X=['one','two','three','four','five']
X_axis=np.arange(len(X))
plt.bar(X_axis-0.2, mean_list, 0.4,label='Mean')
plt.bar(X_axis+0.2, var_list,0.4,label="Varience")
plt.xticks(X_axis,X)
plt.show()

