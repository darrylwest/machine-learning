function [theta, J_history] = gradientDescent(X, y, theta, alpha, num_iters)
%GRADIENTDESCENT Performs gradient descent to learn theta
%   theta = GRADIENTDESENT(X, y, theta, alpha, num_iters) updates theta by 
%   taking num_iters gradient steps with learning rate alpha

% Initialize some useful values
m = length(y); % number of training examples
J_history = zeros(num_iters, 1);

DBUG = false;

for iter = 1:num_iters

    % ====================== YOUR CODE HERE ======================
    % Instructions: Perform a single gradient step on the parameter vector
    %               theta. 
    %
    % Hint: While debugging, it can be useful to print out the values
    %       of the cost function (computeCost) and gradient here.
    %


    % first calc the delta then update theta vector

    delta = (X' * (X * theta - y)) / m;
    theta = theta - alpha * delta;


    % ============================================================

    % Save the cost J in every iteration    
    cost = computeCost(X, y, theta);
    J_history(iter) = cost;

    if DBUG == true && (iter < 10 || iter > num_iters - 10),
      fprintf('%d delta: %f, theta: %f,%f cost: %f\n', iter, delta(1,1), theta, cost);
    end

end

end

% unit tests...
% [theta J_hist] = gradientDescent([1 5; 1 2; 1 4; 1 5],[1 6 4 2]',[0 0]',0.01,1000);
% theta == 5.2148, -0.5733 
%
% [theta J_hist] = gradientDescent([1 5; 1 2],[1 6]',[.5 .5]',0.1,10);
% theta == 1.70986, 0.19229
% J_hist == 5.8853 5.7139 5.5475 ... 4.7861 4.6469, 4.5117

