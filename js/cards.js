
function draw() {
    var canvas = document.getElementById('canvas');
    var ctx = canvas.getContext('2d');

    ctx.fillStyle = "rgb(0,200,200)";
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
    var suits = ["s","c","d","h"];
    var faces = ["6","7","8","9","10","j","q","k","a"];
   
    var deck = [];
    for (var)
}
