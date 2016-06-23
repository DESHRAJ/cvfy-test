import cvfy

app = cvfy.register('gh:107.170.77.168:61805212:3000:8002')

@cvfy.crossdomain
@app.listen()
def getsize():
        
    ## receiving the data
    allimages = cvfy.getImageArray()
    
    data = []
    ## sending back the data
    for image in allimages:
    	data.append(str(len(image.read())))

    cvfy.sendTextArray(data)

    return "Ok"
        
app.run()
