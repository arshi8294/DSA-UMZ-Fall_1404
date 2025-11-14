function combination(n, m:integer): integer;
begin
    if (m = n) or (m = 0) then
        return 1
    else
        return combination(n-1, m) + combination(n-1, m-1)
    end;
