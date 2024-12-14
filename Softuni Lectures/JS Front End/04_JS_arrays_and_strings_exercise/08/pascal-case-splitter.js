function solve(string) {
    console.log(string.match(/[A-Z][a-z]*/g).join(', '));
}

solve('SplitMeIfYouCanHaHaYouCantOrYouCan'); //	Split, Me, If, You, Can, Ha, Ha, You, Cant, Or, You, Can
solve('HoldTheDoor'); //	Hold, The, Door
solve('ThisIsSoAnnoyingToDo'); //	This, Is, So, Annoying, To, Do
