jQuery(function($){
    $(document).ready(function(){
        $("#id_country").change(function(){
            $.ajax({
                url:"/states/",
                type:"POST",
                data:{country: $(this).val(),},
                success: function(result) {
                    console.log(result);
                    cols = document.getElementById("id_state");
                    cols.options.length = 0;
                    cols.options.add(new Option("State", "State"));
                    for(var k in result){
                        cols.options.add(new Option(k, result[k]));
                    }
                },
                headers: {
                    "X-CSRFToken": {{csrf_token}}
                },
                error: function(e){
                    console.error(JSON.stringify(e));
                },
            });
        });
    }); 
});