function returnString(aText,jump){

   for (i = 98; i <= 123; i++){
      aText = aText.replace(new RegExp(String.fromCharCode(i),"g"),String.fromCharCode(i-jump));
      
   }
  return aText;
}

function printString(aText,jump){
  
  aText = returnString(aText,jump); 
  return aText;
}
