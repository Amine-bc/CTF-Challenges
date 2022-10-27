# Solution for Pascal challenge in reverse category for MiniCTF-22-23
*I'll be working using Pascal Language so that you can understand the solution*

 **In order to decode the string in hidden flag using the same key that I could find declared in const simply I will use the Built-in function XorDecode from the same Pascal library *StrUtils* that I found here :**
 *https://www.freepascal.org/docs-html/rtl/strutils/xordecode.html*

- The function will be applied on a hex string so I have to regroup every two digits to have a hex number that represents the ASCII code of a certain character. 
