# Opencv kütüphanesini import eder.
import cv2


# Casecade dosyamızı tanımlar.
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Fotoğrafımızı okuyup bir değişkene atadık
img = cv2.imread('test.jpg')

# Fotoğrafımızı gri formata çevirir.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Fotoğraftaki yüzleri bulur. Bulduğu yüzlerin sol üstünden kordinatı alıp (x,y) olarak atar.
# Yüzün büyüklüğü (w,h) olarak saklar.
# Yani faces değişkeninde dört ayrı değerin listesi tutulmakta.
# scaleFactor verilen görüntünün %10 oranında boyutunun azaltılması anlamına gelmektedir.
# Diğer parametreler için https://docs.opencv.org/2.4.13.2/modules/objdetect/doc/cascade_classification.html#cv2.CascadeClassifier.detectMultiScale
faces = face_cascade.detectMultiScale(img, scaleFactor=1.06, minNeighbors=4)

sayac=0

# Tüm kordinat ve büyüklük verilerini döngüye alıyoruz.
for (x,y,w,h) in faces:
    print(x,y,w,h)
    # rectangle fonksiyonu dikdörtgen çizmek için kullanılır.()
    # (fotoğrafın ismi, koordinatları, karşı kordinatları, rengi, kalınlığı, (istenirse lineType = LINE_8 ile çizgi tipi eklenebilir))
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,255,0), 5)
    cv2.putText(img,str(sayac),(x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,255))   
    sayac +=1

print(len(faces))

# İlk argüman pencerenin ismi, İkinci argüman pencerede gösterilecek olan resmin ismi.
cv2.imshow('Face Detection', img) 

# Herhangi bir klavye tuşuna bastığımzda programı kapatır.
cv2.waitKey(0) 

