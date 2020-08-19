// change active btn(word)
function ChangeActive(){
    var url = $('#_url').html()
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
    var missingAge = $('#missing_age').html().substring(0,1) //실종 나이
    var missingYear = $('#missing_date').html().substring(0,4) //실종 날짜
    var thisDate = new Date()
    var thisYear = thisDate.getFullYear()

    var diffYear = parseInt(thisYear) - parseInt(missingYear)
    
    $('#recent_age').text((parseInt(missingAge)+diffYear)+"살")
}

ChangeActive()
CalRecentAge()