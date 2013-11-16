// Requires kinetic-v4.7.2.js 

function drawScene(containerId, cardsId, decksId) {
    var stage = new Kinetic.Stage({
        width: 800,
        height: 300,
        container: containerId
        });
        
    var layer = new Kinetic.Layer();
    
    var imageObj = document.getElementById(cardsId);

    var cardRect = getCardRect(imageObj, 36, 's6');

    var image = new Kinetic.Image({
        x: 200,
        y: 0,
        height: cardRect.height/3,
        width: cardRect.width/3,
        image: imageObj,
        crop: cardRect
    });
    
    layer.add(image);
    stage.add(layer);
}

