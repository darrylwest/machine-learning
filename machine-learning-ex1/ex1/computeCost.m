function J = computeCost(X, y, theta)
%COMPUTECOST Compute cost for linear regression
%   J = COMPUTECOST(X, y, theta) computes the cost of using theta as the
%   parameter for linear regression to fit the data points in X and y

% Initialize some useful values
m = length(y); % number of training examples


% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta
%               You should set J to the cost.

% X is the design matrix containing training data
% y = is class label vector with the y values

predictions = X * theta;
errors = (predictions - y) .^ 2;

% You need to return the following variables correctly 
J = 1 / (2 * m) * sum(errors);

% or do this -> J = sum((X * theta - y) .^ 2 ) / (2 * m);

% =========================================================================

end

% unit tests...
% computeCost( [1 2; 1 3; 1 4; 1 5], [7;6;5;4], [0.1;0.2] ) == 11.9450
% computeCost( [1 2 3; 1 3 4; 1 4 5; 1 5 6], [7;6;5;4], [0.1;0.2;0.3]) == 7.0175
