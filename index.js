
let personagem = "Gunner"

let experience =  3000

let classe = " "

if (experience < 1000) {
    classe = "Bronze"
}else if(experience >= 1001 || experience <= 2000){
   classe = " Prata"
}else if(experience >= 2001 || experience <= 5000){
    classe = "Ouro"
}else if(experience >= 5001 || experience <= 6000){
    classe = "Platina"
}else if(experience >= 6001 || experience <= 7000){
    classe ="Ascendente"
}else if(experience >= 7001 || experience <= 8000){    
    classe = "Imortal"
}else if(experience >= 9000){
    classe = "Radiante" 
}else{
    console.log("Error")
}       
console.log(`O heroi ${personagem} esta no rank ${classe}`)