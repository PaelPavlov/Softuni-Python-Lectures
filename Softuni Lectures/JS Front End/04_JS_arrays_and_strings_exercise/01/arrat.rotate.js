Array.prototype.rotate = function(count) {
    for ( let i = 0; i < count; i++) {
        this.push(this.shift());
    }
    return this;
}

let arr = [51, 47, 32, 61, 21];
console.log( arr.rotate(2).join(' ') );
// 32 61 21 51 47
