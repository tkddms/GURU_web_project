// change active btn(word)
var url = $('#_url').html()

function ChangeActive(){
    $('#info','#service','#contact','#main').attr('class','nav-item');
    switch(url){
        case '/info/': $('#info').attr('class','nav-item active'); break;
        case '/service/' : $('#service').attr('class','nav-item active'); break;
        case '/contact/' : $('#contact').attr('class','nav-item active'); break;
        default : $('#main').attr('class','nav-item active'); break;
    }
}

// calculate recent age
function CalRecentAge(){
    var _missingAge = $('#missing_age').html().split("살") //실종 나이
    var missingAge = parseInt(_missingAge[0])
    var _missingYear = $('#missing_date').html().split(' ') //실종 날짜
    var missingYear = _missingYear[2]
    var thisDate = new Date()
    var thisYear = thisDate.getFullYear()
    var diffYear = parseInt(thisYear) - parseInt(missingYear)

    console.log(missingYear)

    $('#recent_age').text((missingAge+diffYear)+"살")
}

function AddSex(){
    if($('#sex_inp_div').html()=='1'){
        $('#sex_inp').text("여")
    }else{
        $('#sex_inp').text("남")
    }
}

ChangeActive()
CalRecentAge()
AddSex()