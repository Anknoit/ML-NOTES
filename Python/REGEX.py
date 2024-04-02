import re

txt = "What a piece of work is a Damn 69 nigga man" 

x = re.search("^What.*man$", txt)   #punctuation signs or any shit will change everything
if x:
    print("We have a match!")
else:
    print("No match")

"""
Metacharacters
--------------------------------------------------
Metacharacters are characters with a special meaning:

Character	Description	                                Example	
-------------------------------------------------------------------
[]	A set of characters	                                "[a-m]"	
\	Signals a special sequence 
    (can also be used to escape special characters)	    "\d"	
.	Any character (except newline character)	        "he..o"	
^	Starts with                                     	"^hello"	
$	Ends with	                                        "world$"	
*	Zero or more occurrences	                        "aix*"	
+	One or more occurrences                         	"aix+"	
{}	Exactly the specified number of occurrences     	"al{2}"	
|	Either or	                                        "falls|stays"	
()	Capture and group	 	 

"""
y = re.findall("[a-m]",txt)     #Find all lowercase characters from each word in order alphabetically from a to m
print(y)

z = re.findall("\d", txt)
print(z)

a = re.findall("pi..e", txt)    #When you dont know the exact word so you provide whatever you know and it provides the string that matches the sequence
print(a)
