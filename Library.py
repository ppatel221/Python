# import os
import os.path
import hashlib
import unittest


#function that returns the file path.

def DisplayFilePath(i_file):
	
	print("Your file path:\t",i_file);

	return;

#function that returns the file extension and the file name.

def Displayfile_Ext(i_file):
	print ("file name and extension: ",os.path.basename(i_file))
	return;

#function the size of the file.


def Displayfile_size(i_file):

	print("file size:  ",os.path.getsize(i_file))
	return;

#function to encrypt the content of a file using MD5

def EncryptMD5(i_file):

 hashpass = hashlib.md5(i_file.encode('utf8')).hexdigest()

 print ("encrypted using MD5 :\t");
 print (hashpass);

 return;

#function to encrypt the content of a file using SHA256


def EncryptSHA(i_file):
	hashpass1 = hashlib.sha256(i_file.encode('utf16')).hexdigest();
	

	print ("encrypted using SHA :\t");

	print (hashpass1);

	return;

#function to read the file and display the content of it	

def Read_file(i_file):

	print ("\nfile content\n");

	J=open(i_file, 'r').read();

	print (J);	

	return;
	
##--- Getting file information ---##

i_file = "1.txt";

print("---------------------------------------------------")

DisplayFilePath(i_file);

Displayfile_Ext(i_file);

Displayfile_size(i_file);

EncryptMD5(i_file);

EncryptSHA(i_file);

Read_file(i_file);