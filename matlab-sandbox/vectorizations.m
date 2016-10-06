function vectorizations() 
    % define the data sets theta and X

    theta = [ 2 ; 4 ; 6 ]; 
    X = [ 7 ; 3 ; 1 ];
    m = length( theta );

    % calc the prediction (p) using a standard loop

    p1 = 0;
    for j = 1:m, p1 = p1 + theta(j) * X(j); end;

    fprintf('loop prediction = %d\n', p1);

    p2 = theta' * X;

    fprintf('vectorized prediction = %d\n', p2);

end;
