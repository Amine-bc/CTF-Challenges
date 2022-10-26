Program hideflag ;
uses StrUtils;
Const key='reLkEgmtWUKJihEdOvHbgKhioPfaqw' ;
//--------Main--------//
Var
flag,flaghidden,flag1 : String ;
begin
WriteLn('Enter the flag:');
Read(flag);
flaghidden := XorEncode(key,flag);
WriteLn(flaghidden);
end.