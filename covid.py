import requests
import bs4
import tkinter  as tk
import plyer
import time
import datetime
import threading 
from PIL import Image, ImageTk


#get html text data
def get_html_text(url):
	data=requests.get(url)
	return data


#web scraping
def corona_details_of_india():
	url="https://www.mohfw.gov.in/"#link of minstry of health
	html_data=get_html_text(url)
	#print(html_data.text) #we get  actual text
	bs=bs4.BeautifulSoup(html_data.text,"html.parser")
	#print(bs.prettify())
	#all_details=""
	info_div1=bs.find("div",class_="site-stats-count").find("li",class_="bg-blue")
	count=info_div1.find("strong").get_text()
	text=info_div1.find("span").get_text()
	all_details1=text +" : "+ count+ "\n"
	

	info_div2=bs.find("div",class_="site-stats-count").find("li",class_="bg-green")
	count=info_div2.find("strong").get_text()
	text=info_div2.find("span").get_text()
	all_details2=all_details1 + text +" : "+ count+ "\n"
	all_details1

	info_div3=bs.find("div",class_="site-stats-count").find("li",class_="bg-red")
	count=info_div3.find("strong").get_text()
	text=info_div3.find("span").get_text()
	all_details3= all_details2 + text +" : "+ count+ "\n"

	info_div4=bs.find("div",class_="site-stats-count").find("li",class_="bg-orange")
	count=info_div4.find("strong").get_text()
	text=info_div4.find("span").get_text()
	all_details4=all_details3 + text +" : "+ count+ "\n"
	print(all_details4)
	#all_details=all_details+text +" : "+ count + "\n"
	#print(all_details)
	#return all_details
	#return all_details1
	#return all_details2
	#return all_details3
	return all_details4
     #target div in site to get info
	
	#print(info_div2)
	#print(info_div3)
	#print(info_div4)
corona_details_of_india()#will get all html code


#reload website
def refresh():
	new_data=corona_details_of_india()
	print("refreshing")
	mainlabel['text']=new_data

#notify fun
def notify_me():
	while True:
		plyer.notification.notify(
	      title="COVID-19 NOTIFICATION BOX",
	      message=corona_details_of_india(),
	      timeout=10,
	      app_icon="icopic.ico"
		)
		time.sleep(30)

#this thread


#creating interface 

root= tk.Tk()
root.geometry("600x600")
root.iconbitmap("icopic.ico")
root.title("CORONA LIVE STATUS ")
root.configure(background="white")
f=("Helvetica",24,"bold")




banner=tk.PhotoImage(file= "copic.png")
banner_label=tk.Label(root,image=banner)
banner_label.pack()


mainlabel=tk.Label(root,text=corona_details_of_india(),font=f,bg="white")
mainlabel.pack()

rebtn=tk.Button(root,text="REFRESH",font=f,command=refresh)#we dont use refresh function
rebtn.pack()

infolabel=tk.Label(root,text="Data Is Extracted From Mohfw offical site",font=("Helvetica",14,"bold"),bg="white")
infolabel.pack()


#creat new threading
th1=threading.Thread(target=notify_me)
th1.setDaemon(True)#serves provided thread app close kalar notificatio bhan zata la
th1.start()


root.mainloop()#visible


