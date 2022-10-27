# Solution for Pascal challenge in reverse category for MiniCTF-22-23
*I'll be working using Pascal Language so that you can understand the solution*

 **In order to decode the string in hidden flag using the same key that I could find declared in const simply I will use the Built-in function XorDecode from the same Pascal library *StrUtils* that I found here :**
 *https://www.freepascal.org/docs-html/rtl/strutils/xordecode.html*

- The function will be applied on a hex string so I have to regroup every two decimal digits to have a hex number that represents the ASCII code of a certain character. 
- Then I will get this *010d2907290a0c003226303e010d1a0223172f3d0f2e1a0c12* the code I will give to my encoding function.