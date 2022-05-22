function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


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
                    cols.options.add(new Option("state", "State"));
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
        $("#id_state").change(function(){
            $.ajax({
                url:"/districts/",
                type:"POST",
                data:{division: $(this).val(),},
                success: function(result) {
                    console.log(result);
                    cols = document.getElementById("id_district");
                    cols.options.length = 0;
                    cols.options.add(new Option("District", "District"));

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
        $("#id_district").change(function(){
            $.ajax({
                url:"/cities/",
                type:"POST",
                data:{district: $(this).val(),},
                success: function(result) {
                    console.log(result);
                    cols = document.getElementById("id_citie");
                    cols.options.length = 0;
                    cols.options.add(new Option("Citie", "Citie"));
                    
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