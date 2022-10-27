Program hideflag ;
uses StrUtils ;
Const key='reLkEgmtWUKJihEdOvHbgKhioPfaqw' ;
Const password='113417411012050384811774126521235438611205890259952182051125';
//--------Main--------//
Var
flag, flaghidden : String ;
i, num: integer ;
begin
WriteLn('Enter the password:');
Read(flag);
flaghidden := '' ;
// the xor 

for i := 1 to Length(flag) do
begin
num := (Ord(flag[i]) xor Ord(key[i])) ;
flaghidden := flaghidden + InttoStr(num);
end;


// compare the xor result with password //
if ( Comparestr(password,flaghidden) = 0 ) then 
begin
writeln('yes! this is the password, validate the challenge with it');
end;

end.
