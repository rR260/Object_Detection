from PIL import Image           #library to read image
import pytesseract              #library to scan image
import os                       #library to operate image
import cv2                      #library to open,read and write image
import mysql.connector          #library to connect to database 
import urllib.parse             #library to join multiple url's
url1=os.path.abspath(r'C:/Users/user/Downloads')  #path of the images in the system
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"   #file to scan images
mydb = mysql.connector.connect(             
  host="localhost",
  user="root",
  passwd="",                                #code to establish connectivity between database and python ide
  database="test"
)
sum=0
mycursor = mydb.cursor()                    #database cursor stated active
input_images = input("Enter a list of images you want separated by space: ")  #take images as input from user
userList = input_images.split()                     #list of images is created
for i in range(0,len(userList)):                    #till all the images are scanned and detected
    img=cv2.imread(url1+'/'+userList[i]+'.jpg')     #read the images taken as input
    sql = "SELECT * FROM products WHERE Items =%s"  #search for its price in the database
    id=(userList[i],)                               #scan and detect the image
    mycursor.execute(sql,id)
    myresult = mycursor.fetchall()                  #image price is extracted
    print(myresult)                                 #image along with its price is printed
    sum=sum+myresult[0][1]                          
    cv2.imshow(userList[i],img)                     #image is detected and is displayed along with its name
print("Total Price : ",sum)                         #Total price of all the items is printed
