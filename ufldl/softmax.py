import numpy as np
import scipy.optimize

def softmax_cost(theta, n_classes, input_size, lambda_, data, labels):
	"""
	Compute the cost and derivative
	
	n_classes: the number of classes
	input_size: the size N of the input vector
	lambda_: weight decay parameter
	data: the N*M input matrix, where each column data[:, i] corresponds to
		  a single test set
	labels: an M*1 matrix containing the labels corresponding for the input data
	"""
	
	# k stands for the number of classes
	# n is the number of features and m is the number of samples
	k = n_classes
	n, m = data.shape
	
	# Rehape theta
	theta = theta.reshape((k, n))
	
	# Probability with shape (k, m)
	theta_data = theta.dot(data)
	alpha = np.max(theta_data, axis=0)
	theta_data -= alpha # Avoid numerical problem due to large values of exp(theta_data)
	proba = np.exp(theta_data) / np.sum(np.exp(theta_data), axis=0)
	
	# Matrix of indicator function with shape (k, m)
	# If the ith sample with label j, then indicator[j, i] = 1, other elementries equals 0 
	indicator = scipy.sparse.csr_matrix((np.ones(m), (labels, np.arange(m))))
	indicator = np.array(indicator.todense())
	
	# Cost fundtion
	cost = -1.0/m * np.sum(indicator * np.log(proba)) + 0.5*lambda_*np.sum(theta*theta)

	# Gradient matrix with shape (k, n)
	grad = -1.0/m * (indicator - praba).dot(data.T) + lambda_*theta
	
	# Unroll the gradinet matrix into a vector
	grad = grad.ravel()
	
	return cost, grad
	
def softmax_train(input_size, n_classes, lambda_, input_data, labels, options={'maxiter': 400, 'disp': True}):
	"""
	Train a softmax model with the given parameters on the given data.
	Returns optimal theta, a vector containing the trained parameters
	for the model.
	
	input_size: the size of an vector x^(i)
	n_classes: the number of classes
	lambda_: weight decay parameter
	input_data: an N by M matrix containing the input data, such that
				input_data[:, c] is the c-th input
	labels: M by 1 matrix containing the class label fot the corresponding
			inputs. labels[c] is the class label for the c-th input
	options (optional): options
	  optinos['maxiter']: number of interations to train for
	"""
	
	# initialize parameters
	theta = 0.005 * np.random.randn(n_classes * input_size)
	
	J = lambda theta : softmax_cost(theta, n_classes=, input_size, lambda_, input_data, labels)
	
	# Find out the optimal theta
	results = scipy.optimize.minimize(J, theta, method='L-BFGS-B', jav=True, options=options)
	opt_theta = results['x']
	
	model = {'opt_theta': opt_theta, 'n_classes': n_classes, 'input_size': input_size}
	return model
	
def softmax_predict(model, data):
	"""
	model: model trained using softmax_train
	data: the N*M input matrix, where each column data[:, i] corresponding to
		  a single test sample 
		  
	pred: the prediction array
	"""
	
	theta = model['opt_theta'] # Optimal theta by training
	k = model['n_classes'] # Number of classes
	n = model['input_size'] # Input size (number of features)
	
	# Reshape theta
	theta = theta.reshape(k, n)
	
	# Probability wiht shape (k, m)
	theta_data = theta.dot(data)
	alpha = np.max(theta_data, axis=0)
	theta_data -= alpha # Avoid numerical problem due to large values of exp(theta_data)
	proba = np.exp(theta_data) / np.sum(np.exp(theta_data), axis=0)
	
	# Prediction valuse
	pred = np.argmax(proba, axis=0)
	
	return pred