function set_user_list(users, sel_user) {
    $('#id_user').empty();
    $('#id_user')
        .append($('<option>', { value : '' })
        .text(''));
    var userdropdown = document.getElementById('id_user');

    console.log(users);
    console.log(sel_user)
    for (x in users) {
        user = users[x]
        // create new option element
        var opt = document.createElement('option');
        // create text node to add to option element (opt)
        opt.appendChild( document.createTextNode(user) );
        // set value property of opt
        opt.value = x;
        if (opt.value == sel_user) {
          opt.selected = true;
        }
        // add opt to end of select box (sel)
        userdropdown.appendChild(opt);
    }
    if (sel_user != '' && sel_user != 'AnonymousUser') {
    } else {
        $('#id_goal').empty();
    }
}

$("#id_user").change(function () {
    var user = $(this).val();
    console.log(user)
    if (user != '') {
        $.ajax({
            url: '/goal/get-goals/'+user,
            success: function (response) {
                set_goals(response);
            }
        });
    } else {
        $('#id_goal').empty();
    }
});

function set_goals(response, sel_goal) {
    var  new_options = response.goal_list;
    $('#id_goal').empty();
    $('#id_goal')
        .append($('<option>', { value : '' })
        .text(''));
    $.each(new_options, function(key, value) {
        console.log(key,value)
        if(sel_goal == key) {
            $('#id_goal')
                .append($('<option>', { value : key })
                .text(value)
                .attr('selected',true));
        } else {
            $('#id_goal')
                .append($('<option>', { value : key })
                .text(value));
        }
    });
}

function get_forex_rate(from_year, from_month, from_day, from_currency, to_currency) {
    forex_ep = '/common/api/get-forex/'+from_year+'/'+from_month+'/'+from_day+'/'+from_currency+'/'+to_currency;
    console.log('getting forex rate', forex_ep)
    var ret = 1;
    $.ajax({
        method:"GET",
        url:forex_ep,
        async: false,
        success: function(data){
          console.log(data)
          for (val in data) {
            console.log('returning ', data[val]);
            ret = data[val];
          }
        },
        error: function(error_data){
          console.log("error")
          console.log(error_data)
        }
    })
    return ret;
}
