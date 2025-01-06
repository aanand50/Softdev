//Team Phantom Tollbooth :: Clyde Sinclair, Fierce Dragon
//SoftDev pd0
//K27 - Basic functions in JavaScript
//2025-01-06m

//JavaScript implementations of Day0 recursive Scheme functions

//factorial:

//<your team's fact(n) implementation>
var fa = function(n) {
  if(n==1){
    return 1;
  }
else {
return (n * fa(n-1))}
} 

//TEST CALLS
// (writing here can facilitate EZer copy/pasting into dev console now and later...)
(fact 1) //"should be 1"
(fact 5) //should be 120

//-----------------------------------------------------------------


//fib:

//<your team's fib(n) implementation>

//TEST CALLS
// (writing here can facilitate EZer copy/pasting into dev console now and later...)

//=================================================================

