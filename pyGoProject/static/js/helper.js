function toPoint(x, y){
    var xx = Math.floor(x / SIZE +0.5);
    var yy = Math.floor(y / SIZE +0.5);

    return [xx -1, yy -1];
}

function toCoor(x, y){
    return [(x+1)*SIZE, (y+1)*SIZE];
}


