$("document").ready(function(){ 
    $("#contact").click(function(){                           
        $("#contactus").slideToggle("slow");
        $("#contactus").animate({top:"10%"});    
    }) 
    $("#contactclose").click(function(){
         $("#contactus").hide()
    })
     
    $("#contactus-form").validate({
        rules:{
            name:{required:true,minlength:3},
            email:{email:true, required:true},
            textarea:"required",            
        },
        messages:{
           name:{required:"name is required",minlength:"please enter atleast three character name"},
           email:{email:"please enter valid email",required:"email is required"},
           textarea:"query is required",     

        },
        submitHandler: function(form){  
            let data= new FormData()  
            data.append("name",$("#name").val())
            data.append("email",$("#email").val()) 
            data.append("textarea",$("#textarea").val())           
            data.append("file",$("input[id^='file']")[0].files[0])                                    
            $.ajax({
                url: "/contactus/",
                type: "POST",
                contentType: false,
                processData: false,                
                data: data ,                
                success: function(response) {
                    if(response['status']==200){                        
                        $("#contactus-form").trigger("reset");                       
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