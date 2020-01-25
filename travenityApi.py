import random
def searchTrains(board, dest):
  json = {
  "results": [
    {
      "arrivalTime": "1:35",
      "metro": {
        "metroId": 1429,
        "loc": [28.620331, 77.373905]
      }
    },
    {
      "arrivalTime": "3:35",
      "metro": {
        "metroId": 1427,
        "loc": [28.627924, 77.375070]
      }
    }
  ]
}
  return json

def getCount(imgPath):
  return random.randint(5,30)

def checkTrain(metroId):
  json = {
  "metroId": metroId,
  "density": []
  }
  imgPaths = ['img1.jpg', 'img2.jpg', 'img3.jpg' ,'img4.jpg' ,'img5.jpg' ,'img6.jpg']
  for imgPath in imgPaths:
    count = getCount(imgPath)
    json["density"].append(count)