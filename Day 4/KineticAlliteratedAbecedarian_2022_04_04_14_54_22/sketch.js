/*

#NaPoGenMo #NaPoWRiMO ##napowrimoxayaskala
Using @ayaskala day 4 prompt :

Prompt #4: Abecedarian for a day.

An Abecedarian poem is one in which the first sentence starts with one letter of the alphabet and continues the order in subsequent lines.

going to use alliteration alongside the Abecedarian

alliteration: "the occurrence of the same letter or sound at the beginning of adjacent or closely connected words.

Background sounds are from : Colorscape : Hues into Grooves
 

*/


function setup() {
  createCanvas(displayWidth, displayHeight);
}

function draw() {
 background('violet')
    Poem = 'Alienating Authority always advantageous \n basically because the basis \n currently concludes corruption , confidence, cockiness and collusion \n determining directional delusions \n eating each escape plan, expotentially  \n freedom freezingly fought  \n gaps growing and glowing\n Hertehina happens to hover happily \n intertwining ice inhabitants intensifies \n jumping, jittering, jotting and jowing \n kept kindness\n love locked latitudely \n making mansions, mazes , beyond meditation \n never knowing\n optically observation\n patients , persons , people, pet panickly patient \n Questions Queueing\n responses readily reads "reset, reset, reset" \n sounds singing, swimming , slightly slow\n teasing, taunting as they test \n uniquely unifiers\n vouching against various word vomit\n worrysome?wormhole what would you want?\n xmen? execution?Excerise excorisms? \n You? \n zoo?'
    let r2 = random(2);
     textSize(30)
    fill('blue')
  textAlign(CENTER);
  textLeading((frameCount * 0.059) );
  //textLeading(-24);
 text(Poem, 0, 100+r2, 1000-r2, 1000);
}