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

ChangeActive()