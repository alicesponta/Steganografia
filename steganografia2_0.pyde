widthImg=500;
heightImg=400
#Variabile di appoggio
app=0
def setup():
    global i, img, app,answer, widthImg, heightImg
    #Messaggio mostrato a video appena viene eseguito lo script
    messaggio=input ("Inserisci la tua frase")
    println( str(messaggio))
    #Variabile di appoggio che prende la prima lettera della parola
    app=messaggio[0]
    print(app)
    size(500, 400)
    #Creo l'immagione
    img=createImage(widthImg,heightImg,RGB)
    disegno()
#Funzione per la visualizzazione della finestra per l'inserimento del testo
def input(message=""):
    from javax.swing import JOptionPane 
    return JOptionPane.showInputDialog (frame,message)

    
def disegno():
    global img,app,c,r,g,b,char
    #C è una variabile di appogio per la conversione esadecimale di App
    c=hex(app)
    print(c)
    img.loadPixels()
    for i in range(100*100):
        red(c)
        green(c)
        blue(c)
        img.pixels[i]= (char(c),char(c),char(c))
        img.updatePixels()
        image(img,0,0)
