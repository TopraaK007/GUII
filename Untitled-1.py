from tkinter import *
from tkcalendar import DateEntry
from tkinter import messagebox
import smtplib
master=Tk()

def gonder():
    mesaj=""
    try:
        if var.get():
            if var.get()==1:
                mesaj+="Sisteme Kaydedilecektir!"
                tip=hatirlatma_secenek.get()  if hatirlatma_secenek.get()=='' else 'Genel'
                tarih=hatirlatma_tarih_secici.get()
                m=metin_alani.get("1.0 ","end")

                with open("hatirlatma.txt","w",encoding="utf-8") as dosya:
                    dosya.write("{} kategorisinde {} tarihinde ({}) mesajınız kaydedilmiştir".format(tip,tarih,m))
            else:
                mesaj+="E-posta yoluyla hatırlatma yapılacaktır!"
                sender="kullanici@gmail.com"
                reciever=sender
                try:
                    server=smtplib.SMTP('smtp.gmail.com',587)
                    server.ehlo()
                    server.starttls()
                    subject="{}".format(m)
                    mailContent=f"To:{reciever}\nFrom:{sender}\n\nSubject{subject}"
                    server.sendmail(sender,reciever,mailContent)
                except:
                    print("E-posta yollanamadı!")
                finally:
                    server.quit()    

            messagebox.showinfo("İşlem Başarılı",mesaj)
        else:
            mesaj+="Lütfen Boş Alanları Doldurunuz!" 
            messagebox.showwarning ("Yetersiz Bilgi",mesaj)          
    except:
        mesaj+="Hata lütfen tekrar deneyiniz!"
        messagebox.showerror("İşlem Başarısız",mesaj)
    finally:
        master.destroy()   
    return            

canvas=Canvas(master, height=450,width=750)
canvas.pack()

frame_ust= Frame(master,bg="light blue")
frame_ust.place(relx=0.1,rely=0.1,relheight=0.1,relwidth=0.8)

frame_alt_sol=Frame(master,bg="light blue")
frame_alt_sol.place(relx=0.1,rely=0.22,relwidth=0.23,relheight=0.5)

frame_ust_alt_sag=Frame(master,bg="light blue")
frame_ust_alt_sag.place(rely=0.22,relx=0.34,relheight=0.5,relwidth=0.56)

hatirlatma_t=Label(frame_ust,bg="light blue",text="Hatırlatma Türü:",font="Verdana 8 bold")
hatirlatma_t.pack(padx=10,pady=10,side=LEFT)

hatirlatma_secenek=StringVar(frame_ust)
hatirlatma_secenek.set("\t")
hatirlatma_menu=OptionMenu(frame_ust,hatirlatma_secenek,"Doğum Günü","Evlilik Yıldönümü","Sınav","Alışveriş","Ödemeler")
hatirlatma_menu.pack(padx=10,pady=10,side=LEFT)

hatirlatma_tarih_secici=DateEntry(frame_ust, width=10,background="orange",foreground="black",borderwidth=1,locale="de_DE")
hatirlatma_tarih_secici._top_cal.overrideredirect(False)
hatirlatma_tarih_secici.pack(padx=10,pady=10,side=RIGHT)
hatirlatma_tarihi=Label(frame_ust,text="Hatırlatma Tarihi:",font="Verdana 8 bold",bg="light blue")
hatirlatma_tarihi.pack(pady=10,padx=10,side=RIGHT)

Label(frame_alt_sol,text="Gönderim Tipi:",font="Verdana 8 bold",bg="light blue",).pack(padx=30,pady=10,anchor=NW)

var=IntVar()
R1=Radiobutton(frame_alt_sol,text="Sisteme Kaydet",variable=var,value=1,bg="light blue",font="Verdana 8 ")
R1.pack(anchor=NW,pady=5,padx=15)

R2=Radiobutton(frame_alt_sol,text="E-posta gönder",variable=var,value=2,bg="light blue",font="Verdana 8 ")
R2.pack(anchor=NW,pady=5,padx=15)

Label(frame_alt_sol,text="Hatırlatma Zamanı:",bg="light blue",font="Verdana 7 bold").pack(padx=30,pady=5,anchor=NW)

var1=IntVar()
C1=Checkbutton(frame_alt_sol,text="Bir Ay Önce",bg="light blue",font="Verdana 8",variable=var1,onvalue=1,offvalue=0)
C1.pack(padx=15,pady=5,anchor=NW)

var2=IntVar()
C2=Checkbutton(frame_alt_sol,text="Bir Hafta Önce",bg="light blue",font="Verdana 8",variable=var2,onvalue=1,offvalue=0)
C2.pack(padx=15,pady=5,anchor=NW)

var3=IntVar()
C3=Checkbutton(frame_alt_sol,text="Bir Gün Önce",bg="light blue",font="Verdana 8",variable=var3,onvalue=1,offvalue=0)
C3.pack(padx=15,pady=5,anchor=NW)

Label(frame_ust_alt_sag,text="Hatırlatma Mesajı:",bg="light blue",font="Verdana 8 bold").pack(padx=10,pady=10,anchor=NW)
metin_alani=Text(frame_ust_alt_sag,width=50, height=9)
metin_alani.pack()
hatirltama_mesaji="Hatırlatma Mesajı Giriniz..."
metin_alani.tag_configure('style',foreground='#bfbfbf',font=("Verdana",7,"bold"))
metin_alani.insert(END,hatirltama_mesaji,'style')

Button(frame_ust_alt_sag,text="Gönder",command=gonder).pack(pady=10,anchor=S)




master.mainloop()