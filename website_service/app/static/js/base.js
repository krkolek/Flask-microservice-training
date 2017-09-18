var ROW = '<tr><td>{1}</td><td><button onclick="delete_user(\'{0}\')" style="font-weight: bold; color: red; background-color: white" on>X</button></td></tr>'
var url_input = $("#api_url")
var table = $("#table_of_users");


/**
 * Clears rows with users and put there a loading circle.
 */
function make_loader_row() {
    table.find("tr:gt(0)").remove();
    table.append('<tr><td colspan="2" style="padding-left:70px"><div class="loader"></div></td></tr>')
}

/**
 * Clears table rows and put there message when no users is loaded.
 */
function make_status_row(status) {
    table.find("tr:gt(0)").remove();
    if (status=='success') {
        table.append('<tr><td colspan="2"><h3>No user has been added</h3></td></tr>')
    }
    else {
        table.append('<tr><td colspan="2"><h3>Status: ' + status + '</td></tr>')
    }
}

/**
 * Fill table with received users.
 */
function fill_table(users) {
    table.find("tr:gt(0)").remove();
    $.each(users, function(i, elem) {
        table.append(ROW.format(i, elem));
    })
}

/**
 * Retrieves list of users by AJAX.
 */
function load_users() {
    make_loader_row();

    $.get(url=url_input.val() + "/users",
    {},
    function(data, status) {
        if ($.isEmptyObject(data) || status != 'success') {
            make_status_row(status)
        }
        else {
            fill_table(data)
        }
    });
}

/**
 * Sends post request with new user by AJAX and reloads list of them.
 */
function add_user() {
    name_input = $("#id_name")

    $.post(url_input.val() + "/users",
    JSON.stringify({"name": name_input.val()}),
    function(data, status){
        load_users();
        name_input.val('');
    },
    "json")
}

/**
 * Sends request to delete user by AJAX and reloads list of them.
 */
function delete_user(user_id) {
    $.get(url=url_input.val() + "/users/" + user_id,
    {},
    function(data, status){
        load_users();
    });
}


$("#add_user").submit(function( event ) {
    add_user();
    event.preventDefault();
});
