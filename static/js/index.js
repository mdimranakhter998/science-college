$(document).ready(function(){   
    $(".stats-info").hide()    
    $(".link li").last().click(function(){
        $(this).addClass("active")
        $(this).siblings().removeClass("active") 
        $(".mca-info").hide()
        $(".stats-info").show()     
    })
    $(".link li").first().click(function(){
        $(this).addClass("active")
        $(this).siblings().removeClass("active") 
        $(".stats-info").hide()
        $(".mca-info").show()                    
    })
    $("#bar").click(function(){
        $("#content").toggle()
        $("#items").toggle()           
                     
    })
    
})
