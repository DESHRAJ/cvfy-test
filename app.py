import cvfy

app = cvfy.register('gh:107.170.77.168:61805212:3000:8002')

@cvfy.crossdomain
@app.listen()
def getsize():
        
    ## receiving the data
    alltext = cvfy.getTextArray()
    allimages = cvfy.getImageArray()
    
    ## get size of both images
    size1 = str(len(allimages[0].read()))
    size2 = str(len(allimages[1].read()))
    
    ## sending back the data
    data1 = alltext[0] + ' ' + size1 + ' bytes'
    data2 = alltext[1] + ' ' + size2 + ' bytes'
    cvfy.sendTextArray([data1, data2])

    return "Ok"
        
app.run()
