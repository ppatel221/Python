# Python

The Library.py file contains functions that will help you to dof the follwoing :

* Read from file and display the content

* A function that gives you the size of the file

* A function that Encrypts the contain of a file using MD5 . 

* A function that Encrypts the contain of a file using SHA .

* A function that returns of file name and the file extension .

* A function that returns the path of the file .

# Code example 

The is an example for a function that reads from a file and diplays the content .

```
def Read_file(i_file):

	print ("\nfile content\n");

	J=open(i_file, 'r').read();

	print (J);	

	return;
```

