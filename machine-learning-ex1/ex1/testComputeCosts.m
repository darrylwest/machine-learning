function ok = testComputeCosts()

    ok = true;
    check = 1E-6;

    % X is the design matrix containing training data
    % y = is class label vector with the y values

    X = [1 2; 1 3; 1 4; 1 5];
    y = [ 7; 6; 5; 4 ]; 
    theta = [ 0.1 ; 0.2 ];

    cost = computeCost( X, y, theta );

    fprintf('cost %f\n', cost);

    if abs(cost - 11.9450) > check
      fprintf('cost failed...');
      whos;
      ok = false;
    end

    X = [ 1 2 3; 1 3 4; 1 4 5; 1 5 6];
    y = [ 7; 6; 5; 4 ]; 
    theta = [ 0.1; 0.2 ; 0.3 ];
    cost = computeCost( X, y, theta );

    fprintf('cost %f\n', cost);

    if abs(cost - 7.0175) > check
      fprintf('cost failed...');
      whos;
      ok = false;
    end
    
    % from the housing example
    X = [ 1 1 ; 1 2 ; 1 3 ];
    y = [ 1 ; 2 ; 3 ]; 
    theta = [ 0.0 ; 0.0 ];
    cost = computeCost( X, y, theta );

    fprintf('cost %f\n', cost);

    if abs(cost - 2.333333) > check
      fprintf('cost failed...');
      whos;
      ok = false;
    end
    
    theta = [ 0 ; 1 ];
    cost = computeCost( X, y, theta );

    fprintf('cost %f\n', cost);

    if abs(cost - 0.0) > check
      fprintf('cost failed...');
      whos;
      ok = false;
    end

    % tests complete...
    if ok == true
      fprintf('all tests passed!\n');
    end

end

