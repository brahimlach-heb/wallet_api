
let ruya = document.getElementById('ruya');
let karma = document.getElementById('karma');
let adil = document.getElementById('adil');
let taim = document.getElementById('taim');

let efix = document.getElementById('efix');
let ashab = document.getElementById('ashab');
let turkpin = document.getElementById('turkpin');
let razer = document.getElementById('razer');
let alfurat = document.getElementById('alfurat');
let musaab = document.getElementById('musaab');
let abutalal = document.getElementById('abutalal');
let kuvyet = document.getElementById('kuvyet');
let ziraat = document.getElementById('ziraat');
let codes = document.getElementById('codes');
let bayilar = document.getElementById('bayilar');

let total = document.getElementById('total');
let submit = document.getElementById('submit');



let mood = 'calculate';
let tmp;


let dataPro;
if(localStorage.product != null) {
    dataPro = JSON.parse(localStorage.product)
}else {
    dataPro = [];
}



//total
function getTotal(){

        let result = +ruya.value + +karma.value + +adil.value + +taim.value + +efix.value + +ashab.value + +turkpin.value + +razer.value + +alfurat.value + +musaab.value + +abutalal.value + +kuvyet.value + +ziraat.value + +codes.value + +bayilar.value;
        total.innerHTML = result;
        total.style.background = '#B8860B'

}

//create inputs
submit.onclick = function(){
    let newPro = {
        date:date.value,
        ruya:ruya.value,
        karma:karma.value,
        adil:adil.value,
        taim:taim.value,

        efix:efix.value,
        ashab:ashab.value,
        turkpin:turkpin.value,
        razer:razer.value,
        alfurat:alfurat.value,
        musaab:musaab.value,
        abutalal:abutalal.value,
        kuvyet:kuvyet.value,
        ziraat:ziraat.value,
        codes:codes.value,
        bayilar:bayilar.value,

        total:total.innerHTML,

    }
    if (mood === 'calculate'){
        dataPro.push(newPro);
    }else{
        dataPro[tmp] = newPro;
        mood = 'calculate';
        submit.innerHTML = 'Calculate'
    }
    
    localStorage.setItem('product', JSON.stringify(dataPro))
    clearData()
    showData()
}

//clear inputs
function clearData (){
    date.value = '';
    ruya.value = '';
    karma.value = '';
    adil.value = '';
    taim.value = '';

    efix.value = '';
    ashab.value = '';
    turkpin.value = '';
    razer.value = '';
    alfurat.value = '';
    musaab.value = '';
    abutalal.value = '';
    kuvyet.value = '';
    ziraat.value = '';
    codes.value = '';
    bayilar.value = '';

    total.innerHTML = '';
}

//read
function showData (){
    getTotal()
    let table = '';
    for(let i = 0; i < dataPro.length; i++)
        table += `
            <tr>
                <td>${dataPro[i].date}</td>
                <td>${dataPro[i].ruya}</td>
                <td>${dataPro[i].karma}</td>
                <td>${dataPro[i].adil}</td>
                <td>${dataPro[i].taim}</td>
                
                <td>${dataPro[i].efix}</td>
                <td>${dataPro[i].ashab}</td>
                <td>${dataPro[i].turkpin}</td>
                <td>${dataPro[i].razer}</td>
                <td>${dataPro[i].alfurat}</td>
                <td>${dataPro[i].musaab}</td>
                <td>${dataPro[i].abutalal}</td>
                <td>${dataPro[i].kuvyet}</td>
                <td>${dataPro[i].ziraat}</td>
                <td>${dataPro[i].codes}</td>
                <td>${dataPro[i].bayilar}</td>
                <td class="totalo">${dataPro[i].total}</td>
                <td><button onclick="updateData(${i})" id="delete" class="btn2">Update</button></td>
                <td><button onclick="deleteData(${i})" id="update" class="btn2">Delete</button></td>
            </tr>
        `

    document.getElementById('tbody').innerHTML = table;
}
showData()


//delete
function deleteData(i) {
    dataPro.splice(i,1);
    localStorage.product = JSON.stringify(dataPro)
    showData()
}

//update
function updateData(i){
    date.value = dataPro[i].date;
    ruya.value = dataPro[i].ruya;
    karma.value = dataPro[i].karma;
    adil.value = dataPro[i].adil;
    taim.value = dataPro[i].taim;

    efix.value = dataPro[i].efix;
    ashab.value = dataPro[i].ashab;
    turkpin.value = dataPro[i].turkpin;
    razer.value = dataPro[i].razer;
    alfurat.value = dataPro[i].alfurat;
    musaab.value = dataPro[i].musaab;
    abutalal.value = dataPro[i].abutalal;
    kuvyet.value = dataPro[i].kuvyet;
    ziraat.value = dataPro[i].ziraat;
    codes.value = dataPro[i].codes;
    bayilar.value = dataPro[i].bayilar;

    getTotal()
    submit.innerHTML = 'update';
    mood = 'update';
    tmp = i;
    scroll ({
        top:0,
        behavior:'smooth',
    })
}

