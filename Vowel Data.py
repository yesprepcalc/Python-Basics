import os
import math
import numpy as np
import sklearn
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis

os.chdir('/Volumes/YPNHS/Python Code')
vowel_train = np.loadtxt('vowel_train.csv', delimiter=',', skiprows=1)
vowel_test = np.loadtxt('vowel_test.csv', delimiter=',', skiprows=1)
vowel_train[:5] #first five rows
vowel_train[0,0] #first row, first column

y_tr = vowel_train[:,0]
X_tr = vowel_train[:,1:]
n = len(y_tr)

y_test = vowel_test[:,0]
X_test = vowel_test[:,1:]

#Goal: Quadratic Discriminant Analysis
#to predict whether data is one of 11 vowels

##QDA: using training data,
#find mean vector & covariance matrix for each k class
#form discriminant function for each class
#d(x) = -.5log(determinant(cov_mat)) + (x-mu).T * inv(cov_mat) * (x-mu) + log(p_k)

#save mean vectors, covariance matrix and probability for each class
def QDA_train(y, X):
    means = []
    cov = []
    prob = []

    for i in range(0,11):
        index = (y == (i+1))
        y_k = y[index]
        X_i = X[index]
    
        means.append(X_i.mean(axis=0))

        #eigen decomp Q.T * U * Q
        #Q mat of eigen vec, U diag mat of eigenval
        cov_mat = np.cov(X_i.T)
        #u, Q = np.linalg.eig(cov_mat)
        #U = np.diag(u)
        #eig_decomp = (Q.T.dot(U)).dot(Q)
        
        cov.append(cov_mat) #try eigen decomp on cov mat
        prob.append(math.log(len(y_k)/n))

    means = np.array(means)
    cov = np.array(cov)
    prob = np.array(prob)
    return means, cov, prob

#calculate discriminant function for all k classes
#return index of max class
def QDA_pred(x, means, cov, prob):
    discr = [0]*10
    for i in range(0,10):
        diff = (x - means[i])
        
        log_det = np.linalg.slogdet(cov[i])[1]
        std_mean_diff = (diff.T.dot(np.linalg.inv(cov[i]))).dot(diff)
        discr[i] = log_det + std_mean_diff - 2*prob[i]
    return np.argmin(np.array(discr))+1

def QDA_homemade(tr_class, tr_data, test_data):
    means, cov, prob = QDA_train(tr_class, tr_data)
    m = test_data.shape[0]
    pred_class = [0]*m
    
    for j in range(0,m):
        x = test_data[j]
        pred_class[j] = QDA_pred(x, means, cov, prob)

    return np.array(pred_class)

print("homemade qda predicted classes: ")
print(QDA_homemade(y_tr, X_tr, X_test))

model = QuadraticDiscriminantAnalysis(store_covariance = True)
model.fit(X_tr, y_tr)
print("sklearn qda predicted classes: ")
print(model.predict(X_test))
