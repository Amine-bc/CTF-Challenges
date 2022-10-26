Program solution ;
uses StrUtils;
Const key='reLkEgmtWUKJihEdOvHbgKhioPfaqw' ;
//--------Main--------//
Var
flag,flaghidden : String ;
begin
WriteLn('Enter the flag:');
Read(flaghidden);
flag := XorDecode(key,flaghidden);
WriteLn(flag);
end.