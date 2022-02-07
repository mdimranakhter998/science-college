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
                    if(response['status']==200){                        
                        $("#adminlogin-form").trigger("reset");                       
                        swal({
                            title: "Query successfully!",
                            text: "Thank you for contant us we will contact you soon!",
                            icon: "success",
                            button: "ok",
                          });
                          
                    }
                },            
                  });	
            }
    })
  
})