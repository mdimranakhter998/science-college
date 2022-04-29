$("document").ready(function(){  
    $("#admin").click(function(){                           
        $("#adminlogin").slideToggle("slow");
        $("#adminlogin").animate({top:"10%"});    
    }) 
    $("#adminclose").click(function(){
         $("#adminlogin").hide()
    }) 
    $("#adminlogin-form").validate({                     
        submitHandler: function(form){            
            $.ajax({
                url: "/adminlogin/",
                type: "POST",                
                data: $("#adminlogin-form").serialize(),
                datatype:JSON,
                success: function(response) {
                    if(response['status']==202){    
                      window.location="/admin/"                                 
                       
                          
                    }
                },            
                  });	
            }
    })
  
})