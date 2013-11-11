var cardSuits = ['s','c','d','h'];
var cardFaces = ['2','3','4','5','6','7','8','9','10','j','q','k','a'];

function getCardRect(cardsMap, totalCount, card)
{
	/*TODO: move totalCount to Image property*/
	var suiteIndex = 3; // row in the card map
	if (card[0] === 'd') suiteIndex = 2;
	if (card[0] === 'c') suiteIndex = 1;
	if (card[0] === 's') suiteIndex = 0;
	
	var rowLength = totalCount / 4;
    var startIndex = cardFaces.length - rowLength;

    var cardWidth = Math.floor(cardsMap.width / rowLength);
    var cardHeight = Math.floor(cardsMap.height / 4);
    
    var cardY = suiteIndex + cardHeight;
    var cardX = 0;
    for ( var c = 0; c < rowLength; c++) {
    	if (cardFaces[startIndex + c] === card.substring(1))
		{
    		cardX = c * cardWidth;
    		break;
		}
    }
    
    return { x:cardX, y:cardY, width:cardWidth, height:cardHeight };
}

function draw() {
    var canvas = document.getElementById('canvas');
    var ctx = canvas.getContext('2d');

    ctx.fillStyle = 'rgb(0,200,200)';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    var cards = document.getElementById('cards');
    var packs = document.getElementById('decks');

    var cardWidth = Math.floor(cards.width / 9);
    var cardHeight = Math.floor(cards.height / 4);

    var cardW = Math.floor(cardWidth / 3);
    var cardH = Math.floor(cardHeight / 3);
    
    var cardShift = 1; // 3.6;

    var y = 2;
    for ( var r = 0; r < 4; r++) {
        var x = 2;
        y = r * cardH;

        for ( var c = 0; c < 9; c++) {
            x = c * cardW / cardShift;
            ctx.drawImage(cards, c * cardWidth, r * cardHeight, cardWidth,
                cardHeight, x, y, cardW, cardH);
        }

        x = x + cardW / cardShift;
        ctx.drawImage(packs, r * cardWidth, 0, cardWidth, cardHeight, x, y, cardW, cardH);
    }
}

function shuffle()
{
  
    var deck = [];
}
